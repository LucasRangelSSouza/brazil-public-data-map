# SAEB assessment (INEP): Analytics

Dataset: [lucasrangelss/saeb-analytics](https://www.kaggle.com/datasets/lucasrangelss/saeb-analytics) · snapshot 2026-10-01 · 8 tables · 1,682,209 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb)

SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

**Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`obt_api_saeb_boletim`](#semantic-obt-api-saeb-boletim) | 603,449 | 69 | 69 | `obt_ibge_municipio`, `obt_inep_censo_escola_ano`, `api_saeb_boletim_desempenho`, `api_saeb_boletim_escola_edicao` |
| semantic | [`obt_inep_saeb_indicadores_brasil_ano`](#semantic-obt-inep-saeb-indicadores-brasil-ano) | 453 | 176 | 176 | `inep_saeb_indicadores_brasil` |
| semantic | [`obt_inep_saeb_indicadores_estado_ano`](#semantic-obt-inep-saeb-indicadores-estado-ano) | 9,917 | 180 | 180 | `obt_ibge_uf`, `inep_saeb_indicadores_estados` |
| semantic | [`obt_inep_saeb_indicadores_historico_brasil_ano`](#semantic-obt-inep-saeb-indicadores-historico-brasil-ano) | 24 | 80 | 80 | `inep_saeb_indicadores_historico_brasil` |
| semantic | [`obt_inep_saeb_indicadores_historico_estado_ano`](#semantic-obt-inep-saeb-indicadores-historico-estado-ano) | 714 | 85 | 85 | `obt_ibge_uf`, `inep_saeb_indicadores_historico_estados` |
| semantic | [`obt_inep_saeb_indicadores_municipio_ano`](#semantic-obt-inep-saeb-indicadores-municipio-ano) | 540,927 | 116 | 116 | `obt_ibge_municipio`, `obt_ibge_uf`, `inep_saeb_indicadores_municipios` |
| semantic | [`obt_inep_saeb_micro_escola_ano`](#semantic-obt-inep-saeb-micro-escola-ano) | 461,283 | 23 | 23 | `obt_ibge_municipio`, `obt_ibge_uf`, `obt_inep_censo_escola_ano`, `inep_saeb_escola` … |
| semantic | [`obt_inep_saeb_micro_municipio_ano`](#semantic-obt-inep-saeb-micro-municipio-ano) | 65,442 | 21 | 21 | `obt_ibge_municipio`, `obt_ibge_uf`, `obt_inep_censo_escola_ano`, `inep_saeb_escola` … |

## semantic · obt_api_saeb_boletim

File `semantic__obt_api_saeb_boletim.parquet` · 603,449 rows · 69 columns

Boletim SAEB por escola/edicao/serie. Grao: 1 linha por (co_entidade, ano, id_serie). Consolida proficiencias medias de LP e Matematica, distribuicao por niveis (0-10) e benchmark de escolas similares para todas as edicoes (2011-2023, anos impares). ~511k registros. Campo profic_similares exclusivo desta API. FK: codigo_municipio (codigo IBGE 7 digitos) obtido do Censo Escolar por (codigo_escola=co_entidade, ano). Origem: trusted_zone.api_saeb_boletim_desempenho + api_saeb_boletim_escola_edicao + semantic_zone.obt_inep_censo_escola_ano. API SAEB INEP.

**Built from:** `semantic/obt_ibge_municipio`, `semantic/obt_inep_censo_escola_ano`, `trusted/api_saeb_boletim_desempenho`, `trusted/api_saeb_boletim_escola_edicao`

| Column | Type | Description |
|---|---|---|
| `codigo_entidade` | INTEGER | Codigo INEP da escola (SAEB). Chave primaria junto com ano e id_serie. |
| `ano` | INTEGER | Ano da edicao do SAEB (2011-2023, anos impares). |
| `id_serie` | INTEGER | Serie avaliada: 5=5o ano EF, 9=9o ano EF, 12/13/14=3a serie EM. |
| `serie` | STRING | Descricao legivel da serie. |
| `escola` | STRING | Nome da escola. |
| `uf` | STRING | Sigla da UF. |
| `municipio` | STRING | Nome do municipio. |
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (INT64). FK para obt_ibge_municipio. Obtido do Censo Escolar (obt_inep_censo_escola_ano) por codigo_escola=co_entidade + ano, com fallback ao ano mais recente da escola. |
| `tipo_rede` | STRING | Dependencia administrativa: FEDERAL, ESTADUAL, MUNICIPAL. |
| `inse` | STRING | Nivel socioeconomico (INSE) da escola: Grupo I (mais baixo) a VIII (mais alto). |
| `perc_doc_sup_anos_iniciais` | FLOAT | % docentes EF anos iniciais com formacao superior. |
| `perc_doc_sup_anos_finais` | FLOAT | % docentes EF anos finais com formacao superior. |
| `perc_doc_sup_ensino_medio` | FLOAT | % docentes EM com formacao superior. |
| `qtd_matriculados` | INTEGER | Alunos matriculados avaliados nesta serie/edicao. |
| `qtd_presentes` | INTEGER | Alunos presentes nesta serie/edicao. |
| `taxa_participacao` | FLOAT | Taxa de participacao (%) nesta serie/edicao. |
| `lp_profic_escola` | FLOAT | LP: Proficiencia media desta escola (Escala SAEB). |
| `lp_profic_similares` | FLOAT | LP: Proficiencia media escolas similares. Exclusivo desta API. |
| `lp_profic_municipio` | FLOAT | LP: Proficiencia media do municipio. Disponivel ate 2017. |
| `lp_profic_estado` | FLOAT | LP: Proficiencia media do estado. Disponivel ate 2017. |
| `lp_profic_brasil` | FLOAT | LP: Proficiencia media do Brasil. Disponivel ate 2017. |
| `lp_esc_nivel_0_pct` | FLOAT | Lp esc nivel 0 pct. |
| `lp_esc_nivel_1_pct` | FLOAT | Lp esc nivel 1 pct. |
| `lp_esc_nivel_2_pct` | FLOAT | Lp esc nivel 2 pct. |
| `lp_esc_nivel_3_pct` | FLOAT | Lp esc nivel 3 pct. |
| `lp_esc_nivel_4_pct` | FLOAT | Lp esc nivel 4 pct. |
| `lp_esc_nivel_5_pct` | FLOAT | Lp esc nivel 5 pct. |
| `lp_esc_nivel_6_pct` | FLOAT | Lp esc nivel 6 pct. |
| `lp_esc_nivel_7_pct` | FLOAT | Lp esc nivel 7 pct. |
| `lp_esc_nivel_8_pct` | FLOAT | Lp esc nivel 8 pct. |
| `lp_esc_nivel_9_pct` | FLOAT | Lp esc nivel 9 pct. |
| `lp_sim_nivel_0_pct` | FLOAT | Lp sim nivel 0 pct. |
| `lp_sim_nivel_1_pct` | FLOAT | Lp sim nivel 1 pct. |
| `lp_sim_nivel_2_pct` | FLOAT | Lp sim nivel 2 pct. |
| `lp_sim_nivel_3_pct` | FLOAT | Lp sim nivel 3 pct. |
| `lp_sim_nivel_4_pct` | FLOAT | Lp sim nivel 4 pct. |
| `lp_sim_nivel_5_pct` | FLOAT | Lp sim nivel 5 pct. |
| `lp_sim_nivel_6_pct` | FLOAT | Lp sim nivel 6 pct. |
| `lp_sim_nivel_7_pct` | FLOAT | Lp sim nivel 7 pct. |
| `lp_sim_nivel_8_pct` | FLOAT | Lp sim nivel 8 pct. |
| `lp_sim_nivel_9_pct` | FLOAT | Lp sim nivel 9 pct. |
| `mat_profic_escola` | FLOAT | MAT: Proficiencia media desta escola. |
| `mat_profic_similares` | FLOAT | MAT: Proficiencia media escolas similares. Exclusivo desta API. |
| `mat_profic_municipio` | FLOAT | MAT: Proficiencia media do municipio. Disponivel ate 2017. |
| `mat_profic_estado` | FLOAT | MAT: Proficiencia media do estado. Disponivel ate 2017. |
| `mat_profic_brasil` | FLOAT | MAT: Proficiencia media do Brasil. Disponivel ate 2017. |
| `mat_esc_nivel_0_pct` | FLOAT | Mat esc nivel 0 pct. |
| `mat_esc_nivel_1_pct` | FLOAT | Mat esc nivel 1 pct. |
| `mat_esc_nivel_2_pct` | FLOAT | Mat esc nivel 2 pct. |
| `mat_esc_nivel_3_pct` | FLOAT | Mat esc nivel 3 pct. |
| `mat_esc_nivel_4_pct` | FLOAT | Mat esc nivel 4 pct. |
| `mat_esc_nivel_5_pct` | FLOAT | Mat esc nivel 5 pct. |
| `mat_esc_nivel_6_pct` | FLOAT | Mat esc nivel 6 pct. |
| `mat_esc_nivel_7_pct` | FLOAT | Mat esc nivel 7 pct. |
| `mat_esc_nivel_8_pct` | FLOAT | Mat esc nivel 8 pct. |
| `mat_esc_nivel_9_pct` | FLOAT | Mat esc nivel 9 pct. |
| `mat_esc_nivel_10_pct` | FLOAT | Mat esc nivel 10 pct. |
| `mat_sim_nivel_0_pct` | FLOAT | Mat sim nivel 0 pct. |
| `mat_sim_nivel_1_pct` | FLOAT | Mat sim nivel 1 pct. |
| `mat_sim_nivel_2_pct` | FLOAT | Mat sim nivel 2 pct. |
| `mat_sim_nivel_3_pct` | FLOAT | Mat sim nivel 3 pct. |
| `mat_sim_nivel_4_pct` | FLOAT | Mat sim nivel 4 pct. |
| `mat_sim_nivel_5_pct` | FLOAT | Mat sim nivel 5 pct. |
| `mat_sim_nivel_6_pct` | FLOAT | Mat sim nivel 6 pct. |
| `mat_sim_nivel_7_pct` | FLOAT | Mat sim nivel 7 pct. |
| `mat_sim_nivel_8_pct` | FLOAT | Mat sim nivel 8 pct. |
| `mat_sim_nivel_9_pct` | FLOAT | Mat sim nivel 9 pct. |
| `mat_sim_nivel_10_pct` | FLOAT | Mat sim nivel 10 pct. |
| `data_extracao` | STRING | Data e hora de extração do registro para o Data Lake (ISO 8601). — descrição gerada por IA. |

## semantic · obt_inep_saeb_indicadores_brasil_ano

File `semantic__obt_inep_saeb_indicadores_brasil_ano.parquet` · 453 rows · 176 columns

SAEB Planilha de Resultados INEP — indicadores nacionais (Brasil) por ano. Grão: 1 linha por (ano_saeb, id_agregacao, dependencia_administrativa, localizacao). Médias de proficiência e distribuição por nível em LP, MT, CH, CN para 2º EF, 5º EF, 9º EF e Ensino Médio. Edições: 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023. Origem: trusted_zone.inep_saeb_indicadores_brasil. Fonte: INEP — https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb/resultados

**Built from:** `trusted/inep_saeb_indicadores_brasil`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do SAEB. Edições: 1995, 1997, 1999, 2001, 2003, 2005 (histórico); 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023 (atual). |
| `id_agregacao` | STRING | Identificador do nível de agregação nacional: Brasil, Pública, Federal, Estadual, Municipal, Privada. |
| `dependencia_administrativa` | STRING | Dependência administrativa da escola: Federal, Estadual, Municipal, Privada, Pública (todas as redes), ou Total. |
| `localizacao` | STRING | Localização da escola: Urbana, Rural ou Total. |
| `capital` | STRING | Capital do estado (Sim/Não) ou Interior — disponível para agregações estaduais. |
| `pc_alfabetizado` | FLOAT | Percentual de alunos considerados alfabetizados (2º ano EF). Disponível para edições a partir de 2019 com avaliação de alfabetização. |
| `media_2_lp` | FLOAT | Média de proficiência em Língua Portuguesa — 2º ano EF (Alfabetização). Escala SAEB 0-500. |
| `media_2_mt` | FLOAT | Média de proficiência em Matemática — 2º ano EF (Alfabetização). Escala SAEB 0-500. |
| `media_5_lp` | FLOAT | Média de proficiência em Língua Portuguesa — 5º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_5_mt` | FLOAT | Média de proficiência em Matemática — 5º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_5_ch` | FLOAT | Média de proficiência em Ciências Humanas — 5º ano EF. Escala SAEB 0-500. |
| `media_5_cn` | FLOAT | Média de proficiência em Ciências da Natureza — 5º ano EF. Escala SAEB 0-500. |
| `media_9_lp` | FLOAT | Média de proficiência em Língua Portuguesa — 9º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_9_mt` | FLOAT | Média de proficiência em Matemática — 9º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_9_ch` | FLOAT | Média de proficiência em Ciências Humanas — 9º ano EF. Escala SAEB 0-500. |
| `media_9_cn` | FLOAT | Média de proficiência em Ciências da Natureza — 9º ano EF. Escala SAEB 0-500. |
| `media_12_lp` | FLOAT | Média de proficiência em Língua Portuguesa — Ensino Médio (série 12, tradicional). Escala SAEB 0-500. |
| `media_12_mt` | FLOAT | Média de proficiência em Matemática — Ensino Médio (série 12, tradicional). Escala SAEB 0-500. |
| `media_13_lp` | FLOAT | Média LP — EM integrado (série 13, Ensino Médio integrado ao técnico). Escala SAEB 0-500. |
| `media_13_mt` | FLOAT | Média MT — EM integrado (série 13). Escala SAEB 0-500. |
| `media_14_lp` | FLOAT | Média LP — EM (série 14, tradicional + integrado combinados). Escala SAEB 0-500. |
| `media_14_mt` | FLOAT | Média MT — EM (série 14, trad. + integrado). Escala SAEB 0-500. |
| `nivel_0_lp2` | FLOAT | % alunos 2º EF em LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp2` | FLOAT | % alunos 2º EF em LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp2` | FLOAT | % alunos 2º EF em LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp2` | FLOAT | % alunos 2º EF em LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp2` | FLOAT | % alunos 2º EF em LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp2` | FLOAT | % alunos 2º EF em LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp2` | FLOAT | % alunos 2º EF em LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp2` | FLOAT | % alunos 2º EF em LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp2` | FLOAT | % alunos 2º EF em LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt2` | FLOAT | % alunos 2º EF em MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt2` | FLOAT | % alunos 2º EF em MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt2` | FLOAT | % alunos 2º EF em MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt2` | FLOAT | % alunos 2º EF em MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt2` | FLOAT | % alunos 2º EF em MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt2` | FLOAT | % alunos 2º EF em MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt2` | FLOAT | % alunos 2º EF em MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt2` | FLOAT | % alunos 2º EF em MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt2` | FLOAT | % alunos 2º EF em MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp5` | FLOAT | % alunos 5º EF em LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp5` | FLOAT | % alunos 5º EF em LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp5` | FLOAT | % alunos 5º EF em LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp5` | FLOAT | % alunos 5º EF em LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp5` | FLOAT | % alunos 5º EF em LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp5` | FLOAT | % alunos 5º EF em LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp5` | FLOAT | % alunos 5º EF em LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp5` | FLOAT | % alunos 5º EF em LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp5` | FLOAT | % alunos 5º EF em LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_lp5` | FLOAT | % alunos 5º EF em LP nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt5` | FLOAT | % alunos 5º EF em MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt5` | FLOAT | % alunos 5º EF em MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt5` | FLOAT | % alunos 5º EF em MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt5` | FLOAT | % alunos 5º EF em MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt5` | FLOAT | % alunos 5º EF em MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt5` | FLOAT | % alunos 5º EF em MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt5` | FLOAT | % alunos 5º EF em MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt5` | FLOAT | % alunos 5º EF em MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt5` | FLOAT | % alunos 5º EF em MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt5` | FLOAT | % alunos 5º EF em MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt5` | FLOAT | % alunos 5º EF em MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_ch5` | FLOAT | % alunos 5º EF em CH nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_ch5` | FLOAT | % alunos 5º EF em CH nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_ch5` | FLOAT | % alunos 5º EF em CH nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_ch5` | FLOAT | % alunos 5º EF em CH nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_ch5` | FLOAT | % alunos 5º EF em CH nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_ch5` | FLOAT | % alunos 5º EF em CH nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_ch5` | FLOAT | % alunos 5º EF em CH nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_ch5` | FLOAT | % alunos 5º EF em CH nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_cn5` | FLOAT | % alunos 5º EF em CN nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_cn5` | FLOAT | % alunos 5º EF em CN nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_cn5` | FLOAT | % alunos 5º EF em CN nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_cn5` | FLOAT | % alunos 5º EF em CN nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_cn5` | FLOAT | % alunos 5º EF em CN nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_cn5` | FLOAT | % alunos 5º EF em CN nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_cn5` | FLOAT | % alunos 5º EF em CN nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_cn5` | FLOAT | % alunos 5º EF em CN nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_cn5` | FLOAT | % alunos 5º EF em CN nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp9` | FLOAT | % alunos 9º EF em LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp9` | FLOAT | % alunos 9º EF em LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp9` | FLOAT | % alunos 9º EF em LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp9` | FLOAT | % alunos 9º EF em LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp9` | FLOAT | % alunos 9º EF em LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp9` | FLOAT | % alunos 9º EF em LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp9` | FLOAT | % alunos 9º EF em LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp9` | FLOAT | % alunos 9º EF em LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp9` | FLOAT | % alunos 9º EF em LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt9` | FLOAT | % alunos 9º EF em MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt9` | FLOAT | % alunos 9º EF em MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt9` | FLOAT | % alunos 9º EF em MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt9` | FLOAT | % alunos 9º EF em MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt9` | FLOAT | % alunos 9º EF em MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt9` | FLOAT | % alunos 9º EF em MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt9` | FLOAT | % alunos 9º EF em MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt9` | FLOAT | % alunos 9º EF em MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt9` | FLOAT | % alunos 9º EF em MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt9` | FLOAT | % alunos 9º EF em MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_ch9` | FLOAT | % alunos 9º EF em CH nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_ch9` | FLOAT | % alunos 9º EF em CH nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_ch9` | FLOAT | % alunos 9º EF em CH nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_ch9` | FLOAT | % alunos 9º EF em CH nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_ch9` | FLOAT | % alunos 9º EF em CH nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_ch9` | FLOAT | % alunos 9º EF em CH nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_ch9` | FLOAT | % alunos 9º EF em CH nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_ch9` | FLOAT | % alunos 9º EF em CH nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_ch9` | FLOAT | % alunos 9º EF em CH nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_ch9` | FLOAT | % alunos 9º EF em CH nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_cn9` | FLOAT | % alunos 9º EF em CN nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_cn9` | FLOAT | % alunos 9º EF em CN nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_cn9` | FLOAT | % alunos 9º EF em CN nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_cn9` | FLOAT | % alunos 9º EF em CN nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_cn9` | FLOAT | % alunos 9º EF em CN nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_cn9` | FLOAT | % alunos 9º EF em CN nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_cn9` | FLOAT | % alunos 9º EF em CN nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_cn9` | FLOAT | % alunos 9º EF em CN nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_cn9` | FLOAT | % alunos 9º EF em CN nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp12` | FLOAT | % alunos EM trad. LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp12` | FLOAT | % alunos EM trad. LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp12` | FLOAT | % alunos EM trad. LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp12` | FLOAT | % alunos EM trad. LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp12` | FLOAT | % alunos EM trad. LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp12` | FLOAT | % alunos EM trad. LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp12` | FLOAT | % alunos EM trad. LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp12` | FLOAT | % alunos EM trad. LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp12` | FLOAT | % alunos EM trad. LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt12` | FLOAT | % alunos EM trad. MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt12` | FLOAT | % alunos EM trad. MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt12` | FLOAT | % alunos EM trad. MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt12` | FLOAT | % alunos EM trad. MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt12` | FLOAT | % alunos EM trad. MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt12` | FLOAT | % alunos EM trad. MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt12` | FLOAT | % alunos EM trad. MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt12` | FLOAT | % alunos EM trad. MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt12` | FLOAT | % alunos EM trad. MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt12` | FLOAT | % alunos EM trad. MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt12` | FLOAT | % alunos EM trad. MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp13` | FLOAT | % alunos EM integ. LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp13` | FLOAT | % alunos EM integ. LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp13` | FLOAT | % alunos EM integ. LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp13` | FLOAT | % alunos EM integ. LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp13` | FLOAT | % alunos EM integ. LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp13` | FLOAT | % alunos EM integ. LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp13` | FLOAT | % alunos EM integ. LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp13` | FLOAT | % alunos EM integ. LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp13` | FLOAT | % alunos EM integ. LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt13` | FLOAT | % alunos EM integ. MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt13` | FLOAT | % alunos EM integ. MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt13` | FLOAT | % alunos EM integ. MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt13` | FLOAT | % alunos EM integ. MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt13` | FLOAT | % alunos EM integ. MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt13` | FLOAT | % alunos EM integ. MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt13` | FLOAT | % alunos EM integ. MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt13` | FLOAT | % alunos EM integ. MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt13` | FLOAT | % alunos EM integ. MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt13` | FLOAT | % alunos EM integ. MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt13` | FLOAT | % alunos EM integ. MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp14` | FLOAT | % alunos EM LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp14` | FLOAT | % alunos EM LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp14` | FLOAT | % alunos EM LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp14` | FLOAT | % alunos EM LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp14` | FLOAT | % alunos EM LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp14` | FLOAT | % alunos EM LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp14` | FLOAT | % alunos EM LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp14` | FLOAT | % alunos EM LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp14` | FLOAT | % alunos EM LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt14` | FLOAT | % alunos EM MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt14` | FLOAT | % alunos EM MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt14` | FLOAT | % alunos EM MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt14` | FLOAT | % alunos EM MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt14` | FLOAT | % alunos EM MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt14` | FLOAT | % alunos EM MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt14` | FLOAT | % alunos EM MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt14` | FLOAT | % alunos EM MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt14` | FLOAT | % alunos EM MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt14` | FLOAT | % alunos EM MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt14` | FLOAT | % alunos EM MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |

## semantic · obt_inep_saeb_indicadores_estado_ano

File `semantic__obt_inep_saeb_indicadores_estado_ano.parquet` · 9,917 rows · 180 columns

SAEB Planilha de Resultados INEP — indicadores por estado (UF) e ano. Grão: 1 linha por (ano_saeb, codigo_uf, dependencia_administrativa, localizacao). Médias de proficiência e distribuição por nível em LP, MT, CH, CN para 2º EF, 5º EF, 9º EF e Ensino Médio. Edições: 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023. Origem: trusted_zone.inep_saeb_indicadores_estados. Fonte: INEP — https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb/resultados

**Built from:** `semantic/obt_ibge_uf`, `trusted/inep_saeb_indicadores_estados`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do SAEB. Edições: 1995, 1997, 1999, 2001, 2003, 2005 (histórico); 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023 (atual). |
| `codigo_uf` | INTEGER | Código IBGE numérico da UF (2 dígitos). INT64. |
| `nome_uf` | STRING | Nome da UF. |
| `sigla_uf` | STRING | Sigla de 2 letras da UF. |
| `codigo_regiao` | INTEGER | C?digo IBGE da regi?o geogr?fica. |
| `nome_regiao` | STRING | Nome da regi?o geogr?fica. |
| `dependencia_administrativa` | STRING | Dependência administrativa da escola: Federal, Estadual, Municipal, Privada, Pública (todas as redes), ou Total. |
| `localizacao` | STRING | Localização da escola: Urbana, Rural ou Total. |
| `capital` | STRING | Capital do estado (Sim/Não) ou Interior — disponível para agregações estaduais. |
| `pc_alfabetizado` | FLOAT | Percentual de alunos considerados alfabetizados (2º ano EF). Disponível para edições a partir de 2019 com avaliação de alfabetização. |
| `media_2_lp` | FLOAT | Média de proficiência em Língua Portuguesa — 2º ano EF (Alfabetização). Escala SAEB 0-500. |
| `media_2_mt` | FLOAT | Média de proficiência em Matemática — 2º ano EF (Alfabetização). Escala SAEB 0-500. |
| `media_5_lp` | FLOAT | Média de proficiência em Língua Portuguesa — 5º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_5_mt` | FLOAT | Média de proficiência em Matemática — 5º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_5_ch` | FLOAT | Média de proficiência em Ciências Humanas — 5º ano EF. Escala SAEB 0-500. |
| `media_5_cn` | FLOAT | Média de proficiência em Ciências da Natureza — 5º ano EF. Escala SAEB 0-500. |
| `media_9_lp` | FLOAT | Média de proficiência em Língua Portuguesa — 9º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_9_mt` | FLOAT | Média de proficiência em Matemática — 9º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_9_ch` | FLOAT | Média de proficiência em Ciências Humanas — 9º ano EF. Escala SAEB 0-500. |
| `media_9_cn` | FLOAT | Média de proficiência em Ciências da Natureza — 9º ano EF. Escala SAEB 0-500. |
| `media_12_lp` | FLOAT | Média de proficiência em Língua Portuguesa — Ensino Médio (série 12, tradicional). Escala SAEB 0-500. |
| `media_12_mt` | FLOAT | Média de proficiência em Matemática — Ensino Médio (série 12, tradicional). Escala SAEB 0-500. |
| `media_13_lp` | FLOAT | Média LP — EM integrado (série 13, Ensino Médio integrado ao técnico). Escala SAEB 0-500. |
| `media_13_mt` | FLOAT | Média MT — EM integrado (série 13). Escala SAEB 0-500. |
| `media_14_lp` | FLOAT | Média LP — EM (série 14, tradicional + integrado combinados). Escala SAEB 0-500. |
| `media_14_mt` | FLOAT | Média MT — EM (série 14, trad. + integrado). Escala SAEB 0-500. |
| `nivel_0_lp2` | FLOAT | % alunos 2º EF em LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp2` | FLOAT | % alunos 2º EF em LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp2` | FLOAT | % alunos 2º EF em LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp2` | FLOAT | % alunos 2º EF em LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp2` | FLOAT | % alunos 2º EF em LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp2` | FLOAT | % alunos 2º EF em LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp2` | FLOAT | % alunos 2º EF em LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp2` | FLOAT | % alunos 2º EF em LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp2` | FLOAT | % alunos 2º EF em LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt2` | FLOAT | % alunos 2º EF em MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt2` | FLOAT | % alunos 2º EF em MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt2` | FLOAT | % alunos 2º EF em MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt2` | FLOAT | % alunos 2º EF em MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt2` | FLOAT | % alunos 2º EF em MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt2` | FLOAT | % alunos 2º EF em MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt2` | FLOAT | % alunos 2º EF em MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt2` | FLOAT | % alunos 2º EF em MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt2` | FLOAT | % alunos 2º EF em MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp5` | FLOAT | % alunos 5º EF em LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp5` | FLOAT | % alunos 5º EF em LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp5` | FLOAT | % alunos 5º EF em LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp5` | FLOAT | % alunos 5º EF em LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp5` | FLOAT | % alunos 5º EF em LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp5` | FLOAT | % alunos 5º EF em LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp5` | FLOAT | % alunos 5º EF em LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp5` | FLOAT | % alunos 5º EF em LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp5` | FLOAT | % alunos 5º EF em LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_lp5` | FLOAT | % alunos 5º EF em LP nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt5` | FLOAT | % alunos 5º EF em MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt5` | FLOAT | % alunos 5º EF em MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt5` | FLOAT | % alunos 5º EF em MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt5` | FLOAT | % alunos 5º EF em MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt5` | FLOAT | % alunos 5º EF em MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt5` | FLOAT | % alunos 5º EF em MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt5` | FLOAT | % alunos 5º EF em MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt5` | FLOAT | % alunos 5º EF em MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt5` | FLOAT | % alunos 5º EF em MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt5` | FLOAT | % alunos 5º EF em MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt5` | FLOAT | % alunos 5º EF em MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_ch5` | FLOAT | % alunos 5º EF em CH nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_ch5` | FLOAT | % alunos 5º EF em CH nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_ch5` | FLOAT | % alunos 5º EF em CH nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_ch5` | FLOAT | % alunos 5º EF em CH nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_ch5` | FLOAT | % alunos 5º EF em CH nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_ch5` | FLOAT | % alunos 5º EF em CH nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_ch5` | FLOAT | % alunos 5º EF em CH nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_ch5` | FLOAT | % alunos 5º EF em CH nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_cn5` | FLOAT | % alunos 5º EF em CN nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_cn5` | FLOAT | % alunos 5º EF em CN nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_cn5` | FLOAT | % alunos 5º EF em CN nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_cn5` | FLOAT | % alunos 5º EF em CN nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_cn5` | FLOAT | % alunos 5º EF em CN nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_cn5` | FLOAT | % alunos 5º EF em CN nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_cn5` | FLOAT | % alunos 5º EF em CN nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_cn5` | FLOAT | % alunos 5º EF em CN nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_cn5` | FLOAT | % alunos 5º EF em CN nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp9` | FLOAT | % alunos 9º EF em LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp9` | FLOAT | % alunos 9º EF em LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp9` | FLOAT | % alunos 9º EF em LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp9` | FLOAT | % alunos 9º EF em LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp9` | FLOAT | % alunos 9º EF em LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp9` | FLOAT | % alunos 9º EF em LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp9` | FLOAT | % alunos 9º EF em LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp9` | FLOAT | % alunos 9º EF em LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp9` | FLOAT | % alunos 9º EF em LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt9` | FLOAT | % alunos 9º EF em MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt9` | FLOAT | % alunos 9º EF em MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt9` | FLOAT | % alunos 9º EF em MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt9` | FLOAT | % alunos 9º EF em MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt9` | FLOAT | % alunos 9º EF em MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt9` | FLOAT | % alunos 9º EF em MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt9` | FLOAT | % alunos 9º EF em MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt9` | FLOAT | % alunos 9º EF em MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt9` | FLOAT | % alunos 9º EF em MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt9` | FLOAT | % alunos 9º EF em MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_ch9` | FLOAT | % alunos 9º EF em CH nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_ch9` | FLOAT | % alunos 9º EF em CH nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_ch9` | FLOAT | % alunos 9º EF em CH nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_ch9` | FLOAT | % alunos 9º EF em CH nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_ch9` | FLOAT | % alunos 9º EF em CH nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_ch9` | FLOAT | % alunos 9º EF em CH nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_ch9` | FLOAT | % alunos 9º EF em CH nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_ch9` | FLOAT | % alunos 9º EF em CH nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_ch9` | FLOAT | % alunos 9º EF em CH nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_ch9` | FLOAT | % alunos 9º EF em CH nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_cn9` | FLOAT | % alunos 9º EF em CN nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_cn9` | FLOAT | % alunos 9º EF em CN nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_cn9` | FLOAT | % alunos 9º EF em CN nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_cn9` | FLOAT | % alunos 9º EF em CN nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_cn9` | FLOAT | % alunos 9º EF em CN nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_cn9` | FLOAT | % alunos 9º EF em CN nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_cn9` | FLOAT | % alunos 9º EF em CN nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_cn9` | FLOAT | % alunos 9º EF em CN nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_cn9` | FLOAT | % alunos 9º EF em CN nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp12` | FLOAT | % alunos EM trad. LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp12` | FLOAT | % alunos EM trad. LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp12` | FLOAT | % alunos EM trad. LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp12` | FLOAT | % alunos EM trad. LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp12` | FLOAT | % alunos EM trad. LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp12` | FLOAT | % alunos EM trad. LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp12` | FLOAT | % alunos EM trad. LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp12` | FLOAT | % alunos EM trad. LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp12` | FLOAT | % alunos EM trad. LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt12` | FLOAT | % alunos EM trad. MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt12` | FLOAT | % alunos EM trad. MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt12` | FLOAT | % alunos EM trad. MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt12` | FLOAT | % alunos EM trad. MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt12` | FLOAT | % alunos EM trad. MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt12` | FLOAT | % alunos EM trad. MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt12` | FLOAT | % alunos EM trad. MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt12` | FLOAT | % alunos EM trad. MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt12` | FLOAT | % alunos EM trad. MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt12` | FLOAT | % alunos EM trad. MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt12` | FLOAT | % alunos EM trad. MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp13` | FLOAT | % alunos EM integ. LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp13` | FLOAT | % alunos EM integ. LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp13` | FLOAT | % alunos EM integ. LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp13` | FLOAT | % alunos EM integ. LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp13` | FLOAT | % alunos EM integ. LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp13` | FLOAT | % alunos EM integ. LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp13` | FLOAT | % alunos EM integ. LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp13` | FLOAT | % alunos EM integ. LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp13` | FLOAT | % alunos EM integ. LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt13` | FLOAT | % alunos EM integ. MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt13` | FLOAT | % alunos EM integ. MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt13` | FLOAT | % alunos EM integ. MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt13` | FLOAT | % alunos EM integ. MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt13` | FLOAT | % alunos EM integ. MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt13` | FLOAT | % alunos EM integ. MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt13` | FLOAT | % alunos EM integ. MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt13` | FLOAT | % alunos EM integ. MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt13` | FLOAT | % alunos EM integ. MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt13` | FLOAT | % alunos EM integ. MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt13` | FLOAT | % alunos EM integ. MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp14` | FLOAT | % alunos EM LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp14` | FLOAT | % alunos EM LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp14` | FLOAT | % alunos EM LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp14` | FLOAT | % alunos EM LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp14` | FLOAT | % alunos EM LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp14` | FLOAT | % alunos EM LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp14` | FLOAT | % alunos EM LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp14` | FLOAT | % alunos EM LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp14` | FLOAT | % alunos EM LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt14` | FLOAT | % alunos EM MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt14` | FLOAT | % alunos EM MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt14` | FLOAT | % alunos EM MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt14` | FLOAT | % alunos EM MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt14` | FLOAT | % alunos EM MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt14` | FLOAT | % alunos EM MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt14` | FLOAT | % alunos EM MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt14` | FLOAT | % alunos EM MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt14` | FLOAT | % alunos EM MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt14` | FLOAT | % alunos EM MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt14` | FLOAT | % alunos EM MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |

## semantic · obt_inep_saeb_indicadores_historico_brasil_ano

File `semantic__obt_inep_saeb_indicadores_historico_brasil_ano.parquet` · 24 rows · 80 columns

SAEB Planilha de Resultados INEP — série histórica NACIONAL (Brasil), formato antigo 1995-2005. Grão: 1 linha por (ano_saeb, dependencia_administrativa). Distribuição percentual de alunos por nível de proficiência (0 a 13) em MT e LP para 5º EF, 9º EF e Ensino Médio. Edições: 1995, 1997, 1999, 2001, 2003, 2005. ATENÇÃO: formato diferente das edições atuais (2007+) — até 14 níveis de proficiência vs máx 11 nas edições atuais; sem disciplinas CH/CN; sem campo media_*. Origem: trusted_zone.inep_saeb_indicadores_historico_brasil. Fonte: INEP — https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb/resultados

**Built from:** `trusted/inep_saeb_indicadores_historico_brasil`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do SAEB. Edições: 1995, 1997, 1999, 2001, 2003, 2005 (histórico); 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023 (atual). |
| `dependencia_administrativa` | STRING | Dependência administrativa: Estadual, Municipal, Total, Particular, Federal, Pública. |
| `nivel_0_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_12_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 12 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_13_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 13 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_12_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 12 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_13_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 13 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_12_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 12 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_13_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 13 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |

## semantic · obt_inep_saeb_indicadores_historico_estado_ano

File `semantic__obt_inep_saeb_indicadores_historico_estado_ano.parquet` · 714 rows · 85 columns

SAEB Planilha de Resultados INEP — série histórica por ESTADO (UF), formato antigo 1995-2005. Grão: 1 linha por (ano_saeb, codigo_uf, dependencia_administrativa). ~714 linhas total. Distribuição percentual de alunos por nível de proficiência (0 a 13) em MT e LP para 5º EF, 9º EF e Ensino Médio. Edições: 1995, 1997, 1999, 2001, 2003, 2005. ATENÇÃO: formato diferente das edições atuais (2007+) — até 14 níveis vs máx 11; sem CH/CN; sem media_*. Origem: trusted_zone.inep_saeb_indicadores_historico_estados. Fonte: INEP — https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb/resultados

**Built from:** `semantic/obt_ibge_uf`, `trusted/inep_saeb_indicadores_historico_estados`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do SAEB. Edições: 1995, 1997, 1999, 2001, 2003, 2005 (histórico); 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023 (atual). |
| `codigo_uf` | INTEGER | Código IBGE numérico da UF (2 dígitos). INT64. |
| `nome_uf` | STRING | Nome da UF. |
| `sigla_uf` | STRING | Sigla de 2 letras da UF. |
| `codigo_regiao` | INTEGER | C?digo IBGE da regi?o geogr?fica. |
| `nome_regiao` | STRING | Nome da regi?o geogr?fica. |
| `dependencia_administrativa` | STRING | Dependência administrativa: Estadual, Municipal, Total, Particular. |
| `nivel_0_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_12_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 12 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_13_mt5` | FLOAT | % alunos 5º EF em MT (hist. 1995-2005) nível 13 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_12_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 12 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_13_mt9` | FLOAT | % alunos 9º EF em MT (hist. 1995-2005) nível 13 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_12_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 12 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_13_mt12` | FLOAT | % alunos EM MT (hist. 1995-2005) nível 13 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_lp5` | FLOAT | % alunos 5º EF em LP (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_lp9` | FLOAT | % alunos 9º EF em LP (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_11_lp12` | FLOAT | % alunos EM LP (hist. 1995-2005) nível 11 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |

## semantic · obt_inep_saeb_indicadores_municipio_ano

File `semantic__obt_inep_saeb_indicadores_municipio_ano.parquet` · 540,927 rows · 116 columns

SAEB Planilha de Resultados INEP — indicadores por município e ano. Grão: 1 linha por (ano_saeb, codigo_municipio, dependencia_administrativa, localizacao). Contém médias de proficiência (escala 0-500) e distribuição percentual por nível de proficiência em Língua Portuguesa e Matemática para 5º EF, 9º EF e Ensino Médio. Edições: 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023. FK: codigo_municipio -> obt_ibge_municipio. Fonte: INEP — https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb/resultados

**Built from:** `semantic/obt_ibge_municipio`, `semantic/obt_ibge_uf`, `trusted/inep_saeb_indicadores_municipios`

| Column | Type | Description |
|---|---|---|
| `ano_saeb` | INTEGER | Ano de aplicação do SAEB. Edições: 1995, 1997, 1999, 2001, 2003, 2005 (histórico); 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023 (atual). |
| `codigo_municipio` | INTEGER | Código IBGE de 7 dígitos do município. INT64. FK para obt_ibge_municipio. |
| `nome_municipio` | STRING | Nome do munic?pio. |
| `codigo_uf` | INTEGER | Código IBGE numérico da UF (2 dígitos). INT64. |
| `nome_uf` | STRING | Nome da UF. |
| `sigla_uf` | STRING | Sigla de 2 letras da UF. |
| `codigo_regiao` | INTEGER | C?digo IBGE da regi?o geogr?fica. |
| `nome_regiao` | STRING | Nome da regi?o geogr?fica. |
| `dependencia_administrativa` | STRING | Dependência administrativa da escola: Federal, Estadual, Municipal, Privada, Pública (todas as redes), ou Total. |
| `localizacao` | STRING | Localização da escola: Urbana, Rural ou Total. |
| `media_5_lp` | FLOAT | Média de proficiência em Língua Portuguesa — 5º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_5_mt` | FLOAT | Média de proficiência em Matemática — 5º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_9_lp` | FLOAT | Média de proficiência em Língua Portuguesa — 9º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_9_mt` | FLOAT | Média de proficiência em Matemática — 9º ano do Ensino Fundamental. Escala SAEB 0-500. |
| `media_12_lp` | FLOAT | Média de proficiência em Língua Portuguesa — Ensino Médio (série 12, tradicional). Escala SAEB 0-500. |
| `media_12_mt` | FLOAT | Média de proficiência em Matemática — Ensino Médio (série 12, tradicional). Escala SAEB 0-500. |
| `nivel_0_lp5` | FLOAT | % alunos 5º EF em LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp5` | FLOAT | % alunos 5º EF em LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp5` | FLOAT | % alunos 5º EF em LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp5` | FLOAT | % alunos 5º EF em LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp5` | FLOAT | % alunos 5º EF em LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp5` | FLOAT | % alunos 5º EF em LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp5` | FLOAT | % alunos 5º EF em LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp5` | FLOAT | % alunos 5º EF em LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp5` | FLOAT | % alunos 5º EF em LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_lp5` | FLOAT | % alunos 5º EF em LP nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt5` | FLOAT | % alunos 5º EF em MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt5` | FLOAT | % alunos 5º EF em MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt5` | FLOAT | % alunos 5º EF em MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt5` | FLOAT | % alunos 5º EF em MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt5` | FLOAT | % alunos 5º EF em MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt5` | FLOAT | % alunos 5º EF em MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt5` | FLOAT | % alunos 5º EF em MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt5` | FLOAT | % alunos 5º EF em MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt5` | FLOAT | % alunos 5º EF em MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt5` | FLOAT | % alunos 5º EF em MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt5` | FLOAT | % alunos 5º EF em MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp9` | FLOAT | % alunos 9º EF em LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp9` | FLOAT | % alunos 9º EF em LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp9` | FLOAT | % alunos 9º EF em LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp9` | FLOAT | % alunos 9º EF em LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp9` | FLOAT | % alunos 9º EF em LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp9` | FLOAT | % alunos 9º EF em LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp9` | FLOAT | % alunos 9º EF em LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp9` | FLOAT | % alunos 9º EF em LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp9` | FLOAT | % alunos 9º EF em LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt9` | FLOAT | % alunos 9º EF em MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt9` | FLOAT | % alunos 9º EF em MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt9` | FLOAT | % alunos 9º EF em MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt9` | FLOAT | % alunos 9º EF em MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt9` | FLOAT | % alunos 9º EF em MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt9` | FLOAT | % alunos 9º EF em MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt9` | FLOAT | % alunos 9º EF em MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt9` | FLOAT | % alunos 9º EF em MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt9` | FLOAT | % alunos 9º EF em MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt9` | FLOAT | % alunos 9º EF em MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp12` | FLOAT | % alunos EM trad. LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp12` | FLOAT | % alunos EM trad. LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp12` | FLOAT | % alunos EM trad. LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp12` | FLOAT | % alunos EM trad. LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp12` | FLOAT | % alunos EM trad. LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp12` | FLOAT | % alunos EM trad. LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp12` | FLOAT | % alunos EM trad. LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp12` | FLOAT | % alunos EM trad. LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp12` | FLOAT | % alunos EM trad. LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt12` | FLOAT | % alunos EM trad. MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt12` | FLOAT | % alunos EM trad. MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt12` | FLOAT | % alunos EM trad. MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt12` | FLOAT | % alunos EM trad. MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt12` | FLOAT | % alunos EM trad. MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt12` | FLOAT | % alunos EM trad. MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt12` | FLOAT | % alunos EM trad. MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt12` | FLOAT | % alunos EM trad. MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt12` | FLOAT | % alunos EM trad. MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt12` | FLOAT | % alunos EM trad. MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt12` | FLOAT | % alunos EM trad. MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp13` | FLOAT | % alunos EM integ. LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp13` | FLOAT | % alunos EM integ. LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp13` | FLOAT | % alunos EM integ. LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp13` | FLOAT | % alunos EM integ. LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp13` | FLOAT | % alunos EM integ. LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp13` | FLOAT | % alunos EM integ. LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp13` | FLOAT | % alunos EM integ. LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp13` | FLOAT | % alunos EM integ. LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp13` | FLOAT | % alunos EM integ. LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt13` | FLOAT | % alunos EM integ. MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt13` | FLOAT | % alunos EM integ. MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt13` | FLOAT | % alunos EM integ. MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt13` | FLOAT | % alunos EM integ. MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt13` | FLOAT | % alunos EM integ. MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt13` | FLOAT | % alunos EM integ. MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt13` | FLOAT | % alunos EM integ. MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt13` | FLOAT | % alunos EM integ. MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt13` | FLOAT | % alunos EM integ. MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt13` | FLOAT | % alunos EM integ. MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt13` | FLOAT | % alunos EM integ. MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_lp14` | FLOAT | % alunos EM LP nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_lp14` | FLOAT | % alunos EM LP nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_lp14` | FLOAT | % alunos EM LP nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_lp14` | FLOAT | % alunos EM LP nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_lp14` | FLOAT | % alunos EM LP nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_lp14` | FLOAT | % alunos EM LP nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_lp14` | FLOAT | % alunos EM LP nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_lp14` | FLOAT | % alunos EM LP nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_lp14` | FLOAT | % alunos EM LP nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_0_mt14` | FLOAT | % alunos EM MT nível 0 de proficiência (Abaixo do básico). SAEB — Planilha de Resultados INEP. |
| `nivel_1_mt14` | FLOAT | % alunos EM MT nível 1 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_2_mt14` | FLOAT | % alunos EM MT nível 2 de proficiência (Básico). SAEB — Planilha de Resultados INEP. |
| `nivel_3_mt14` | FLOAT | % alunos EM MT nível 3 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_4_mt14` | FLOAT | % alunos EM MT nível 4 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_5_mt14` | FLOAT | % alunos EM MT nível 5 de proficiência (Adequado). SAEB — Planilha de Resultados INEP. |
| `nivel_6_mt14` | FLOAT | % alunos EM MT nível 6 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_7_mt14` | FLOAT | % alunos EM MT nível 7 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_8_mt14` | FLOAT | % alunos EM MT nível 8 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_9_mt14` | FLOAT | % alunos EM MT nível 9 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |
| `nivel_10_mt14` | FLOAT | % alunos EM MT nível 10 de proficiência (Avançado). SAEB — Planilha de Resultados INEP. |

## semantic · obt_inep_saeb_micro_escola_ano

File `semantic__obt_inep_saeb_micro_escola_ano.parquet` · 461,283 rows · 23 columns

SAEB microdados contextuais por escola e edicao. Grao: 1 linha por (codigo_escola, ano). id_municipio_saeb preserva o identificador municipal interno do SAEB; codigo_municipio/nome_municipio so sao preenchidos quando o identificador bate com IBGE. UF e regiao sao enriquecidas por ID_UF/obt_ibge_uf. Dependencia administrativa e marcada como Nao disponivel na origem quando os arquivos raw nao trazem a dimensao. Fonte: trusted_zone.inep_saeb_escola. INEP 2013-2023 bienal.

**Built from:** `semantic/obt_ibge_municipio`, `semantic/obt_ibge_uf`, `semantic/obt_inep_censo_escola_ano`, `trusted/inep_saeb_escola`, `trusted/inep_saeb_microdados_escola`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano da edicao do SAEB (bienal: 2011-2023). |
| `codigo_escola` | INTEGER | Identificador SAEB da escola. NAO corresponde ao CO_ENTIDADE do Censo. |
| `nome_escola` | STRING | Nome da escola quando disponivel na origem. |
| `id_municipio_saeb` | INTEGER | Identificador municipal interno do SAEB nos arquivos microdados escola. |
| `codigo_municipio` | INTEGER | Codigo IBGE de 7 digitos do municipio, preenchido apenas quando o identificador da origem bate com IBGE. |
| `nome_municipio` | STRING | Nome do municipio, preenchido apenas quando disponivel na origem ou por join IBGE valido. |
| `codigo_uf` | INTEGER | Codigo IBGE numerico da UF (2 digitos). |
| `nome_uf` | STRING | Nome da UF. |
| `sigla_uf` | STRING | Sigla da UF (2 letras). |
| `codigo_regiao` | INTEGER | Codigo IBGE da regiao geografica. |
| `nome_regiao` | STRING | Nome da regiao geografica. |
| `codigo_dependencia_administrativa` | INTEGER | Codigo da dependencia administrativa quando disponivel na origem. |
| `dependencia_administrativa` | STRING | Dependencia administrativa decodificada; Nao disponivel na origem quando ausente no raw. |
| `codigo_localizacao` | INTEGER | Codigo de localizacao: 1=Urbana, 2=Rural. |
| `localizacao` | STRING | Localizacao decodificada: Urbana, Rural ou Nao informado. |
| `nivel_socio_economico` | STRING | Nivel socioeconomico (INSE) da escola: I a VIII. |
| `media_5ef_lp` | FLOAT | Proficiencia media SAEB 5o ano EF - Lingua Portuguesa. |
| `media_5ef_mt` | FLOAT | Proficiencia media SAEB 5o ano EF - Matematica. |
| `media_9ef_lp` | FLOAT | Proficiencia media SAEB 9o ano EF - Lingua Portuguesa. |
| `media_9ef_mt` | FLOAT | Proficiencia media SAEB 9o ano EF - Matematica. |
| `media_3em_lp` | FLOAT | Proficiencia media SAEB 3o ano EM - Lingua Portuguesa. |
| `media_3em_mt` | FLOAT | Proficiencia media SAEB 3o ano EM - Matematica. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |

## semantic · obt_inep_saeb_micro_municipio_ano

File `semantic__obt_inep_saeb_micro_municipio_ano.parquet` · 65,442 rows · 21 columns

SAEB microdados agregados por municipio SAEB interno, edicao, dependencia administrativa e localizacao. Grao: (id_municipio_saeb/codigo_municipio quando disponivel, ano, dependencia_administrativa, localizacao). Municipio IBGE vem por ponte real com Censo/IBGE. Fonte: trusted_zone.inep_saeb_escola + trusted_zone.inep_saeb_microdados_escola.

**Built from:** `semantic/obt_ibge_municipio`, `semantic/obt_ibge_uf`, `semantic/obt_inep_censo_escola_ano`, `trusted/inep_saeb_escola`, `trusted/inep_saeb_microdados_escola`

| Column | Type | Description |
|---|---|---|
| `id_municipio_saeb` | INTEGER | Código identificador do município atribuído pelo sistema do SAEB. — descrição gerada por IA. |
| `codigo_municipio` | INTEGER | Código IBGE de identificação do município (7 dígitos). — descrição gerada por IA. |
| `nome_municipio` | STRING | Nome do município correspondente aos dados. — descrição gerada por IA. |
| `codigo_uf` | INTEGER | Código IBGE da Unidade da Federação (UF). — descrição gerada por IA. |
| `nome_uf` | STRING | Nome completo da Unidade da Federação (Estado). — descrição gerada por IA. |
| `sigla_uf` | STRING | Sigla de duas letras da Unidade da Federação (UF). — descrição gerada por IA. |
| `codigo_regiao` | INTEGER | Código numérico da região geográfica brasileira. — descrição gerada por IA. |
| `nome_regiao` | STRING | Nome da região geográfica brasileira (ex: Norte, Nordeste). — descrição gerada por IA. |
| `ano` | INTEGER | Ano da edicao do SAEB (bienal: 2011-2023). |
| `codigo_dependencia_administrativa` | INTEGER | Código da dependência administrativa das escolas (ex: 1-Federal, 2-Estadual, 3-Municipal). — descrição gerada por IA. |
| `dependencia_administrativa` | STRING | Descrição da dependência administrativa da rede de ensino (ex: 'Estadual', 'Municipal', 'Não disponível na origem'). — descrição gerada por IA. |
| `codigo_localizacao` | INTEGER | Código da zona/localização geográfica da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `localizacao` | STRING | Descrição da localização da escola ('Urbana' ou 'Rural'). — descrição gerada por IA. |
| `quantidade_escolas_avaliadas` | INTEGER | Quantidade total de escolas avaliadas dentro do grupo de agregação. — descrição gerada por IA. |
| `media_5ef_lp` | FLOAT | Proficiencia media SAEB 5o ano EF - Lingua Portuguesa. |
| `media_5ef_mt` | FLOAT | Proficiencia media SAEB 5o ano EF - Matematica. |
| `media_9ef_lp` | FLOAT | Proficiencia media SAEB 9o ano EF - Lingua Portuguesa. |
| `media_9ef_mt` | FLOAT | Proficiencia media SAEB 9o ano EF - Matematica. |
| `media_3em_lp` | FLOAT | Proficiencia media SAEB 3o ano EM - Lingua Portuguesa. |
| `media_3em_mt` | FLOAT | Proficiencia media SAEB 3o ano EM - Matematica. |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |
