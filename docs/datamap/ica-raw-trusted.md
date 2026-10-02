# Literate Child Indicator (INEP): Raw and Trusted

Dataset: [lucasrangelss/ica-raw-trusted](https://www.kaggle.com/datasets/lucasrangelss/ica-raw-trusted) · snapshot 2026-09-30 · 4 tables · 11,026 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais)

Share of children literate at the right age, with the targets agreed up to 2030, by municipality (municipal network) and by state and Brazil (public network).

**Grain and keys:** Municipality by edition (wide format in trusted, long series in semantic); one row per state plus a Brazil row.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://lucas.rangeltech.net/datamap/](https://lucas.rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`inep_ica_municipios`](#raw-inep-ica-municipios) | 5,485 | 21 | 0 | source |
| raw | [`inep_ica_ufs`](#raw-inep-ica-ufs) | 28 | 19 | 0 | source |
| trusted | [`inep_ica_municipios`](#trusted-inep-ica-municipios) | 5,485 | 21 | 0 | `inep_ica_municipios` |
| trusted | [`inep_ica_ufs`](#trusted-inep-ica-ufs) | 28 | 20 | 0 | `inep_ica_ufs` |

## raw · inep_ica_municipios

File `raw__inep_ica_municipios.parquet` · 5,485 rows · 21 columns

**Feeds:** `trusted/inep_ica_municipios`

| Column | Type | Description |
|---|---|---|
| `ANO` | STRING |  |
| `CO_UF` | STRING |  |
| `SG_UF` | STRING |  |
| `CO_MUNICIPIO` | STRING |  |
| `NO_MUNICIPIO` | STRING |  |
| `NO_TP_REDE` | STRING |  |
| `PC_ALUNO_ALFABETIZADO_2023` | STRING |  |
| `PC_ALUNO_ALFABETIZADO_2024` | STRING |  |
| `PC_ALUNO_ALFABETIZADO_2025` | STRING |  |
| `META_FINAL_2024` | STRING |  |
| `META_FINAL_2025` | STRING |  |
| `META_FINAL_2026` | STRING |  |
| `META_FINAL_2027` | STRING |  |
| `META_FINAL_2028` | STRING |  |
| `META_FINAL_2029` | STRING |  |
| `META_FINAL_2030` | STRING |  |
| `CO_NIVEL_ALFABETIZACAO` | STRING |  |
| `PC_AVALIADOS_LP` | STRING |  |
| `ano_referencia` | STRING |  |
| `arquivo_origem` | STRING |  |
| `dt_ingestao_lake` | STRING |  |

## raw · inep_ica_ufs

File `raw__inep_ica_ufs.parquet` · 28 rows · 19 columns

**Feeds:** `trusted/inep_ica_ufs`

| Column | Type | Description |
|---|---|---|
| `ANO` | STRING |  |
| `CD_UF` | STRING |  |
| `SIGLA_UF` | STRING |  |
| `NOME_UF` | STRING |  |
| `REDE` | STRING |  |
| `PC_ALUNO_ALFABETIZADO_2023` | STRING |  |
| `PC_ALUNO_ALFABETIZADO_2024` | STRING |  |
| `PC_ALUNO_ALFABETIZADO_2025` | STRING |  |
| `META_FINAL_2024` | STRING |  |
| `META_FINAL_2025` | STRING |  |
| `META_FINAL_2026` | STRING |  |
| `META_FINAL_2027` | STRING |  |
| `META_FINAL_2028` | STRING |  |
| `META_FINAL_2029` | STRING |  |
| `META_FINAL_2030` | STRING |  |
| `PC_AVALIADOS_LP` | STRING |  |
| `ano_referencia` | STRING |  |
| `arquivo_origem` | STRING |  |
| `dt_ingestao_lake` | STRING |  |

## trusted · inep_ica_municipios

File `trusted__inep_ica_municipios.parquet` · 5,485 rows · 21 columns

ICA/INEP — resultado e metas de alfabetizacao por municipio (rede municipal). Formato largo, uma coluna por ano. Fonte: Avaliacao da Alfabetizacao.

**Built from:** `raw/inep_ica_municipios`

**Feeds:** `semantic/obt_ica_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER |  |
| `co_uf` | INTEGER |  |
| `sg_uf` | STRING |  |
| `codigo_municipio` | INTEGER |  |
| `nome_municipio` | STRING |  |
| `rede` | STRING |  |
| `pc_aluno_alfabetizado_2023` | FLOAT |  |
| `pc_aluno_alfabetizado_2024` | FLOAT |  |
| `pc_aluno_alfabetizado_2025` | FLOAT |  |
| `meta_final_2024` | FLOAT |  |
| `meta_final_2025` | FLOAT |  |
| `meta_final_2026` | FLOAT |  |
| `meta_final_2027` | FLOAT |  |
| `meta_final_2028` | FLOAT |  |
| `meta_final_2029` | FLOAT |  |
| `meta_final_2030` | FLOAT |  |
| `co_nivel_alfabetizacao` | INTEGER |  |
| `pc_avaliados_lp` | FLOAT |  |
| `ano_referencia` | INTEGER |  |
| `arquivo_origem` | STRING |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · inep_ica_ufs

File `trusted__inep_ica_ufs.parquet` · 28 rows · 20 columns

ICA/INEP — resultado e metas de alfabetizacao por UF e Brasil (rede publica). Formato largo, uma coluna por ano. Fonte: Avaliacao da Alfabetizacao.

**Built from:** `raw/inep_ica_ufs`

**Feeds:** `semantic/obt_ica_uf_ano`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER |  |
| `co_uf` | INTEGER |  |
| `sg_uf` | STRING |  |
| `nome_uf` | STRING |  |
| `e_brasil` | BOOLEAN |  |
| `rede` | STRING |  |
| `pc_aluno_alfabetizado_2023` | FLOAT |  |
| `pc_aluno_alfabetizado_2024` | FLOAT |  |
| `pc_aluno_alfabetizado_2025` | FLOAT |  |
| `meta_final_2024` | FLOAT |  |
| `meta_final_2025` | FLOAT |  |
| `meta_final_2026` | FLOAT |  |
| `meta_final_2027` | FLOAT |  |
| `meta_final_2028` | FLOAT |  |
| `meta_final_2029` | FLOAT |  |
| `meta_final_2030` | FLOAT |  |
| `pc_avaliados_lp` | FLOAT |  |
| `ano_referencia` | INTEGER |  |
| `arquivo_origem` | STRING |  |
| `dt_ingestao_lake` | TIMESTAMP |  |
