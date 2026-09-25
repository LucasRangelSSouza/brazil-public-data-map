# Brazil public data map

![Social preview for the Brazil public data map](docs/assets/social-preview.png)

An executable map of Brazilian public education and procurement sources. The project turns a source registry and a small synthetic PNCP fixture into reviewable raw, trusted, and semantic Parquet layers. It prioritizes local reproduction. A reader needs no cloud account, credential, large data dump, or private infrastructure.

![Public-source release boundary](docs/assets/public-release-boundary.png)

## Current release controls

- registry of official INEP, FNDE, IBGE, and PNCP sources;
- organization-only PNCP identifier policy;
- SHA-256 release manifest with source lineage and privacy approval;
- registry validation and a layer-wide privacy audit;
- fixture-first tests that run without private infrastructure.

## Architecture and local workflow

```mermaid
flowchart LR
    R[Official source registry] --> X[Local extractor or fixture]
    X --> P[Identifier policy and privacy audit]
    P --> L[Raw, trusted, semantic Parquet layers]
    L --> M[Manifest and dataset card]
    M --> D[Reviewed distribution decision]
```

The release path writes three Parquet layers, `privacy-audit.json`, and `manifest.json`. The manifest records only the declared package files, so stale files in an output directory do not silently become part of a release record.

## Quick start

```powershell
python -m unittest discover -s tests -v
.\scripts\check.ps1
python -m brazil_data_map validate-registry
python -m brazil_data_map build-fixture-release --output .local-release --retrieved-at 2026-01-03T00:00:00Z
```

On macOS and Linux, `make check` runs the same validation sequence.

## Privacy boundary

The release gate excludes natural-person and unknown supplier records. It never preserves a supplier document, name, contact, or address in the released record. Eligible CNPJ records receive a deterministic `golden_organization_id` for linkage only. It is not identity verification or supplier qualification.

[contracts/identifier-policy.yaml](contracts/identifier-policy.yaml) defines the rule. Before the audit runs, the release policy redacts CPF-like and email-like content in retained free-text fields; the audit rejects any value that remains.

## Kaggle policy

Kaggle distributes reviewed release artifacts. The first PNCP release is available at [Brazil PNCP Procurement History: January 2025](https://www.kaggle.com/datasets/lucasrangelss/brazil-pncp-procurement-history). It passed the source, field-minimization, privacy, deterministic-build, manifest, and clean-download checks recorded in the release evidence.

Read the planned release boundary in [docs/dataset-card.md](docs/dataset-card.md).
The implementation contract is in [docs/release-contract.md](docs/release-contract.md).
The [source catalog](docs/source-catalog.md), [join map](docs/join-map.md), and [data dictionary](docs/data-dictionary.md) document the public analytical boundary.

## Portability

`dags/pncp_incremental_update.py` is an Airflow template. It has no token, bucket, project ID, or environment connection. A deployer supplies approved connections and local output paths in their own Airflow environment.

The local command builds raw, trusted, and semantic Parquet layers, `privacy-audit.json`, and `manifest.json` from synthetic records. Pass the same `--retrieved-at` value twice to reproduce the manifest hashes. Git ignores `.local-release`. Delete it after inspection.

To retrieve one bounded PNCP publication window directly from the official public endpoint, provide an explicit date range and a modality code:

```powershell
python -m brazil_data_map fetch-pncp-publications --start 2026-09-20 --end 2026-09-20 --modality-id 6 --output .local-pncp-release
```

The command does not publish data. Review the source terms, extraction window, fields, and generated audit before distributing an output.

For a resumable historical acquisition, use the checkpointed backfill command. It records each successful `day:modality` window locally, deduplicates repeated source IDs by most recent update timestamp, and writes a new local release candidate. The capture, checkpoint, and release remain ignored by Git.

```powershell
python -m brazil_data_map backfill-pncp --start 2025-01-01 --end 2025-01-07 --modality-ids 1,6,8 --output .local-pncp-backfill --git-commit (git rev-parse HEAD)
```

Use small, reviewable ranges first. A completed window is not a distribution approval, and a bounded acquisition must be labeled with its actual coverage.

The full command and review contract are documented in [docs/pncp-backfill.md](docs/pncp-backfill.md).

When a reviewer retains a bounded capture locally, rebuild it with the current release controls before distribution. The capture path remains local and Git-ignored; the command writes a new candidate rather than modifying the capture.

```powershell
python -m brazil_data_map rebuild-pncp-capture --input .local-pncp-backfill\normalized-source-capture.jsonl --output .local-pncp-rebuilt\release --retrieved-at 2026-09-24T11:19:40.003138+00:00 --git-commit (git rev-parse HEAD)
```

The repository records a sanitized [successful source-access run](docs/evidence/pncp-publication-run-2026-09-23.md). It documents the command, scope, counts, field set, caption, and limitation without retaining source records.

A separate [historical-window evidence record](docs/evidence/pncp-historical-window-2025-01-01.md) documents the first resumed 2025 checkpoint without retaining source records.

Open [notebooks/01_local_release_walkthrough.ipynb](notebooks/01_local_release_walkthrough.ipynb) to run the same synthetic path interactively.

## Testing

`scripts/check.ps1` (or `make check` on macOS and Linux) compiles the package, validates the registry, validates the distribution profile, and runs fixture-backed tests. The suite covers retry and pagination behavior, resumable window checkpoints, natural-key deduplication, identifier classification, field and value leakage, schema and timestamp validation, layer reconciliation, manifest lineage, notebook validity, and deterministic Parquet release hashes.

## Articles and case study

The first article draft, [Public data is not automatically privacy-safe](articles/public-data-is-not-automatically-privacy-safe.md), explains the release gate and links its claims to [evidence](articles/public-data-release-claim-map.md). The follow-up drafts cover [organization linkage limits](docs/articles/golden-organization-id-without-identity-overreach.md) and [policy testing](docs/articles/testing-a-privacy-policy-like-software.md). They remain Markdown review artifacts until manual publication.

## Limitations

The PNCP version is a bounded seven-day, modality-6 window. It is not a complete historical archive, a legal certification, or a procurement recommendation system. The education dataset remains pending because its direct SIOPE aggregate extraction and source-specific review are not complete. Every later release must complete source-specific retrieval, terms review, schema review, privacy audit, deterministic-build comparison, and reviewer approval.

## License

[Apache-2.0](LICENSE).
