# PNCP Kaggle release, version 1

Lucas released the public dataset [Brazil PNCP Procurement History: January 2025](https://www.kaggle.com/datasets/lucasrangelss/brazil-pncp-procurement-history) on 2026-09-25. It covers PNCP publications dated from 2025-01-01 through 2025-01-07 for modality 6, with 1,979 records in each raw, trusted, and semantic layer.

The candidate was rebuilt twice from the same bounded public-source capture at commit `6ea75f48eda6904867bf414060e77571a5aeca30`. Both manifests were identical. The published manifest SHA-256 is `9301e83840fc575b841bcce31cff19a6b72bd37528a88fdee4b50c2fddb20c66`; its privacy audit passed with zero violations.

An independent clean download of the Kaggle version reproduced every declared file hash and the 1,979-row count for all three Parquet layers. A session without a Kaggle login displayed the public data card, version 1, the seven package files, and the `other` source-terms license setting.

The source assessment relies on the [PNCP open-data page](https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos), which describes downloadable API copies of public procurement information, and the [PNCP FAQ](https://www.gov.br/pncp/pt-br/pncp/perguntas-e-respostas/), which states that the portal provides data for consultation, reuse, and monitoring. The Kaggle package preserves these source boundaries in `release_approval.md`; it does not assert a new license over PNCP data.

The release removes notice subjects, names, contacts, addresses, source-system URLs, document content, supplier-result fields, and unreviewed metadata. It retains a controlled procurement category instead of source free text. This is a limited data-engineering release, not a statement about data quality, legal compliance, supplier eligibility, or PNCP-wide coverage.

## Version 2 (2026-09-25): text only

Version 2 rewrites the package README and the dataset description after a style and evidence audit. The three Parquet layers, `privacy-audit.json`, and `release_manifest.json` are byte-identical to version 1: both versions download to the manifest SHA-256 `9301e83840fc575b841bcce31cff19a6b72bd37528a88fdee4b50c2fddb20c66`, so the pin in `pncp-opportunity-recommender` (version 1) is unaffected.
