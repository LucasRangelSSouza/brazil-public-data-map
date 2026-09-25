from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from .download import download_public_file
from .backfill import rebuild_capture_release, run_backfill
from .distribution import validate_distribution_profile
from .pipeline import build_public_release
from .pncp import fetch_publications
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
    download_command = commands.add_parser("download", help="download an explicit HTTPS public source file")
    download_command.add_argument("--url", required=True)
    download_command.add_argument("--output", type=Path, required=True)
    pncp_command = commands.add_parser("fetch-pncp-publications", help="build a local release from a public PNCP publication window")
    pncp_command.add_argument("--start", required=True, help="ISO-8601 date, for example 2026-09-20")
    pncp_command.add_argument("--end", required=True, help="ISO-8601 date, for example 2026-09-20")
    pncp_command.add_argument("--modality-id", type=int, required=True)
    pncp_command.add_argument("--output", type=Path, required=True)
    pncp_command.add_argument("--retrieved-at", help="optional ISO-8601 timestamp for a deterministic manifest")
    backfill_command = commands.add_parser("backfill-pncp", help="resume a bounded local PNCP backfill and build a local release candidate")
    backfill_command.add_argument("--start", required=True, help="ISO-8601 start date")
    backfill_command.add_argument("--end", required=True, help="ISO-8601 end date")
    backfill_command.add_argument("--modality-ids", required=True, help="comma-separated positive modality ids, for example 1,6,8")
    backfill_command.add_argument("--output", type=Path, required=True, help="ignored local output directory")
    backfill_command.add_argument("--retrieved-at", help="optional ISO-8601 timestamp for the release manifest")
    backfill_command.add_argument("--git-commit", help="optional source commit recorded in the manifest")
    rebuild_command = commands.add_parser("rebuild-pncp-capture", help="rebuild a local PNCP candidate from an ignored JSONL capture")
    rebuild_command.add_argument("--input", type=Path, required=True, help="local normalized PNCP JSONL capture")
    rebuild_command.add_argument("--output", type=Path, required=True, help="candidate output directory")
    rebuild_command.add_argument("--retrieved-at", required=True, help="original capture timestamp for a deterministic manifest")
    rebuild_command.add_argument("--git-commit", required=True, help="source commit recorded in the manifest")
    profile_command = commands.add_parser("validate-distribution-profile", help="validate distribution metadata without publishing")
    profile_command.add_argument("--path", type=Path, default=Path("release_profiles/official_sources.json"))
    args = parser.parse_args()

    if args.command == "validate-registry":
        registry = load_registry(args.path)
        print(json.dumps({"status": "passed", "sources": len(registry["sources"])}, indent=2))
    elif args.command == "build-fixture-release":
        records = json.loads(args.input.read_text(encoding="utf-8"))
        result = build_public_release(records, args.output, args.source_id, args.source_url, retrieved_at=args.retrieved_at)
        print(json.dumps({"status": "passed", "output": str(args.output), "record_counts": result["audit"]["record_counts"]}, indent=2))
    elif args.command == "download":
        print(json.dumps(download_public_file(args.url, args.output), indent=2))
    elif args.command == "fetch-pncp-publications":
        records = fetch_publications(date.fromisoformat(args.start), date.fromisoformat(args.end), args.modality_id)
        result = build_public_release(
            records,
            args.output,
            "pncp",
            "https://pncp.gov.br/api/consulta/v1/contratacoes/publicacao",
            retrieved_at=args.retrieved_at,
        )
        print(json.dumps({"status": "passed", "output": str(args.output), "record_counts": result["audit"]["record_counts"]}, indent=2))
    elif args.command == "backfill-pncp":
        modality_ids = [int(value) for value in args.modality_ids.split(",") if value.strip()]
        result = run_backfill(
            date.fromisoformat(args.start),
            date.fromisoformat(args.end),
            modality_ids,
            args.output,
            retrieved_at=args.retrieved_at,
            git_commit=args.git_commit,
        )
        print(json.dumps({"status": "passed", **result}, indent=2))
    elif args.command == "rebuild-pncp-capture":
        result = rebuild_capture_release(
            args.input,
            args.output,
            retrieved_at=args.retrieved_at,
            git_commit=args.git_commit,
        )
        print(json.dumps({"status": "passed", "output": str(args.output), "record_counts": result["audit"]["record_counts"]}, indent=2))
    elif args.command == "validate-distribution-profile":
        profile = json.loads(args.path.read_text(encoding="utf-8"))
        validate_distribution_profile(profile)
        print(json.dumps({"status": "passed", "distribution_status": profile["distribution_status"], "datasets": len(profile["datasets"])}, indent=2))


if __name__ == "__main__":
    main()
