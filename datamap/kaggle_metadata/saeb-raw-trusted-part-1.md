# SAEB assessment (INEP): Raw and Trusted

40 tables, 61,355,678 rows, snapshot 2026-10-01. SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb
- **How it is fetched:** Indicators up to 2023 are `.rar` files named `planilha_de_resultados_{year}.rar` on download.inep.gov.br/saeb/resultados/; from 2025 a single `.xlsx`. The link for each edition is on that year's sub-page of the SAEB results page.
- **Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/saeb-raw-trusted-part-1
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/saeb-raw-trusted-part-1.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/saeb.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `api_saeb_boletim_raw` | 464,751 | 5 |
| raw | `inep_saeb_aluno_2013` | 5,395,142 | 94 |
| raw | `inep_saeb_aluno_2015` | 5,031,032 | 94 |
| raw | `inep_saeb_aluno_2017` | 8,388,310 | 95 |
| raw | `inep_saeb_aluno_2019` | 7,074,919 | 143 |
| raw | `inep_saeb_aluno_2021` | 7,464,687 | 176 |
| raw | `inep_saeb_aluno_2023` | 7,073,491 | 169 |
| raw | `inep_saeb_arquivos` | 64 | 19 |
| raw | `inep_saeb_arquivos_conteudo` | 720 | 20 |
| raw | `inep_saeb_microdados_csv_2011_ts_item` | 518 | 8 |
| raw | `inep_saeb_microdados_csv_2011_ts_pesos` | 184,518 | 14 |
| raw | `inep_saeb_microdados_csv_2011_ts_quest_diretor` | 58,960 | 221 |
| raw | `inep_saeb_microdados_csv_2011_ts_quest_escola` | 58,960 | 75 |
| raw | `inep_saeb_microdados_csv_2011_ts_quest_professor` | 316,668 | 163 |
| raw | `inep_saeb_microdados_csv_2011_ts_resultado_brasil` | 162 | 10 |
| raw | `inep_saeb_microdados_csv_2011_ts_resultado_escola` | 72,808 | 15 |
| raw | `inep_saeb_microdados_csv_2011_ts_resultado_municipio` | 60,608 | 18 |
| raw | `inep_saeb_microdados_csv_2011_ts_resultado_regiao` | 810 | 11 |
| raw | `inep_saeb_microdados_csv_2011_ts_resultado_uf` | 4,374 | 13 |
| raw | `inep_saeb_microdados_csv_2013_ts_aluno_3em` | 150,429 | 94 |
| raw | `inep_saeb_microdados_csv_2013_ts_aluno_5ef` | 2,524,125 | 85 |
| raw | `inep_saeb_microdados_csv_2013_ts_aluno_9ef` | 2,720,588 | 91 |
| raw | `inep_saeb_microdados_csv_2013_ts_diretor` | 56,737 | 118 |
| raw | `inep_saeb_microdados_csv_2013_ts_escola` | 59,251 | 127 |
| raw | `inep_saeb_microdados_csv_2013_ts_item` | 518 | 15 |
| raw | `inep_saeb_microdados_csv_2013_ts_professor` | 237,186 | 134 |
| raw | `inep_saeb_microdados_csv_2015_ts_aluno_3em` | 114,225 | 94 |
| raw | `inep_saeb_microdados_csv_2015_ts_aluno_5ef` | 2,497,431 | 85 |
| raw | `inep_saeb_microdados_csv_2015_ts_aluno_9ef` | 2,419,376 | 91 |
| raw | `inep_saeb_microdados_csv_2015_ts_diretor` | 55,693 | 118 |
| raw | `inep_saeb_microdados_csv_2015_ts_escola` | 57,744 | 128 |
| raw | `inep_saeb_microdados_csv_2015_ts_item` | 518 | 15 |
| raw | `inep_saeb_microdados_csv_2015_ts_professor` | 274,179 | 134 |
| raw | `inep_saeb_microdados_csv_2017_ts_aluno_3em_ag` | 1,966,507 | 95 |
| raw | `inep_saeb_microdados_csv_2017_ts_aluno_3em_esc` | 1,456,325 | 95 |
| raw | `inep_saeb_microdados_csv_2017_ts_aluno_5ef` | 2,624,019 | 86 |
| raw | `inep_saeb_microdados_csv_2017_ts_aluno_9ef` | 2,341,459 | 92 |
| raw | `inep_saeb_microdados_csv_2017_ts_diretor` | 73,674 | 118 |
| raw | `inep_saeb_microdados_csv_2017_ts_escola` | 73,674 | 154 |
| raw | `inep_saeb_microdados_csv_2017_ts_item` | 518 | 15 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/saeb-raw-trusted-part-1", path="raw__api_saeb_boletim_raw.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
