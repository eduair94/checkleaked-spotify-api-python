"""Test doubles for the requests-based transport."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Mapping, Optional


class FakeResponse:
    def __init__(
        self,
        status: int = 200,
        body: Any = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        self.status_code = status
        self.headers = {
            "content-type": "application/json",
            **dict(headers or {}),
        }
        self.content = json.dumps(
            {"success": True, "data": {"ok": True}}
            if body is None
            else body
        ).encode()


class FakeSession:
    def __init__(self, *responses: Any) -> None:
        self.responses: List[Any] = list(responses) or [FakeResponse()]
        self.calls: List[Dict[str, Any]] = []
        self.closed = False

    def request(self, method: str, url: str, **kwargs: Any) -> Any:
        self.calls.append({"method": method, "url": url, **kwargs})
        response = self.responses.pop(0) if len(self.responses) > 1 else self.responses[0]
        if isinstance(response, Exception):
            raise response
        return response

    def close(self) -> None:
        self.closed = True

