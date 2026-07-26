"""Shared public types for the Spotify Data API SDK."""

from __future__ import annotations

from typing import Any, Dict, List, Mapping, Sequence, TypedDict, Union

JsonScalar = Union[str, int, float, bool, None]
JsonValue = Union[JsonScalar, List["JsonValue"], Dict[str, "JsonValue"]]
QueryScalar = Union[str, int, float, bool]
QueryValue = Union[QueryScalar, Sequence[Union[str, int, float]]]
QueryParams = Mapping[str, QueryValue]
Headers = Mapping[str, str]
IdInput = Union[str, int]
IdList = Union[str, Sequence[IdInput]]


class SuccessEnvelope(TypedDict, total=False):
    """Standard API success envelope."""

    success: bool
    data: Any
    metadata: Dict[str, Any]


class ErrorEnvelope(TypedDict, total=False):
    """Standard API error envelope."""

    success: bool
    error: str
    message: str

