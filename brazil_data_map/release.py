from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_manifest(
    root: Path,
    source_id: str,
    source_url: str,
    approvals: dict[str, str],
    retrieved_at: str | None = None,
    files: Iterable[Path] | None = None,
    source_input_sha256: str | None = None,
    row_counts: dict[str, int] | None = None,
    git_commit: str | None = None,
    distribution_version: str | None = None,
) -> dict[str, Any]:
    release_files = list(files) if files is not None else [path for path in root.rglob("*") if path.is_file()]
    file_entries = [
        {"path": path.relative_to(root).as_posix(), "sha256": sha256(path), "bytes": path.stat().st_size}
        for path in sorted(release_files)
    ]
    manifest = {
        "schema_version": "1.1",
        "source_id": source_id,
        "source_url": source_url,
        "retrieved_at": retrieved_at or datetime.now(timezone.utc).isoformat(),
        "files": file_entries,
        "source_input_sha256": source_input_sha256 or "not_recorded",
        "row_counts": row_counts or {},
        "git_commit": git_commit or "not_recorded",
        "distribution_version": distribution_version or "not_published",
        **approvals,
    }
    validate_manifest(manifest)
    return manifest


def validate_manifest(manifest: dict[str, Any]) -> None:
    required = {
        "schema_version", "source_id", "source_url", "retrieved_at", "files", "privacy_gate",
        "source_input_sha256", "row_counts", "git_commit", "distribution_version",
    }
    missing = sorted(required - manifest.keys())
    if missing:
        raise ValueError(f"manifest missing required fields: {', '.join(missing)}")
    if manifest["privacy_gate"] != "passed":
        raise ValueError("privacy_gate must be passed before release")
    if not str(manifest["source_url"]).startswith("https://"):
        raise ValueError("source_url must be an HTTPS source")
    if manifest["source_input_sha256"] != "not_recorded" and len(str(manifest["source_input_sha256"])) != 64:
        raise ValueError("source_input_sha256 must be a SHA-256 digest or not_recorded")
    if not isinstance(manifest["row_counts"], dict):
        raise ValueError("row_counts must be an object")
    for item in manifest["files"]:
        if not item.get("path") or len(item.get("sha256", "")) != 64:
            raise ValueError("manifest file entries require path and SHA-256")
