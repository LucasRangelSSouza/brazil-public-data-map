# Brazil public data map

An executable map of Brazilian public education and procurement sources. The repository documents official sources, applies a release gate to procurement identifiers, and builds reproducible local release metadata. It does not publish data to Kaggle or contain credentials.

## Current release controls

- registry of official INEP, FNDE, IBGE, and PNCP sources;
- organization-only PNCP identifier policy;
- SHA-256 release manifest with source lineage and privacy approval;
- registry validation and a layer-wide privacy audit;
- fixture-first tests that run without private infrastructure.

## Quick start

```powershell
python -m unittest discover -s tests -v
make check
python -m brazil_data_map validate-registry
python -m brazil_data_map build-fixture-release --output .local-release --retrieved-at 2026-01-03T00:00:00Z
```

## Privacy boundary

The release gate excludes natural-person and unknown supplier records. It never preserves a supplier document, name, contact, or address in the released record. Eligible CNPJ records receive a deterministic `golden_organization_id` for linkage only. It is not identity verification or supplier qualification.

## Kaggle policy

Kaggle is the planned distribution channel for reviewed release artifacts. No Kaggle link or publishing automation appears here until an account exists and a release passes the source, terms, privacy, and manifest gates.

Read the planned release boundary in [docs/dataset-card.md](docs/dataset-card.md).
The implementation contract is in [docs/release-contract.md](docs/release-contract.md).
The [source catalog](docs/source-catalog.md), [join map](docs/join-map.md), and [data dictionary](docs/data-dictionary.md) document the public analytical boundary.

## Portability

`dags/pncp_incremental_update.py` is an Airflow template. It has no token, bucket, project ID, or environment connection. A deployer supplies approved connections and local output paths in their own Airflow environment.

The local command builds raw, trusted, and semantic Parquet layers, `privacy-audit.json`, and `manifest.json` from synthetic records. Pass the same `--retrieved-at` value twice to reproduce the manifest hashes. `.local-release` is ignored by Git. Delete it after inspection.

Open [notebooks/01_local_release_walkthrough.ipynb](notebooks/01_local_release_walkthrough.ipynb) to run the same synthetic path interactively.

## License

Apache-2.0.
