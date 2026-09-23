# Project memory

## Scope

This repository maps reproducible releases of Brazilian public education and procurement data. It contains no private migration automation, credentials, large source dumps, or person-level records.

## Current state

- A source registry lists initial official sources.
- The PNCP identifier gate releases only organization records with a derived golden organization ID.
- Release manifests require source lineage, file hashes, and a passed privacy gate.

## Next verifiable task

Implement the fixture-backed PNCP incremental extraction path with pagination, retry, deduplication, raw/trusted/semantic layer separation, and release validation.

