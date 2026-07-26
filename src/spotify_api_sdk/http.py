"""HTTP transport for the Spotify Data API."""

from __future__ import annotations

import json
import random
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any, Dict, Mapping, Optional
from urllib.parse import urlencode, urlsplit, urlunsplit

from .config import ResolvedConfig
from .errors import (
    AuthError,
    HttpError,
    NetworkError,
    RateLimitError,
    SpotifyApiError,
    TimeoutError,
)
from .ids import normalize_id, normalize_ids
from .types import Headers, QueryParams, SuccessEnvelope

_ID_SINGLE_KEYS = {"id", "spotify_track_id"}
_ID_MULTI_KEYS = {"ids", "seed_tracks", "seed_artists"}


@dataclass
class RawResponse:
    """Decoded HTTP response used by the transport."""

    status: int
    headers: Mapping[str, str]
    data: Any
    content: bytes


def _safe_url(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def _stringify(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _serialize_query(query: Optional[QueryParams]) -> str:
    if not query:
        return ""
    pairs = []
    for key, value in query.items():
        if value is None:
            continue
        if key in _ID_MULTI_KEYS:
            normalized = normalize_ids(value)  # type: ignore[arg-type]
            if normalized:
                pairs.append((key, normalized))
        elif key in _ID_SINGLE_KEYS and not isinstance(value, (list, tuple)):
            pairs.append((key, normalize_id(value)))  # type: ignore[arg-type]
        elif isinstance(value, (list, tuple)):
            if value:
                pairs.append((key, ",".join(_stringify(item) for item in value)))
        else:
            pairs.append((key, _stringify(value)))
    return urlencode(pairs)


def _decode(content: bytes, content_type: str) -> Any:
    if not content:
        return None
    text = content.decode("utf-8", errors="replace")
    if "json" in content_type.lower() or text.lstrip().startswith(("{", "[")):
        try:
            return json.loads(text)
        except ValueError:
            pass
    return text


def _message(body: Any, fallback: str) -> str:
    if isinstance(body, str) and body:
        return body[:500]
    if isinstance(body, dict):
        for key in ("message", "error", "detail", "msg"):
            value = body.get(key)
            if isinstance(value, str) and value:
                return value
    return fallback


def _code(body: Any) -> Optional[str]:
    if isinstance(body, dict):
        for key in ("code", "error"):
            value = body.get(key)
            if isinstance(value, (str, int)):
                return str(value)
    return None


def _retry_after_ms(value: Optional[str]) -> Optional[int]:
    if not value:
        return None
    try:
        return max(0, int(float(value) * 1000))
    except ValueError:
        pass
    try:
        parsed = parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return max(
            0,
            int((parsed - datetime.now(timezone.utc)).total_seconds() * 1000),
        )
    except (TypeError, ValueError):
        return None


class SpotifyHttpClient:
    """Low-level HTTP client shared by every resource namespace."""

    def __init__(self, config: ResolvedConfig) -> None:
        self.config = config

    def request_raw(
        self,
        method: str,
        path: str,
        *,
        query: Optional[QueryParams] = None,
        body: Any = None,
        timeout: Optional[float] = None,
        retries: Optional[int] = None,
        headers: Optional[Headers] = None,
    ) -> SuccessEnvelope:
        """Return the complete success envelope for a request."""

        response = self._request_response(
            method,
            path,
            query=query,
            body=body,
            timeout=timeout,
            retries=retries,
            headers=headers,
        )
        if isinstance(response.data, dict):
            data = response.data
            if data.get("success") is False:
                raise self._http_error(
                    response.status,
                    data,
                    _safe_url(self._build_url(path, query)),
                    response.headers,
                )
            if "success" in data and "data" in data:
                return data  # type: ignore[return-value]
        return {"success": True, "data": response.data}

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Optional[QueryParams] = None,
        body: Any = None,
        timeout: Optional[float] = None,
        retries: Optional[int] = None,
        headers: Optional[Headers] = None,
    ) -> Any:
        """Return the unwrapped ``data`` payload."""

        return self.request_raw(
            method,
            path,
            query=query,
            body=body,
            timeout=timeout,
            retries=retries,
            headers=headers,
        ).get("data")

    def get(
        self,
        path: str,
        query: Optional[QueryParams] = None,
        *,
        timeout: Optional[float] = None,
        retries: Optional[int] = None,
        headers: Optional[Headers] = None,
    ) -> Any:
        return self.request(
            "GET",
            path,
            query=query,
            timeout=timeout,
            retries=retries,
            headers=headers,
        )

    def post(
        self,
        path: str,
        body: Any = None,
        query: Optional[QueryParams] = None,
        *,
        timeout: Optional[float] = None,
        retries: Optional[int] = None,
        headers: Optional[Headers] = None,
    ) -> Any:
        return self.request(
            "POST",
            path,
            query=query,
            body=body,
            timeout=timeout,
            retries=retries,
            headers=headers,
        )

    def delete(
        self,
        path: str,
        query: Optional[QueryParams] = None,
        *,
        timeout: Optional[float] = None,
        retries: Optional[int] = None,
        headers: Optional[Headers] = None,
    ) -> Any:
        return self.request(
            "DELETE",
            path,
            query=query,
            timeout=timeout,
            retries=retries,
            headers=headers,
        )

    def close(self) -> None:
        close = getattr(self.config.session, "close", None)
        if callable(close):
            close()

    def _build_url(self, path: str, query: Optional[QueryParams]) -> str:
        suffix = path if path.startswith("/") else f"/{path}"
        encoded = _serialize_query(query)
        url = f"{self.config.channel.base_url}{suffix}"
        return f"{url}?{encoded}" if encoded else url

    def _request_response(
        self,
        method: str,
        path: str,
        *,
        query: Optional[QueryParams],
        body: Any,
        timeout: Optional[float],
        retries: Optional[int],
        headers: Optional[Headers],
    ) -> RawResponse:
        method = method.upper()
        url = self._build_url(path, query)
        safe_url = _safe_url(url)
        timeout_s = self.config.timeout_s if timeout is None else float(timeout)
        max_retries = self.config.retries if retries is None else max(0, retries)
        request_headers: Dict[str, str] = {
            "x-rapidapi-key": self.config.api_key,
            "accept": "application/json",
            "user-agent": self.config.user_agent,
            **self.config.headers,
            **dict(headers or {}),
        }
        if self.config.channel.host:
            request_headers["x-rapidapi-host"] = self.config.channel.host
        data = None
        if body is not None:
            data = body if isinstance(body, str) else json.dumps(body)
            request_headers.setdefault("content-type", "application/json")

        info = {"method": method, "url": url, "headers": request_headers}
        if self.config.on_request:
            self.config.on_request(info)
        if self.config.debug:
            self.config.debug(f"-> {method} {url}", None)

        last_error: Optional[SpotifyApiError] = None
        for attempt in range(max_retries + 1):
            started = time.monotonic()
            try:
                response = self.config.session.request(
                    method,
                    url,
                    headers=request_headers,
                    data=data,
                    timeout=timeout_s,
                )
            except Exception as error:  # noqa: BLE001 - normalized below
                last_error = self._network_error(error, safe_url, timeout_s)
                if attempt >= max_retries:
                    raise last_error
                self._retry(attempt, method, url, error=last_error)
                continue

            status = int(response.status_code)
            response_headers = response.headers or {}
            duration_ms = int((time.monotonic() - started) * 1000)
            if self.config.on_response:
                self.config.on_response(
                    {
                        "method": method,
                        "url": url,
                        "status": status,
                        "duration_ms": duration_ms,
                    }
                )
            if self.config.debug:
                self.config.debug(
                    f"<- {status} {method} {url} ({duration_ms}ms)",
                    None,
                )

            if (status == 429 or status >= 500) and attempt < max_retries:
                retry_after = _retry_after_ms(response_headers.get("retry-after"))
                self._retry(
                    attempt,
                    method,
                    url,
                    status=status,
                    retry_after_ms=retry_after,
                )
                continue

            content = response.content or b""
            decoded = _decode(
                content,
                response_headers.get("content-type", ""),
            )
            if not 200 <= status < 300:
                raise self._http_error(
                    status,
                    decoded,
                    safe_url,
                    response_headers,
                )
            return RawResponse(
                status=status,
                headers=response_headers,
                data=decoded,
                content=content,
            )

        if last_error is not None:
            raise last_error
        raise NetworkError("Request failed", url=safe_url)

    def _retry(
        self,
        attempt: int,
        method: str,
        url: str,
        *,
        status: Optional[int] = None,
        error: Optional[SpotifyApiError] = None,
        retry_after_ms: Optional[int] = None,
    ) -> None:
        base_ms = int(self.config.retry_delay_s * 1000 * (2 ** attempt))
        delay_ms = retry_after_ms
        if delay_ms is None:
            delay_ms = base_ms + random.randrange(
                0,
                max(1, int(self.config.retry_delay_s * 1000)),
            )
        info = {
            "attempt": attempt + 1,
            "method": method,
            "url": url,
            "status": status,
            "error": error,
            "delay_ms": delay_ms,
        }
        if self.config.on_retry:
            self.config.on_retry(info)
        if self.config.debug:
            self.config.debug(f"retry {attempt + 1} after {delay_ms}ms", info)
        time.sleep(delay_ms / 1000.0)

    def _network_error(
        self,
        error: Exception,
        url: str,
        timeout_s: float,
    ) -> SpotifyApiError:
        try:
            import requests

            if isinstance(error, requests.exceptions.Timeout):
                return TimeoutError(
                    f"Request timed out after {timeout_s}s",
                    code="TIMEOUT",
                    url=url,
                )
        except Exception:  # pragma: no cover
            pass
        return NetworkError(
            f"Network error: {error}",
            code="NETWORK",
            url=url,
        )

    def _http_error(
        self,
        status: int,
        body: Any,
        url: str,
        headers: Mapping[str, str],
    ) -> HttpError:
        message = _message(body, f"HTTP {status}")
        code = _code(body)
        if status in (401, 403):
            return AuthError(
                message,
                status=status,
                code=code,
                body=body,
                url=url,
            )
        if status == 429:
            return RateLimitError(
                message,
                status=status,
                code=code,
                body=body,
                url=url,
                retry_after_ms=_retry_after_ms(headers.get("retry-after")),
            )
        return HttpError(
            message,
            status=status,
            code=code,
            body=body,
            url=url,
        )

