# checkleaked-spotify-api

[![PyPI version](https://img.shields.io/pypi/v/checkleaked-spotify-api.svg)](https://pypi.org/project/checkleaked-spotify-api/)
[![Python versions](https://img.shields.io/pypi/pyversions/checkleaked-spotify-api.svg)](https://pypi.org/project/checkleaked-spotify-api/)
[![CI](https://github.com/eduair94/checkleaked-spotify-api-python/actions/workflows/ci.yml/badge.svg)](https://github.com/eduair94/checkleaked-spotify-api-python/actions/workflows/ci.yml)
[![license: MIT](https://img.shields.io/pypi/l/checkleaked-spotify-api.svg)](./LICENSE)

Typed Python SDK for the **Spotify Data API**, covering the same 110 methods
and 25 namespaces as
[`@checkleaked/spotify-api`](https://www.npmjs.com/package/@checkleaked/spotify-api).
It works with both the
[RapidAPI spotify81 API](https://rapidapi.com/airaudoeduardo/api/spotify81)
and the direct
[CheckLeaked proxy](https://spotify-proxy.checkleaked.cc/docs).

This is a data API client. It does not require Spotify OAuth credentials.

## Install

```bash
pip install checkleaked-spotify-api
```

## Quick start

```python
from spotify_api_sdk import SpotifyApiClient

spotify = SpotifyApiClient(api_key="your-rapidapi-key")

results = spotify.search.search(
    "daft punk",
    type="artists",
    limit=5,
)

artist = spotify.artists.overview(
    "spotify:artist:4tZwfgrHOc3mvqYlEYSvVi"
)

lyrics = spotify.tracks.lyrics(
    "https://open.spotify.com/track/0DiWol3AO6WpXZgp0goxAV",
    format="lrc",
)
```

Methods return the API's unwrapped `data` payload. Use
`client.request_raw(...)` when you need the complete success envelope.

## Providers

RapidAPI is the default and automatically adds
`x-rapidapi-host: spotify81.p.rapidapi.com`:

```python
spotify = SpotifyApiClient(
    api_key="your-rapidapi-key",
    provider="rapidapi",
)
```

The direct proxy exposes the same methods and paths. Use a key issued by the
direct portal:

```python
spotify = SpotifyApiClient(
    api_key="your-direct-proxy-key",
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
accept a free-form `body` mapping.

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
    print(error.retry_after_ms)
except AuthError:
    print("Invalid or unsubscribed API key")
except SpotifyApiError as error:
    print(error.status, error.code, error.url)
```

## Configuration

```python
spotify = SpotifyApiClient(
    api_key="...",
    provider="rapidapi",   # rapidapi (default) | proxy
    timeout=30,
    retries=2,
    retry_delay=0.5,
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
