from __future__ import annotations

import json
import hashlib
import re
from datetime import datetime
from pathlib import Path
from pathlib import PurePosixPath
from typing import Any

import pyarrow.parquet as pq


EXPECTED_TABLES_BY_LAYER = {"raw": 13, "trusted": 28, "semantic": 6}
_SLUG_PATTERN = re.compile(r"^pncp-(raw|trusted|semantic)-[a-z0-9-]+$")
_TABLE_PATTERN = re.compile(r"^(?:pncp_|obt_pncp_)[a-z0-9_]+$")
_RELEASE_STATUSES = {
    "inventory-only",
    "ready",
    "excluded-with-rationale",
    "unavailable-with-evidence",
}
_KAGGLE_MAX_DATASET_BYTES = 200_000_000_000
_KAGGLE_MAX_TOP_LEVEL_FILES = 50
_BUNDLE_SLUG_PATTERN = re.compile(r"^pncp-[a-z0-9-]+-(?:data|semantic)$")


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_pncp_table_catalog(path: Path) -> dict[str, Any]:
    catalog = json.loads(path.read_text(encoding="utf-8"))
    validate_pncp_table_catalog(catalog)
    return catalog


def load_pncp_publication_plan(path: Path, catalog: dict[str, Any]) -> dict[str, Any]:
    plan = json.loads(path.read_text(encoding="utf-8"))
    validate_pncp_publication_plan(plan, catalog)
    return plan


