# PNCP public procurement: Analytics

6 tables, 10,341,852 rows, snapshot 2026-09-30. Procurement notices (including editais), contracts, price-registration records (atas) and annual procurement plans (PCA) with their items, published through the PNCP consultation API.

## Where the data comes from

- **Publisher:** Portal Nacional de Contratações Públicas (PNCP)
- **Official source:** https://pncp.gov.br/api/consulta/v1
- **How it is fetched:** Public REST API, no key. Four domains are read through the `/atualizacao` axis so a window returns everything that entered or changed: `contratacoes/atualizacao`, `contratos/atualizacao`, `atas/atualizacao`, `pca/atualizacao`. Notices require the modality code (loop 1..19) and a page size of at most 50; the plan endpoint uses `dataInicio`/`dataFim`.
- **Grain and keys:** One row per natural key, keeping the latest version by `dataAtualizacaoGlobal`: `numero_controle_pncp` for notices and contracts, `numero_controle_pncp_ata` for atas, `id_pca_pncp` for plans. Municipality is reachable through `unidade_codigo_ibge` (IBGE code).

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `semantic` tables join and reshape trusted tables for analysis; build them from the matching raw-and-trusted dataset. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://lucas.rangeltech.net/datamap/#/dataset/pncp-analytics
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/pncp-analytics.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/pncp.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| semantic | `obt_pncp_atas` | 1,076,677 | 25 |
| semantic | `obt_pncp_contratacoes` | 3,763,118 | 48 |
| semantic | `obt_pncp_contratos` | 3,428,193 | 55 |
| semantic | `obt_pncp_editais_semantico` | 1,248,539 | 29 |
| semantic | `obt_pncp_pca` | 7,534 | 9 |
| semantic | `obt_pncp_pca_itens` | 817,791 | 23 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/pncp-analytics", path="semantic__obt_pncp_atas.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://lucas.rangeltech.net
