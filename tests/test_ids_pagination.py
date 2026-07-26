from __future__ import annotations

from typing import Any, Dict, List

from spotify_api_sdk import collect, normalize_id, normalize_ids, paginate


def test_normalize_id_accepts_bare_uri_and_url() -> None:
    assert normalize_id("abc") == "abc"
    assert normalize_id("spotify:track:abc123") == "abc123"
    assert (
        normalize_id("https://open.spotify.com/intl-es/artist/artist123?si=x")
        == "artist123"
    )


def test_normalize_ids_accepts_strings_and_sequences() -> None:
    assert normalize_ids("spotify:track:a,b") == "a,b"
    assert normalize_ids(["spotify:track:a", "https://open.spotify.com/track/b"]) == "a,b"


def test_paginate_and_collect_are_bounded() -> None:
    calls: List[Dict[str, int]] = []

    def fetcher(*, offset: int, limit: int) -> List[int]:
        calls.append({"offset": offset, "limit": limit})
        return list(range(offset, min(offset + limit, 5)))

    pages = list(paginate(fetcher, limit=2))
    assert pages == [[0, 1], [2, 3], [4]]
    assert calls == [
        {"offset": 0, "limit": 2},
        {"offset": 2, "limit": 2},
        {"offset": 4, "limit": 2},
    ]

    calls.clear()
    assert collect(fetcher, limit=2, max_items=3) == [0, 1, 2]

