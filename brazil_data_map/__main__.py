from __future__ import annotations

import argparse
import json
from pathlib import Path

from .pipeline import build_public_release
from .registry import load_registry


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate public-source release controls.")
    commands = parser.add_subparsers(dest="command", required=True)
    registry_command = commands.add_parser("validate-registry", help="validate an official-source registry")
    registry_command.add_argument("--path", type=Path, default=Path("sources/registry.json"))
    fixture_command = commands.add_parser("build-fixture-release", help="build a local synthetic release candidate")
    fixture_command.add_argument("--input", type=Path, default=Path("tests/fixtures/pncp_records.json"))
    fixture_command.add_argument("--output", type=Path, required=True)
    fixture_command.add_argument("--source-id", default="pncp")
    fixture_command.add_argument("--source-url", default="https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos")
    fixture_command.add_argument("--retrieved-at", help="optional ISO-8601 timestamp for deterministic fixture builds")
    args = parser.parse_args()

    if args.command == "validate-registry":
        registry = load_registry(args.path)
        print(json.dumps({"status": "passed", "sources": len(registry["sources"])}, indent=2))
    elif args.command == "build-fixture-release":
        records = json.loads(args.input.read_text(encoding="utf-8"))
        result = build_public_release(records, args.output, args.source_id, args.source_url, retrieved_at=args.retrieved_at)
        print(json.dumps({"status": "passed", "output": str(args.output), "record_counts": result["audit"]["record_counts"]}, indent=2))


if __name__ == "__main__":
    main()
