"""Opt-in live provider tests.

Set SPOTIFY_API_KEY for RapidAPI and/or SPOTIFY_PROXY_API_KEY for the direct
proxy. Secrets are never printed.
"""

from __future__ import annotations

import os

import pytest

from spotify_api_sdk import SpotifyApiClient


@pytest.mark.live
def test_rapidapi_search_live() -> None:
    key = os.environ.get("SPOTIFY_API_KEY")
    if not key:
        pytest.skip("SPOTIFY_API_KEY is not configured")
    result = SpotifyApiClient(
        key,
        provider="rapidapi",
        retries=0,
    ).search.search("Daft Punk", type="multi", limit=1)
    assert isinstance(result, dict)
    assert any(name in result for name in ("artists", "tracks", "topResults"))


@pytest.mark.live
def test_direct_proxy_search_live() -> None:
    key = os.environ.get("SPOTIFY_PROXY_API_KEY")
    if not key:
        pytest.skip("SPOTIFY_PROXY_API_KEY is not configured")
    result = SpotifyApiClient(
        key,
        provider="proxy",
        retries=0,
    ).search.search("Daft Punk", type="multi", limit=1)
    assert isinstance(result, dict)
    assert any(name in result for name in ("artists", "tracks", "topResults"))

