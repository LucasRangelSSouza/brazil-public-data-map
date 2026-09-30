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
- A one-day, modality-6 checkpoint for 2025-01-01 remains an unpublished source-access proof. The separately reviewed seven-day PNCP version-one release is public and should not be confused with that early checkpoint.
- A capture-rebuild command reapplies the current PNCP allowlist and privacy controls to an ignored, bounded public-source JSONL capture before a candidate can be reviewed for distribution.
- `docs/research/pncp-v2-deadline-item-scope.md` defines the bounded PNCP v2 research decision: retain validated deadlines and structured item fields, derive a controlled category, and exclude the raw item description pending a separate review.
- The executable v2 candidate path fetches paginated items at procurement-item grain and exposes `build-pncp-item-candidate`. It requires every parent key needed by the official item route, drops descriptions and source links before writing layers, and is not yet a published dataset.
- A bounded live smoke on 2026-09-28 verified the item route with one 2026-09-20 modality-6 publication parent: five item records returned, with no raw description or source link in the normalized output. The API returned a direct JSON list, which the client now supports. See `docs/evidence/pncp-item-route-smoke-2026-09-28.md`.
- A full one-day local v2 candidate from 2026-09-20 modality 6 produced 513 records per layer, passed the privacy audit, and had every manifest file hash recomputed successfully. The normalized item capture supports a second build with no live item request and an identical manifest. It remains ignored and `not_published`; see `docs/evidence/pncp-v2-item-candidate-2026-09-28.md`.
- Kaggle version 1 of `lucasrangelss/brazil-pncp-procurement-history` is public. Its 2025-01-01 through 2025-01-07 modality-6 coverage has 1,979 rows per layer; two builds produced identical manifests and a clean download matched every declared hash.
- Kaggle version 3 of `lucasrangelss/brazil-pncp-procurement-history` is public. It is a bounded 2026-09-20 modality-6 item-grain sample with 25 procurement parents and 513 rows per layer. A clean public download matched the release manifest hashes and row counts; see `docs/evidence/pncp-kaggle-release-v3.md`.
- On 2026-09-29, twelve separate trusted PNCP reference-table datasets were published to Kaggle and passed a clean-download check of five files each, including manifest hashes, Parquet row counts, and automated CPF/email scans. The batch evidence is `docs/evidence/pncp-trusted-reference-batch-2026-09-29.md`.
- A grouped `pncp-reference-codes-data` Kaggle dataset is published at version 2. It contains 12 trusted lookup tables (272 summed rows), including 11 already available as unchanged standalone legacy datasets and one previously unpublished reference table. A clean download matched the grouped manifest, all 12 Parquet row counts, and 38 downloadable file hashes. The Kaggle control file `dataset-metadata.json` is not included in downloads; its hash is stored separately. Evidence: `docs/evidence/pncp-reference-codes-grouped-v2-2026-09-29.md` and `sources/pncp_release_registry.json`.
- The 47-table PNCP catalogue and 219-operation API inventory validate. Thirteen table-layer entries have release evidence (12 legacy standalone lookups plus the new reference table); 34 remain `inventory-only` (15 trusted, 13 raw, and 6 semantic). The subject plan maps 47 pairs to 14 grouped datasets; only `pncp-reference-codes-data` version 2 is a published grouped target. The table inventory is not PNCP-wide historical coverage.
- The public map now includes `validate-pncp-release-package`, which verifies package identity, cutoff, file hashes, Parquet integrity/row count, and the automated privacy audit after a clean download. The full repository suite passed 64 tests after these catalogue changes.
- The grouped-bundle verifier now supports direct-download flat filenames (`raw__`, `trusted__`, `semantic__`) and clean downloads without the Kaggle control metadata file. The public suite passes 72 tests; private release-tool tests pass 18 tests.

- Kaggle version 1 of `lucasrangelss/brazil-education-data-lake` is public: SIOPE annual municipal declarations 2019-2023 joined to IBGE, 27,830 rows per layer, manifest `44f25960…3506`, built at `379da09`, two identical builds, clean download verified. `total_expenditure_paid` is the municipality-wide total (renamed from a misleading `education_expenditure_paid`).
- Consumers: pncp-opportunity-recommender v0.2.0 pins PNCP v1; education-finance-mlops v0.2.0 pins education v1.

## Next verifiable task

The Censo aggregate extractor validates the approved INEP 2023 XLSX table 1.2 and writes 5,570 municipality-year enrollment records from a locally verified source package. The joined candidate has 27,830 rows/layer, 5,566 matched 2023 records, explicit nulls before 2023, a passed privacy audit, deterministic manifest comparison, and an approval at `docs/release-reviews/education-siope-censo-2023-v2.md`. It was published and clean-download verified as Kaggle education dataset version 3, manifest SHA-256 `311ffeba83b6ccac3d423703b77acb96e6de5ca7c4a86cc9c82881b719caa86d`. A PNCP release with deadlines and item descriptions remains a separate future candidate.
