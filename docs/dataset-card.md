# Dataset card: Brazil PNCP procurement history

## Status

This repository provides a synthetic release fixture and portable extraction controls. It does not yet publish a Kaggle dataset. The intended dataset slug is `brazil-pncp-procurement-history` after a reviewed release and Kaggle account setup.

## Intended content

The future release will contain eligible public procurement records in raw, trusted, and semantic layers. The raw layer preserves eligible source fields and ingestion lineage. The trusted layer keeps the latest record per natural key. The semantic layer exposes documented analysis keys. Document binaries and unnecessary direct identifiers remain out of scope.

![Public-source release boundary](assets/public-release-boundary.png)

## Privacy and limitations

The release gate excludes natural-person and unknown supplier documents. It derives an organization linkage key only for an eligible CNPJ record. Public source availability does not settle redistribution terms; each source requires a release-time review. The [PNCP open-data page](https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos) is the starting point for source access, while the package remains subject to the release contract.

## Reproducibility

Run `make check` to validate the fixture pipeline. The Airflow template is portable and does not contain Kaggle credentials, storage locations, or infrastructure identifiers.
