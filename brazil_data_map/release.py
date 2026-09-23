from __future__ import annotations

from datetime import datetime, timezone
import hashlib
from pathlib import Path
from typing import Any


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_manifest(root: Path, source_id: str, source_url: str, approvals: dict[str, str]) -> dict[str, Any]:
    files = [
        {"path": path.relative_to(root).as_posix(), "sha256": sha256(path), "bytes": path.stat().st_size}
        for path in sorted(root.rglob("*")) if path.is_file()
    ]
    manifest = {
        "schema_version": "1.0",
        "source_id": source_id,
        "source_url": source_url,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "files": files,
        **approvals,
    }
    validate_manifest(manifest)
    return manifest


def validate_manifest(manifest: dict[str, Any]) -> None:
    required = {"schema_version", "source_id", "source_url", "retrieved_at", "files", "privacy_gate"}
    missing = sorted(required - manifest.keys())
    if missing:
        raise ValueError(f"manifest missing required fields: {', '.join(missing)}")
    if manifest["privacy_gate"] != "passed":
        raise ValueError("privacy_gate must be passed before release")
    if not str(manifest["source_url"]).startswith("https://"):
        raise ValueError("source_url must be an HTTPS source")
    for item in manifest["files"]:
        if not item.get("path") or len(item.get("sha256", "")) != 64:
            raise ValueError("manifest file entries require path and SHA-256")
