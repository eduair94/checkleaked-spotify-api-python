"""Structured errors raised by the Spotify Data API SDK."""

from __future__ import annotations

from typing import Any, Optional

#: Codes that are never retried automatically: waiting cannot fix them (an
#: exhausted quota or a bad key, even when they come with an HTTP 429), or a
#: retry could repeat a request that already ran (``OUTCOME_UNKNOWN``, a 503:
#: check the request's effect before sending it again).
NON_RETRYABLE_CODES = frozenset(
    {
        "QUOTA_EXCEEDED",
        "MISSING_API_KEY",
        "INVALID_API_KEY",
        "KEY_REVOKED",
        "KEY_EXPIRED",
        "OUTCOME_UNKNOWN",
    }
)


def _resolve_retryable(
    status: Optional[int],
    code: Optional[str],
    retryable: Optional[bool],
) -> bool:
    # A code waiting cannot fix wins over a body's generic ``retryable`` flag
    # (which the API derives from the HTTP status alone).
    if code in NON_RETRYABLE_CODES:
        return False
    if retryable is not None:
        return retryable
    if code in ("TIMEOUT", "NETWORK"):
        return True
    return status is not None and (status == 429 or status >= 500)


class SpotifyApiError(Exception):
    """Base error for all SDK failures.

    ``code`` is the API's machine-readable code (for example
    ``INVALID_PARAMETER`` or ``UPSTREAM_THROTTLED``), an older endpoint's
    ``error`` string, or ``TIMEOUT`` / ``NETWORK`` / ``CONFIG`` for client-side
    failures. ``request_id`` is the id to quote when contacting support.
    """

    def __init__(
        self,
        message: str,
        *,
        status: Optional[int] = None,
        code: Optional[str] = None,
        body: Any = None,
        url: Optional[str] = None,
        request_id: Optional[str] = None,
        retry_after_ms: Optional[int] = None,
        retryable: Optional[bool] = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.body = body
        self.url = url
        self.request_id = request_id
        self.retry_after_ms = retry_after_ms
        self.retryable = _resolve_retryable(status, code, retryable)

    @property
    def param(self) -> Optional[str]:
        """The query parameter the API rejected (``param`` in a 400 body)."""

        if isinstance(self.body, dict) and isinstance(self.body.get("param"), str):
            return str(self.body["param"])
        return None


class HttpError(SpotifyApiError):
    """A non-successful HTTP response, or an error reported in a 2xx body."""


class AuthError(HttpError):
    """Authentication failed."""


class RateLimitError(HttpError):
    """The API returned HTTP 429 (your own rate limit or quota)."""

    def __init__(
        self,
        message: str,
        *,
        status: int = 429,
        code: Optional[str] = None,
        body: Any = None,
        url: Optional[str] = None,
        retry_after_ms: Optional[int] = None,
        request_id: Optional[str] = None,
        retryable: Optional[bool] = None,
    ) -> None:
        super().__init__(
            message,
            status=status,
            code=code,
            body=body,
            url=url,
            request_id=request_id,
            retry_after_ms=retry_after_ms,
            retryable=retryable,
        )


class NetworkError(SpotifyApiError):
    """A transport-level network failure."""


class TimeoutError(NetworkError):  # noqa: A001 - intentional public API
    """The request timed out."""


class ValidationError(SpotifyApiError):
    """Invalid SDK configuration or method arguments."""
