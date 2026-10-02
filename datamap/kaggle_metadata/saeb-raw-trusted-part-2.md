# SAEB assessment (INEP): Raw and Trusted

40 tables, 24,401,699 rows, snapshot 2026-10-02. SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb
- **How it is fetched:** Indicators up to 2023 are `.rar` files named `planilha_de_resultados_{year}.rar` on download.inep.gov.br/saeb/resultados/; from 2025 a single `.xlsx`. The link for each edition is on that year's sub-page of the SAEB results page.
- **Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://lucas.rangeltech.net/datamap/#/dataset/saeb-raw-trusted-part-2
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/saeb-raw-trusted-part-2.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/saeb.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `inep_saeb_microdados_csv_2017_ts_professor` | 753,668 | 135 |
| raw | `inep_saeb_microdados_csv_2019_ts_aluno_2ef` | 85,788 | 53 |
| raw | `inep_saeb_microdados_csv_2019_ts_aluno_34em` | 2,018,515 | 91 |
| raw | `inep_saeb_microdados_csv_2019_ts_aluno_5ef` | 2,581,685 | 89 |
| raw | `inep_saeb_microdados_csv_2019_ts_aluno_9ef` | 2,388,931 | 129 |
| raw | `inep_saeb_microdados_csv_2019_ts_diretor` | 74,176 | 262 |
| raw | `inep_saeb_microdados_csv_2019_ts_escola` | 70,606 | 137 |
| raw | `inep_saeb_microdados_csv_2019_ts_item` | 854 | 15 |
| raw | `inep_saeb_microdados_csv_2019_ts_professor` | 388,119 | 140 |
| raw | `inep_saeb_microdados_csv_2019_ts_secretario_municipal` | 5,412 | 204 |
| raw | `inep_saeb_microdados_csv_2021_ts_aluno_2ef` | 29,819 | 53 |
| raw | `inep_saeb_microdados_csv_2021_ts_aluno_34em` | 2,288,747 | 106 |
| raw | `inep_saeb_microdados_csv_2021_ts_aluno_5ef` | 2,554,184 | 104 |
| raw | `inep_saeb_microdados_csv_2021_ts_aluno_9ef` | 2,591,937 | 144 |
| raw | `inep_saeb_microdados_csv_2021_ts_diretor` | 74,539 | 219 |
| raw | `inep_saeb_microdados_csv_2021_ts_educacao_infantil_2021` | 62,927 | 421 |
| raw | `inep_saeb_microdados_csv_2021_ts_escola` | 70,897 | 137 |
| raw | `inep_saeb_microdados_csv_2021_ts_item` | 854 | 15 |
| raw | `inep_saeb_microdados_csv_2021_ts_professor` | 565,640 | 135 |
| raw | `inep_saeb_microdados_csv_2021_ts_secretario_municipal` | 5,568 | 140 |
| raw | `inep_saeb_microdados_csv_2021_ts_secretario_municipal_2021` | 5,568 | 159 |
| raw | `inep_saeb_microdados_csv_2023_ts_aluno_2ef` | 37,104 | 55 |
| raw | `inep_saeb_microdados_csv_2023_ts_aluno_34em` | 2,091,337 | 117 |
| raw | `inep_saeb_microdados_csv_2023_ts_aluno_5ef` | 2,442,143 | 152 |
| raw | `inep_saeb_microdados_csv_2023_ts_aluno_9ef` | 2,502,907 | 153 |
| raw | `inep_saeb_microdados_csv_2023_ts_diretor` | 107,089 | 237 |
| raw | `inep_saeb_microdados_csv_2023_ts_escola` | 70,151 | 137 |
| raw | `inep_saeb_microdados_csv_2023_ts_item` | 993 | 16 |
| raw | `inep_saeb_microdados_csv_2023_ts_professor` | 411,876 | 162 |
| raw | `inep_saeb_microdados_csv_2023_ts_secretario_municipal` | 5,568 | 182 |
| raw | `inep_saeb_microdados_csv_tabelas` | 64 | 13 |
| raw | `inep_saeb_microdados_txt_1997_biologia_03ano_txt` | 8,005 | 1 |
| raw | `inep_saeb_microdados_txt_1997_ciencias_04serie_txt` | 23,506 | 1 |
| raw | `inep_saeb_microdados_txt_1997_ciencias_08serie_txt` | 18,822 | 1 |
| raw | `inep_saeb_microdados_txt_1997_diretor_97_txt` | 2,351 | 1 |
| raw | `inep_saeb_microdados_txt_1997_docente_97_txt` | 19,339 | 1 |
| raw | `inep_saeb_microdados_txt_1997_escola_97_txt` | 2,351 | 1 |
| raw | `inep_saeb_microdados_txt_1997_fisica_03ano_txt` | 7,988 | 1 |
| raw | `inep_saeb_microdados_txt_1997_matematica_03ano_txt` | 8,136 | 1 |
| raw | `inep_saeb_microdados_txt_1997_matematica_04serie_txt` | 23,535 | 1 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/saeb-raw-trusted-part-2", path="raw__inep_saeb_microdados_csv_2017_ts_professor.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://lucas.rangeltech.net
