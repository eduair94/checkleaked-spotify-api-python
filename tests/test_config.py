from __future__ import annotations

import pytest

from spotify_api_sdk import SpotifyApiClient, ValidationError
from spotify_api_sdk.config import (
    PROXY_BASE_URL,
    RAPIDAPI_BASE_URL,
    RAPIDAPI_HOST,
    resolve_config,
)

from .helpers import FakeSession


def test_rapidapi_is_the_default_provider() -> None:
    config = resolve_config("key", session=FakeSession())
    assert config.provider == "rapidapi"
    assert config.channel.base_url == RAPIDAPI_BASE_URL
    assert config.channel.host == RAPIDAPI_HOST


def test_proxy_provider_uses_the_direct_base_without_host_header() -> None:
    config = resolve_config("key", provider="proxy", session=FakeSession())
    assert config.channel.base_url == PROXY_BASE_URL
    assert config.channel.host is None


def test_transport_alias_matches_whatsapp_sdk_style() -> None:
    config = resolve_config("key", transport="proxy", session=FakeSession())
    assert config.provider == "proxy"


def test_api_key_can_come_from_environment(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("SPOTIFY_API_KEY", "env-key")
    config = resolve_config(session=FakeSession())
    assert config.api_key == "env-key"


@pytest.mark.parametrize("provider", ["unknown", "", "RapidAPI"])
def test_invalid_provider_is_rejected(provider: str) -> None:
    with pytest.raises(ValidationError):
        resolve_config("key", provider=provider, session=FakeSession())


def test_missing_key_is_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("SPOTIFY_API_KEY", raising=False)
    monkeypatch.delenv("RAPIDAPI_KEY", raising=False)
    with pytest.raises(ValidationError):
        SpotifyApiClient(session=FakeSession())


def test_retry_wait_cap_and_504_retries_default_and_are_configurable() -> None:
    config = resolve_config("key", session=FakeSession())
    assert config.max_retry_delay_s == 10.0
    assert config.gateway_timeout_retries == 1
    custom = SpotifyApiClient(
        "key",
        session=FakeSession(),
        max_retry_delay=2.5,
        gateway_timeout_retries=0,
    ).config
    assert custom.max_retry_delay_s == 2.5
    assert custom.gateway_timeout_retries == 0
    with pytest.raises(ValidationError):
        resolve_config("key", max_retry_delay=-1, session=FakeSession())

