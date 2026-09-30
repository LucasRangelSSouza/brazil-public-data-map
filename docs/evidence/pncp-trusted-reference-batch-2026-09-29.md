# PNCP trusted reference release batch

## Published datasets

| Table | Records | Kaggle dataset | Manifest SHA-256 |
|---|---:|---|---|
| `pncp_dom_modalidades` | 19 | [PNCP Trusted Modality Reference](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-modalidades) | `d88e114fb606a2635759eb161ae421c1218f0e65d64a9025de44b53031582af9` |
| `pncp_dom_amparos_legais` | 183 | [PNCP Legal Grounds Reference](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-amparos-legais) | `870437d038c55867c9ca52019d39a216bc896544639229200f664d254cfd1253` |
| `pncp_dom_catalogos` | 2 | [PNCP Catalogues Reference](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-catalogos) | `7567e2d8fe20afc8302d144a8be21f69c005f828422ead01acd15ef42723db72` |
| `pncp_dom_categoria_item_pca` | 8 | [PNCP PCA Item Categories](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-categoria-item-pca) | `3e39e7f737b28615bc6af3c01adf0a05203ccebcd59264b354270daae9b1bc3c` |
| `pncp_dom_criterios_julgamento` | 9 | [PNCP Judgment Criteria](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-criterios-julgamento) | `cde6236caa96556b5fb6cdb4f1ebf4cd174f26c0d94a2cc52e4b52bf35237dfa` |
| `pncp_dom_fontes_orcamentarias` | 6 | [PNCP Budget Sources](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-fontes-orcamentarias) | `a6701f9e7df687957e794f13af75d471f88850ee4ecbe4586e0a4502d9f82c5e` |
| `pncp_dom_portes_empresa` | 6 | [PNCP Company Sizes](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-portes-empresa) | `56bf2aed8b996b775694f372701928d52f56f48c995c3821267df8c81ba1e533` |
| `pncp_dom_tipos_contrato` | 12 | [PNCP Contract Types](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-tipos-contrato) | `447394473d40a713b16727970479132b64c445df97334a9b38ad79c98d14edaf` |
| `pncp_dom_modos_disputa` | 6 | [PNCP Dispute Modes](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-modos-disputa) | `017ea8258dea6a00ced2a4ef8785f27533492c184d68dd20fdfd64d37b19d582` |
| `pncp_dom_tipos_documento` | 20 | [PNCP Document Types](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-tipos-documento) | `51c8e9800aaeb20645868b6201be21d27504ea27257d6e4325a692bb484eaaa6` |
| `pncp_dom_tipos_instrumento_cobranca` | 1 | [PNCP Billing Instrument Types](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-tipos-instrumento-cobranca) | `bc4ef7f467d048856a4ccf09087d23942fe004e7084b0b8c9658b3beacd98f6f` |
| `pncp_dom_tipos_instrumento_convocatorio` | 5 | [PNCP Notice Instrument Types](https://www.kaggle.com/datasets/lucasrangelss/pncp-trusted-dom-tipos-instrumento-convocatorio) | `1b7b8c20fdddbb03f17e151e4535980e92f1d5a7134e7c1d3d3d127068647729` |

Each dataset contains one trusted reference table through 31 July 2026; internal ingestion metadata is not part of the published schema. Automated scans found no CPF or email matches in the twelve release artifacts.

## Verification

All twelve Kaggle datasets report `ready`. Their clean downloads returned five files each; the validator matched every declared hash and Parquet row count. No mismatch occurred. The public audit manifests record zero CPF or email matches. The latest four releases add 6 dispute modes, 20 document types, one billing instrument type, and 5 notice instrument types.

The map repository test suite passed all 64 tests. Its API inventory links the collection `GET` operation for every released table to the matching Kaggle slug. Detail routes and write operations remain `inventory-only`.

The modality release has an additional source-mutation note in its [table-specific evidence](pncp-trusted-dom-modalidades-2026-09-29.md). A cutoff-filtered Kaggle artifact preserves the snapshot; a later API response may not reproduce overwritten values.

## Remaining scope

These twelve releases cover small trusted reference tables only. The other 16 trusted tables remain unpublished, as do all 13 raw tables and all 6 semantic tables. The catalogue is incomplete; release evidence or a documented exclusion is still needed for each remaining table and public API operation.
