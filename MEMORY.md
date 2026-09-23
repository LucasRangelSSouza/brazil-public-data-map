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

## Next verifiable task

Review the repository against the full public-release contract, run the final scope scan and CI, then publish the GitHub repository. Kaggle publication remains blocked until a reviewed historical dataset and distribution account exist.
