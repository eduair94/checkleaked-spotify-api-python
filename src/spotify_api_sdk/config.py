"""Client configuration and provider presets."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any, Callable, Dict, Mapping, Optional, Union

from .errors import ValidationError

RAPIDAPI_BASE_URL = "https://spotify81.p.rapidapi.com"
RAPIDAPI_HOST = "spotify81.p.rapidapi.com"
PROXY_BASE_URL = "https://spotify-proxy.checkleaked.cc/spotify-data"
DEFAULT_USER_AGENT = (
    "checkleaked-spotify-api-python/1.0.0 "
    "(+https://pypi.org/project/checkleaked-spotify-api/)"
)

Hook = Callable[[Mapping[str, Any]], None]
Debug = Union[bool, Callable[[str, Optional[Any]], None]]


@dataclass(frozen=True)
class Channel:
    """A resolved base URL and its optional RapidAPI host header."""

    base_url: str
    host: Optional[str] = None


@dataclass
class ResolvedConfig:
    api_key: str
    provider: str
    channel: Channel
    timeout_s: float
    retries: int
    retry_delay_s: float
    headers: Dict[str, str]
    user_agent: str
    session: Any
    debug: Optional[Callable[[str, Optional[Any]], None]]
    on_request: Optional[Hook]
    on_response: Optional[Hook]
    on_retry: Optional[Hook]


def _debug_logger(value: Debug) -> Optional[Callable[[str, Optional[Any]], None]]:
    if value is True:
        def log(message: str, detail: Optional[Any] = None) -> None:
            suffix = "" if detail is None else f" {detail!r}"
            print(f"[spotify-api] {message}{suffix}")

        return log
    if callable(value):
        return value
    return None


def resolve_config(
    api_key: Optional[str] = None,
    *,
    provider: str = "rapidapi",
    transport: Optional[str] = None,
    base_url: Optional[str] = None,
    host: Optional[str] = None,
    timeout: float = 30.0,
    retries: int = 2,
    retry_delay: float = 0.5,
    headers: Optional[Mapping[str, str]] = None,
    user_agent: Optional[str] = None,
    session: Any = None,
    debug: Debug = False,
    on_request: Optional[Hook] = None,
    on_response: Optional[Hook] = None,
    on_retry: Optional[Hook] = None,
) -> ResolvedConfig:
    """Resolve and validate a client configuration."""

    if transport is not None:
        provider = transport
    if provider not in ("rapidapi", "proxy"):
        raise ValidationError(
            f"Invalid provider: {provider!r}. Expected 'rapidapi' or 'proxy'.",
            code="CONFIG",
        )

    resolved_key = (
        api_key
        or os.environ.get("SPOTIFY_API_KEY")
        or os.environ.get("RAPIDAPI_KEY")
    )
    if not isinstance(resolved_key, str) or not resolved_key.strip():
        raise ValidationError(
            "api_key is required (or set SPOTIFY_API_KEY / RAPIDAPI_KEY)",
            code="CONFIG",
        )
    if timeout <= 0:
        raise ValidationError("timeout must be greater than 0", code="CONFIG")
    if retry_delay < 0:
        raise ValidationError("retry_delay must be at least 0", code="CONFIG")

    if provider == "rapidapi":
        channel = Channel(
            base_url=(base_url or RAPIDAPI_BASE_URL).rstrip("/"),
            host=RAPIDAPI_HOST if host is None else host,
        )
    else:
        channel = Channel(
            base_url=(base_url or PROXY_BASE_URL).rstrip("/"),
            host=host,
        )

    if session is None:
        import requests

        session = requests.Session()

    return ResolvedConfig(
        api_key=resolved_key.strip(),
        provider=provider,
        channel=channel,
        timeout_s=float(timeout),
        retries=max(0, int(retries)),
        retry_delay_s=float(retry_delay),
        headers=dict(headers or {}),
        user_agent=user_agent or DEFAULT_USER_AGENT,
        session=session,
        debug=_debug_logger(debug),
        on_request=on_request,
        on_response=on_response,
        on_retry=on_retry,
    )

