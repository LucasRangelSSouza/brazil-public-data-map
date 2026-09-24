# PNCP historical-window evidence

## Scope

On 2026-09-24, the local checkpointed backfill retrieved the public PNCP publication window for 2025-01-01 and modality 6. The command used the official publication route and wrote its output to a Git-ignored local directory.

## Observed result

The completed checkpoint recorded `2025-01-01:6`. The release candidate contained two raw records, two trusted records, and two semantic records. The privacy audit passed with zero violations. Its manifest recorded schema version 1.1, the extractor commit, source input SHA-256, output file SHA-256 values, and `distribution_version: not_published`.

No source records, organization identifiers, or payload excerpts are retained in this evidence file.

## Limitation

This is one historical day and one modality. It proves that the checkpointed historical path can resume after rate limiting; it is not a historical dataset, a terms assessment, a Kaggle release, or a statement about the coverage of PNCP procurement activity.
