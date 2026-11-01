# Changelog

## 2.1.1 - 2026-11-01

Documentation only: the README links the Spotify Data MCP server.

## 2.1.0 - 2026-11-01

Matches `@checkleaked/spotify-api` 2.1.0.

### Added

- `tracks.insights(ids=...)` (`GET /track_insights`): genres,
  moods and activities with Spotify's weights, BPM, credits with roles, the
  30-second preview MP3, `has_lyrics`, vocal languages, ISRC and release date
  for up to 50 tracks per call. Entries in request order with `status` (`ok`,
  `not_found`, `error`), plus `missing` and `unavailable`.
- `artists.insights(ids=...)` (`GET /artist_insights`): genres, moods and
  activities with weights and the tempo range of up to 20 artists, aggregated
  from Spotify's descriptors of each artist's top tracks.
- `include` option on `tracks.get` (`insights`, `playcount`, `total_tracks`),
  `albums.get` (`playcounts`) and `artists.get` (`stats`, `insights`): play
  counts, genres / moods / BPM and artist stats in the same call (pass a
  list or a comma-separated string). Responses carry `include_status`.
- `include` option on `playlists.tracks`, `tracks.recommendations`,
  `search.search` (tracks bucket), `charts.top200_tracks` and
  `charts.viral_tracks` (in each entry's `trackMetadata`; `insights`,
  `playcount`), and `artists.overview` (`insights`): every track's
  lifetime play count (user
  playlists included) and genres / moods / BPM / credits.
- User agent `checkleaked-spotify-api-python/2.1.0`.

### API changes this release documents (2026-10-21)

- `tracks.get` (and album tracks in `albums.get`) now fill `preview_url` for
  most tracks (it was always `None`), and album tracks list their own artists
  (featured artists included) instead of repeating the album artists.

## 2.0.1 - 2026-10-14

Matches `@checkleaked/spotify-api` 2.0.1 (the first 2.x release on npm) and
the Spotify Data API as of 2026-10-13. 2.0.0 was built before the API started
answering timeouts as 503, so it spends every retry on them: upgrade.

### Changed

- A timeout counts against `gateway_timeout_retries` (default 1) in every
  form it arrives in: a 503 whose `code` is `UPSTREAM_TIMEOUT` (the API's
  answer since 2026-10), an HTTP 504, or Cloudflare's HTTP 524 (the API did
  not answer within about 100 s). 2.0.0 recognised only the 504, so it used
  every retry on a 503 timeout or a 524. Other 5xx, a plain-text 502 from the
  network edge included, still use every retry.
- User agent `checkleaked-spotify-api-python/2.0.1`.

### API changes this release documents (2026-10-13)

- Timeouts are HTTP 503 with `code` `UPSTREAM_TIMEOUT` and `Retry-After: 5`
  (they were 504 with `Retry-After: 30`): the network edge in front of the API
  replaced 502/504 bodies with plain text. The API answers no 502 or 504 at
  all now; lane failures that were 502 are 503 `UPSTREAM_UNAVAILABLE`. A 503
  that names no other wait carries `Retry-After: 5`, and the 503 bodies some
  endpoints build themselves (`/upc_lookup`, `/artist_compare`,
  `/playlist_analysis`, `/browse/*`) now carry every error field (`retryable`,
  `status`, `retry_after_s`, `timestamp`).
- These returned `None` (an HTTP 200 with an empty body) when Spotify did not
  answer, and now raise a 503 that the SDK retries: `artists.top_tracks`
  (`UPSTREAM_UNAVAILABLE`), `browse.categories` and
  `browse.featured_playlists` (`UPSTREAM_TIMEOUT`), and `lookups.isrc`
  (`UPSTREAM_TIMEOUT` after about 12 s).
- `lookups.isrc` and `lookups.upc` raise 404 for an ISRC or UPC Spotify does
  not have, and a repeat within about 10 minutes raises the same 404 at once.
  `lookups.upc` answers 404 only when Spotify answered for every barcode form
  (as given, padded to 14 digits, and the 12-digit UPC-A form); when one of
  those searches failed it raises 503 `UPSTREAM_UNAVAILABLE` (retried) instead
  of a 404, or of an album only the shorter UPC-A form matched (that form can
  match another album). Its timeouts and lane failures are 503 (they were 504
  and 502).
