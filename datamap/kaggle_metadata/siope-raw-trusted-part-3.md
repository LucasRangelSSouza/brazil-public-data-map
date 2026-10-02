# SIOPE education finance: Raw and Trusted

8 tables, 338,297,208 rows, snapshot 2026-10-01. Education revenue, expenditure and indicators reported by municipalities and states, from the SIOPE open-data API (Olinda), the FNDE SIOPE exports, and the budget execution report (RREO) PDFs parsed into tables.

## Where the data comes from

- **Publisher:** Fundo Nacional de Desenvolvimento da Educação (FNDE)
- **Official source:** https://www.fnde.gov.br/siope/
- **How it is fetched:** The open-data API is an OData service at https://www.fnde.gov.br/olinda-ide/servico/DADOS_ABERTOS_SIOPE/versao/v1/odata. The RREO reports are PDFs published by FNDE and parsed into tables.
- **Grain and keys:** Municipality (or state) by year and reporting period. Indicator rows repeat by `num_periodo`, so analyses keep the latest period per municipality and year. Municipality joins to IBGE through `codigo_municipio`.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/siope-raw-trusted-part-3
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/siope-raw-trusted-part-3.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/siope.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `rreo_siope_municipio` | 354,435 | 9 |
| raw | `rreo_siope_uf` | 1,685 | 10 |
| raw | `siope_data` | 190,229 | 6 |
| trusted | `api_olinda_siope_dados_gerais` | 382,669 | 63 |
| trusted | `api_olinda_siope_despesas` | 305,518,954 | 32 |
| trusted | `api_olinda_siope_despesas_funcao_educacao` | 3,060,656 | 23 |
| trusted | `api_olinda_siope_indicadores` | 14,993,255 | 24 |
| trusted | `api_olinda_siope_informacoes_complementares` | 13,795,325 | 21 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/siope-raw-trusted-part-3", path="raw__rreo_siope_municipio.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
