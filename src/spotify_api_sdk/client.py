"""High-level Spotify Data API client."""

from __future__ import annotations

from typing import Any, Mapping, Optional

from .config import Debug, Hook, ResolvedConfig, resolve_config
from .http import SpotifyHttpClient
from .resources import RESOURCE_CLASSES, ClientResources


class SpotifyApiClient(ClientResources, SpotifyHttpClient):
    """Client exposing all 25 typed Spotify Data API namespaces."""

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
