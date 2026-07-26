# API reference

Generated from the canonical TypeScript SDK and OpenAPI contract.
Pythonic `snake_case` methods also expose their npm-compatible `camelCase` aliases.

## `ai`

- `health(query=None)` — GET `/ai/health`
- `types(query=None)` — GET `/ai/types`
- `analyze(query=None, body=None)` — POST `/ai/analyze`
- `chart_trends(query=None, body=None)` (alias: `chartTrends`) — POST `/ai/chart-trends`
- `artist_summary(query=None, body=None)` (alias: `artistSummary`) — POST `/ai/artist-summary`
- `album_review(query=None, body=None)` (alias: `albumReview`) — POST `/ai/album-review`
- `track_deep_dive(query=None, body=None)` (alias: `trackDeepDive`) — POST `/ai/track-deep-dive`
- `playlist_curator(query=None, body=None)` (alias: `playlistCurator`) — POST `/ai/playlist-curator`
- `market_comparison(query=None, body=None)` (alias: `marketComparison`) — POST `/ai/market-comparison`
- `genre_landscape(query=None, body=None)` (alias: `genreLandscape`) — POST `/ai/genre-landscape`
- `mood_profile(query=None, body=None)` (alias: `moodProfile`) — POST `/ai/mood-profile`
- `viral_potential(query=None, body=None)` (alias: `viralPotential`) — POST `/ai/viral-potential`
- `custom(query=None, body=None)` — POST `/ai/custom`

## `albums`

- `get(ids, contrast=None)` — GET `/albums`
- `tracks(id, offset=None, limit=None)` — GET `/album_tracks`
- `metadata(id, contrast=None)` — GET `/album_metadata`

## `analysis`

- `artist_compare(ids)` (alias: `artistCompare`) — GET `/artist_compare`
- `audio_features(id)` (alias: `audioFeatures`) — GET `/audio_features`
- `playlist_analysis(id)` (alias: `playlistAnalysis`) — GET `/playlist_analysis`

## `artists`

- `get(ids, contrast=None)` — GET `/artists`
- `overview(id, contrast=None)` — GET `/artist_overview`
- `discography_overview(id)` (alias: `discographyOverview`) — GET `/artist_discography_overview`
- `albums(id, offset=None, limit=None)` — GET `/artist_albums`
- `singles(id, offset=None, limit=None)` — GET `/artist_singles`
- `appears_on(id)` (alias: `appearsOn`) — GET `/artist_appears_on`
- `discovered_on(id)` (alias: `discoveredOn`) — GET `/artist_discovered_on`
- `featuring(id)` — GET `/artist_featuring`
- `related(id)` — GET `/artist_related`
- `top_tracks(id, market=None)` (alias: `topTracks`) — GET `/artist_top_tracks`

## `audiobooks`

- `get(ids, market=None)` — GET `/audiobooks`
- `get_by_id(id, market=None)` (alias: `getById`) — GET `/audiobooks/{id}`
- `chapters(id, offset=None, limit=None)` — GET `/audiobooks/{id}/chapters`

## `batch`

- `album_metadata(ids)` (alias: `albumMetadata`) — GET `/album_metadata_batch`
- `artist_overview(ids)` (alias: `artistOverview`) — GET `/artist_overview_batch`
- `track_credits(ids)` (alias: `trackCredits`) — GET `/track_credits_batch`
- `track_lyrics(ids, format=None)` (alias: `trackLyrics`) — GET `/track_lyrics_batch`
- `track_popularity(ids)` (alias: `trackPopularity`) — GET `/track_popularity_batch`

## `browse`

- `categories(country=None, locale=None, limit=None, offset=None)` — GET `/browse/categories`
- `category(id, country=None, locale=None)` — GET `/browse/categories/{id}`
- `featured_playlists(country=None, locale=None, limit=None, offset=None)` (alias: `featuredPlaylists`) — GET `/browse/featured-playlists`
- `new_releases(country=None, limit=None, offset=None)` (alias: `newReleases`) — GET `/browse/new-releases`
- `recommendations(seed_tracks=None, seed_artists=None, seed_genres=None, limit=None)` — GET `/browse/recommendations`

## `cache`

- `stats(query=None)` — GET `/cache/stats`
- `invalidate(key=None, pattern=None)` — POST `/cache/invalidate`

## `charts`

- `top_by_monthly_listeners(query=None)` (alias: `topByMonthlyListeners`) — GET `/top_20_by_monthly_listeners`
- `top200_tracks(period=None, country=None, date=None)` (alias: `top200Tracks`) — GET `/top_200_tracks`
- `top_artists(period=None, country=None)` (alias: `topArtists`) — GET `/top_artists`
- `top_albums(period=None, country=None)` (alias: `topAlbums`) — GET `/top_albums`
- `viral_tracks(country=None)` (alias: `viralTracks`) — GET `/viral_tracks`
- `top_by_followers(query=None)` (alias: `topByFollowers`) — GET `/top_20_by_followers`

## `concerts`

