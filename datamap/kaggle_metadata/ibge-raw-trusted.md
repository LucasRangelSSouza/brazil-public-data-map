# IBGE geography: Raw and Trusted

4 tables, 11,196 rows, snapshot 2026-10-01. States and municipalities with their IBGE codes: the key that joins almost every education table.

## Where the data comes from

- **Publisher:** Instituto Brasileiro de Geografia e Estatística (IBGE)
- **Official source:** https://servicodados.ibge.gov.br/api/docs/localidades
- **How it is fetched:** Public REST API of IBGE localities, no key.
- **Grain and keys:** One row per municipality or state.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/ibge-raw-trusted
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/ibge-raw-trusted.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/ibge.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `ibge_estados` | 27 | 7 |
| raw | `ibge_municipios` | 5,571 | 24 |
| trusted | `ibge_estados` | 27 | 7 |
| trusted | `ibge_municipios` | 5,571 | 13 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/ibge-raw-trusted", path="raw__ibge_estados.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
