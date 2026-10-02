# SAEB assessment (INEP): Raw and Trusted

38 tables, 5,526,123 rows, snapshot 2026-10-01. SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb
- **How it is fetched:** Indicators up to 2023 are `.rar` files named `planilha_de_resultados_{year}.rar` on download.inep.gov.br/saeb/resultados/; from 2025 a single `.xlsx`. The link for each edition is on that year's sub-page of the SAEB results page.
- **Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/saeb-raw-trusted-part-4
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/saeb-raw-trusted-part-4.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/saeb.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `inep_saeb_microdados_txt_2003_escola_03_txt` | 6,637 | 1 |
| raw | `inep_saeb_microdados_txt_2003_mascara_txt` | 356,880 | 1 |
| raw | `inep_saeb_microdados_txt_2003_matematica_03ano_txt` | 26,187 | 1 |
| raw | `inep_saeb_microdados_txt_2003_matematica_04serie_txt` | 46,131 | 1 |
| raw | `inep_saeb_microdados_txt_2003_matematica_08serie_txt` | 36,908 | 1 |
| raw | `inep_saeb_microdados_txt_2003_portugues_03ano_txt` | 26,219 | 1 |
| raw | `inep_saeb_microdados_txt_2003_portugues_04serie_txt` | 46,067 | 1 |
| raw | `inep_saeb_microdados_txt_2003_portugues_08serie_txt` | 37,009 | 1 |
| raw | `inep_saeb_microdados_txt_2003_turma_03_txt` | 8,957 | 1 |
| raw | `inep_saeb_microdados_txt_2005_diretor_05_txt` | 4,851 | 1 |
| raw | `inep_saeb_microdados_txt_2005_docente_05_txt` | 16,014 | 1 |
| raw | `inep_saeb_microdados_txt_2005_escola_05_txt` | 4,851 | 1 |
| raw | `inep_saeb_microdados_txt_2005_matematica_03ano_txt` | 22,255 | 1 |
| raw | `inep_saeb_microdados_txt_2005_matematica_04serie_txt` | 41,783 | 1 |
| raw | `inep_saeb_microdados_txt_2005_matematica_08serie_txt` | 33,189 | 1 |
| raw | `inep_saeb_microdados_txt_2005_portugues_03ano_txt` | 22,285 | 1 |
| raw | `inep_saeb_microdados_txt_2005_portugues_04serie_txt` | 42,146 | 1 |
| raw | `inep_saeb_microdados_txt_2005_portugues_08serie_txt` | 33,164 | 1 |
| raw | `inep_saeb_microdados_txt_2005_turma_05_txt` | 8,007 | 1 |
| raw | `inep_saeb_microdados_txt_tabelas` | 68 | 13 |
| raw | `inep_saeb_resultados_planilhas_linhas` | 1,045,960 | 8 |
| raw | `saeb_indicadores_brasil` | 453 | 178 |
| raw | `saeb_indicadores_estados` | 9,917 | 179 |
| raw | `saeb_indicadores_historico_brasil` | 24 | 84 |
| raw | `saeb_indicadores_historico_estados` | 714 | 84 |
| raw | `saeb_indicadores_municipios` | 540,927 | 115 |
| trusted | `api_saeb_boletim_desempenho` | 1,206,898 | 34 |
| trusted | `api_saeb_boletim_escola_edicao` | 464,749 | 20 |
| trusted | `inep_saeb_escola` | 402,323 | 20 |
| trusted | `inep_saeb_indicadores_brasil` | 453 | 178 |
| trusted | `inep_saeb_indicadores_erros_amostrais` | 429 | 11 |
| trusted | `inep_saeb_indicadores_estados` | 9,917 | 179 |
| trusted | `inep_saeb_indicadores_historico_brasil` | 24 | 85 |
| trusted | `inep_saeb_indicadores_historico_estados` | 714 | 85 |
| trusted | `inep_saeb_indicadores_municipios` | 540,927 | 115 |
| trusted | `inep_saeb_microdados_escola` | 461,283 | 28 |
| trusted | `inep_saeb_microdados_item` | 4,255 | 29 |
| trusted | `inep_saeb_secretario` | 16,548 | 6 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/saeb-raw-trusted-part-4", path="raw__inep_saeb_microdados_txt_2003_escola_03_txt.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
