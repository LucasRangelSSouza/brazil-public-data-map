# Project memory

## Scope

This repository maps reproducible releases of Brazilian public education and procurement data. It contains no private migration automation, credentials, large source dumps, or person-level records.

## Current state

- A source registry lists initial official sources.
- The PNCP identifier gate releases only organization records with a derived golden organization ID.
- Registry validation requires unique official HTTPS sources.
- The release pipeline writes raw, trusted, and semantic Parquet layers, a privacy audit, and a manifest from synthetic fixture records.
- The pipeline now applies a source-specific public field allowlist before it writes any layer; source fields outside the approved list cannot enter a release artifact.
- Release manifests require source lineage, file hashes, and a passed privacy gate.
- The public PNCP publication adapter has fixture-backed pagination and retry tests, plus one sanitized real execution record.
- The checkpointed PNCP backfill stores completed `day:modality` windows locally, skips them on rerun, and deduplicates source IDs by the latest update timestamp. Its generated release manifest records input and file hashes, row counts, schema version, extractor commit, privacy result, and distribution state.
- A sanitized historical-window execution for 2025-01-01 and modality 6 retrieved two records per released layer, passed the privacy audit, and remains explicitly unpublished.
- A capture-rebuild command reapplies the current PNCP allowlist and privacy controls to an ignored, bounded public-source JSONL capture before a candidate can be reviewed for distribution.
- Kaggle version 1 of `lucasrangelss/brazil-pncp-procurement-history` is public. Its 2025-01-01 through 2025-01-07 modality-6 coverage has 1,979 rows per layer; two builds produced identical manifests and a clean download matched every declared hash.

- Kaggle version 1 of `lucasrangelss/brazil-education-data-lake` is public: SIOPE annual municipal declarations 2019-2023 joined to IBGE, 27,830 rows per layer, manifest `44f25960…3506`, built at `379da09`, two identical builds, clean download verified. `total_expenditure_paid` is the municipality-wide total (renamed from a misleading `education_expenditure_paid`).
- Consumers: pncp-opportunity-recommender v0.2.0 pins PNCP v1; education-finance-mlops v0.2.0 pins education v1.

## Next verifiable task

Add a reviewed Censo Escolar municipality-year aggregate to the education release (version 2), and a PNCP release with deadlines and item descriptions for the recommender.