- `locations(query)` — GET `/partner/concert-locations`
- `feed(geo_hash, geoname_id, from_=None, to=None, radius_in_km=None, concept_uris=None, pagination_key=None, details=None, details_limit=None, parsed=None)` — GET `/partner/concert-feed`
- `get(id, parsed=None, authenticated=None)` — GET `/partner/concert`
- `by_artist(id, geo_hash=None, include_nearby=None, details=None, details_limit=None, parsed=None)` (alias: `byArtist`) — GET `/partner/artist-concerts`
- `search_artists(query, geo_hash=None, include_nearby=None, limit=None, details=None, details_limit=None, parsed=None)` (alias: `searchArtists`) — GET `/partner/search-concert-artists`

## `credentials`

- `status(query=None)` — GET `/credentials/status`
- `redis_cookies(query=None)` (alias: `redisCookies`) — GET `/cookies/redis`

## `downloads`

- `track(q)` — GET `/download_track`
- `soundcloud(q)` — GET `/download_track_sc`

## `episodes`

- `get(ids, market=None)` — GET `/episodes`
- `by_id(id, market=None)` (alias: `byId`) — GET `/episodes/{id}`

## `health`

- `ping(query=None)` — GET `/ping`
- `get(query=None)` — GET `/health`
- `instance(query=None)` — GET `/health/instance`
- `cluster(query=None)` — GET `/health/cluster`
- `cluster_strict(query=None)` (alias: `clusterStrict`) — GET `/health/cluster/strict`
- `proxies(query=None)` — GET `/health/proxies`
- `clear_proxies(query=None, body=None)` (alias: `clearProxies`) — POST `/health/proxies/clear`
- `clear_errors(query=None, body=None)` (alias: `clearErrors`) — POST `/health/clear-errors`

## `lookups`

- `isrc(isrc)` — GET `/isrc_lookup`
- `upc(upc)` — GET `/upc_lookup`

## `markets`

- `get(query=None)` — GET `/markets`

## `partner`

- `playlist(id, offset=None, limit=None)` — GET `/partner/playlist`
- `track(id)` — GET `/partner/track`
- `track_count(spotify_track_id=None, isrc=None)` (alias: `trackCount`) — GET `/partner/track/count`
- `album(id, locale=None, offset=None, limit=None)` — GET `/partner/album`
- `artist_overview(id, locale=None, include_prerelease=None)` (alias: `artistOverview`) — GET `/partner/artist-overview`
- `artist_discography(id, offset=None, limit=None)` (alias: `artistDiscography`) — GET `/partner/artist-discography`

## `playlists`

- `get(id)` — GET `/playlist`
- `tracks(id, offset=None, limit=None)` — GET `/playlist_tracks`
- `from_seed(uri)` (alias: `fromSeed`) — GET `/seed_to_playlist`

## `search`

- `search(q, type=None, offset=None, limit=None, number_of_top_results=None, contrast=None)` — GET `/search`
- `top_results(q, number_of_top_results=None, contrast=None)` (alias: `topResults`) — GET `/search_top_results`
- `lyrics(q, format=None)` — GET `/search_lyrics`
- `suggestions(q, offset=None, limit=None, number_of_top_results=None, include_authors=None, debug=None, timeout=None, contrast=None)` — GET `/search_suggestions`
- `multi_market(q, type=None, markets=None, limit=None)` (alias: `multiMarket`) — GET `/search_multi_market`

## `shows`

- `get(ids, market=None)` — GET `/shows`
- `get_by_id(id, market=None)` (alias: `getById`) — GET `/shows/{id}`
- `episodes(id, offset=None, limit=None)` — GET `/shows/{id}/episodes`

## `snapshots`

- `list(id)` — GET `/playlist_snapshot`
- `create(id=None, webhook=None)` — POST `/playlist_snapshot`

## `tracking`

- `track(type, id)` — POST `/tracking/track`
- `untrack(type, id)` — DELETE `/tracking/untrack`
- `items(offset=None, limit=None)` — GET `/tracking/items`
- `item(spotify_type, spotify_id)` — GET `/tracking/items/{spotifyType}/{spotifyId}`
- `logs(offset=None, limit=None)` — GET `/tracking/logs`
- `stats(query=None)` — GET `/tracking/stats`
- `health(query=None)` — GET `/tracking/health`

## `tracks`

- `get(ids, contrast=None)` — GET `/tracks`
- `credits(id)` — GET `/track_credits`
- `lyrics(id, format=None, vocal_removal=None)` — GET `/track_lyrics`
- `recommendations(limit=None, seed_tracks=None, seed_artists=None, seed_genres=None)` — GET `/recommendations`

## `users`

- `profile(id, playlist_limit=None, artist_limit=None, episode_limit=None)` — GET `/user_profile`
- `followers(id)` — GET `/user_followers`

## `webhooks`

- `get(query=None)` — GET `/webhooks`
- `register(url=None, events=None)` — POST `/webhooks/register`
- `stats(query=None)` — GET `/webhooks/stats`
- `delete(id)` — DELETE `/webhooks/{id}`
- `test(id)` — POST `/webhooks/{id}/test`
- `deliveries(id)` — GET `/webhooks/{id}/deliveries`

