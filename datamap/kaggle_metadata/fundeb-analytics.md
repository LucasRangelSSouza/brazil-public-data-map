# FUNDEB: Analytics

4 tables, 4,105,508 rows, snapshot 2026-09-30. The FUNDEB panel: complementation by VAAF, VAAT and VAAR, distribution, qualification and indicators per entity and year.

## Where the data comes from

- **Publisher:** Fundo Nacional de Desenvolvimento da Educação (FNDE)
- **Official source:** https://www.fnde.gov.br/
- **How it is fetched:** Published by FNDE as the FUNDEB panel; the raw tables are the panel exports as delivered.
- **Grain and keys:** One row per federal entity (state or municipality) and year for the panel tables.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `semantic` tables join and reshape trusted tables for analysis; build them from the matching raw-and-trusted dataset. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/fundeb-analytics
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/fundeb-analytics.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/fundeb.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| semantic | `obt_fnde_fundeb_cronograma_vaat_municipio_ano` | 13,030 | 24 |
| semantic | `obt_fnde_fundeb_distribuicao_municipio_mes` | 3,382,306 | 16 |
| semantic | `obt_fnde_fundeb_indicadores_siope_municipio_ano` | 626,256 | 12 |
| semantic | `obt_fnde_fundeb_municipio_ano` | 83,916 | 34 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/fundeb-analytics", path="semantic__obt_fnde_fundeb_cronograma_vaat_municipio_ano.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
