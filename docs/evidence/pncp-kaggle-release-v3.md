# PNCP Kaggle release, version 3

Kaggle published version 3 of [Brazil PNCP Procurement History](https://www.kaggle.com/datasets/lucasrangelss/brazil-pncp-procurement-history) on 2026-09-28. This version contains one bounded item-grain sample: 25 PNCP publication parents dated 2026-09-20 for modality 6, producing 513 records in each of the raw, trusted, and semantic layers.

The published release manifest has SHA-256 `15610ca71e2b23c5c622272c8f38d2fc276b20d229e5709b58ad47467935528f`. Its privacy audit passed with zero violations. The candidate's normalized item capture was replayed without a source request, and both deterministic manifests matched before publication.

Kaggle's clean public download resolved version 3 and reproduced the declared hashes for `privacy-audit.json`, `raw_records.parquet`, `trusted_records.parquet`, and `semantic_records.parquet`. Each published Parquet file contains 513 rows.

The package credits PNCP, uses Kaggle's `other` licence setting, and makes no new licence claim over source data. It excludes item descriptions, notice text, URLs, documents, contacts, addresses, supplier-result fields, and direct personal identifiers. The release is a limited data-engineering sample, not a complete history, supplier recommendation, eligibility assessment, or legal conclusion.
