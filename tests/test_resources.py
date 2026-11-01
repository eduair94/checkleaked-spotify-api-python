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


def test_exposes_all_23_namespaces_and_108_methods() -> None:
    client, _ = sdk()
    assert NAMESPACE_COUNT == 23
    assert ENDPOINT_COUNT == 108
    assert len(RESOURCE_CLASSES) == 23
    for namespace in RESOURCE_CLASSES:
        assert getattr(client, namespace) is not None


def test_operator_only_admin_methods_are_gone() -> None:
    client, _ = sdk()
    assert "cache" not in RESOURCE_CLASSES
    assert "credentials" not in RESOURCE_CLASSES
    for name in ("proxies", "clear_proxies", "clear_errors"):
        assert not hasattr(client.health, name)


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
    client.tracking.track("track", "spotify:track:abc", label="mine")
    call = session.calls[0]
    assert call["method"] == "POST"
    assert call["url"].endswith("/tracking/track")
    assert call["data"] == (
        '{"spotifyType": "track", "spotifyId": "abc", "label": "mine"}'
    )


def test_tracking_untrack_and_logs_use_server_parameter_names() -> None:
    client, session = sdk()
    client.tracking.untrack(
        spotify_type="track",
        spotify_id="https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT",
    )
    client.tracking.logs(spotify_type="artist", change_type="followers_change")
    assert session.calls[0]["method"] == "DELETE"
    assert session.calls[0]["url"].endswith(
        "/tracking/untrack?spotifyType=track&spotifyId=4cOdK2wGLETKBW3PvgPWqT"
    )
    assert session.calls[1]["url"].endswith(
        "/tracking/logs?spotifyType=artist&changeType=followers_change"
    )


def test_webhook_register_sends_playlist_and_callback() -> None:
    client, session = sdk()
    client.webhooks.register(
        "37i9dQZF1DXcBWIGoYBM5M",
        "https://example.test/hook",
        events=["playlist.tracks.added"],
    )
    call = session.calls[0]
    assert call["url"].endswith("/webhooks/register")
    assert call["data"] == (
        '{"playlistId": "37i9dQZF1DXcBWIGoYBM5M", '
        '"callbackUrl": "https://example.test/hook", '
        '"events": ["playlist.tracks.added"]}'
    )


def test_status_counts_and_single_track() -> None:
    client, session = sdk()
    client.status()
    client.health.status()
    client.tracks.counts(
        ["spotify:track:0VjIjW4GlUZAMYd2vXMi3b", "7ouMYWpwJ422jRcDASZB7P"]
    )
    client.tracks.get_by_id("spotify:track:4cOdK2wGLETKBW3PvgPWqT", market="US")
    urls = [call["url"] for call in session.calls]
    assert urls[0].endswith("/status")
    assert urls[1].endswith("/status")
    assert urls[2].endswith(
        "/partner/tracks/count?ids=0VjIjW4GlUZAMYd2vXMi3b%2C7ouMYWpwJ422jRcDASZB7P"
    )
    assert urls[3].endswith("/tracks/4cOdK2wGLETKBW3PvgPWqT?market=US")


def test_market_slim_and_audio_feature_ids() -> None:
    client, session = sdk()
    client.albums.get(["a", "b"], market="GB")
    client.partner.track("t", slim=True)
    client.analysis.audio_features(["x", "y"])
    urls = [call["url"] for call in session.calls]
    assert urls[0].endswith("/albums?ids=a%2Cb&market=GB")
    assert urls[1].endswith("/partner/track?id=t&slim=true")
    assert urls[2].endswith("/audio_features?ids=x%2Cy")


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