- `tracks.get_by_id`: every error the route itself answers has Spotify's
  `error` object (`error.body["error"]["status"]`), the 503 for a track that
  could not be fetched included, also through the direct API; a timeout is 503
  `UPSTREAM_TIMEOUT` (was 504). The exception is a 503 `LOAD_SHED` from the
  overload guard, which any route can answer and whose `error.body["error"]`
  is `True`: branch on `error.code` first.
- A 503 `OUTCOME_UNKNOWN` (new code) means a request that changes something
  (e.g. `webhooks.test`, `tracking.track`, `snapshots.create`) may or may not
  have run: it is never retried automatically (`retryable` is `False`, no
  `Retry-After`; added to `NON_RETRYABLE_CODES`). Check its effect before
  sending it again.
- `error.code` changes on 400s that moved to the standard envelope:
  `MISSING_PARAMETER` / `INVALID_PARAMETER` instead of the title strings on
  every `/partner/*` parameter error; `INVALID_PARAMETER` instead of
  `Too many ids` on `/albums` with more than 50 ids; `INVALID_PARAMETER`
  instead of `pagination_not_supported` on `/artist_appears_on` and
  `/artist_discovered_on` with `offset` / `limit` (the reason stays in
  `error.body["reason"]`); `MISSING_PARAMETER` / `INVALID_PARAMETER` (was
  `None`) on `/search` with an invalid `type` and on `/search_top_results`,
  `/search_suggestions` and `/search_lyrics` without `q`. Every old body field
  is still in `error.body`.

## 2.0.0 - 2026-10-13

Released on PyPI on 2026-10-13. Matches the Spotify Data API spec 1.2.0
(`@checkleaked/spotify-api` 2.0.0 was never published to npm; its first 2.x
release is 2.0.1). Prepared as 1.1.0 (never published) and released as a
major version because of the breaking changes below, so `~=1.0` and `<2` pins
do not pick it up automatically.

### Breaking changes

- 2xx responses that report a failure now raise (1.0 returned them as data):
  `success: false`, `error: true`, or an error `code` such as
  `LYRICS_NOT_AVAILABLE`. Catch `LYRICS_NOT_AVAILABLE` if a track without
  lyrics is a normal result for you.
- `error.code` is the API's machine-readable `code` (e.g.
  `INVALID_PARAMETER`) instead of the `error` title, and `error: true` is no
  longer reported as the code `"True"`.
- Removed the operator-only methods (they need an operator key):
  `health.proxies`, `health.clear_proxies`, `health.clear_errors`, the `cache`
  namespace (`stats`, `invalidate`) and the `credentials` namespace (`status`,
  `redis_cookies`).
- Renamed keyword arguments: `tracking.track(type=..., id=...)` and
  `tracking.untrack(type=..., id=...)` are now `spotify_type=` /
  `spotify_id=` (positional calls such as `track("track", "<id>")` still
  work), and `analysis.audio_features(id=...)` is now `ids=`.
- `webhooks.register` takes `(playlist_id, callback_url, events=None,
  secret=None)` instead of the keyword-only `url=` (1.0's call never worked;
  see Fixed).
- `snapshots.list()` entries no longer contain `capturedBy`: the API stopped
  returning who took a snapshot.

### Added

- `client.status()` (also `client.health.status()`): public service status from
  `GET /status`, with per-endpoint-family success rates and latency.
- `client.tracks.counts(ids)`: play counts for up to 50 tracks in one call
  (`GET /partner/tracks/count`). API deployments older than 1.2.0 answer 404;
  fall back to `partner.track_count()` per id.
- `client.tracks.get_by_id(id, market=None)`: `GET /tracks/{id}`, which answers
  404 for an id Spotify does not know.
- `market` on `albums.get`, `artists.get`, `playlists.get`, `playlists.tracks`,
  `search.search`, `lookups.upc`, `tracks.recommendations` and
  `browse.recommendations`.
