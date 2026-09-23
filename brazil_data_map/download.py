from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Callable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def download_public_file(url: str, destination: Path, retries: int = 2, opener: Callable[..., object] = urlopen) -> dict[str, str | int]:
    """Download an explicit HTTPS public URL with bounded retry and a content hash."""
    if not url.startswith("https://"):
        raise ValueError("public downloads require an HTTPS URL")
    request = Request(url, headers={"User-Agent": "brazil-public-data-map/0.1"})
    for attempt in range(retries + 1):
        try:
            with opener(request, timeout=30) as response:
                payload = response.read()
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)
            return {"url": url, "path": destination.as_posix(), "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()}
        except (HTTPError, URLError) as error:
            if attempt == retries:
                raise RuntimeError(f"public download failed after {retries + 1} attempts: {url}") from error
    raise AssertionError("unreachable")
