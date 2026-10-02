# QEdu early childhood: Raw and Trusted

5 tables, 33,296 rows, snapshot 2026-09-30. Early childhood education attendance, teachers, infrastructure and policies per municipality, collected from the QEdu site.

## Where the data comes from

- **Publisher:** QEdu
- **Official source:** https://qedu.org.br/
- **How it is fetched:** Collected from the QEdu site; field names in the JSON do not match the domain names, so the raw table keeps the JSON as delivered.
- **Grain and keys:** Municipality. Two endpoints (basic infrastructure and teachers) return no data at the source for early childhood, which is not a parsing error.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/qedu-raw-trusted
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/qedu-raw-trusted.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/qedu.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `wscrap_qedu_educacao_infantil_raw` | 5,570 | 8 |
| trusted | `wscrap_qedu_educacao_infantil_atendimento` | 11,016 | 9 |
| trusted | `wscrap_qedu_educacao_infantil_docentes` | 5,570 | 18 |
| trusted | `wscrap_qedu_educacao_infantil_infraestrutura` | 5,570 | 24 |
| trusted | `wscrap_qedu_educacao_infantil_politicas` | 5,570 | 19 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/qedu-raw-trusted", path="raw__wscrap_qedu_educacao_infantil_raw.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
