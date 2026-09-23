from __future__ import annotations

import argparse
import json
from pathlib import Path

from .registry import load_registry


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate public-source release controls.")
    commands = parser.add_subparsers(dest="command", required=True)
    registry_command = commands.add_parser("validate-registry", help="validate an official-source registry")
    registry_command.add_argument("--path", type=Path, default=Path("sources/registry.json"))
    args = parser.parse_args()

    if args.command == "validate-registry":
        registry = load_registry(args.path)
        print(json.dumps({"status": "passed", "sources": len(registry["sources"])}, indent=2))


if __name__ == "__main__":
    main()
