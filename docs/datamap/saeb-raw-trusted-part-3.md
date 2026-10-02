# SAEB assessment (INEP): Raw and Trusted

Dataset: [lucasrangelss/saeb-raw-trusted-part-3](https://www.kaggle.com/datasets/lucasrangelss/saeb-raw-trusted-part-3) · snapshot 2026-10-01 · 40 tables · 812,794 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb)

SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

**Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`inep_saeb_microdados_txt_1997_matematica_08serie_txt`](#raw-inep-saeb-microdados-txt-1997-matematica-08serie-txt) | 18,806 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_portugues_03ano_txt`](#raw-inep-saeb-microdados-txt-1997-portugues-03ano-txt) | 8,147 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_portugues_04serie_txt`](#raw-inep-saeb-microdados-txt-1997-portugues-04serie-txt) | 23,404 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_portugues_08serie_txt`](#raw-inep-saeb-microdados-txt-1997-portugues-08serie-txt) | 18,862 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_quimica_03ano_txt`](#raw-inep-saeb-microdados-txt-1997-quimica-03ano-txt) | 7,985 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_biologia_03ano_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-biologia-03ano-txt) | 11,805 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_ciencias_04serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-ciencias-04serie-txt) | 21,533 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_ciencias_08serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-ciencias-08serie-txt) | 17,928 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_fisica_03ano_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-fisica-03ano-txt) | 11,690 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_03ano_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-geografia-03ano-txt) | 11,756 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_04serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-geografia-04serie-txt) | 21,509 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_08serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-geografia-08serie-txt) | 17,946 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_03ano_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-historia-03ano-txt) | 11,792 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_04serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-historia-04serie-txt) | 21,501 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_08serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-historia-08serie-txt) | 17,987 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_03ano_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-matematica-03ano-txt) | 11,788 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_04serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-matematica-04serie-txt) | 21,572 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_08serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-matematica-08serie-txt) | 17,890 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_03ano_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-portugues-03ano-txt) | 11,890 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_04serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-portugues-04serie-txt) | 21,542 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_08serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-portugues-08serie-txt) | 17,920 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_alunos_zip_quimica_03ano_txt`](#raw-inep-saeb-microdados-txt-1999-dados-alunos-zip-quimica-03ano-txt) | 11,715 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_diretores_zip_diretores_99_txt`](#raw-inep-saeb-microdados-txt-1999-dados-diretores-zip-diretores-99-txt) | 8,829 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_docentes_zip_docentes_99_txt`](#raw-inep-saeb-microdados-txt-1999-dados-docentes-zip-docentes-99-txt) | 63,992 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_escolas_zip_escolas_99_txt`](#raw-inep-saeb-microdados-txt-1999-dados-escolas-zip-escolas-99-txt) | 8,829 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_03ano_txt`](#raw-inep-saeb-microdados-txt-1999-dados-turmas-zip-turmas-03ano-txt) | 2,998 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_04serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-turmas-zip-turmas-04serie-txt) | 4,968 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_08serie_txt`](#raw-inep-saeb-microdados-txt-1999-dados-turmas-zip-turmas-08serie-txt) | 3,422 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_diretor_01_txt`](#raw-inep-saeb-microdados-txt-2001-diretor-01-txt) | 8,732 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_docente_01_txt`](#raw-inep-saeb-microdados-txt-2001-docente-01-txt) | 21,864 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_escola_01_txt`](#raw-inep-saeb-microdados-txt-2001-escola-01-txt) | 8,732 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_matematica_03ano_txt`](#raw-inep-saeb-microdados-txt-2001-matematica-03ano-txt) | 36,152 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_matematica_04serie_txt`](#raw-inep-saeb-microdados-txt-2001-matematica-04serie-txt) | 57,258 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_matematica_08serie_txt`](#raw-inep-saeb-microdados-txt-2001-matematica-08serie-txt) | 50,300 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_portugues_03ano_txt`](#raw-inep-saeb-microdados-txt-2001-portugues-03ano-txt) | 36,263 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_portugues_04serie_txt`](#raw-inep-saeb-microdados-txt-2001-portugues-04serie-txt) | 57,254 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_portugues_08serie_txt`](#raw-inep-saeb-microdados-txt-2001-portugues-08serie-txt) | 50,492 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2001_turma_01_txt`](#raw-inep-saeb-microdados-txt-2001-turma-01-txt) | 11,737 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_diretor_03_txt`](#raw-inep-saeb-microdados-txt-2003-diretor-03-txt) | 6,628 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_2003_docente_03_txt`](#raw-inep-saeb-microdados-txt-2003-docente-03-txt) | 17,376 | 1 | 1 | source |

## raw · inep_saeb_microdados_txt_1997_matematica_08serie_txt

File `raw__inep_saeb_microdados_txt_1997_matematica_08serie_txt.parquet` · 18,806 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_08SERIE.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_portugues_03ano_txt

File `raw__inep_saeb_microdados_txt_1997_portugues_03ano_txt.parquet` · 8,147 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_03ANO.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_portugues_04serie_txt

File `raw__inep_saeb_microdados_txt_1997_portugues_04serie_txt.parquet` · 23,404 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_04SERIE.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_portugues_08serie_txt

File `raw__inep_saeb_microdados_txt_1997_portugues_08serie_txt.parquet` · 18,862 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_08SERIE.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_quimica_03ano_txt

File `raw__inep_saeb_microdados_txt_1997_quimica_03ano_txt.parquet` · 7,985 rows · 1 columns

Raw de linhas TXT do microdado historico QUIMICA_03ANO.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_biologia_03ano_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_biologia_03ano_txt.parquet` · 11,805 rows · 1 columns

Raw de linhas TXT do microdado historico BIOLOGIA_03ANO.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_ciencias_04serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_ciencias_04serie_txt.parquet` · 21,533 rows · 1 columns

Raw de linhas TXT do microdado historico CIENCIAS_04SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_ciencias_08serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_ciencias_08serie_txt.parquet` · 17,928 rows · 1 columns

Raw de linhas TXT do microdado historico CIENCIAS_08SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_fisica_03ano_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_fisica_03ano_txt.parquet` · 11,690 rows · 1 columns

Raw de linhas TXT do microdado historico FISICA_03ANO.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_03ano_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_03ano_txt.parquet` · 11,756 rows · 1 columns

Raw de linhas TXT do microdado historico GEOGRAFIA_03ANO.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_04serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_04serie_txt.parquet` · 21,509 rows · 1 columns

Raw de linhas TXT do microdado historico GEOGRAFIA_04SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_08serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_geografia_08serie_txt.parquet` · 17,946 rows · 1 columns

Raw de linhas TXT do microdado historico GEOGRAFIA_08SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_03ano_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_03ano_txt.parquet` · 11,792 rows · 1 columns

Raw de linhas TXT do microdado historico HISTORIA_03ANO.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_04serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_04serie_txt.parquet` · 21,501 rows · 1 columns

Raw de linhas TXT do microdado historico HISTORIA_04SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_08serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_historia_08serie_txt.parquet` · 17,987 rows · 1 columns

Raw de linhas TXT do microdado historico HISTORIA_08SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_03ano_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_03ano_txt.parquet` · 11,788 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_03ANO.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_04serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_04serie_txt.parquet` · 21,572 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_04SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_08serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_matematica_08serie_txt.parquet` · 17,890 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_08SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_03ano_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_03ano_txt.parquet` · 11,890 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_03ANO.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_04serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_04serie_txt.parquet` · 21,542 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_04SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_08serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_portugues_08serie_txt.parquet` · 17,920 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_08SERIE.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_alunos_zip_quimica_03ano_txt

File `raw__inep_saeb_microdados_txt_1999_dados_alunos_zip_quimica_03ano_txt.parquet` · 11,715 rows · 1 columns

Raw de linhas TXT do microdado historico QUIMICA_03ANO.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_diretores_zip_diretores_99_txt

File `raw__inep_saeb_microdados_txt_1999_dados_diretores_zip_diretores_99_txt.parquet` · 8,829 rows · 1 columns

Raw de linhas TXT do microdado historico diretores_99.txt do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_docentes_zip_docentes_99_txt

File `raw__inep_saeb_microdados_txt_1999_dados_docentes_zip_docentes_99_txt.parquet` · 63,992 rows · 1 columns

Raw de linhas TXT do microdado historico DOCENTES_99.TXT do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_escolas_zip_escolas_99_txt

File `raw__inep_saeb_microdados_txt_1999_dados_escolas_zip_escolas_99_txt.parquet` · 8,829 rows · 1 columns

Raw de linhas TXT do microdado historico escolas_99.txt do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_03ano_txt

File `raw__inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_03ano_txt.parquet` · 2,998 rows · 1 columns

Raw de linhas TXT do microdado historico Turmas_03ANO.txt do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_04serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_04serie_txt.parquet` · 4,968 rows · 1 columns

Raw de linhas TXT do microdado historico Turmas_04SERIE.txt do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_08serie_txt

File `raw__inep_saeb_microdados_txt_1999_dados_turmas_zip_turmas_08serie_txt.parquet` · 3,422 rows · 1 columns

Raw de linhas TXT do microdado historico Turmas_08SERIE.txt do Saeb 1999.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_diretor_01_txt

File `raw__inep_saeb_microdados_txt_2001_diretor_01_txt.parquet` · 8,732 rows · 1 columns

Raw de linhas TXT do microdado historico DIRETOR_01.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_docente_01_txt

File `raw__inep_saeb_microdados_txt_2001_docente_01_txt.parquet` · 21,864 rows · 1 columns

Raw de linhas TXT do microdado historico DOCENTE_01.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_escola_01_txt

File `raw__inep_saeb_microdados_txt_2001_escola_01_txt.parquet` · 8,732 rows · 1 columns

Raw de linhas TXT do microdado historico ESCOLA_01.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_matematica_03ano_txt

File `raw__inep_saeb_microdados_txt_2001_matematica_03ano_txt.parquet` · 36,152 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_03ANO.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_matematica_04serie_txt

File `raw__inep_saeb_microdados_txt_2001_matematica_04serie_txt.parquet` · 57,258 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_04SERIE.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_matematica_08serie_txt

File `raw__inep_saeb_microdados_txt_2001_matematica_08serie_txt.parquet` · 50,300 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_08SERIE.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_portugues_03ano_txt

File `raw__inep_saeb_microdados_txt_2001_portugues_03ano_txt.parquet` · 36,263 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_03ANO.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_portugues_04serie_txt

File `raw__inep_saeb_microdados_txt_2001_portugues_04serie_txt.parquet` · 57,254 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_04SERIE.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_portugues_08serie_txt

File `raw__inep_saeb_microdados_txt_2001_portugues_08serie_txt.parquet` · 50,492 rows · 1 columns

Raw de linhas TXT do microdado historico PORTUGUES_08SERIE.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2001_turma_01_txt

File `raw__inep_saeb_microdados_txt_2001_turma_01_txt.parquet` · 11,737 rows · 1 columns

Raw de linhas TXT do microdado historico TURMA_01.TXT do Saeb 2001.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_diretor_03_txt

File `raw__inep_saeb_microdados_txt_2003_diretor_03_txt.parquet` · 6,628 rows · 1 columns

Raw de linhas TXT do microdado historico DIRETOR_03.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_2003_docente_03_txt

File `raw__inep_saeb_microdados_txt_2003_docente_03_txt.parquet` · 17,376 rows · 1 columns

Raw de linhas TXT do microdado historico DOCENTE_03.TXT do Saeb 2003.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |
