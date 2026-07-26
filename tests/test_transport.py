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

