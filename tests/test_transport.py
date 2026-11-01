from __future__ import annotations

from typing import Any, Dict, List

import pytest
import requests

from spotify_api_sdk import (
    AuthError,
    RateLimitError,
    SpotifyApiClient,
    SpotifyApiError,
    TimeoutError,
)

from .helpers import FakeResponse, FakeSession


def client(session: FakeSession, **config: Any) -> SpotifyApiClient:
    return SpotifyApiClient(
        "test-key",
        session=session,
        retry_delay=0,
        **config,
    )


def test_builds_query_and_injects_rapidapi_headers() -> None:
    session = FakeSession()
    sdk = client(session)
    result = sdk.search.search(
        "daft punk",
        limit=10,
        extra_query={"ids": ["spotify:track:abc", "def"]},
    )
    call = session.calls[0]
    assert result == {"ok": True}
    assert call["url"].endswith(
        "/search?ids=abc%2Cdef&q=daft+punk&limit=10"
    )
    assert call["headers"]["x-rapidapi-key"] == "test-key"
    assert call["headers"]["x-rapidapi-host"] == "spotify81.p.rapidapi.com"


def test_proxy_provider_omits_rapidapi_host() -> None:
    session = FakeSession()
    sdk = client(session, provider="proxy")
    sdk.markets.get()
    call = session.calls[0]
    assert call["url"] == (
        "https://spotify-proxy.checkleaked.cc/spotify-data/markets"
    )
    assert "x-rapidapi-host" not in call["headers"]


def test_non_enveloped_success_is_returned_directly() -> None:
    session = FakeSession(FakeResponse(body={"markets": ["US"]}))
    sdk = client(session)
    assert sdk.markets.get() == {"markets": ["US"]}


def test_request_raw_returns_complete_envelope() -> None:
    body = {"success": True, "data": {"ok": 1}, "metadata": {"cached": True}}
    sdk = client(FakeSession(FakeResponse(body=body)))
    assert sdk.request_raw("GET", "/ping") == body


def test_success_false_at_http_200_raises() -> None:
    sdk = client(
        FakeSession(
            FakeResponse(
                body={
                    "success": False,
                    "error": "UPSTREAM",
                    "message": "failed",
                }
            )
        )
    )
    with pytest.raises(SpotifyApiError) as caught:
        sdk.health.ping()
    assert caught.value.code == "UPSTREAM"


def test_auth_error_is_structured_and_url_is_redacted() -> None:
    sdk = client(
        FakeSession(
            FakeResponse(
                status=401,
                body={"success": False, "error": "Invalid API key"},
            )
        ),
        retries=0,
    )
    with pytest.raises(AuthError) as caught:
        sdk.search.search("secret query")
    assert caught.value.status == 401
    assert caught.value.code == "Invalid API key"
    assert "secret+query" not in (caught.value.url or "")


