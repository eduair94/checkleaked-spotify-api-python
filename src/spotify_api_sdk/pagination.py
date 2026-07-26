"""Pagination helpers matching the TypeScript SDK."""

from __future__ import annotations

from typing import Any, Callable, Iterable, Iterator, List, Optional, Sequence, TypeVar

T = TypeVar("T")
I = TypeVar("I")


def _default_get_items(page: Any) -> Sequence[Any]:
    return page if isinstance(page, list) else []


def paginate(
    fetcher: Callable[..., T],
    *,
    get_items: Optional[Callable[[T], Sequence[Any]]] = None,
    offset: int = 0,
    limit: int = 50,
    max_items: Optional[int] = None,
    max_pages: int = 100,
) -> Iterator[T]:
    """Yield pages until a short page or a configured bound is reached."""

    extractor = get_items or _default_get_items
    seen = 0
    current_offset = offset
    for _ in range(max_pages):
        result = fetcher(offset=current_offset, limit=limit)
        items = extractor(result)
        yield result
        seen += len(items)
        if len(items) < limit:
            return
        if max_items is not None and seen >= max_items:
            return
        current_offset += limit


def collect(
    fetcher: Callable[..., T],
    *,
    get_items: Optional[Callable[[T], Sequence[I]]] = None,
    offset: int = 0,
    limit: int = 50,
    max_items: Optional[int] = None,
    max_pages: int = 100,
) -> List[I]:
    """Collect items across all bounded pages."""

    extractor: Callable[[T], Sequence[I]]
    if get_items is None:
        extractor = _default_get_items
    else:
        extractor = get_items
    output: List[I] = []
    for page in paginate(
        fetcher,
        get_items=extractor,
        offset=offset,
        limit=limit,
        max_items=max_items,
        max_pages=max_pages,
    ):
        for item in extractor(page):
            output.append(item)
            if max_items is not None and len(output) >= max_items:
                return output
    return output
