"""Python SDK for the CheckLeaked Spotify Data API."""

from .client import SpotifyApiClient, SpotifyClient, create_client
from .errors import (
    AuthError,
    HttpError,
    NetworkError,
    RateLimitError,
    SpotifyApiError,
    TimeoutError,
    ValidationError,
)
from .ids import normalize_id, normalize_ids
from .pagination import collect, paginate
from .types import (
    ErrorEnvelope,
    Headers,
    IdInput,
    IdList,
    JsonValue,
    QueryParams,
    QueryValue,
    SuccessEnvelope,
)

__version__ = "1.0.0"

__all__ = [
    "AuthError",
    "ErrorEnvelope",
    "Headers",
    "HttpError",
    "IdInput",
    "IdList",
    "JsonValue",
    "NetworkError",
    "QueryParams",
    "QueryValue",
    "RateLimitError",
    "SpotifyApiClient",
    "SpotifyApiError",
    "SpotifyClient",
    "SuccessEnvelope",
    "TimeoutError",
    "ValidationError",
    "__version__",
    "collect",
    "create_client",
    "normalize_id",
    "normalize_ids",
    "paginate",
]

