from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Callable
from urllib.request import Request, urlopen


OPENAPI_SOURCES = {
    "consulta-api": "https://pncp.gov.br/api/consulta/v3/api-docs",
    "integration-api": "https://pncp.gov.br/api/pncp/v3/api-docs",
}
HTTP_METHODS = {"delete", "get", "patch", "post", "put"}
OPERATION_STATUSES = {
    "inventory-only",
    "ready",
    "excluded-with-rationale",
    "unavailable-with-evidence",
}


def build_operation_inventory(specifications: dict[str, dict[str, Any]]) -> dict[str, Any]:
    operations: list[dict[str, Any]] = []
    for source_id in sorted(specifications):
        specification = specifications[source_id]
        for path, path_item in sorted(specification.get("paths", {}).items()):
            inherited_parameters = path_item.get("parameters", [])
            for method, operation in sorted(path_item.items()):
                if method.lower() not in HTTP_METHODS or not isinstance(operation, dict):
                    continue
                parameters = inherited_parameters + operation.get("parameters", [])
                normalized_parameters = [
                    {
                        "name": parameter.get("name"),
                        "in": parameter.get("in"),
                        "required": bool(parameter.get("required", False)),
                        "type": (parameter.get("schema") or {}).get("type"),
                    }
                    for parameter in parameters
                ]
                normalized_parameters.sort(key=lambda value: (str(value["in"]), str(value["name"])))
                operations.append(
                    {
                        "source_api": source_id,
                        "method": method.upper(),
                        "path": path,
                        "operation_id": operation.get("operationId"),
                        "tags": sorted(operation.get("tags", [])),
                        "parameters": normalized_parameters,
                        "authentication_required": bool(operation.get("security", specification.get("security", []))),
                        "release_status": "inventory-only",
                        "linked_table_slugs": [],
                    }
                )
    operations.sort(key=lambda value: (value["source_api"], value["path"], value["method"]))
    return {
        "schema_version": "1.0",
        "observed_at": datetime.now(timezone.utc).date().isoformat(),
        "official_openapi_sources": OPENAPI_SOURCES,
        "operation_count": len(operations),
        "release_status": "inventory-only",
        "operations": operations,
    }


def validate_operation_inventory(catalog: dict[str, Any]) -> None:
    if catalog.get("schema_version") != "1.0":
        raise ValueError("PNCP operation catalog schema_version must be 1.0")
    operations = catalog.get("operations")
    if not isinstance(operations, list) or not operations:
        raise ValueError("PNCP operation catalog requires operations")
    if catalog.get("operation_count") != len(operations):
        raise ValueError("operation_count must match the operation entries")
    if catalog.get("release_status") != "inventory-only":
        raise ValueError("operation inventory must not claim release completion")

    seen: set[tuple[str, str, str]] = set()
    for operation in operations:
        key = (operation.get("source_api"), operation.get("method"), operation.get("path"))
        if not all(isinstance(part, str) and part for part in key):
            raise ValueError("each operation requires a source API, method, and path")
        if key in seen:
            raise ValueError(f"duplicate PNCP operation: {key}")
        if operation.get("release_status") not in OPERATION_STATUSES:
            raise ValueError(f"invalid operation status for {key}")
        if not isinstance(operation.get("linked_table_slugs"), list):
            raise ValueError(f"linked_table_slugs must be a list for {key}")
        if operation.get("release_status") == "ready" and not operation["linked_table_slugs"]:
            raise ValueError(f"ready operation requires at least one linked table slug: {key}")
        seen.add(key)


def sync_operation_inventory(
    output_path: Path,
    *,
    opener: Callable[..., Any] = urlopen,
) -> dict[str, Any]:
    specifications: dict[str, dict[str, Any]] = {}
    for source_id, url in OPENAPI_SOURCES.items():
        request = Request(url, headers={"Accept": "application/json", "User-Agent": "brazil-public-data-map/0.1"})
        with opener(request, timeout=30) as response:
            specifications[source_id] = json.loads(response.read().decode("utf-8"))
    catalog = build_operation_inventory(specifications)
    validate_operation_inventory(catalog)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(catalog, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return catalog
