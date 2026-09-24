# PNCP bounded historical-week evidence

## Scope

On 2026-09-24, a local checkpointed capture completed seven public PNCP publication windows: 2025-01-01 through 2025-01-07, each for modality 6. The command used the official public publication route and wrote capture artifacts to a Git-ignored directory.

## Observed result

The checkpoint recorded seven completed windows. After deterministic source-ID reconciliation, the local release candidate contained 1,979 records in each layer: raw, trusted, and semantic. The privacy audit passed with zero violations, while the manifest recorded schema version 1.1, the extractor commit, the source-input SHA-256 digest, layer file SHA-256 digests, and `distribution_version: not_published`.

The run initially exposed identifier-like strings in two public free-text values. The release gate stopped the build. The extractor policy now redacts CPF-like and email-like content before layer construction, and the regression test proves that the audit remains active after redaction. The rebuilt local release passed the audit.

This evidence file keeps no source records, organization identifiers, payload excerpts, or local capture files.

## Limitation

This is a seven-day window for one modality. It is not a complete historical dataset, a source-terms assessment, a Kaggle release, or a statement about PNCP-wide coverage.
