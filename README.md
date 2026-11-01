# checkleaked-spotify-api

[![PyPI version](https://img.shields.io/pypi/v/checkleaked-spotify-api.svg)](https://pypi.org/project/checkleaked-spotify-api/)
[![Python versions](https://img.shields.io/pypi/pyversions/checkleaked-spotify-api.svg)](https://pypi.org/project/checkleaked-spotify-api/)
[![CI](https://github.com/eduair94/checkleaked-spotify-api-python/actions/workflows/ci.yml/badge.svg)](https://github.com/eduair94/checkleaked-spotify-api-python/actions/workflows/ci.yml)
[![license: MIT](https://img.shields.io/pypi/l/checkleaked-spotify-api.svg)](./LICENSE)

Typed Python SDK for the **Spotify Data API**, covering the same 108 methods
and 23 namespaces as
[`@checkleaked/spotify-api`](https://www.npmjs.com/package/@checkleaked/spotify-api).
It works with both the
[RapidAPI spotify81 API](https://rapidapi.com/airaudoeduardo/api/spotify81)
and the direct
[CheckLeaked API](https://spotify-proxy.checkleaked.cc/docs).

This is a data API client. It does not require Spotify OAuth credentials.

**Links:** [Website and live demo](https://spotify.checkleaked.cc) ·
[API reference](https://spotify-proxy.checkleaked.cc/docs) ·
[Status page](https://spotify.checkleaked.cc/status) ·
[Pricing](https://spotify.checkleaked.cc/pricing) ·
[Changelog](./CHANGELOG.md) · Support: admin@checkleaked.cc

**Guides:** [Spotify play count API](https://spotify.checkleaked.cc/spotify-play-count-api) ·
[Spotify monthly listeners API](https://spotify.checkleaked.cc/spotify-monthly-listeners-api) ·
[Spotify lyrics API](https://spotify.checkleaked.cc/spotify-lyrics-api) ·
[Spotify Web API alternative](https://spotify.checkleaked.cc/spotify-web-api-alternative)

## Install

```bash
pip install checkleaked-spotify-api
```

## Quick start

```python
from spotify_api_sdk import SpotifyApiClient

spotify = SpotifyApiClient(api_key="your-rapidapi-key")

# Play counts for up to 50 tracks per call
counts = spotify.tracks.counts(
    ["0VjIjW4GlUZAMYd2vXMi3b", "spotify:track:7ouMYWpwJ422jRcDASZB7P"]
)

results = spotify.search.search(
    "daft punk",
    type="artists",
    limit=5,
)

# slim=True drops the heavy blocks; stats and top tracks are kept
artist = spotify.artists.overview(
    "spotify:artist:4tZwfgrHOc3mvqYlEYSvVi",
    slim=True,
)

lyrics = spotify.tracks.lyrics(
    "https://open.spotify.com/track/0DiWol3AO6WpXZgp0goxAV",
    format="lrc",
)

status = spotify.status()  # per-endpoint-family service status
```

Methods return the API's payload. Endpoints that wrap it in
`{success, data, metadata}` are unwrapped to `data`; use
`client.request_raw(...)` when you need the complete envelope.

## Play counts

| Need | Method |
| --- | --- |
| Many tracks (up to 50 per call) | `tracks.counts(ids)` |
| One track, by id or ISRC | `partner.track_count(spotify_track_id=...)` / `(isrc=...)` |
| Track + album + artists + play count | `partner.track(id, slim=True)` |
| Every track of an album | `partner.album(id)` or `albums.tracks(id)` |
| Every track of a playlist | `partner.playlist(id)` |

Spotify reports `0` for tracks with fewer than 1,000 plays. `tracks.counts`
needs an API release that serves `/partner/tracks/count`; an older deployment
answers 404, so fall back to `partner.track_count()` per id.

## Extra data (`include`)

Several methods take an `include` option (a list or a comma-separated
string) that adds data the plain response lacks, in the same call. Each option
costs some extra time; a value that could not be fetched is `None`, never an
error, and the response's `include_status` says how many resolved.

| Method | `include` options |
| --- | --- |
| `tracks.get` | `insights` (genres, moods, activities, BPM, credits, lyrics flag, languages), `playcount`, `total_tracks` |
| `albums.get` | `playcounts` (on every album track) |
| `artists.get` | `stats` (followers, monthly listeners, world rank, top cities), `insights` |
| `artists.overview` | `insights` (in `data.artistUnion.insights`) |
| `playlists.tracks`, `tracks.recommendations`, `search.search` (track hits) | `insights`, `playcount` |
| `charts.top200_tracks`, `charts.viral_tracks` | `insights`, `playcount` (in each entry's `trackMetadata`) |

```python
page = spotify.playlists.tracks("37i9dQZF1DXcBWIGoYBM5M", include=["playcount", "insights"])
hits = spotify.search.search("get lucky", type="tracks", limit=10, include="playcount")
```

These options need the 2026-10-21 API release; an older deployment ignores
`include` (or answers 404 for the `insights` methods).

## Providers

RapidAPI is the default and automatically adds
`x-rapidapi-host: spotify81.p.rapidapi.com`:

```python
spotify = SpotifyApiClient(
    api_key="your-rapidapi-key",
    provider="rapidapi",
)
```

The direct API exposes the same methods and paths. Use a key issued by the
direct portal:

```python
spotify = SpotifyApiClient(
    api_key="your-direct-api-key",
    provider="proxy",
)
```

The API key may be omitted when `SPOTIFY_API_KEY` or `RAPIDAPI_KEY` is set.

## Pythonic and npm-compatible names

Python methods use `snake_case`, while npm-style `camelCase` aliases are also
available:

```python
spotify.artists.top_tracks(id, market="US")
spotify.artists.topTracks(id, market="US")  # exact npm-style alias
```

Every method supports per-call `request_timeout`, `request_retries`,
`request_headers`, and an additional `extra_query` mapping. POST methods also
accept a free-form `body` mapping. The `timeout` argument of
`search.search()` is different: it is the API's own search budget in
milliseconds, and it can only shorten a search, which ends within about 20
seconds anyway.

Responses are cached for a while (play counts about an hour, catalog objects up
to a day). Pass `extra_query={"cache": "false"}` to skip the cached copy; a
given URL is refreshed at most once every 10 seconds.

## IDs, URIs, and URLs

Spotify IDs may be supplied as bare IDs, Spotify URIs, or open.spotify.com
URLs. Multi-ID methods accept comma-separated strings or Python sequences.

```python
from spotify_api_sdk import normalize_id, normalize_ids

normalize_id("spotify:track:0DiWol3AO6WpXZgp0goxAV")
normalize_ids([
    "spotify:artist:4tZwfgrHOc3mvqYlEYSvVi",
    "https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02",
])
```

Spotify relinks some tracks to another id in a market: `tracks.get` then
returns an object whose `id` differs from the one you asked for, with
`linked_from.id` set to your id.

`tracks.get`, `albums.get` and `artists.get` leave out ids they have no object
for and list them in one of two arrays: `missing` means Spotify does not know
the id (asking again will not help); `unavailable` means it could not be
fetched this time, so ask for those ids again later. When none of the ids
could be fetched, the call raises a 503 `UPSTREAM_UNAVAILABLE` error instead
(retried automatically). `tracks.get_by_id` raises 404 for an id Spotify does
not know and 503 when it could not be fetched.

```python
result = spotify.tracks.get(ids)
retry_later = result.get("unavailable", [])  # ask again later
not_on_spotify = result.get("missing", [])   # drop for good
```

## Pagination

```python
from spotify_api_sdk import collect

items = collect(
    lambda **page: spotify.artists.albums(id=artist_id, **page),
    get_items=lambda response: (
        response.get("data", {})
        .get("artist", {})
        .get("discography", {})
        .get("albums", {})
        .get("items", [])
    ),
    limit=50,
    max_items=500,
)
```

## Errors

Every failure raises a `SpotifyApiError` subclass. A 2xx body that reports a
failure (`success: false`, `error: true`, or an error `code` such as
`LYRICS_NOT_AVAILABLE` for a track without lyrics) raises too.

```python
from spotify_api_sdk import (
    AuthError,
    HttpError,
    RateLimitError,
    SpotifyApiError,
    TimeoutError,
)

try:
    spotify.search.search("daft punk")
except RateLimitError as error:
    print(error.code, error.retry_after_ms)  # RATE_LIMITED / QUOTA_EXCEEDED
except AuthError:
    print("Invalid or unsubscribed API key")
except SpotifyApiError as error:
    print(error.status, error.code, error.request_id, error.param, error.retryable)
```

| HTTP | `code` | Meaning |
| --- | --- | --- |
| 400 | `INVALID_PARAMETER`, `MISSING_PARAMETER` | Fix the request (`error.param`) |
| 401 | `MISSING_API_KEY`, `INVALID_API_KEY`, `KEY_REVOKED`, `KEY_EXPIRED` | Key problem |
| 404 | `NOT_FOUND`, `UNKNOWN_ENDPOINT` | Entity or route does not exist |
| 422 | `VIDEO_UNAVAILABLE`, `AGE_RESTRICTED`, `PREMIUM_ONLY` | Downloads only |
| 429 | `RATE_LIMITED`, `QUOTA_EXCEEDED` | **Your** rate limit or quota |
| 503 | `UPSTREAM_UNAVAILABLE`, `UPSTREAM_THROTTLED`, `UPSTREAM_TIMEOUT`, `LOAD_SHED` | Temporary, retried automatically |
| 503 | `OUTCOME_UNKNOWN` | A request that changes something may or may not have run: never retried automatically, check its effect first |

Spotify-side problems arrive as 503 with `Retry-After`, never as 401/429.
The API never answers 502 or 504: a request that runs out of time is a 503
`UPSTREAM_TIMEOUT` (it was a 504 before 2026-10). A plain-text 502, 504 or
524 comes from the network edge: a 504 or 524 (the edge stopped waiting, after
about 100 s) counts as a timeout, a 502 is retried like any other 5xx.
429 and 5xx responses are retried with backoff, honoring `Retry-After` (or the
body's `retry_after_s`); errors that waiting cannot fix (`QUOTA_EXCEEDED`, a
bad or revoked key, `retryable: false`) are raised immediately. No single wait
is longer than `max_retry_delay` (default 10 seconds), even when `Retry-After`
asks for more (`error.retry_after_ms` still reports what the API asked for).
A timeout (a 503 whose `code` is `UPSTREAM_TIMEOUT`, or a 504 or 524 from the
edge) means the API already spent its whole time budget on the request, so it
is retried at most `gateway_timeout_retries` times (default once); every
other 5xx can use all `retries`.
Quote `error.request_id` when you contact support.

## Tracking and webhooks

```python
spotify.tracking.track("artist", "06HL4z0CvFAxyc27GXpf02", label="Taylor")
changes = spotify.tracking.logs(
    spotify_type="artist",
    change_type="monthly_listeners_change",
)

spotify.webhooks.register(
    "37i9dQZF1DXcBWIGoYBM5M",
    "https://example.com/spotify-hook",
    events=["playlist.tracks.added", "playlist.tracks.removed"],
)
```

Tracked items and webhooks belong to the calling account; RapidAPI identifies
you automatically. Tracking also works with a direct API key; webhooks are not
available with direct API keys yet.

## Configuration

```python
spotify = SpotifyApiClient(
    api_key="...",
    provider="rapidapi",   # rapidapi (default) | proxy
    timeout=30,
    retries=2,
    retry_delay=0.5,
    max_retry_delay=10,          # longest wait before a retry, in seconds
    gateway_timeout_retries=1,   # retries a timeout may use (0 = never)
    headers={"x-my-header": "value"},
    debug=True,
    on_request=lambda info: print("request", info["url"]),
    on_response=lambda info: print("response", info["status"]),
    on_retry=lambda info: print("retry", info["attempt"]),
)
```

The client is also a context manager:

```python
with SpotifyApiClient(api_key="...") as spotify:
    markets = spotify.markets.get()
```

See [API_REFERENCE.md](./API_REFERENCE.md) for every namespace and method.