def test_429_retries_and_honors_retry_after(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sleeps: List[float] = []
    monkeypatch.setattr("spotify_api_sdk.http.time.sleep", sleeps.append)
    retries: List[Dict[str, Any]] = []
    session = FakeSession(
        FakeResponse(
            status=429,
            body={"message": "slow down"},
            headers={"retry-after": "0.01"},
        ),
        FakeResponse(body={"success": True, "data": {"ok": "retried"}}),
    )
    sdk = client(session, on_retry=retries.append)
    assert sdk.health.ping() == {"ok": "retried"}
    assert len(session.calls) == 2
    assert sleeps == [0.01]
    assert retries[0]["status"] == 429


def test_final_429_exposes_retry_after() -> None:
    sdk = client(
        FakeSession(
            FakeResponse(
                status=429,
                body={"message": "slow down"},
                headers={"retry-after": "2"},
            )
        ),
        retries=0,
    )
    with pytest.raises(RateLimitError) as caught:
        sdk.health.ping()
    assert caught.value.retry_after_ms == 2000


def test_timeout_is_normalized() -> None:
    sdk = client(
        FakeSession(requests.exceptions.Timeout("late")),
        retries=0,
    )
    with pytest.raises(TimeoutError) as caught:
        sdk.health.ping(request_timeout=0.1)
    assert caught.value.code == "TIMEOUT"


def test_context_manager_closes_session() -> None:
    session = FakeSession()
    with client(session) as sdk:
        assert sdk.health.ping() == {"ok": True}
    assert session.closed is True



C1_ENVELOPE = {
    "success": False,
    "error": "Invalid parameter",
    "message": '"ids" must be a comma-separated list of Spotify track ids.',
    "code": "INVALID_PARAMETER",
    "status": 400,
    "status_code": 400,
    "retryable": False,
    "param": "ids",
    "request_id": "body-request-id",
}


def test_error_envelope_exposes_code_request_id_and_param() -> None:
    sdk = client(
        FakeSession(
            FakeResponse(
                status=400,
                body=C1_ENVELOPE,
                headers={"x-request-id": "hdr-request-id"},
            )
        )
    )
    with pytest.raises(SpotifyApiError) as caught:
        sdk.tracks.get("not-an-id")
    error = caught.value
    assert error.status == 400
    assert error.code == "INVALID_PARAMETER"
    assert error.request_id == "hdr-request-id"
    assert error.param == "ids"
    assert error.retryable is False
    assert str(error) == C1_ENVELOPE["message"]


def test_request_id_falls_back_to_the_body() -> None:
    sdk = client(FakeSession(FakeResponse(status=400, body=C1_ENVELOPE)))
    with pytest.raises(SpotifyApiError) as caught:
        sdk.tracks.get("not-an-id")
    assert caught.value.request_id == "body-request-id"


def test_error_true_at_http_200_raises_with_its_code() -> None:
    sdk = client(
        FakeSession(
            FakeResponse(
                body={
                    "error": True,
                    "code": "LYRICS_NOT_AVAILABLE",
                    "message": "lyrics for this track is not available on spotify!",
                }
            )
        )
    )
    with pytest.raises(SpotifyApiError) as caught:
        sdk.tracks.lyrics("4iV5W9uYEdYUVa79Axb7Rh")
    assert caught.value.status == 200
    assert caught.value.code == "LYRICS_NOT_AVAILABLE"
    assert caught.value.retryable is False


def test_error_flag_without_code_raises_without_a_fake_code() -> None:
    sdk = client(FakeSession(FakeResponse(body={"error": True, "message": "nope"})))
    with pytest.raises(SpotifyApiError) as caught:
        sdk.health.ping()
    assert caught.value.code is None
    assert str(caught.value) == "nope"


def test_successful_bodies_with_error_false_are_returned() -> None:
    lyrics = {"error": False, "syncType": "LINE_SYNCED", "lines": []}
    sdk = client(FakeSession(FakeResponse(body=lyrics)))
    assert sdk.tracks.lyrics("0VjIjW4GlUZAMYd2vXMi3b") == lyrics


def test_exhausted_quota_is_not_retried() -> None:
    session = FakeSession(
        FakeResponse(
            status=429,
            body={
                "code": "QUOTA_EXCEEDED",
                "message": "Quota used up",
                "retryable": True,
            },
        )
    )
    with pytest.raises(RateLimitError) as caught:
        client(session).health.ping()
    assert len(session.calls) == 1
    assert caught.value.code == "QUOTA_EXCEEDED"
    assert caught.value.retryable is False


def test_rapidapi_message_only_429s_get_codes() -> None:
    monthly = FakeSession(
        FakeResponse(
            status=429,
            body={
                "message": "You have exceeded the MONTHLY quota for Requests "
                "on your current plan, BASIC. Upgrade your plan."
            },
        )
    )
    with pytest.raises(RateLimitError) as caught:
        client(monthly).health.ping()
    assert len(monthly.calls) == 1
    assert caught.value.code == "QUOTA_EXCEEDED"

    per_second = FakeSession(
        FakeResponse(
            status=429,
            body={"message": "You have exceeded the rate limit per second"},
        )
    )
    with pytest.raises(RateLimitError) as caught:
        client(per_second, retries=0).health.ping()
    assert caught.value.code == "RATE_LIMITED"
    assert caught.value.retryable is True


def test_upstream_throttled_retries_after_body_retry_after_s(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sleeps: List[float] = []
    monkeypatch.setattr("spotify_api_sdk.http.time.sleep", sleeps.append)
    session = FakeSession(
        FakeResponse(
            status=503,
            body={"code": "UPSTREAM_THROTTLED", "retry_after_s": 1},
        ),
        FakeResponse(body={"success": True, "data": {"ok": 1}}),
    )
    assert client(session).health.ping() == {"ok": 1}
    assert sleeps == [1.0]


THROTTLED = {"code": "UPSTREAM_THROTTLED", "retryable": True, "retry_after_s": 30}
TIMED_OUT = {"code": "UPSTREAM_TIMEOUT", "retryable": True}


def test_long_retry_after_is_capped_at_10s_by_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sleeps: List[float] = []
    monkeypatch.setattr("spotify_api_sdk.http.time.sleep", sleeps.append)
    retries: List[Dict[str, Any]] = []
    session = FakeSession(
        FakeResponse(status=503, body=THROTTLED, headers={"retry-after": "30"})
    )
    with pytest.raises(SpotifyApiError) as caught:
        client(session, retries=1, on_retry=retries.append).health.ping()
    assert len(session.calls) == 2
    assert sleeps == [10.0]
    assert retries[0]["delay_ms"] == 10_000
    # The error still reports what the API asked for.
    assert caught.value.retry_after_ms == 30_000


def test_max_retry_delay_bounds_every_wait(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    sleeps: List[float] = []
    monkeypatch.setattr("spotify_api_sdk.http.time.sleep", sleeps.append)
    session = FakeSession(
        FakeResponse(status=503, body=THROTTLED, headers={"retry-after": "30"}),
        FakeResponse(status=503, body=THROTTLED),
        requests.exceptions.ConnectionError("reset"),
        FakeResponse(body={"success": True, "data": {"ok": 1}}),
    )
    sdk = SpotifyApiClient(
        "test-key",
        session=session,
        retries=3,
        retry_delay=60,
        max_retry_delay=0.005,
    )
    assert sdk.health.ping() == {"ok": 1}
    assert sleeps == [0.005, 0.005, 0.005]


def test_504_is_retried_at_most_once_by_default(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("spotify_api_sdk.http.time.sleep", lambda _: None)
    session = FakeSession(
        FakeResponse(status=504, body=TIMED_OUT, headers={"retry-after": "0"})
    )
    with pytest.raises(SpotifyApiError) as caught:
        client(session, retries=3).health.ping()
    assert caught.value.status == 504
    assert caught.value.code == "UPSTREAM_TIMEOUT"
    assert len(session.calls) == 2


def test_gateway_timeout_retries_is_configurable_and_only_limits_504s(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("spotify_api_sdk.http.time.sleep", lambda _: None)
    never = FakeSession(
        FakeResponse(status=504, body=TIMED_OUT, headers={"retry-after": "0"})
    )
    with pytest.raises(SpotifyApiError):
        client(never, retries=3, gateway_timeout_retries=0).health.ping()
    assert len(never.calls) == 1

    mixed = FakeSession(
        FakeResponse(status=504, body=TIMED_OUT, headers={"retry-after": "0"}),
        FakeResponse(status=503, body=THROTTLED, headers={"retry-after": "0"}),
        FakeResponse(body={"success": True, "data": {"ok": 7}}),
    )
    assert client(mixed, retries=2).health.ping() == {"ok": 7}
    assert len(mixed.calls) == 3


def test_503_upstream_timeout_counts_as_a_gateway_timeout(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Since 2026-10 the API answers a timeout as 503 UPSTREAM_TIMEOUT.
    monkeypatch.setattr("spotify_api_sdk.http.time.sleep", lambda _: None)
    session = FakeSession(
        FakeResponse(status=503, body=TIMED_OUT, headers={"retry-after": "0"})
    )
    with pytest.raises(SpotifyApiError) as caught:
        client(session, retries=3).health.ping()
    assert caught.value.status == 503
    assert caught.value.code == "UPSTREAM_TIMEOUT"
    assert len(session.calls) == 2

    # Any other 503 code may use every retry.
    other = FakeSession(
        FakeResponse(status=503, body=THROTTLED, headers={"retry-after": "0"})
    )
    with pytest.raises(SpotifyApiError):
        client(other, retries=3).health.ping()
    assert len(other.calls) == 4


def test_cloudflare_524_counts_as_a_gateway_timeout_but_502_does_not(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Cloudflare answers 524 (plain text) when the origin took about 100 s.
    monkeypatch.setattr("spotify_api_sdk.http.time.sleep", lambda _: None)

    def edge(status: int) -> FakeResponse:
        response = FakeResponse(
            status=status, headers={"content-type": "text/plain"}
        )
        response.content = f"error code: {status}".encode()
        return response

    timeout = FakeSession(edge(524))
    with pytest.raises(SpotifyApiError) as caught:
        client(timeout, retries=3).health.ping()
    assert caught.value.status == 524
    assert len(timeout.calls) == 2  # gateway_timeout_retries (1)

    never = FakeSession(edge(524))
    with pytest.raises(SpotifyApiError):
        client(never, retries=3, gateway_timeout_retries=0).health.ping()
    assert len(never.calls) == 1

    # A plain-text 502 from the edge is not a timeout: every retry.
    bad_gateway = FakeSession(edge(502))
    with pytest.raises(SpotifyApiError):
        client(bad_gateway, retries=3).health.ping()
    assert len(bad_gateway.calls) == 4


def test_503_outcome_unknown_is_never_retried(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # The request may already have run (a forwarded write whose result is
    # unknown): sending it again could repeat it.
    monkeypatch.setattr("spotify_api_sdk.http.time.sleep", lambda _: None)
    body = {
        "success": False,
        "error": "Outcome unknown",
        "code": "OUTCOME_UNKNOWN",
        "status": 503,
        "retryable": False,
        "request_id": "r-1",
    }
    session = FakeSession(FakeResponse(status=503, body=body))
    with pytest.raises(SpotifyApiError) as caught:
        client(session, retries=3).health.ping()
    assert caught.value.status == 503
    assert caught.value.code == "OUTCOME_UNKNOWN"
    assert caught.value.retryable is False
    assert caught.value.request_id == "r-1"
    assert len(session.calls) == 1

    # Even a body claiming ``retryable: true`` is not retried: the code wins.
    claimed = FakeSession(
        FakeResponse(
            status=503, body={"code": "OUTCOME_UNKNOWN", "retryable": True}
        )
    )
    with pytest.raises(SpotifyApiError) as caught2:
        client(claimed, retries=3).health.ping()
    assert caught2.value.retryable is False
    assert len(claimed.calls) == 1
