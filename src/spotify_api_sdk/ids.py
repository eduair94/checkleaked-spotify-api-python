"""Spotify ID normalization helpers."""

from __future__ import annotations

import re
from typing import Sequence

from .types import IdInput, IdList

_URI_RE = re.compile(r"^spotify:[a-z0-9]+:([A-Za-z0-9]+)$", re.IGNORECASE)
_URL_RE = re.compile(
    r"open\.spotify\.com/(?:intl-[a-z-]+/)?[a-z-]+/([A-Za-z0-9]+)",
    re.IGNORECASE,
)


def normalize_id(value: IdInput) -> str:
    """Reduce a Spotify ID, URI, or URL to its bare ID."""

    text = str(value).strip()
    uri_match = _URI_RE.search(text)
    if uri_match:
        return uri_match.group(1)
    url_match = _URL_RE.search(text)
    if url_match:
        return url_match.group(1)
    return text


def normalize_ids(value: IdList) -> str:
    """Normalize a comma-separated string or sequence and join it with commas."""

    values: Sequence[IdInput]
    if isinstance(value, str):
        values = value.split(",")
    else:
        values = list(value)
    return ",".join(
        normalized
        for normalized in (normalize_id(item) for item in values)
        if normalized
    )
