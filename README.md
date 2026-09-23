# Brazil public data map

An executable map of Brazilian public education and procurement sources. The repository documents official sources, applies a release gate to procurement identifiers, and builds reproducible local release metadata. It does not publish data to Kaggle or contain credentials.

## Current release controls

- registry of official INEP, FNDE, IBGE, and PNCP sources;
- organization-only PNCP identifier policy;
- SHA-256 release manifest with source lineage and privacy approval;
- fixture-first tests that run without private infrastructure.

## Quick start

```powershell
python -m unittest discover -s tests -v
make check
```

## Privacy boundary

The release gate excludes natural-person and unknown supplier records. It never preserves a supplier document, name, contact, or address in the released record. Eligible CNPJ records receive a deterministic `golden_organization_id` for linkage only. It is not identity verification or supplier qualification.

## Kaggle policy

Kaggle is the planned distribution channel for reviewed release artifacts. No Kaggle link or publishing automation appears here until an account exists and a release passes the source, terms, privacy, and manifest gates.

Read the planned release boundary in [docs/dataset-card.md](docs/dataset-card.md).

## Portability

`dags/pncp_incremental_update.py` is an Airflow template. It has no token, bucket, project ID, or environment connection. A deployer supplies approved connections and local output paths in their own Airflow environment.

## License

Apache-2.0.
