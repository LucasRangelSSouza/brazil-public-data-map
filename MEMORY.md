# Project memory

## Scope

This repository maps reproducible releases of Brazilian public education and procurement data. It contains no private migration automation, credentials, large source dumps, or person-level records.

## Current state

- A source registry lists initial official sources.
- The PNCP identifier gate releases only organization records with a derived golden organization ID.
- Registry validation requires unique official HTTPS sources.
- The release pipeline writes raw, trusted, and semantic Parquet layers, a privacy audit, and a manifest from synthetic fixture records.
- Release manifests require source lineage, file hashes, and a passed privacy gate.
- The public PNCP publication adapter has fixture-backed pagination and retry tests, plus one sanitized real execution record.
- The checkpointed PNCP backfill stores completed `day:modality` windows locally, skips them on rerun, and deduplicates source IDs by the latest update timestamp. Its generated release manifest records input and file hashes, row counts, schema version, extractor commit, privacy result, and distribution state.
- A sanitized historical-window execution for 2025-01-01 and modality 6 retrieved two records per released layer, passed the privacy audit, and remains explicitly unpublished.

## Next verifiable task

Review the repository against the full public-release contract, run the final scope scan and CI, then publish the GitHub repository. Kaggle publication remains blocked until a reviewed historical dataset and distribution decision exist.
