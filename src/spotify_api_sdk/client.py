"""High-level Spotify Data API client."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from .config import (
    DEFAULT_GATEWAY_TIMEOUT_RETRIES,
    DEFAULT_MAX_RETRY_DELAY_S,
    Debug,
    Hook,
    ResolvedConfig,
    resolve_config,
)
from .http import SpotifyHttpClient
from .resources import RESOURCE_CLASSES, ClientResources
from .types import Headers


class SpotifyApiClient(ClientResources, SpotifyHttpClient):
    """Client exposing all 23 typed Spotify Data API namespaces."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        provider: str = "rapidapi",
        transport: Optional[str] = None,
        base_url: Optional[str] = None,
        host: Optional[str] = None,
        timeout: float = 30.0,
        retries: int = 2,
        retry_delay: float = 0.5,
        max_retry_delay: float = DEFAULT_MAX_RETRY_DELAY_S,
        gateway_timeout_retries: int = DEFAULT_GATEWAY_TIMEOUT_RETRIES,
        headers: Optional[Mapping[str, str]] = None,
        user_agent: Optional[str] = None,
        session: Any = None,
        debug: Debug = False,
        on_request: Optional[Hook] = None,
        on_response: Optional[Hook] = None,
        on_retry: Optional[Hook] = None,
    ) -> None:
        config: ResolvedConfig = resolve_config(
            api_key,
            provider=provider,
            transport=transport,
            base_url=base_url,
            host=host,
            timeout=timeout,
            retries=retries,
            retry_delay=retry_delay,
            max_retry_delay=max_retry_delay,
            gateway_timeout_retries=gateway_timeout_retries,
            headers=headers,
            user_agent=user_agent,
            session=session,
            debug=debug,
            on_request=on_request,
            on_response=on_response,
            on_retry=on_retry,
        )
        super().__init__(config)
        for name, resource_class in RESOURCE_CLASSES.items():
            setattr(self, name, resource_class(self))

    def status(
        self,
        *,
        request_timeout: Optional[float] = None,
        request_retries: Optional[int] = None,
        request_headers: Optional[Headers] = None,
    ) -> Any:
        """Public service status (``GET /status``).

        Overall state plus per-endpoint-family success rates and latency.
        Shortcut for ``client.health.status()``.
        """

        return self.health.status(
            request_timeout=request_timeout,
            request_retries=request_retries,
            request_headers=request_headers,
        )

    def __enter__(self) -> "SpotifyApiClient":
        return self

    def __exit__(self, *_: Any) -> None:
        self.close()


SpotifyClient = SpotifyApiClient


def create_client(
    api_key: Optional[str] = None,
    **config: Any,
) -> SpotifyApiClient:
    """Create a :class:`SpotifyApiClient`."""

    return SpotifyApiClient(api_key, **config)
