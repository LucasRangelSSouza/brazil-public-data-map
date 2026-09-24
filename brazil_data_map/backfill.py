from __future__ import annotations

from datetime import date, timedelta
import json
from pathlib import Path
from typing import Any, Callable, Iterable

from .pipeline import build_public_release
from .pncp import fetch_publications


FetchPublications = Callable[[date, date, int], list[dict[str, Any]]]


def iter_days(start: date, end: date) -> Iterable[date]:
    if end < start:
        raise ValueError("end date must not precede start date")
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def window_key(day: date, modality_id: int) -> str:
    return f"{day.isoformat()}:{modality_id}"


def deduplicate_latest(records: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    for record in records:
        source_id = str(record["id"])
        if source_id not in latest or str(record["updated_at"]) >= str(latest[source_id]["updated_at"]):
            latest[source_id] = record
    return [latest[source_id] for source_id in sorted(latest)]


def _load_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default


def _append_json_lines(path: Path, records: list[dict[str, Any]]) -> None:
    if not records:
        return
    with path.open("a", encoding="utf-8") as stream:
        for record in records:
            stream.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def _read_json_lines(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def run_backfill(
    start: date,
    end: date,
    modality_ids: Iterable[int],
    output_root: Path,
    *,
    fetcher: FetchPublications = fetch_publications,
    retrieved_at: str | None = None,
    git_commit: str | None = None,
) -> dict[str, Any]:
    """Resume a bounded PNCP backfill and produce a reviewed local release candidate.

    The checkpoint is intentionally local. It contains window completion metadata only;
    normalized source records remain in an ignored JSONL capture beside the release.
    """
    normalized_modalities = tuple(sorted({int(modality_id) for modality_id in modality_ids}))
    if not normalized_modalities:
        raise ValueError("at least one modality id is required")
    if any(modality_id < 1 for modality_id in normalized_modalities):
        raise ValueError("modality ids must be positive")

    output_root.mkdir(parents=True, exist_ok=True)
    checkpoint_path = output_root / "checkpoint.json"
    capture_path = output_root / "normalized-source-capture.jsonl"
    checkpoint = _load_json(checkpoint_path, {"completed_windows": []})
    completed = set(checkpoint.get("completed_windows", []))
    fetched_windows = 0
    failure: RuntimeError | None = None

    for day in iter_days(start, end):
        for modality_id in normalized_modalities:
            key = window_key(day, modality_id)
            if key in completed:
                continue
            try:
                records = fetcher(day, day, modality_id)
            except RuntimeError as error:
                failure = error
                break
            _append_json_lines(capture_path, records)
            completed.add(key)
            checkpoint = {
                "completed_windows": sorted(completed),
                "window_grain": "day:modality_id",
                "source": "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao",
            }
            checkpoint_path.write_text(json.dumps(checkpoint, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            fetched_windows += 1
        if failure:
            break

    records = deduplicate_latest(_read_json_lines(capture_path))
    release_root = output_root / "release"
    result = build_public_release(
        records,
        release_root,
        "pncp",
        "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao",
        retrieved_at=retrieved_at,
        git_commit=git_commit,
    )
    summary = {
        "fetched_windows": fetched_windows,
        "completed_windows": len(completed),
        "deduplicated_records": len(records),
        "release_root": str(release_root),
        "audit": result["audit"],
    }
    if failure:
        raise RuntimeError(f"backfill stopped after creating a local checkpointed release: {summary}") from failure
    return summary
