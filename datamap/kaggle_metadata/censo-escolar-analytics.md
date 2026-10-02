# School Census (INEP): Analytics

10 tables, 974,300,023 rows, snapshot 2026-10-01. Yearly School Census microdata at school level: schools, classes, teachers, enrolments and infrastructure, with the historical series recovered from 1995. Student-level and teacher-level microdata are not released.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar
- **How it is fetched:** INEP publishes one ZIP of microdata per year on the open-data page. Download the year, read the CSV inside and apply the data dictionary shipped in the same ZIP.
- **Grain and keys:** School by year for the school tables; the semantic tables aggregate to school-year and municipality-year. The 2025 edition changed the enrolment file from student level to school-level aggregates.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `semantic` tables join and reshape trusted tables for analysis; build them from the matching raw-and-trusted dataset. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://lucas.rangeltech.net/datamap/#/dataset/censo-escolar-analytics
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/censo-escolar-analytics.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/censo-escolar.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| semantic | `f_censo_escolar` | 178,050 | 64 |
| semantic | `f_censo_escolar_municipio` | 5,596 | 39 |
| semantic | `obt_inep_censo_docente_escola_ano` | 7,341,023 | 156 |
| semantic | `obt_inep_censo_escola_ano` | 7,376,443 | 85 |
| semantic | `obt_inep_censo_infraestrutura_escola` | 944,184,704 | 15 |
| semantic | `obt_inep_censo_matricula_escola_ano` | 7,341,017 | 243 |
| semantic | `obt_inep_censo_municipio_ano` | 170,578 | 32 |
| semantic | `obt_inep_censo_municipio_rede_ano` | 352,866 | 30 |
| semantic | `obt_inep_censo_perguntas` | 8,723 | 20 |
| semantic | `obt_inep_censo_turma_escola_ano` | 7,341,023 | 190 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/censo-escolar-analytics", path="semantic__f_censo_escolar.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://lucas.rangeltech.net
