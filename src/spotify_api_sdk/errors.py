"""Structured errors raised by the Spotify Data API SDK."""

from __future__ import annotations

from typing import Any, Optional


class SpotifyApiError(Exception):
    """Base error for all SDK failures."""

    def __init__(
        self,
        message: str,
        *,
        status: Optional[int] = None,
        code: Optional[str] = None,
        body: Any = None,
        url: Optional[str] = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.body = body
        self.url = url


class HttpError(SpotifyApiError):
    """A non-successful HTTP response."""


class AuthError(HttpError):
    """Authentication failed."""


class RateLimitError(HttpError):
    """The API returned HTTP 429."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 429,
        code: Optional[str] = None,
        body: Any = None,
        url: Optional[str] = None,
        retry_after_ms: Optional[int] = None,
    ) -> None:
        super().__init__(
            message,
            status=status,
            code=code,
            body=body,
            url=url,
        )
        self.retry_after_ms = retry_after_ms


class NetworkError(SpotifyApiError):
    """A transport-level network failure."""


class TimeoutError(NetworkError):  # noqa: A001 - intentional public API
    """The request timed out."""


class ValidationError(SpotifyApiError):
    """Invalid SDK configuration or method arguments."""

