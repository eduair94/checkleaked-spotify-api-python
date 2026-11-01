"""Resource primitives used by generated namespace classes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple
from urllib.parse import quote

from .errors import ValidationError
from .ids import normalize_id
from .types import Headers, QueryValue

# JSON body fields that carry a single Spotify id (e.g. POST /tracking/track).
_ID_BODY_FIELDS = frozenset({"spotifyId"})


@dataclass(frozen=True)
class Endpoint:
    key: str
    method: str
    path: str
    path_fields: Tuple[Tuple[str, str], ...] = ()
    query_fields: Tuple[Tuple[str, str], ...] = ()
    body_fields: Tuple[Tuple[str, str], ...] = ()


class Resource:
    """Base class for generated resource namespaces."""

    def __init__(self, client: Any) -> None:
        self._client = client

    def _invoke(self, endpoint: Endpoint, values: Mapping[str, Any]) -> Any:
        path = endpoint.path
        for python_name, wire_name in endpoint.path_fields:
            value = values.get(python_name)
            if value is None:
                raise ValidationError(
                    f"{endpoint.key}: {python_name} is required",
                    code="VALIDATION",
                )
            path = path.replace(
                "{" + wire_name + "}",
                quote(normalize_id(value), safe=""),
            )

        query_value = (
            values.get("extra_query")
            if "extra_query" in values
            else values.get("query")
        )
        query: Dict[str, QueryValue] = dict(query_value or {})
        for python_name, wire_name in endpoint.query_fields:
            value = values.get(python_name)
            if value is not None:
                query[wire_name] = value

        body = values.get("body")
        # Body fields skip the query-string id normalization, so reduce
        # Spotify URIs/URLs to bare ids here.
        explicit_body = {
            wire_name: (
                normalize_id(values[python_name])
                if wire_name in _ID_BODY_FIELDS
                else values[python_name]
            )
            for python_name, wire_name in endpoint.body_fields
            if values.get(python_name) is not None
        }
        if explicit_body:
            if body is None:
                body = explicit_body
            elif isinstance(body, Mapping):
                body = {**body, **explicit_body}
            else:
                raise ValidationError(
                    f"{endpoint.key}: body must be a mapping when body fields "
                    "are supplied",
                    code="VALIDATION",
                )

        return self._client.request(
            endpoint.method,
            path,
            query=query or None,
            body=body,
            timeout=values.get("request_timeout"),
            retries=values.get("request_retries"),
            headers=values.get("request_headers"),
        )
