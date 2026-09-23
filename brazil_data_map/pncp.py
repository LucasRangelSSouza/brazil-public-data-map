from __future__ import annotations

from copy import deepcopy
from typing import Any, Callable


def incremental_snapshot(fetch_page: Callable[[str], list[dict[str, Any]]], watermark: str, retries: int = 2):
    raw: list[dict[str, Any]] = []
    while True:
        for attempt in range(retries + 1):
            try:
                page = fetch_page(watermark)
                break
            except RuntimeError:
                if attempt == retries:
                    raise
        if not page:
            break
        raw.extend(deepcopy(page))
        watermark = max(watermark, *(item["updated_at"] for item in page))

    latest: dict[str, dict[str, Any]] = {}
    for item in raw:
        if item["updated_at"] >= latest.get(item["id"], {}).get("updated_at", ""):
            latest[item["id"]] = item
    trusted = [latest[key] for key in sorted(latest)]
    semantic = [{**item, "natural_key": item["id"]} for item in trusted]
    return raw, trusted, semantic, watermark
