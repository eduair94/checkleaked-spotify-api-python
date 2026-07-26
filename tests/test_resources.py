from __future__ import annotations

from spotify_api_sdk import SpotifyApiClient
from spotify_api_sdk.resources import (
    ENDPOINT_COUNT,
    NAMESPACE_COUNT,
    RESOURCE_CLASSES,
)

from .helpers import FakeSession


def sdk() -> tuple[SpotifyApiClient, FakeSession]:
    session = FakeSession()
    return SpotifyApiClient("key", session=session), session


def test_exposes_all_25_namespaces_and_110_methods() -> None:
    client, _ = sdk()
    assert NAMESPACE_COUNT == 25
    assert ENDPOINT_COUNT == 110
    assert len(RESOURCE_CLASSES) == 25
    for namespace in RESOURCE_CLASSES:
        assert getattr(client, namespace) is not None


def test_search_uses_pythonic_parameter_names_and_wire_names() -> None:
    client, session = sdk()
    client.search.suggestions(
        "daft punk",
        number_of_top_results=3,
        include_authors=True,
    )
    url = session.calls[0]["url"]
    assert "q=daft+punk" in url
    assert "numberOfTopResults=3" in url
    assert "includeAuthors=true" in url


def test_path_parameters_are_normalized_and_encoded() -> None:
    client, session = sdk()
    client.artists.overview(
        "https://open.spotify.com/intl-es/artist/4tZwfgrHOc3mvqYlEYSvVi"
    )
    assert session.calls[0]["url"].endswith(
        "/artist_overview?id=4tZwfgrHOc3mvqYlEYSvVi"
    )

    client.browse.category("a/b c")
    assert session.calls[1]["url"].endswith(
        "/browse/categories/a%2Fb%20c"
    )


def test_post_body_is_built_from_typed_fields() -> None:
    client, session = sdk()
    client.tracking.track("track", "spotify:track:abc")
    call = session.calls[0]
    assert call["method"] == "POST"
    assert call["url"].endswith("/tracking/track")
    assert call["data"] == '{"type": "track", "id": "spotify:track:abc"}'


def test_free_form_ai_body_and_query_are_forwarded() -> None:
    client, session = sdk()
    client.ai.analyze({"subject": "track"}, query={"market": "US"})
    call = session.calls[0]
    assert call["url"].endswith("/ai/analyze?market=US")
    assert call["data"] == '{"subject": "track"}'


def test_npm_camel_case_aliases_are_available() -> None:
    client, session = sdk()
    client.artists.topTracks("artist-id", market="US")
    assert session.calls[0]["url"].endswith(
        "/artist_top_tracks?id=artist-id&market=US"
    )


def test_wire_query_named_query_does_not_conflict_with_extra_query() -> None:
    client, session = sdk()
    client.concerts.locations("Montevideo", extra_query={"limit": 5})
    assert session.calls[0]["url"].endswith(
        "/partner/concert-locations?limit=5&query=Montevideo"
    )