def validate_pncp_publication_plan(plan: dict[str, Any], catalog: dict[str, Any]) -> None:
    if plan.get("schema_version") != "1.0":
        raise ValueError("PNCP publication plan schema_version must be 1.0")
    size_limit = plan.get("size_limit_bytes")
    if not isinstance(size_limit, int) or isinstance(size_limit, bool) or not 0 < size_limit <= _KAGGLE_MAX_DATASET_BYTES:
        raise ValueError("publication plan size_limit_bytes must not exceed Kaggle's 200 GB cap")
    max_files = plan.get("max_top_level_files")
    if not isinstance(max_files, int) or isinstance(max_files, bool) or not 1 <= max_files <= _KAGGLE_MAX_TOP_LEVEL_FILES:
        raise ValueError("publication plan max_top_level_files must not exceed Kaggle's 50-file cap")

    catalogue_entries = {
        (table["table_id"], table["layer"]): table
        for table in catalog.get("tables", [])
    }
    planned: list[tuple[str, str]] = []
    target_by_pair: dict[tuple[str, str], str] = {}
    seen_slugs: set[str] = set()
    seen_subjects: set[str] = set()
    subjects = plan.get("subjects")
    if not isinstance(subjects, list) or not subjects:
        raise ValueError("publication plan requires subject groups")
    for subject in subjects:
        subject_id = subject.get("subject_id")
        datasets = subject.get("datasets")
        if not isinstance(subject_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", subject_id):
            raise ValueError(f"invalid publication subject identifier: {subject_id}")
        if subject_id in seen_subjects or not isinstance(datasets, list) or not datasets:
            raise ValueError(f"duplicate or empty publication subject: {subject_id}")
        seen_subjects.add(subject_id)
        kinds: set[str] = set()
        for dataset in datasets:
            kind = dataset.get("kind")
            slug = dataset.get("kaggle_slug")
            table_layers = dataset.get("table_layers")
            if kind not in {"data", "semantic"}:
                raise ValueError(f"unsupported bundle kind in subject {subject_id}: {kind}")
            if kind in kinds:
                raise ValueError(f"subject has more than one {kind} bundle: {subject_id}")
            kinds.add(kind)
            if not isinstance(slug, str) or not _BUNDLE_SLUG_PATTERN.fullmatch(slug) or len(slug) > 50:
                raise ValueError(f"invalid Kaggle dataset slug in subject {subject_id}: {slug}")
            if slug in seen_slugs:
                raise ValueError(f"duplicate Kaggle dataset slug: {slug}")
            seen_slugs.add(slug)
            if not isinstance(table_layers, list) or not table_layers:
                raise ValueError(f"empty dataset bundle: {slug}")
            for entry in table_layers:
                table_id = entry.get("table_id")
                layer = entry.get("layer")
                if (table_id, layer) not in catalogue_entries:
                    raise ValueError(f"publication plan references an unknown table-layer pair: {table_id}/{layer}")
                if kind == "semantic" and layer != "semantic":
                    raise ValueError("bundle kind does not match table layer")
                if kind == "data" and layer not in {"raw", "trusted"}:
                    raise ValueError("bundle kind does not match table layer")
                planned.append((table_id, layer))
                target_by_pair[(table_id, layer)] = slug
        if "semantic" in kinds and "data" not in kinds:
            # Semantic-only subjects are valid (e.g. an analytical projection with no raw/trusted table).
            continue

    expected = set(catalogue_entries)
    observed = set(planned)
    if len(planned) != len(observed):
        raise ValueError("publication plan contains a duplicate table-layer pair")
    missing = expected - observed
    extra = observed - expected
    if missing or extra:
        raise ValueError(f"publication plan coverage differs from the table catalogue; missing={sorted(missing)}, extra={sorted(extra)}")
    for pair, table in catalogue_entries.items():
        if table.get("kaggle_slug") != target_by_pair.get(pair):
            raise ValueError(f"table catalogue target does not match its publication plan: {pair[0]}/{pair[1]}")


def validate_pncp_release_bundle(
    catalog: dict[str, Any],
    plan: dict[str, Any],
    kaggle_slug: str,
    package_dir: Path,
) -> dict[str, Any]:
    """Verify a complete subject/layer Kaggle package and its published Parquets."""
    validate_pncp_publication_plan(plan, catalog)
    selected = [
        (subject, dataset)
        for subject in plan["subjects"]
        for dataset in subject["datasets"]
        if dataset["kaggle_slug"] == kaggle_slug
    ]
    if len(selected) != 1:
        raise ValueError(f"expected one publication-plan entry for Kaggle dataset: {kaggle_slug}")
    subject, bundle = selected[0]
    root = package_dir.resolve(strict=True)
    manifest_path = root / "release_manifest.json"
    readme_path = root / "README.md"
    for required in (manifest_path, readme_path):
        if not required.is_file():
            raise ValueError(f"release bundle is missing required file: {required.name}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    cutoff = catalog.get("data_cutoff")
    if (
        manifest.get("schema_version") != "2.0"
        or manifest.get("dataset_slug") != kaggle_slug
        or manifest.get("subject_id") != subject["subject_id"]
        or manifest.get("bundle_kind") != bundle["kind"]
        or manifest.get("data_cutoff") != cutoff
    ):
        raise ValueError("release manifest does not match the subject bundle contract")

    expected_pairs = {
        (entry["table_id"], entry["layer"])
        for entry in bundle["table_layers"]
    }
    table_entries = manifest.get("tables")
    if not isinstance(table_entries, list):
        raise ValueError("release manifest requires table entries")
    observed_pairs = [
        (entry.get("table_id"), entry.get("layer"))
        for entry in table_entries
        if isinstance(entry, dict)
    ]
    if len(observed_pairs) != len(set(observed_pairs)) or set(observed_pairs) != expected_pairs:
        raise ValueError("bundle table coverage does not match publication plan")

    declared_files = manifest.get("files")
    if not isinstance(declared_files, list) or not declared_files:
        raise ValueError("release bundle manifest requires file hashes")
    seen_paths: set[str] = set()
    resolved_files: dict[str, Path] = {}
    if any(path.is_symlink() for path in root.rglob("*")):
        raise ValueError("release bundle must not contain symbolic links")
    for item in declared_files:
        relative = item.get("path") if isinstance(item, dict) else None
        if not isinstance(relative, str) or relative in seen_paths or "\\" in relative:
            raise ValueError("release bundle manifest contains an invalid or duplicate file path")
        relpath = PurePosixPath(relative)
        if relpath.is_absolute() or ".." in relpath.parts or not relpath.parts:
            raise ValueError("release bundle file paths must be safe relative paths")
        candidate = root / Path(*relpath.parts)
        if candidate.is_symlink():
            raise ValueError("release bundle manifest points to a symbolic link")
        path = candidate.resolve(strict=True)
        if root not in path.parents or not path.is_file():
            raise ValueError("release bundle manifest points outside the package or to a non-file")
        expected_hash = item.get("sha256")
        expected_bytes = item.get("bytes")
        if (
            not isinstance(expected_hash, str)
            or not re.fullmatch(r"[a-fA-F0-9]{64}", expected_hash)
            or not isinstance(expected_bytes, int)
            or isinstance(expected_bytes, bool)
        ):
            raise ValueError("release bundle file entry requires byte size and SHA-256")
        if path.stat().st_size != expected_bytes or _sha256_file(path) != expected_hash.lower():
            raise ValueError(f"file hash or size mismatch: {relative}")
        seen_paths.add(relative)
        resolved_files[relative] = path

    expected_declared = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file() and path.name not in {"release_manifest.json", "dataset-metadata.json"}
    }
    if seen_paths != expected_declared:
        raise ValueError("release bundle contains undeclared files or omits files from its manifest")
    if "README.md" not in seen_paths:
        raise ValueError("release bundle must hash its dataset card")
    kaggle_metadata_path = root / "dataset-metadata.json"
    if kaggle_metadata_path.exists():
        if manifest.get("kaggle_metadata_sha256") != _sha256_file(kaggle_metadata_path):
            raise ValueError("local Kaggle control metadata hash does not match the release manifest")
        metadata = json.loads(kaggle_metadata_path.read_text(encoding="utf-8"))
        if metadata.get("id") != f"lucasrangelss/{kaggle_slug}":
            raise ValueError("local Kaggle control metadata points to a different dataset slug")

    total_rows = 0
    table_paths: set[str] = set()
    for entry in table_entries:
        table_id = entry["table_id"]
        layer = entry["layer"]
        row_count = entry.get("row_count")
        if not isinstance(row_count, int) or isinstance(row_count, bool) or row_count < 0:
            raise ValueError(f"release table requires a non-negative row count: {table_id}/{layer}")
        file_paths = [entry.get("parquet_path"), entry.get("schema_path"), entry.get("privacy_audit_path")]
        if any(not isinstance(path, str) or path not in resolved_files for path in file_paths):
            raise ValueError(f"release table is missing a hashed Parquet, schema, or audit file: {table_id}/{layer}")
        parquet_path, schema_path, audit_path = (resolved_files[path] for path in file_paths)
        if (
            parquet_path.suffix.lower() != ".parquet"
            or parquet_path.name != f"{layer}__{table_id}.parquet"
            or schema_path.name != f"schema__{table_id}__{layer}.json"
            or audit_path.name != f"privacy-audit__{table_id}__{layer}.json"
        ):
            raise ValueError(f"release table file paths do not match their declared roles: {table_id}/{layer}")
        if parquet_path.relative_to(root).as_posix() in table_paths:
            raise ValueError("multiple table-layer entries point to the same Parquet file")
        table_paths.add(parquet_path.relative_to(root).as_posix())
        if pq.ParquetFile(parquet_path).metadata.num_rows != row_count:
            raise ValueError(f"Parquet row count does not match the bundle manifest: {table_id}/{layer}")
        if entry.get("schema_sha256") != _sha256_file(schema_path):
            raise ValueError(f"schema hash does not match the bundle manifest: {table_id}/{layer}")
        if entry.get("privacy_audit_sha256") != _sha256_file(audit_path):
            raise ValueError(f"privacy audit hash does not match the bundle manifest: {table_id}/{layer}")
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        if (
            audit.get("status") != "passed"
            or audit.get("rows_released") != row_count
            or audit.get("direct_identifier_matches") != 0
        ):
            raise ValueError(f"release privacy audit failed: {table_id}/{layer}")
        total_rows += row_count

    actual_bytes = sum(path.stat().st_size for path in root.rglob("*") if path.is_file())
    if actual_bytes > plan["size_limit_bytes"]:
        raise ValueError("release bundle exceeds Kaggle's configured size limit")
    if len(list(root.iterdir())) > plan["max_top_level_files"]:
        raise ValueError("release bundle exceeds Kaggle's configured top-level file limit")
    return {
        "status": "passed",
        "dataset_slug": kaggle_slug,
        "subject_id": subject["subject_id"],
        "bundle_kind": bundle["kind"],
        "table_layers_checked": len(table_entries),
        "row_count": total_rows,
        "files_checked": len(seen_paths) + 1,
        "bytes": actual_bytes,
        "hash_mismatches": 0,
    }


def validate_pncp_table_catalog(catalog: dict[str, Any]) -> None:
    if catalog.get("schema_version") != "1.0":
        raise ValueError("PNCP table catalog schema_version must be 1.0")
    if catalog.get("release_status") != "inventory-only":
        raise ValueError("an inventory catalog must not claim release completion")

    tables = catalog.get("tables")
    if not isinstance(tables, list) or not tables:
        raise ValueError("PNCP table catalog requires table entries")
    if catalog.get("expected_table_count") != len(tables):
        raise ValueError("expected_table_count must match the table entries")

    seen_tables: set[tuple[str, str]] = set()
    seen_slugs: dict[str, tuple[bool, str]] = {}
    counts = {layer: 0 for layer in EXPECTED_TABLES_BY_LAYER}
    for table in tables:
        layer = table.get("layer")
        table_id = table.get("table_id")
        slug = table.get("kaggle_slug")
        endpoint = table.get("source_endpoint")
        status = table.get("release_status")
        domain = table.get("domain")
        derivation = table.get("derivation")

        if layer not in counts:
            raise ValueError(f"unsupported PNCP layer: {layer}")
        if not isinstance(table_id, str) or not _TABLE_PATTERN.fullmatch(table_id):
            raise ValueError(f"invalid PNCP table identifier: {table_id}")
        is_bundle_slug = isinstance(slug, str) and bool(_BUNDLE_SLUG_PATTERN.fullmatch(slug))
        if (
            not isinstance(slug, str)
            or len(slug) > 50
            or not (_SLUG_PATTERN.fullmatch(slug) or is_bundle_slug)
        ):
            raise ValueError(f"invalid Kaggle slug for {table_id}")
        if not isinstance(endpoint, str) or not (endpoint.startswith("/api/") or endpoint.startswith("derived:")):
            raise ValueError(f"table {table_id} requires an official endpoint or derivation reference")
        if not isinstance(domain, str) or not domain or not isinstance(derivation, str) or not derivation:
            raise ValueError(f"table {table_id} requires a domain and derivation")
        if status not in _RELEASE_STATUSES:
            raise ValueError(f"table {table_id} has an invalid release status")
        if status == "ready":
            _validate_release_evidence(table, catalog.get("data_cutoff"))

        key = (layer, table_id)
        if key in seen_tables:
            raise ValueError(f"duplicate PNCP table entry: {layer}/{table_id}")
        previous = seen_slugs.get(slug)
        if previous is not None:
            previous_is_bundle, previous_status = previous
            if not is_bundle_slug or not previous_is_bundle:
                raise ValueError(f"duplicate Kaggle slug: {slug}")
            if status != previous_status:
                raise ValueError(f"shared Kaggle bundle slug has inconsistent release status: {slug}")
        seen_tables.add(key)
        seen_slugs[slug] = (is_bundle_slug, status)
        counts[layer] += 1

    if counts != EXPECTED_TABLES_BY_LAYER:
        raise ValueError(f"PNCP table inventory counts differ from the reviewed snapshot: {counts}")
    if catalog.get("counts_by_layer") != counts:
        raise ValueError("counts_by_layer must match the table entries")


def _validate_release_evidence(table: dict[str, Any], catalogue_cutoff: Any) -> None:
    table_id = table["table_id"]
    evidence = table.get("release_evidence")
    if not isinstance(evidence, dict):
        raise ValueError(f"ready table requires release_evidence: {table_id}")

    slug = table["kaggle_slug"]
    dataset_url = evidence.get("dataset_url")
    url_pattern = rf"^https://www\.kaggle\.com/datasets/[A-Za-z0-9_-]+/{re.escape(slug)}$"
    if not isinstance(dataset_url, str) or not re.fullmatch(url_pattern, dataset_url):
        raise ValueError(f"ready table requires its exact Kaggle dataset URL: {table_id}")
    if evidence.get("data_cutoff") != catalogue_cutoff:
        raise ValueError(f"ready table cutoff must match the catalogue cutoff: {table_id}")

    row_count = evidence.get("row_count")
    if not isinstance(row_count, int) or isinstance(row_count, bool) or row_count < 1:
        raise ValueError(f"ready table requires a positive integer row_count: {table_id}")
    if not isinstance(evidence.get("manifest_sha256"), str) or not re.fullmatch(
        r"[a-fA-F0-9]{64}", evidence["manifest_sha256"]
    ):
        raise ValueError(f"ready table requires a SHA-256 release manifest hash: {table_id}")

    verified_at = evidence.get("verified_at")
    try:
        timestamp = datetime.fromisoformat(verified_at.replace("Z", "+00:00"))
    except (AttributeError, TypeError, ValueError) as error:
        raise ValueError(f"ready table requires an ISO-8601 verified_at timestamp: {table_id}") from error
    if timestamp.tzinfo is None:
        raise ValueError(f"ready table verified_at timestamp must include a timezone: {table_id}")

    clean_download = evidence.get("clean_download")
    if (
        not isinstance(clean_download, dict)
        or clean_download.get("status") != "passed"
        or not isinstance(clean_download.get("files_checked"), int)
        or clean_download["files_checked"] < 1
        or clean_download.get("hash_mismatches") != 0
    ):
        raise ValueError(f"clean-download verification must pass for ready table: {table_id}")


def validate_pncp_release_package(
    catalog: dict[str, Any],
    kaggle_slug: str,
    package_dir: Path,
) -> dict[str, Any]:
    """Verify a downloaded public release package against its catalogue contract."""
    entries = [
        table
        for table in catalog.get("tables", [])
        if table.get("kaggle_slug") == kaggle_slug
        or table.get("legacy_publication", {}).get("dataset_slug") == kaggle_slug
    ]
    if len(entries) != 1:
        raise ValueError(f"expected one catalogue entry for Kaggle slug: {kaggle_slug}")
    entry = entries[0]

    root = package_dir.resolve(strict=True)
    manifest_path = root / "release_manifest.json"
    schema_path = root / "schema.json"
    audit_path = root / "privacy-audit.json"
    readme_path = root / "README.md"
    for required in (manifest_path, schema_path, audit_path, readme_path):
        if not required.is_file():
            raise ValueError(f"release package is missing required file: {required.name}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if (
        manifest.get("dataset_slug") != kaggle_slug
        or manifest.get("table_id") != entry.get("table_id")
        or manifest.get("layer") != entry.get("layer")
    ):
        raise ValueError("release manifest does not match the catalogue entry")
    manifest_cutoff = manifest.get("data_cutoff")
    catalogue_cutoff = catalog.get("data_cutoff")
    if not isinstance(manifest_cutoff, str) or not isinstance(catalogue_cutoff, str):
        raise ValueError("release manifest and catalogue require a data cutoff")
    if datetime.fromisoformat(manifest_cutoff.replace("Z", "+00:00")).date().isoformat() != catalogue_cutoff[:10]:
        raise ValueError("release manifest cutoff does not match the catalogue entry")

    declared_files = manifest.get("files")
    if not isinstance(declared_files, list) or not declared_files:
        raise ValueError("release manifest requires file hashes")
    seen_paths: set[str] = set()
    parquet_paths: list[Path] = []
    for item in declared_files:
        relative = item.get("path") if isinstance(item, dict) else None
        if not isinstance(relative, str) or relative in seen_paths:
            raise ValueError("release manifest contains an invalid or duplicate file path")
        relpath = PurePosixPath(relative)
        if relpath.is_absolute() or ".." in relpath.parts or len(relpath.parts) != 1:
            raise ValueError("release manifest file paths must be flat relative filenames")
        path = (root / relative).resolve(strict=True)
        if root not in path.parents or not path.is_file():
            raise ValueError("release manifest points outside the package")
        expected_hash = item.get("sha256")
        expected_bytes = item.get("bytes")
        if (
            not isinstance(expected_hash, str)
            or not re.fullmatch(r"[a-fA-F0-9]{64}", expected_hash)
            or not isinstance(expected_bytes, int)
            or isinstance(expected_bytes, bool)
        ):
            raise ValueError("release manifest file entry requires byte size and SHA-256")
        digest = _sha256_file(path)
        if path.stat().st_size != expected_bytes or digest != expected_hash.lower():
            raise ValueError(f"file hash or size mismatch: {relative}")
        if path.suffix.lower() == ".parquet":
            parquet_paths.append(path)
        seen_paths.add(relative)

    if "schema.json" not in seen_paths or "privacy-audit.json" not in seen_paths or not parquet_paths:
        raise ValueError("release package must hash schema, privacy audit, and Parquet data")
    schema_hash = _sha256_file(schema_path)
    if schema_hash != manifest.get("schema_sha256"):
        raise ValueError("release schema hash does not match the manifest")

    row_count = manifest.get("row_count")
    if not isinstance(row_count, int) or isinstance(row_count, bool) or row_count < 1:
        raise ValueError("release manifest requires a positive row_count")
    observed_rows = sum(pq.ParquetFile(path).metadata.num_rows for path in parquet_paths)
    if observed_rows != row_count:
        raise ValueError("Parquet row count does not match the release manifest")

    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    scan = manifest.get("automated_scan")
    if (
        not isinstance(scan, dict)
        or audit.get("status") != "passed"
        or scan.get("status") != "passed"
        or audit.get("rows_released") != row_count
        or scan.get("rows_released") != row_count
        or audit.get("direct_identifier_matches") != 0
        or scan.get("direct_identifier_matches") != 0
    ):
        raise ValueError("release privacy audit does not match the passing manifest scan")

    return {
        "status": "passed",
        "dataset_slug": kaggle_slug,
        "table_id": entry["table_id"],
        "row_count": row_count,
        "files_checked": len(declared_files) + 2,
        "hash_mismatches": 0,
        "manifest_sha256": _sha256_file(manifest_path),
    }