- `slim` on `partner.track`, `artists.overview` and `partner.artist_overview`
  (drops the heavy embedded blocks; play counts and stats are kept).
- More typed parameters: chart `date` on every Spotify chart and `city` on the
  top 200; the download options; `include_audiobooks` and `timeout` on search;
  the top-results flags; browse category section paging; snapshot list paging;
  tracking log filters; `limit` on webhook deliveries; `vocal_removal` on batch
  lyrics.
- Errors expose `request_id`, `retryable`, `param` and `retry_after_ms`
  (now on every error, not only `RateLimitError`).
- Client options `max_retry_delay` (seconds, default 10) and
  `gateway_timeout_retries` (default 1).

### Changed

- Errors reported inside a 2xx body now raise: `success: false`, `error: true`,
  or an error `code` such as `LYRICS_NOT_AVAILABLE`.
- `error.code` prefers the API's machine-readable `code` over the `error`
  title, and `error: true` is no longer reported as the code `"True"`.
- 429 and 5xx responses are not retried when waiting cannot help
  (`QUOTA_EXCEEDED`, a revoked or invalid key, `retryable: false`, or
  RapidAPI's monthly-quota message). RapidAPI's message-only 429s get the code
  `QUOTA_EXCEEDED` or `RATE_LIMITED`.
- Retry waits fall back to the body's `retry_after_s` when there is no
  `Retry-After` header.
- A wait before a retry never exceeds `max_retry_delay` (default 10 s), even
  when `Retry-After` asks for more (the API sends up to 30 s on 503/504); the
  error's `retry_after_ms` still reports the requested wait.
- A 504 (`UPSTREAM_TIMEOUT`) is retried at most `gateway_timeout_retries`
  times (default once): the API already spent its whole time budget on that
  request. With the defaults, a call whose every attempt times out after 20 s
  now gives up after about 50 s instead of about 2 minutes.
- User agent `checkleaked-spotify-api-python/2.0.0`; the package homepage now
  points to the API reference.
- Docs: `search.search(timeout=...)` is the API's search budget in
  milliseconds and can only shorten a search (about 20 s at most);
  `tracks.get`, `albums.get` and `artists.get` list ids Spotify does not know
  in `missing` and ids to retry later in `unavailable`; `tracks.get_by_id`
  raises 404 for an unknown id and 503 when it could not be fetched; webhooks
  need a RapidAPI account.

### Fixed

- `tracking.track` / `tracking.untrack` send `spotifyType` / `spotifyId` (and
  `label`), the names the API reads. 1.0 sent `type` / `id` and always got a
  400. The positional order is unchanged (`track("track", "<id>")`), and
  Spotify URIs/URLs are reduced to bare ids.
- `webhooks.register(playlist_id, callback_url, events=None, secret=None)`
  sends the body the API expects. 1.0 sent `url`, which always failed.
- `analysis.audio_features(ids)` sends `ids`. 1.0 sent `id`, which the API
  rejects.

### Removed

- Operator-only methods, which now need an operator key: `health.proxies`,
  `health.clear_proxies`, `health.clear_errors`, the `cache` namespace
  (`stats`, `invalidate`) and the `credentials` namespace (`status`,
  `redis_cookies`).

### Deprecated

- `health.instance`, `health.cluster` and `health.cluster_strict`: internal
  diagnostics, use `status()`.
- Parameters the API ignores, kept for compatibility: `country` on
  `browse.categories` and `browse.featured_playlists`, `authenticated` on
  `concerts.get`, `webhook` on `snapshots.create`, `contrast` on
  `search.top_results`, `period` on `charts.top_albums`, `offset` / `limit` on
  `tracking.items`.

## 1.0.0 - 2026-07-26

- Initial Python release matching `@checkleaked/spotify-api`.
- 110 methods across all 25 Spotify Data API namespaces.
- RapidAPI `spotify81` and direct CheckLeaked proxy provider presets.
- Typed parameters, Spotify ID/URI/URL normalization, pagination helpers,
  retries, timeouts, lifecycle hooks, structured errors, and sync context
  manager support.
