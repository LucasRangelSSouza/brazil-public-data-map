# PNCP modality reference release verification

## Release identity

- Dataset: [PNCP Trusted Modality Reference](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-modalidades)
- Layer and grain: trusted reference data, one row per modality code
- Source route: [`GET /api/pncp/v1/modalidades`](https://pncp.gov.br/api/pncp/v1/modalidades)
- Cutoff: 31 July 2026, inclusive through 23:59:59 UTC
- Released rows: 19
- Released fields: `id`, `nome`, `descricao`, `statusAtivo`, `dataInclusao`, and `dataAtualizacao`
- Internal ingestion metadata and the source-only `irp` field are absent.

## Historical boundary

The dataset preserves a historical source snapshot through the cutoff. A live check on 29 September 2026 returned 19 modality records. Nine records had source timestamps through the requested cutoff; ten records had since changed and the public endpoint no longer returned their pre-cutoff values. The released snapshot contains the 19 rows whose timestamps meet the cutoff. The Kaggle files are the reproducible record of that historical state because the mutable endpoint no longer returns all earlier values.

This release covers one reference table. It does not establish coverage of other trusted tables, the raw layer, the semantic layer, or the remaining PNCP API operations.

## Publication checks

- The field allowlist retained the six documented public fields and excluded internal metadata.
- The automated direct-identifier scan passed: 19 rows scanned, 19 released, and zero CPF/email matches.
- The release manifest records the source cutoff, schema hash, row count, file hashes, and source-mutation observation. Its SHA-256 is `d88e114fb606a2635759eb161ae421c1218f0e65d64a9025de44b53031582af9`.
- A clean public Kaggle download returned all five release files. Their hashes matched the staged package; there were zero mismatches.
- The public Kaggle page returned HTTP 200 without authentication.
- The map repository test suite passed: 64 tests, including package integrity validation against the clean download.

## Known limit

The live endpoint cannot reconstruct the ten superseded pre-cutoff values. A local refresh from that endpoint creates a new snapshot. To reproduce the published historical artifact, download the pinned Kaggle dataset and verify its manifest hashes.
