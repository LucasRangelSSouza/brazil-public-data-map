# SAEB assessment (INEP): Raw and Trusted

40 tables, 812,794 rows, snapshot 2026-10-01. SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb
- **How it is fetched:** Indicators up to 2023 are `.rar` files named `planilha_de_resultados_{year}.rar` on download.inep.gov.br/saeb/resultados/; from 2025 a single `.xlsx`. The link for each edition is on that year's sub-page of the SAEB results page.
- **Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/saeb-raw-trusted-part-3
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/saeb-raw-trusted-part-3.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/saeb.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `inep_saeb_microdados_txt_1997_matematica_08serie_txt` | 18,806 | 1 |
| raw | `inep_saeb_microdados_txt_1997_portugues_03ano_txt` | 8,147 | 1 |
| raw | `inep_saeb_microdados_txt_1997_portugues_04serie_txt` | 23,404 | 1 |
| raw | `inep_saeb_microdados_txt_1997_portugues_08serie_txt` | 18,862 | 1 |
| raw | `inep_saeb_microdados_txt_1997_quimica_03ano_txt` | 7,985 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_biologia_03ano_txt` | 11,805 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_ciencias_04serie_txt` | 21,533 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_ciencias_08serie_txt` | 17,928 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_fisica_03ano_txt` | 11,690 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_03ano_txt` | 11,756 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_04serie_txt` | 21,509 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_08serie_txt` | 17,946 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_03ano_txt` | 11,792 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_04serie_txt` | 21,501 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_08serie_txt` | 17,987 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_03ano_txt` | 11,788 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_04serie_txt` | 21,572 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_08serie_txt` | 17,890 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_03ano_txt` | 11,890 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_04serie_txt` | 21,542 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_08serie_txt` | 17,920 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_alunos_zip_quimica_03ano_txt` | 11,715 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_diretores_zip_diretores_99_txt` | 8,829 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_docentes_zip_docentes_99_txt` | 63,992 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_escolas_zip_escolas_99_txt` | 8,829 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_03ano_txt` | 2,998 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_04serie_txt` | 4,968 | 1 |
| raw | `inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_08serie_txt` | 3,422 | 1 |
| raw | `inep_saeb_microdados_txt_2001_diretor_01_txt` | 8,732 | 1 |
| raw | `inep_saeb_microdados_txt_2001_docente_01_txt` | 21,864 | 1 |
| raw | `inep_saeb_microdados_txt_2001_escola_01_txt` | 8,732 | 1 |
| raw | `inep_saeb_microdados_txt_2001_matematica_03ano_txt` | 36,152 | 1 |
| raw | `inep_saeb_microdados_txt_2001_matematica_04serie_txt` | 57,258 | 1 |
| raw | `inep_saeb_microdados_txt_2001_matematica_08serie_txt` | 50,300 | 1 |
| raw | `inep_saeb_microdados_txt_2001_portugues_03ano_txt` | 36,263 | 1 |
| raw | `inep_saeb_microdados_txt_2001_portugues_04serie_txt` | 57,254 | 1 |
| raw | `inep_saeb_microdados_txt_2001_portugues_08serie_txt` | 50,492 | 1 |
| raw | `inep_saeb_microdados_txt_2001_turma_01_txt` | 11,737 | 1 |
| raw | `inep_saeb_microdados_txt_2003_diretor_03_txt` | 6,628 | 1 |
| raw | `inep_saeb_microdados_txt_2003_docente_03_txt` | 17,376 | 1 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/saeb-raw-trusted-part-3", path="raw__inep_saeb_microdados_txt_1997_matematica_08serie_txt.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
