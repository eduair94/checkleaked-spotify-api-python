"""Generated Spotify Data API resource namespaces.

Do not edit manually. Run ``node scripts/generate_resources.mjs``.
"""

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional, Sequence, Type

from ._resource import Endpoint, Resource
from .types import Headers, IdList, QueryParams

ENDPOINT_COUNT = 110
NAMESPACE_COUNT = 25

_AI_HEALTH = Endpoint(
    key="ai.health",
    method="GET",
    path="/ai/health",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_TYPES = Endpoint(
    key="ai.types",
    method="GET",
    path="/ai/types",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_ANALYZE = Endpoint(
    key="ai.analyze",
    method="POST",
    path="/ai/analyze",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_CHART_TRENDS = Endpoint(
    key="ai.chartTrends",
    method="POST",
    path="/ai/chart-trends",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_ARTIST_SUMMARY = Endpoint(
    key="ai.artistSummary",
    method="POST",
    path="/ai/artist-summary",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_ALBUM_REVIEW = Endpoint(
    key="ai.albumReview",
    method="POST",
    path="/ai/album-review",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_TRACK_DEEP_DIVE = Endpoint(
    key="ai.trackDeepDive",
    method="POST",
    path="/ai/track-deep-dive",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_PLAYLIST_CURATOR = Endpoint(
    key="ai.playlistCurator",
    method="POST",
    path="/ai/playlist-curator",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_MARKET_COMPARISON = Endpoint(
    key="ai.marketComparison",
    method="POST",
    path="/ai/market-comparison",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_GENRE_LANDSCAPE = Endpoint(
    key="ai.genreLandscape",
    method="POST",
    path="/ai/genre-landscape",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_MOOD_PROFILE = Endpoint(
    key="ai.moodProfile",
    method="POST",
    path="/ai/mood-profile",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_VIRAL_POTENTIAL = Endpoint(
    key="ai.viralPotential",
    method="POST",
    path="/ai/viral-potential",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_AI_CUSTOM = Endpoint(
    key="ai.custom",
    method="POST",
    path="/ai/custom",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_ALBUMS_GET = Endpoint(
    key="albums.get",
    method="GET",
    path="/albums",
    path_fields=(),
    query_fields=(("ids", "ids"), ("contrast", "contrast")),
    body_fields=(),
)

_ALBUMS_TRACKS = Endpoint(
    key="albums.tracks",
    method="GET",
    path="/album_tracks",
    path_fields=(),
    query_fields=(("id", "id"), ("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_ALBUMS_METADATA = Endpoint(
    key="albums.metadata",
    method="GET",
    path="/album_metadata",
    path_fields=(),
    query_fields=(("id", "id"), ("contrast", "contrast")),
    body_fields=(),
)

_ANALYSIS_ARTIST_COMPARE = Endpoint(
    key="analysis.artistCompare",
    method="GET",
    path="/artist_compare",
    path_fields=(),
    query_fields=(("ids", "ids"),),
    body_fields=(),
)

_ANALYSIS_AUDIO_FEATURES = Endpoint(
    key="analysis.audioFeatures",
    method="GET",
    path="/audio_features",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_ANALYSIS_PLAYLIST_ANALYSIS = Endpoint(
    key="analysis.playlistAnalysis",
    method="GET",
    path="/playlist_analysis",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_ARTISTS_GET = Endpoint(
    key="artists.get",
    method="GET",
    path="/artists",
    path_fields=(),
    query_fields=(("ids", "ids"), ("contrast", "contrast")),
    body_fields=(),
)

_ARTISTS_OVERVIEW = Endpoint(
    key="artists.overview",
    method="GET",
    path="/artist_overview",
    path_fields=(),
    query_fields=(("id", "id"), ("contrast", "contrast")),
    body_fields=(),
)

_ARTISTS_DISCOGRAPHY_OVERVIEW = Endpoint(
    key="artists.discographyOverview",
    method="GET",
    path="/artist_discography_overview",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_ARTISTS_ALBUMS = Endpoint(
    key="artists.albums",
    method="GET",
    path="/artist_albums",
    path_fields=(),
    query_fields=(("id", "id"), ("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_ARTISTS_SINGLES = Endpoint(
    key="artists.singles",
    method="GET",
    path="/artist_singles",
    path_fields=(),
    query_fields=(("id", "id"), ("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_ARTISTS_APPEARS_ON = Endpoint(
    key="artists.appearsOn",
    method="GET",
    path="/artist_appears_on",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_ARTISTS_DISCOVERED_ON = Endpoint(
    key="artists.discoveredOn",
    method="GET",
    path="/artist_discovered_on",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_ARTISTS_FEATURING = Endpoint(
    key="artists.featuring",
    method="GET",
    path="/artist_featuring",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_ARTISTS_RELATED = Endpoint(
    key="artists.related",
    method="GET",
    path="/artist_related",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_ARTISTS_TOP_TRACKS = Endpoint(
    key="artists.topTracks",
    method="GET",
    path="/artist_top_tracks",
    path_fields=(),
    query_fields=(("id", "id"), ("market", "market")),
    body_fields=(),
)

_AUDIOBOOKS_GET = Endpoint(
    key="audiobooks.get",
    method="GET",
    path="/audiobooks",
    path_fields=(),
    query_fields=(("ids", "ids"), ("market", "market")),
    body_fields=(),
)

_AUDIOBOOKS_GET_BY_ID = Endpoint(
    key="audiobooks.getById",
    method="GET",
    path="/audiobooks/{id}",
    path_fields=(("id", "id"),),
    query_fields=(("market", "market"),),
    body_fields=(),
)

_AUDIOBOOKS_CHAPTERS = Endpoint(
    key="audiobooks.chapters",
    method="GET",
    path="/audiobooks/{id}/chapters",
    path_fields=(("id", "id"),),
    query_fields=(("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_BATCH_ALBUM_METADATA = Endpoint(
    key="batch.albumMetadata",
    method="GET",
    path="/album_metadata_batch",
    path_fields=(),
    query_fields=(("ids", "ids"),),
    body_fields=(),
)

_BATCH_ARTIST_OVERVIEW = Endpoint(
    key="batch.artistOverview",
    method="GET",
    path="/artist_overview_batch",
    path_fields=(),
    query_fields=(("ids", "ids"),),
    body_fields=(),
)

_BATCH_TRACK_CREDITS = Endpoint(
    key="batch.trackCredits",
    method="GET",
    path="/track_credits_batch",
    path_fields=(),
    query_fields=(("ids", "ids"),),
    body_fields=(),
)

_BATCH_TRACK_LYRICS = Endpoint(
    key="batch.trackLyrics",
    method="GET",
    path="/track_lyrics_batch",
    path_fields=(),
    query_fields=(("ids", "ids"), ("format", "format")),
    body_fields=(),
)

_BATCH_TRACK_POPULARITY = Endpoint(
    key="batch.trackPopularity",
    method="GET",
    path="/track_popularity_batch",
    path_fields=(),
    query_fields=(("ids", "ids"),),
    body_fields=(),
)

_BROWSE_CATEGORIES = Endpoint(
    key="browse.categories",
    method="GET",
    path="/browse/categories",
    path_fields=(),
    query_fields=(("country", "country"), ("locale", "locale"), ("limit", "limit"), ("offset", "offset")),
    body_fields=(),
)

_BROWSE_CATEGORY = Endpoint(
    key="browse.category",
    method="GET",
    path="/browse/categories/{id}",
    path_fields=(("id", "id"),),
    query_fields=(("country", "country"), ("locale", "locale")),
    body_fields=(),
)

_BROWSE_FEATURED_PLAYLISTS = Endpoint(
    key="browse.featuredPlaylists",
    method="GET",
    path="/browse/featured-playlists",
    path_fields=(),
    query_fields=(("country", "country"), ("locale", "locale"), ("limit", "limit"), ("offset", "offset")),
    body_fields=(),
)

_BROWSE_NEW_RELEASES = Endpoint(
    key="browse.newReleases",
    method="GET",
    path="/browse/new-releases",
    path_fields=(),
    query_fields=(("country", "country"), ("limit", "limit"), ("offset", "offset")),
    body_fields=(),
)

_BROWSE_RECOMMENDATIONS = Endpoint(
    key="browse.recommendations",
    method="GET",
    path="/browse/recommendations",
    path_fields=(),
    query_fields=(("seed_tracks", "seed_tracks"), ("seed_artists", "seed_artists"), ("seed_genres", "seed_genres"), ("limit", "limit")),
    body_fields=(),
)

_CACHE_STATS = Endpoint(
    key="cache.stats",
    method="GET",
    path="/cache/stats",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_CACHE_INVALIDATE = Endpoint(
    key="cache.invalidate",
    method="POST",
    path="/cache/invalidate",
    path_fields=(),
    query_fields=(),
    body_fields=(("key", "key"), ("pattern", "pattern")),
)

_CHARTS_TOP_BY_MONTHLY_LISTENERS = Endpoint(
    key="charts.topByMonthlyListeners",
    method="GET",
    path="/top_20_by_monthly_listeners",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_CHARTS_TOP200_TRACKS = Endpoint(
    key="charts.top200Tracks",
    method="GET",
    path="/top_200_tracks",
    path_fields=(),
    query_fields=(("period", "period"), ("country", "country"), ("date", "date")),
    body_fields=(),
)

_CHARTS_TOP_ARTISTS = Endpoint(
    key="charts.topArtists",
    method="GET",
    path="/top_artists",
    path_fields=(),
    query_fields=(("period", "period"), ("country", "country")),
    body_fields=(),
)

_CHARTS_TOP_ALBUMS = Endpoint(
    key="charts.topAlbums",
    method="GET",
    path="/top_albums",
    path_fields=(),
    query_fields=(("period", "period"), ("country", "country")),
    body_fields=(),
)

_CHARTS_VIRAL_TRACKS = Endpoint(
    key="charts.viralTracks",
    method="GET",
    path="/viral_tracks",
    path_fields=(),
    query_fields=(("country", "country"),),
    body_fields=(),
)

_CHARTS_TOP_BY_FOLLOWERS = Endpoint(
    key="charts.topByFollowers",
    method="GET",
    path="/top_20_by_followers",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_CONCERTS_LOCATIONS = Endpoint(
    key="concerts.locations",
    method="GET",
    path="/partner/concert-locations",
    path_fields=(),
    query_fields=(("query", "query"),),
    body_fields=(),
)

_CONCERTS_FEED = Endpoint(
    key="concerts.feed",
    method="GET",
    path="/partner/concert-feed",
    path_fields=(),
    query_fields=(("geo_hash", "geoHash"), ("geoname_id", "geonameId"), ("from_", "from"), ("to", "to"), ("radius_in_km", "radiusInKm"), ("concept_uris", "conceptUris"), ("pagination_key", "paginationKey"), ("details", "details"), ("details_limit", "detailsLimit"), ("parsed", "parsed")),
    body_fields=(),
)

_CONCERTS_GET = Endpoint(
    key="concerts.get",
    method="GET",
    path="/partner/concert",
    path_fields=(),
    query_fields=(("id", "id"), ("parsed", "parsed"), ("authenticated", "authenticated")),
    body_fields=(),
)

_CONCERTS_BY_ARTIST = Endpoint(
    key="concerts.byArtist",
    method="GET",
    path="/partner/artist-concerts",
    path_fields=(),
    query_fields=(("id", "id"), ("geo_hash", "geoHash"), ("include_nearby", "includeNearby"), ("details", "details"), ("details_limit", "detailsLimit"), ("parsed", "parsed")),
    body_fields=(),
)

_CONCERTS_SEARCH_ARTISTS = Endpoint(
    key="concerts.searchArtists",
    method="GET",
    path="/partner/search-concert-artists",
    path_fields=(),
    query_fields=(("query", "query"), ("geo_hash", "geoHash"), ("include_nearby", "includeNearby"), ("limit", "limit"), ("details", "details"), ("details_limit", "detailsLimit"), ("parsed", "parsed")),
    body_fields=(),
)

_CREDENTIALS_STATUS = Endpoint(
    key="credentials.status",
    method="GET",
    path="/credentials/status",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_CREDENTIALS_REDIS_COOKIES = Endpoint(
    key="credentials.redisCookies",
    method="GET",
    path="/cookies/redis",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_DOWNLOADS_TRACK = Endpoint(
    key="downloads.track",
    method="GET",
    path="/download_track",
    path_fields=(),
    query_fields=(("q", "q"),),
    body_fields=(),
)

_DOWNLOADS_SOUNDCLOUD = Endpoint(
    key="downloads.soundcloud",
    method="GET",
    path="/download_track_sc",
    path_fields=(),
    query_fields=(("q", "q"),),
    body_fields=(),
)

_EPISODES_GET = Endpoint(
    key="episodes.get",
    method="GET",
    path="/episodes",
    path_fields=(),
    query_fields=(("ids", "ids"), ("market", "market")),
    body_fields=(),
)

_EPISODES_BY_ID = Endpoint(
    key="episodes.byId",
    method="GET",
    path="/episodes/{id}",
    path_fields=(("id", "id"),),
    query_fields=(("market", "market"),),
    body_fields=(),
)

_HEALTH_PING = Endpoint(
    key="health.ping",
    method="GET",
    path="/ping",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_HEALTH_GET = Endpoint(
    key="health.get",
    method="GET",
    path="/health",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_HEALTH_INSTANCE = Endpoint(
    key="health.instance",
    method="GET",
    path="/health/instance",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_HEALTH_CLUSTER = Endpoint(
    key="health.cluster",
    method="GET",
    path="/health/cluster",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_HEALTH_CLUSTER_STRICT = Endpoint(
    key="health.clusterStrict",
    method="GET",
    path="/health/cluster/strict",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_HEALTH_PROXIES = Endpoint(
    key="health.proxies",
    method="GET",
    path="/health/proxies",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_HEALTH_CLEAR_PROXIES = Endpoint(
    key="health.clearProxies",
    method="POST",
    path="/health/proxies/clear",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_HEALTH_CLEAR_ERRORS = Endpoint(
    key="health.clearErrors",
    method="POST",
    path="/health/clear-errors",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_LOOKUPS_ISRC = Endpoint(
    key="lookups.isrc",
    method="GET",
    path="/isrc_lookup",
    path_fields=(),
    query_fields=(("isrc", "isrc"),),
    body_fields=(),
)

_LOOKUPS_UPC = Endpoint(
    key="lookups.upc",
    method="GET",
    path="/upc_lookup",
    path_fields=(),
    query_fields=(("upc", "upc"),),
    body_fields=(),
)

_MARKETS_GET = Endpoint(
    key="markets.get",
    method="GET",
    path="/markets",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_PARTNER_PLAYLIST = Endpoint(
    key="partner.playlist",
    method="GET",
    path="/partner/playlist",
    path_fields=(),
    query_fields=(("id", "id"), ("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_PARTNER_TRACK = Endpoint(
    key="partner.track",
    method="GET",
    path="/partner/track",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_PARTNER_TRACK_COUNT = Endpoint(
    key="partner.trackCount",
    method="GET",
    path="/partner/track/count",
    path_fields=(),
    query_fields=(("spotify_track_id", "spotify_track_id"), ("isrc", "isrc")),
    body_fields=(),
)

_PARTNER_ALBUM = Endpoint(
    key="partner.album",
    method="GET",
    path="/partner/album",
    path_fields=(),
    query_fields=(("id", "id"), ("locale", "locale"), ("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_PARTNER_ARTIST_OVERVIEW = Endpoint(
    key="partner.artistOverview",
    method="GET",
    path="/partner/artist-overview",
    path_fields=(),
    query_fields=(("id", "id"), ("locale", "locale"), ("include_prerelease", "includePrerelease")),
    body_fields=(),
)

_PARTNER_ARTIST_DISCOGRAPHY = Endpoint(
    key="partner.artistDiscography",
    method="GET",
    path="/partner/artist-discography",
    path_fields=(),
    query_fields=(("id", "id"), ("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_PLAYLISTS_GET = Endpoint(
    key="playlists.get",
    method="GET",
    path="/playlist",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_PLAYLISTS_TRACKS = Endpoint(
    key="playlists.tracks",
    method="GET",
    path="/playlist_tracks",
    path_fields=(),
    query_fields=(("id", "id"), ("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_PLAYLISTS_FROM_SEED = Endpoint(
    key="playlists.fromSeed",
    method="GET",
    path="/seed_to_playlist",
    path_fields=(),
    query_fields=(("uri", "uri"),),
    body_fields=(),
)

_SEARCH_SEARCH = Endpoint(
    key="search.search",
    method="GET",
    path="/search",
    path_fields=(),
    query_fields=(("q", "q"), ("type", "type"), ("offset", "offset"), ("limit", "limit"), ("number_of_top_results", "numberOfTopResults"), ("contrast", "contrast")),
    body_fields=(),
)

_SEARCH_TOP_RESULTS = Endpoint(
    key="search.topResults",
    method="GET",
    path="/search_top_results",
    path_fields=(),
    query_fields=(("q", "q"), ("number_of_top_results", "numberOfTopResults"), ("contrast", "contrast")),
    body_fields=(),
)

_SEARCH_LYRICS = Endpoint(
    key="search.lyrics",
    method="GET",
    path="/search_lyrics",
    path_fields=(),
    query_fields=(("q", "q"), ("format", "format")),
    body_fields=(),
)

_SEARCH_SUGGESTIONS = Endpoint(
    key="search.suggestions",
    method="GET",
    path="/search_suggestions",
    path_fields=(),
    query_fields=(("q", "q"), ("offset", "offset"), ("limit", "limit"), ("number_of_top_results", "numberOfTopResults"), ("include_authors", "includeAuthors"), ("debug", "debug"), ("timeout", "timeout"), ("contrast", "contrast")),
    body_fields=(),
)

_SEARCH_MULTI_MARKET = Endpoint(
    key="search.multiMarket",
    method="GET",
    path="/search_multi_market",
    path_fields=(),
    query_fields=(("q", "q"), ("type", "type"), ("markets", "markets"), ("limit", "limit")),
    body_fields=(),
)

_SHOWS_GET = Endpoint(
    key="shows.get",
    method="GET",
    path="/shows",
    path_fields=(),
    query_fields=(("ids", "ids"), ("market", "market")),
    body_fields=(),
)

_SHOWS_GET_BY_ID = Endpoint(
    key="shows.getById",
    method="GET",
    path="/shows/{id}",
    path_fields=(("id", "id"),),
    query_fields=(("market", "market"),),
    body_fields=(),
)

_SHOWS_EPISODES = Endpoint(
    key="shows.episodes",
    method="GET",
    path="/shows/{id}/episodes",
    path_fields=(("id", "id"),),
    query_fields=(("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_SNAPSHOTS_LIST = Endpoint(
    key="snapshots.list",
    method="GET",
    path="/playlist_snapshot",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_SNAPSHOTS_CREATE = Endpoint(
    key="snapshots.create",
    method="POST",
    path="/playlist_snapshot",
    path_fields=(),
    query_fields=(),
    body_fields=(("id", "id"), ("webhook", "webhook")),
)

_TRACKING_TRACK = Endpoint(
    key="tracking.track",
    method="POST",
    path="/tracking/track",
    path_fields=(),
    query_fields=(),
    body_fields=(("type", "type"), ("id", "id")),
)

_TRACKING_UNTRACK = Endpoint(
    key="tracking.untrack",
    method="DELETE",
    path="/tracking/untrack",
    path_fields=(),
    query_fields=(("type", "type"), ("id", "id")),
    body_fields=(),
)

_TRACKING_ITEMS = Endpoint(
    key="tracking.items",
    method="GET",
    path="/tracking/items",
    path_fields=(),
    query_fields=(("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_TRACKING_ITEM = Endpoint(
    key="tracking.item",
    method="GET",
    path="/tracking/items/{spotifyType}/{spotifyId}",
    path_fields=(("spotify_type", "spotifyType"), ("spotify_id", "spotifyId")),
    query_fields=(),
    body_fields=(),
)

_TRACKING_LOGS = Endpoint(
    key="tracking.logs",
    method="GET",
    path="/tracking/logs",
    path_fields=(),
    query_fields=(("offset", "offset"), ("limit", "limit")),
    body_fields=(),
)

_TRACKING_STATS = Endpoint(
    key="tracking.stats",
    method="GET",
    path="/tracking/stats",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_TRACKING_HEALTH = Endpoint(
    key="tracking.health",
    method="GET",
    path="/tracking/health",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_TRACKS_GET = Endpoint(
    key="tracks.get",
    method="GET",
    path="/tracks",
    path_fields=(),
    query_fields=(("ids", "ids"), ("contrast", "contrast")),
    body_fields=(),
)

_TRACKS_CREDITS = Endpoint(
    key="tracks.credits",
    method="GET",
    path="/track_credits",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_TRACKS_LYRICS = Endpoint(
    key="tracks.lyrics",
    method="GET",
    path="/track_lyrics",
    path_fields=(),
    query_fields=(("id", "id"), ("format", "format"), ("vocal_removal", "vocalRemoval")),
    body_fields=(),
)

_TRACKS_RECOMMENDATIONS = Endpoint(
    key="tracks.recommendations",
    method="GET",
    path="/recommendations",
    path_fields=(),
    query_fields=(("limit", "limit"), ("seed_tracks", "seed_tracks"), ("seed_artists", "seed_artists"), ("seed_genres", "seed_genres")),
    body_fields=(),
)

_USERS_PROFILE = Endpoint(
    key="users.profile",
    method="GET",
    path="/user_profile",
    path_fields=(),
    query_fields=(("id", "id"), ("playlist_limit", "playlistLimit"), ("artist_limit", "artistLimit"), ("episode_limit", "episodeLimit")),
    body_fields=(),
)

_USERS_FOLLOWERS = Endpoint(
    key="users.followers",
    method="GET",
    path="/user_followers",
    path_fields=(),
    query_fields=(("id", "id"),),
    body_fields=(),
)

_WEBHOOKS_GET = Endpoint(
    key="webhooks.get",
    method="GET",
    path="/webhooks",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_WEBHOOKS_REGISTER = Endpoint(
    key="webhooks.register",
    method="POST",
    path="/webhooks/register",
    path_fields=(),
    query_fields=(),
    body_fields=(("url", "url"), ("events", "events")),
)

_WEBHOOKS_STATS = Endpoint(
    key="webhooks.stats",
    method="GET",
    path="/webhooks/stats",
    path_fields=(),
    query_fields=(),
    body_fields=(),
)

_WEBHOOKS_DELETE = Endpoint(
    key="webhooks.delete",
    method="DELETE",
    path="/webhooks/{id}",
    path_fields=(("id", "id"),),
    query_fields=(),
    body_fields=(),
)

_WEBHOOKS_TEST = Endpoint(
    key="webhooks.test",
    method="POST",
    path="/webhooks/{id}/test",
    path_fields=(("id", "id"),),
    query_fields=(),
    body_fields=(),
)

_WEBHOOKS_DELIVERIES = Endpoint(
    key="webhooks.deliveries",
    method="GET",
    path="/webhooks/{id}/deliveries",
    path_fields=(("id", "id"),),
    query_fields=(),
    body_fields=(),
)

class AiResource(Resource):
    """ai endpoints."""

    def health(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /ai/health."""
        return self._invoke(_AI_HEALTH, locals())

    def types(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /ai/types."""
        return self._invoke(_AI_TYPES, locals())

    def analyze(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/analyze."""
        return self._invoke(_AI_ANALYZE, locals())

    def chart_trends(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/chart-trends."""
        return self._invoke(_AI_CHART_TRENDS, locals())

    chartTrends = chart_trends

    def artist_summary(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/artist-summary."""
        return self._invoke(_AI_ARTIST_SUMMARY, locals())

    artistSummary = artist_summary

    def album_review(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/album-review."""
        return self._invoke(_AI_ALBUM_REVIEW, locals())

    albumReview = album_review

    def track_deep_dive(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/track-deep-dive."""
        return self._invoke(_AI_TRACK_DEEP_DIVE, locals())

    trackDeepDive = track_deep_dive

    def playlist_curator(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/playlist-curator."""
        return self._invoke(_AI_PLAYLIST_CURATOR, locals())

    playlistCurator = playlist_curator

    def market_comparison(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/market-comparison."""
        return self._invoke(_AI_MARKET_COMPARISON, locals())

    marketComparison = market_comparison

    def genre_landscape(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/genre-landscape."""
        return self._invoke(_AI_GENRE_LANDSCAPE, locals())

    genreLandscape = genre_landscape

    def mood_profile(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/mood-profile."""
        return self._invoke(_AI_MOOD_PROFILE, locals())

    moodProfile = mood_profile

    def viral_potential(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/viral-potential."""
        return self._invoke(_AI_VIRAL_POTENTIAL, locals())

    viralPotential = viral_potential

    def custom(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /ai/custom."""
        return self._invoke(_AI_CUSTOM, locals())


class AlbumsResource(Resource):
    """albums endpoints."""

    def get(
        self,
        ids: IdList,
        *,
        contrast: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /albums."""
        return self._invoke(_ALBUMS_GET, locals())

    def tracks(
        self,
        id: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /album_tracks."""
        return self._invoke(_ALBUMS_TRACKS, locals())

    def metadata(
        self,
        id: str,
        *,
        contrast: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /album_metadata."""
        return self._invoke(_ALBUMS_METADATA, locals())


class AnalysisResource(Resource):
    """analysis endpoints."""

    def artist_compare(
        self,
        ids: IdList,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_compare."""
        return self._invoke(_ANALYSIS_ARTIST_COMPARE, locals())

    artistCompare = artist_compare

    def audio_features(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /audio_features."""
        return self._invoke(_ANALYSIS_AUDIO_FEATURES, locals())

    audioFeatures = audio_features

    def playlist_analysis(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /playlist_analysis."""
        return self._invoke(_ANALYSIS_PLAYLIST_ANALYSIS, locals())

    playlistAnalysis = playlist_analysis


class ArtistsResource(Resource):
    """artists endpoints."""

    def get(
        self,
        ids: IdList,
        *,
        contrast: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artists."""
        return self._invoke(_ARTISTS_GET, locals())

    def overview(
        self,
        id: str,
        *,
        contrast: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_overview."""
        return self._invoke(_ARTISTS_OVERVIEW, locals())

    def discography_overview(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_discography_overview."""
        return self._invoke(_ARTISTS_DISCOGRAPHY_OVERVIEW, locals())

    discographyOverview = discography_overview

    def albums(
        self,
        id: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_albums."""
        return self._invoke(_ARTISTS_ALBUMS, locals())

    def singles(
        self,
        id: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_singles."""
        return self._invoke(_ARTISTS_SINGLES, locals())

    def appears_on(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_appears_on."""
        return self._invoke(_ARTISTS_APPEARS_ON, locals())

    appearsOn = appears_on

    def discovered_on(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_discovered_on."""
        return self._invoke(_ARTISTS_DISCOVERED_ON, locals())

    discoveredOn = discovered_on

    def featuring(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_featuring."""
        return self._invoke(_ARTISTS_FEATURING, locals())

    def related(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_related."""
        return self._invoke(_ARTISTS_RELATED, locals())

    def top_tracks(
        self,
        id: str,
        *,
        market: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_top_tracks."""
        return self._invoke(_ARTISTS_TOP_TRACKS, locals())

    topTracks = top_tracks


class AudiobooksResource(Resource):
    """audiobooks endpoints."""

    def get(
        self,
        ids: IdList,
        *,
        market: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /audiobooks."""
        return self._invoke(_AUDIOBOOKS_GET, locals())

    def get_by_id(
        self,
        id: str,
        *,
        market: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /audiobooks/{id}."""
        return self._invoke(_AUDIOBOOKS_GET_BY_ID, locals())

    getById = get_by_id

    def chapters(
        self,
        id: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /audiobooks/{id}/chapters."""
        return self._invoke(_AUDIOBOOKS_CHAPTERS, locals())


class BatchResource(Resource):
    """batch endpoints."""

    def album_metadata(
        self,
        ids: IdList,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /album_metadata_batch."""
        return self._invoke(_BATCH_ALBUM_METADATA, locals())

    albumMetadata = album_metadata

    def artist_overview(
        self,
        ids: IdList,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /artist_overview_batch."""
        return self._invoke(_BATCH_ARTIST_OVERVIEW, locals())

    artistOverview = artist_overview

    def track_credits(
        self,
        ids: IdList,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /track_credits_batch."""
        return self._invoke(_BATCH_TRACK_CREDITS, locals())

    trackCredits = track_credits

    def track_lyrics(
        self,
        ids: IdList,
        *,
        format: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /track_lyrics_batch."""
        return self._invoke(_BATCH_TRACK_LYRICS, locals())

    trackLyrics = track_lyrics

    def track_popularity(
        self,
        ids: IdList,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /track_popularity_batch."""
        return self._invoke(_BATCH_TRACK_POPULARITY, locals())

    trackPopularity = track_popularity


class BrowseResource(Resource):
    """browse endpoints."""

    def categories(
        self,
        *,
        country: Optional[str] = None,
        locale: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /browse/categories."""
        return self._invoke(_BROWSE_CATEGORIES, locals())

    def category(
        self,
        id: str,
        *,
        country: Optional[str] = None,
        locale: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /browse/categories/{id}."""
        return self._invoke(_BROWSE_CATEGORY, locals())

    def featured_playlists(
        self,
        *,
        country: Optional[str] = None,
        locale: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /browse/featured-playlists."""
        return self._invoke(_BROWSE_FEATURED_PLAYLISTS, locals())

    featuredPlaylists = featured_playlists

    def new_releases(
        self,
        *,
        country: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /browse/new-releases."""
        return self._invoke(_BROWSE_NEW_RELEASES, locals())

    newReleases = new_releases

    def recommendations(
        self,
        *,
        seed_tracks: Optional[Sequence[str]] = None,
        seed_artists: Optional[Sequence[str]] = None,
        seed_genres: Optional[str] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /browse/recommendations."""
        return self._invoke(_BROWSE_RECOMMENDATIONS, locals())


class CacheResource(Resource):
    """cache endpoints."""

    def stats(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /cache/stats."""
        return self._invoke(_CACHE_STATS, locals())

    def invalidate(
        self,
        *,
        key: Optional[str] = None,
        pattern: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        body: Optional[Mapping[str, Any]] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /cache/invalidate."""
        return self._invoke(_CACHE_INVALIDATE, locals())


class ChartsResource(Resource):
    """charts endpoints."""

    def top_by_monthly_listeners(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /top_20_by_monthly_listeners."""
        return self._invoke(_CHARTS_TOP_BY_MONTHLY_LISTENERS, locals())

    topByMonthlyListeners = top_by_monthly_listeners

    def top200_tracks(
        self,
        *,
        period: Optional[str] = None,
        country: Optional[str] = None,
        date: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /top_200_tracks."""
        return self._invoke(_CHARTS_TOP200_TRACKS, locals())

    top200Tracks = top200_tracks

    def top_artists(
        self,
        *,
        period: Optional[str] = None,
        country: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /top_artists."""
        return self._invoke(_CHARTS_TOP_ARTISTS, locals())

    topArtists = top_artists

    def top_albums(
        self,
        *,
        period: Optional[str] = None,
        country: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /top_albums."""
        return self._invoke(_CHARTS_TOP_ALBUMS, locals())

    topAlbums = top_albums

    def viral_tracks(
        self,
        *,
        country: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /viral_tracks."""
        return self._invoke(_CHARTS_VIRAL_TRACKS, locals())

    viralTracks = viral_tracks

    def top_by_followers(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /top_20_by_followers."""
        return self._invoke(_CHARTS_TOP_BY_FOLLOWERS, locals())

    topByFollowers = top_by_followers


class ConcertsResource(Resource):
    """concerts endpoints."""

    def locations(
        self,
        query: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/concert-locations."""
        return self._invoke(_CONCERTS_LOCATIONS, locals())

    def feed(
        self,
        geo_hash: str,
        geoname_id: str,
        *,
        from_: Optional[str] = None,
        to: Optional[str] = None,
        radius_in_km: Optional[int] = None,
        concept_uris: Optional[str] = None,
        pagination_key: Optional[str] = None,
        details: Optional[bool] = None,
        details_limit: Optional[int] = None,
        parsed: Optional[bool] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/concert-feed."""
        return self._invoke(_CONCERTS_FEED, locals())

    def get(
        self,
        id: str,
        *,
        parsed: Optional[bool] = None,
        authenticated: Optional[bool] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/concert."""
        return self._invoke(_CONCERTS_GET, locals())

    def by_artist(
        self,
        id: str,
        *,
        geo_hash: Optional[str] = None,
        include_nearby: Optional[bool] = None,
        details: Optional[bool] = None,
        details_limit: Optional[int] = None,
        parsed: Optional[bool] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/artist-concerts."""
        return self._invoke(_CONCERTS_BY_ARTIST, locals())

    byArtist = by_artist

    def search_artists(
        self,
        query: str,
        *,
        geo_hash: Optional[str] = None,
        include_nearby: Optional[bool] = None,
        limit: Optional[int] = None,
        details: Optional[bool] = None,
        details_limit: Optional[int] = None,
        parsed: Optional[bool] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/search-concert-artists."""
        return self._invoke(_CONCERTS_SEARCH_ARTISTS, locals())

    searchArtists = search_artists


class CredentialsResource(Resource):
    """credentials endpoints."""

    def status(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /credentials/status."""
        return self._invoke(_CREDENTIALS_STATUS, locals())

    def redis_cookies(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /cookies/redis."""
        return self._invoke(_CREDENTIALS_REDIS_COOKIES, locals())

    redisCookies = redis_cookies


class DownloadsResource(Resource):
    """downloads endpoints."""

    def track(
        self,
        q: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /download_track."""
        return self._invoke(_DOWNLOADS_TRACK, locals())

    def soundcloud(
        self,
        q: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /download_track_sc."""
        return self._invoke(_DOWNLOADS_SOUNDCLOUD, locals())


class EpisodesResource(Resource):
    """episodes endpoints."""

    def get(
        self,
        ids: IdList,
        *,
        market: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /episodes."""
        return self._invoke(_EPISODES_GET, locals())

    def by_id(
        self,
        id: str,
        *,
        market: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /episodes/{id}."""
        return self._invoke(_EPISODES_BY_ID, locals())

    byId = by_id


class HealthResource(Resource):
    """health endpoints."""

    def ping(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /ping."""
        return self._invoke(_HEALTH_PING, locals())

    def get(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /health."""
        return self._invoke(_HEALTH_GET, locals())

    def instance(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /health/instance."""
        return self._invoke(_HEALTH_INSTANCE, locals())

    def cluster(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /health/cluster."""
        return self._invoke(_HEALTH_CLUSTER, locals())

    def cluster_strict(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /health/cluster/strict."""
        return self._invoke(_HEALTH_CLUSTER_STRICT, locals())

    clusterStrict = cluster_strict

    def proxies(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /health/proxies."""
        return self._invoke(_HEALTH_PROXIES, locals())

    def clear_proxies(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /health/proxies/clear."""
        return self._invoke(_HEALTH_CLEAR_PROXIES, locals())

    clearProxies = clear_proxies

    def clear_errors(
        self,
        body: Any = None,
        *,
        query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /health/clear-errors."""
        return self._invoke(_HEALTH_CLEAR_ERRORS, locals())

    clearErrors = clear_errors


class LookupsResource(Resource):
    """lookups endpoints."""

    def isrc(
        self,
        isrc: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /isrc_lookup."""
        return self._invoke(_LOOKUPS_ISRC, locals())

    def upc(
        self,
        upc: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /upc_lookup."""
        return self._invoke(_LOOKUPS_UPC, locals())


class MarketsResource(Resource):
    """markets endpoints."""

    def get(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /markets."""
        return self._invoke(_MARKETS_GET, locals())


class PartnerResource(Resource):
    """partner endpoints."""

    def playlist(
        self,
        id: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/playlist."""
        return self._invoke(_PARTNER_PLAYLIST, locals())

    def track(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/track."""
        return self._invoke(_PARTNER_TRACK, locals())

    def track_count(
        self,
        *,
        spotify_track_id: Optional[str] = None,
        isrc: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/track/count."""
        return self._invoke(_PARTNER_TRACK_COUNT, locals())

    trackCount = track_count

    def album(
        self,
        id: str,
        *,
        locale: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/album."""
        return self._invoke(_PARTNER_ALBUM, locals())

    def artist_overview(
        self,
        id: str,
        *,
        locale: Optional[str] = None,
        include_prerelease: Optional[bool] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/artist-overview."""
        return self._invoke(_PARTNER_ARTIST_OVERVIEW, locals())

    artistOverview = artist_overview

    def artist_discography(
        self,
        id: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /partner/artist-discography."""
        return self._invoke(_PARTNER_ARTIST_DISCOGRAPHY, locals())

    artistDiscography = artist_discography


class PlaylistsResource(Resource):
    """playlists endpoints."""

    def get(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /playlist."""
        return self._invoke(_PLAYLISTS_GET, locals())

    def tracks(
        self,
        id: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /playlist_tracks."""
        return self._invoke(_PLAYLISTS_TRACKS, locals())

    def from_seed(
        self,
        uri: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /seed_to_playlist."""
        return self._invoke(_PLAYLISTS_FROM_SEED, locals())

    fromSeed = from_seed


class SearchResource(Resource):
    """search endpoints."""

    def search(
        self,
        q: str,
        *,
        type: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        number_of_top_results: Optional[int] = None,
        contrast: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /search."""
        return self._invoke(_SEARCH_SEARCH, locals())

    def top_results(
        self,
        q: str,
        *,
        number_of_top_results: Optional[int] = None,
        contrast: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /search_top_results."""
        return self._invoke(_SEARCH_TOP_RESULTS, locals())

    topResults = top_results

    def lyrics(
        self,
        q: str,
        *,
        format: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /search_lyrics."""
        return self._invoke(_SEARCH_LYRICS, locals())

    def suggestions(
        self,
        q: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        number_of_top_results: Optional[int] = None,
        include_authors: Optional[bool] = None,
        debug: Optional[bool] = None,
        timeout: Optional[int] = None,
        contrast: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /search_suggestions."""
        return self._invoke(_SEARCH_SUGGESTIONS, locals())

    def multi_market(
        self,
        q: str,
        *,
        type: Optional[str] = None,
        markets: Optional[str] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /search_multi_market."""
        return self._invoke(_SEARCH_MULTI_MARKET, locals())

    multiMarket = multi_market


class ShowsResource(Resource):
    """shows endpoints."""

    def get(
        self,
        ids: IdList,
        *,
        market: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /shows."""
        return self._invoke(_SHOWS_GET, locals())

    def get_by_id(
        self,
        id: str,
        *,
        market: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /shows/{id}."""
        return self._invoke(_SHOWS_GET_BY_ID, locals())

    getById = get_by_id

    def episodes(
        self,
        id: str,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /shows/{id}/episodes."""
        return self._invoke(_SHOWS_EPISODES, locals())


class SnapshotsResource(Resource):
    """snapshots endpoints."""

    def list(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /playlist_snapshot."""
        return self._invoke(_SNAPSHOTS_LIST, locals())

    def create(
        self,
        *,
        id: Optional[str] = None,
        webhook: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        body: Optional[Mapping[str, Any]] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /playlist_snapshot."""
        return self._invoke(_SNAPSHOTS_CREATE, locals())


class TrackingResource(Resource):
    """tracking endpoints."""

    def track(
        self,
        type: str,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        body: Optional[Mapping[str, Any]] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /tracking/track."""
        return self._invoke(_TRACKING_TRACK, locals())

    def untrack(
        self,
        type: str,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """DELETE /tracking/untrack."""
        return self._invoke(_TRACKING_UNTRACK, locals())

    def items(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /tracking/items."""
        return self._invoke(_TRACKING_ITEMS, locals())

    def item(
        self,
        spotify_type: str,
        spotify_id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /tracking/items/{spotifyType}/{spotifyId}."""
        return self._invoke(_TRACKING_ITEM, locals())

    def logs(
        self,
        *,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /tracking/logs."""
        return self._invoke(_TRACKING_LOGS, locals())

    def stats(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /tracking/stats."""
        return self._invoke(_TRACKING_STATS, locals())

    def health(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /tracking/health."""
        return self._invoke(_TRACKING_HEALTH, locals())


class TracksResource(Resource):
    """tracks endpoints."""

    def get(
        self,
        ids: IdList,
        *,
        contrast: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /tracks."""
        return self._invoke(_TRACKS_GET, locals())

    def credits(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /track_credits."""
        return self._invoke(_TRACKS_CREDITS, locals())

    def lyrics(
        self,
        id: str,
        *,
        format: Optional[str] = None,
        vocal_removal: Optional[bool] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /track_lyrics."""
        return self._invoke(_TRACKS_LYRICS, locals())

    def recommendations(
        self,
        *,
        limit: Optional[int] = None,
        seed_tracks: Optional[Sequence[str]] = None,
        seed_artists: Optional[Sequence[str]] = None,
        seed_genres: Optional[str] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /recommendations."""
        return self._invoke(_TRACKS_RECOMMENDATIONS, locals())


class UsersResource(Resource):
    """users endpoints."""

    def profile(
        self,
        id: str,
        *,
        playlist_limit: Optional[int] = None,
        artist_limit: Optional[int] = None,
        episode_limit: Optional[int] = None,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /user_profile."""
        return self._invoke(_USERS_PROFILE, locals())

    def followers(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /user_followers."""
        return self._invoke(_USERS_FOLLOWERS, locals())


class WebhooksResource(Resource):
    """webhooks endpoints."""

    def get(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /webhooks."""
        return self._invoke(_WEBHOOKS_GET, locals())

    def register(
        self,
        *,
        url: Optional[str] = None,
        events: Optional[Sequence[str]] = None,
        extra_query: Optional[QueryParams] = None,
        body: Optional[Mapping[str, Any]] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /webhooks/register."""
        return self._invoke(_WEBHOOKS_REGISTER, locals())

    def stats(
        self,
        query: Optional[QueryParams] = None,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /webhooks/stats."""
        return self._invoke(_WEBHOOKS_STATS, locals())

    def delete(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """DELETE /webhooks/{id}."""
        return self._invoke(_WEBHOOKS_DELETE, locals())

    def test(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        body: Optional[Mapping[str, Any]] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """POST /webhooks/{id}/test."""
        return self._invoke(_WEBHOOKS_TEST, locals())

    def deliveries(
        self,
        id: str,
        *,
        extra_query: Optional[QueryParams] = None,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """GET /webhooks/{id}/deliveries."""
        return self._invoke(_WEBHOOKS_DELIVERIES, locals())


class ClientResources:
    """Static namespace annotations for :class:`SpotifyApiClient`."""

    ai: AiResource
    albums: AlbumsResource
    analysis: AnalysisResource
    artists: ArtistsResource
    audiobooks: AudiobooksResource
    batch: BatchResource
    browse: BrowseResource
    cache: CacheResource
    charts: ChartsResource
    concerts: ConcertsResource
    credentials: CredentialsResource
    downloads: DownloadsResource
    episodes: EpisodesResource
    health: HealthResource
    lookups: LookupsResource
    markets: MarketsResource
    partner: PartnerResource
    playlists: PlaylistsResource
    search: SearchResource
    shows: ShowsResource
    snapshots: SnapshotsResource
    tracking: TrackingResource
    tracks: TracksResource
    users: UsersResource
    webhooks: WebhooksResource


RESOURCE_CLASSES: Dict[str, Type[Resource]] = {
    "ai": AiResource,
    "albums": AlbumsResource,
    "analysis": AnalysisResource,
    "artists": ArtistsResource,
    "audiobooks": AudiobooksResource,
    "batch": BatchResource,
    "browse": BrowseResource,
    "cache": CacheResource,
    "charts": ChartsResource,
    "concerts": ConcertsResource,
    "credentials": CredentialsResource,
    "downloads": DownloadsResource,
    "episodes": EpisodesResource,
    "health": HealthResource,
    "lookups": LookupsResource,
    "markets": MarketsResource,
    "partner": PartnerResource,
    "playlists": PlaylistsResource,
    "search": SearchResource,
    "shows": ShowsResource,
    "snapshots": SnapshotsResource,
    "tracking": TrackingResource,
    "tracks": TracksResource,
    "users": UsersResource,
    "webhooks": WebhooksResource,
}

