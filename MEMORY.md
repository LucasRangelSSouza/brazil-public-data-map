# Project memory

## Scope

This repository maps reproducible releases of Brazilian public education and procurement data. It contains no private migration automation, credentials, large source dumps, or person-level records.

## Current state

- A source registry lists initial official sources.
- The PNCP identifier gate releases only organization records with a derived golden organization ID.
- Registry validation requires unique official HTTPS sources.
- The release pipeline writes raw, trusted, and semantic JSON layers, a privacy audit, and a manifest from synthetic fixture records.
- Release manifests require source lineage, file hashes, and a passed privacy gate.

## Next verifiable task

Add source-specific retrieval adapters, data dictionaries, and additional article drafts. Publish only after a final public-scope scan and a verified CI run.
