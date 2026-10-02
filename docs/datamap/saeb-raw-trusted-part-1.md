# SAEB assessment (INEP): Raw and Trusted

Dataset: [lucasrangelss/saeb-raw-trusted-part-1](https://www.kaggle.com/datasets/lucasrangelss/saeb-raw-trusted-part-1) · snapshot 2026-10-01 · 40 tables · 61,355,678 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb)

SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

**Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`api_saeb_boletim_raw`](#raw-api-saeb-boletim-raw) | 464,751 | 5 | 5 | source |
| raw | [`inep_saeb_aluno_2013`](#raw-inep-saeb-aluno-2013) | 5,395,142 | 94 | 94 | `inep_saeb_microdados_csv_2013_ts_aluno_3em`, `inep_saeb_microdados_csv_2013_ts_aluno_5ef`, `inep_saeb_microdados_csv_2013_ts_aluno_9ef` |
| raw | [`inep_saeb_aluno_2015`](#raw-inep-saeb-aluno-2015) | 5,031,032 | 94 | 94 | `inep_saeb_microdados_csv_2015_ts_aluno_3em`, `inep_saeb_microdados_csv_2015_ts_aluno_5ef`, `inep_saeb_microdados_csv_2015_ts_aluno_9ef` |
| raw | [`inep_saeb_aluno_2017`](#raw-inep-saeb-aluno-2017) | 8,388,310 | 95 | 95 | `inep_saeb_microdados_csv_2017_ts_aluno_3em_ag`, `inep_saeb_microdados_csv_2017_ts_aluno_3em_esc`, `inep_saeb_microdados_csv_2017_ts_aluno_5ef`, `inep_saeb_microdados_csv_2017_ts_aluno_9ef` |
| raw | [`inep_saeb_aluno_2019`](#raw-inep-saeb-aluno-2019) | 7,074,919 | 143 | 143 | `inep_saeb_microdados_csv_2019_ts_aluno_2ef`, `inep_saeb_microdados_csv_2019_ts_aluno_34em`, `inep_saeb_microdados_csv_2019_ts_aluno_5ef`, `inep_saeb_microdados_csv_2019_ts_aluno_9ef` |
| raw | [`inep_saeb_aluno_2021`](#raw-inep-saeb-aluno-2021) | 7,464,687 | 176 | 176 | `inep_saeb_microdados_csv_2021_ts_aluno_2ef`, `inep_saeb_microdados_csv_2021_ts_aluno_34em`, `inep_saeb_microdados_csv_2021_ts_aluno_5ef`, `inep_saeb_microdados_csv_2021_ts_aluno_9ef` |
| raw | [`inep_saeb_aluno_2023`](#raw-inep-saeb-aluno-2023) | 7,073,491 | 169 | 169 | `inep_saeb_microdados_csv_2023_ts_aluno_2ef`, `inep_saeb_microdados_csv_2023_ts_aluno_34em`, `inep_saeb_microdados_csv_2023_ts_aluno_5ef`, `inep_saeb_microdados_csv_2023_ts_aluno_9ef` |
| raw | [`inep_saeb_arquivos`](#raw-inep-saeb-arquivos) | 64 | 19 | 19 | source |
| raw | [`inep_saeb_arquivos_conteudo`](#raw-inep-saeb-arquivos-conteudo) | 720 | 20 | 20 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_item`](#raw-inep-saeb-microdados-csv-2011-ts-item) | 518 | 8 | 8 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_pesos`](#raw-inep-saeb-microdados-csv-2011-ts-pesos) | 184,518 | 14 | 14 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_quest_diretor`](#raw-inep-saeb-microdados-csv-2011-ts-quest-diretor) | 58,960 | 221 | 221 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_quest_escola`](#raw-inep-saeb-microdados-csv-2011-ts-quest-escola) | 58,960 | 75 | 75 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_quest_professor`](#raw-inep-saeb-microdados-csv-2011-ts-quest-professor) | 316,668 | 163 | 163 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_resultado_brasil`](#raw-inep-saeb-microdados-csv-2011-ts-resultado-brasil) | 162 | 10 | 10 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_resultado_escola`](#raw-inep-saeb-microdados-csv-2011-ts-resultado-escola) | 72,808 | 15 | 15 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_resultado_municipio`](#raw-inep-saeb-microdados-csv-2011-ts-resultado-municipio) | 60,608 | 18 | 18 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_resultado_regiao`](#raw-inep-saeb-microdados-csv-2011-ts-resultado-regiao) | 810 | 11 | 11 | source |
| raw | [`inep_saeb_microdados_csv_2011_ts_resultado_uf`](#raw-inep-saeb-microdados-csv-2011-ts-resultado-uf) | 4,374 | 13 | 13 | source |
| raw | [`inep_saeb_microdados_csv_2013_ts_aluno_3em`](#raw-inep-saeb-microdados-csv-2013-ts-aluno-3em) | 150,429 | 94 | 94 | source |
| raw | [`inep_saeb_microdados_csv_2013_ts_aluno_5ef`](#raw-inep-saeb-microdados-csv-2013-ts-aluno-5ef) | 2,524,125 | 85 | 85 | source |
| raw | [`inep_saeb_microdados_csv_2013_ts_aluno_9ef`](#raw-inep-saeb-microdados-csv-2013-ts-aluno-9ef) | 2,720,588 | 91 | 91 | source |
| raw | [`inep_saeb_microdados_csv_2013_ts_diretor`](#raw-inep-saeb-microdados-csv-2013-ts-diretor) | 56,737 | 118 | 118 | source |
| raw | [`inep_saeb_microdados_csv_2013_ts_escola`](#raw-inep-saeb-microdados-csv-2013-ts-escola) | 59,251 | 127 | 127 | source |
| raw | [`inep_saeb_microdados_csv_2013_ts_item`](#raw-inep-saeb-microdados-csv-2013-ts-item) | 518 | 15 | 15 | source |
| raw | [`inep_saeb_microdados_csv_2013_ts_professor`](#raw-inep-saeb-microdados-csv-2013-ts-professor) | 237,186 | 134 | 134 | source |
| raw | [`inep_saeb_microdados_csv_2015_ts_aluno_3em`](#raw-inep-saeb-microdados-csv-2015-ts-aluno-3em) | 114,225 | 94 | 94 | source |
| raw | [`inep_saeb_microdados_csv_2015_ts_aluno_5ef`](#raw-inep-saeb-microdados-csv-2015-ts-aluno-5ef) | 2,497,431 | 85 | 85 | source |
| raw | [`inep_saeb_microdados_csv_2015_ts_aluno_9ef`](#raw-inep-saeb-microdados-csv-2015-ts-aluno-9ef) | 2,419,376 | 91 | 91 | source |
| raw | [`inep_saeb_microdados_csv_2015_ts_diretor`](#raw-inep-saeb-microdados-csv-2015-ts-diretor) | 55,693 | 118 | 118 | source |
| raw | [`inep_saeb_microdados_csv_2015_ts_escola`](#raw-inep-saeb-microdados-csv-2015-ts-escola) | 57,744 | 128 | 128 | source |
| raw | [`inep_saeb_microdados_csv_2015_ts_item`](#raw-inep-saeb-microdados-csv-2015-ts-item) | 518 | 15 | 15 | source |
| raw | [`inep_saeb_microdados_csv_2015_ts_professor`](#raw-inep-saeb-microdados-csv-2015-ts-professor) | 274,179 | 134 | 134 | source |
| raw | [`inep_saeb_microdados_csv_2017_ts_aluno_3em_ag`](#raw-inep-saeb-microdados-csv-2017-ts-aluno-3em-ag) | 1,966,507 | 95 | 95 | source |
| raw | [`inep_saeb_microdados_csv_2017_ts_aluno_3em_esc`](#raw-inep-saeb-microdados-csv-2017-ts-aluno-3em-esc) | 1,456,325 | 95 | 95 | source |
| raw | [`inep_saeb_microdados_csv_2017_ts_aluno_5ef`](#raw-inep-saeb-microdados-csv-2017-ts-aluno-5ef) | 2,624,019 | 86 | 86 | source |
| raw | [`inep_saeb_microdados_csv_2017_ts_aluno_9ef`](#raw-inep-saeb-microdados-csv-2017-ts-aluno-9ef) | 2,341,459 | 92 | 92 | source |
| raw | [`inep_saeb_microdados_csv_2017_ts_diretor`](#raw-inep-saeb-microdados-csv-2017-ts-diretor) | 73,674 | 118 | 118 | source |
| raw | [`inep_saeb_microdados_csv_2017_ts_escola`](#raw-inep-saeb-microdados-csv-2017-ts-escola) | 73,674 | 154 | 154 | source |
| raw | [`inep_saeb_microdados_csv_2017_ts_item`](#raw-inep-saeb-microdados-csv-2017-ts-item) | 518 | 15 | 15 | source |

## raw · api_saeb_boletim_raw

File `raw__api_saeb_boletim_raw.parquet` · 464,751 rows · 5 columns

Tabela da camada raw (bronze) que armazena os dados brutos de indicadores educacionais e avaliações (como SAEB/IDEB) por escola e ano de referência.

**Feeds:** `trusted/api_saeb_boletim_desempenho`, `trusted/api_saeb_boletim_escola_edicao`

| Column | Type | Description |
|---|---|---|
| `co_entidade` | INTEGER | Código de identificação único da escola (código INEP) no formato numérico/texto. |
| `ano` | INTEGER | Ano de referência dos dados educacionais e avaliações escolares. |
| `json_bruto` | STRING | Payload JSON original contendo os indicadores contextuais, participação e resultados detalhados da escola. |
| `status` | STRING | Estado atual do capítulo, que pode indicar se ele está ativo, inativo, em revisão, etc. |
| `dt_extracao` | STRING | Data e carimbo de data/hora (timestamp ISO 8601 com fuso UTC) em que a extração do dado foi realizada. |

## raw · inep_saeb_aluno_2013

File `raw__inep_saeb_aluno_2013.parquet` · 5,395,142 rows · 94 columns

Microdados de alunos participantes da Prova Brasil e SAEB, contendo informações cadastrais da escola, dados demográficos, respostas dos blocos de provas de Língua Portuguesa e Matemática, proficiências calculadas (TRI e escala SAEB) e respostas ao questionário socioeconômico.

**Built from:** `raw/inep_saeb_microdados_csv_2013_ts_aluno_3em`, `raw/inep_saeb_microdados_csv_2013_ts_aluno_5ef`, `raw/inep_saeb_microdados_csv_2013_ts_aluno_9ef`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de referência da edição da Prova Brasil/SAEB (ex: 2013). |
| `ID_REGIAO` | STRING | Código identificador da região geográfica da escola (1 a 5). |
| `ID_UF` | STRING | Código identificador da Unidade da Federação (UF) da escola. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. |
| `ID_AREA` | STRING | Código de área da escola (1 para Urbana, 2 para Rural). |
| `ID_ESCOLA` | STRING | Código INEP identificador único da escola. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 para Sim, 0 para Não). |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 para Urbana, 2 para Rural). |
| `ID_TURMA` | STRING | Código identificador único da turma do aluno no Censo Escolar. |
| `ID_SERIE` | STRING | Série ou ano escolar avaliado do aluno (ex: 5 para 5º ano, 9 para 9º ano). |
| `ID_ALUNO` | STRING | Código identificador único do aluno gerado pelo INEP. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno no momento do Censo Escolar. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador de preenchimento do caderno de prova pelo aluno (1 para Sim, 0 para Não). |
| `ID_CADERNO` | STRING | Identificador do caderno de prova (versão do teste) respondido pelo aluno. |
| `ID_BLOCO_1` | STRING | Identificador do primeiro bloco de itens da prova do aluno. |
| `ID_BLOCO_2` | STRING | Identificador do segundo bloco de itens da prova do aluno. |
| `TX_RESP_BLOCO_1_LP` | STRING | Vetor de caracteres com as respostas do aluno para o Bloco 1 de Língua Portuguesa. |
| `TX_RESP_BLOCO_2_LP` | STRING | Vetor de caracteres com as respostas do aluno para o Bloco 2 de Língua Portuguesa. |
| `TX_RESP_BLOCO_1_MT` | STRING | Vetor de caracteres com as respostas do aluno para o Bloco 1 de Matemática. |
| `TX_RESP_BLOCO_2_MT` | STRING | Vetor de caracteres com as respostas do aluno para o Bloco 2 de Matemática. |
| `IN_PROFICIENCIA` | STRING | Indicador se o aluno possui proficiência calculada (1 para Sim, 0 para Não). |
| `IN_PROVA_BRASIL` | STRING | Indicador de participação na Prova Brasil (1 para Sim, 0 para Não). |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da ANEB (Avaliação Nacional da Educação Básica). |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para cálculo de proficiência em Língua Portuguesa. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para cálculo de proficiência em Matemática. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência padronizada do aluno em Língua Portuguesa via Teoria de Resposta ao Item (TRI). |
| `DESVIO_PADRAO_LP` | STRING | Desvio padrão da proficiência estimada do aluno em Língua Portuguesa. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota de proficiência do aluno em Língua Portuguesa na escala histórica do SAEB (ex: 0 a 500). |
| `DESVIO_PADRAO_LP_SAEB` | STRING | Desvio padrão da proficiência em Língua Portuguesa na escala histórica do SAEB. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência padronizada do aluno em Matemática via Teoria de Resposta ao Item (TRI). |
| `DESVIO_PADRAO_MT` | STRING | Desvio padrão da proficiência estimada do aluno em Matemática. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota de proficiência do aluno em Matemática na escala histórica do SAEB (ex: 0 a 500). |
| `DESVIO_PADRAO_MT_SAEB` | STRING | Desvio padrão da proficiência em Matemática na escala histórica do SAEB. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico pelo aluno (1 para Sim, 0 para Não). |
| `TX_RESP_Q001` | STRING | Resposta do aluno à questão 1 do questionário socioeconômico. |
| `TX_RESP_Q002` | STRING | Resposta do aluno à questão 2 do questionário socioeconômico. |
| `TX_RESP_Q003` | STRING | Resposta do aluno à questão 3 do questionário socioeconômico. |
| `TX_RESP_Q004` | STRING | Resposta do aluno à questão 4 do questionário socioeconômico. |
| `TX_RESP_Q005` | STRING | Resposta do aluno à questão 5 do questionário socioeconômico. |
| `TX_RESP_Q006` | STRING | Resposta do aluno à questão 6 do questionário socioeconômico. |
| `TX_RESP_Q007` | STRING | Resposta do aluno à questão 7 do questionário socioeconômico. |
| `TX_RESP_Q008` | STRING | Resposta do aluno à questão 8 do questionário socioeconômico. |
| `TX_RESP_Q009` | STRING | Resposta do aluno à questão 9 do questionário socioeconômico. |
| `TX_RESP_Q010` | STRING | Resposta do aluno à questão 10 do questionário socioeconômico. |
| `TX_RESP_Q011` | STRING | Resposta do aluno à questão 11 do questionário socioeconômico. |
| `TX_RESP_Q012` | STRING | Resposta do aluno à questão 12 do questionário socioeconômico. |
| `TX_RESP_Q013` | STRING | Resposta do aluno à questão 13 do questionário socioeconômico. |
| `TX_RESP_Q014` | STRING | Resposta do aluno à questão 14 do questionário socioeconômico. |
| `TX_RESP_Q015` | STRING | Resposta do aluno à questão 15 do questionário socioeconômico. |
| `TX_RESP_Q016` | STRING | Resposta do aluno à questão 16 do questionário socioeconômico. |
| `TX_RESP_Q017` | STRING | Resposta do aluno à questão 17 do questionário socioeconômico. |
| `TX_RESP_Q018` | STRING | Resposta do aluno à questão 18 do questionário socioeconômico. |
| `TX_RESP_Q019` | STRING | Resposta do aluno à questão 19 do questionário socioeconômico. |
| `TX_RESP_Q020` | STRING | Resposta do aluno à questão 20 do questionário socioeconômico. |
| `TX_RESP_Q021` | STRING | Resposta do aluno à questão 21 do questionário socioeconômico. |
| `TX_RESP_Q022` | STRING | Resposta do aluno à questão 22 do questionário socioeconômico. |
| `TX_RESP_Q023` | STRING | Resposta do aluno à questão 23 do questionário socioeconômico. |
| `TX_RESP_Q024` | STRING | Resposta do aluno à questão 24 do questionário socioeconômico. |
| `TX_RESP_Q025` | STRING | Resposta do aluno à questão 25 do questionário socioeconômico. |
| `TX_RESP_Q026` | STRING | Resposta do aluno à questão 26 do questionário socioeconômico. |
| `TX_RESP_Q027` | STRING | Resposta do aluno à questão 27 do questionário socioeconômico. |
| `TX_RESP_Q028` | STRING | Resposta do aluno à questão 28 do questionário socioeconômico. |
| `TX_RESP_Q029` | STRING | Resposta do aluno à questão 29 do questionário socioeconômico. |
| `TX_RESP_Q030` | STRING | Resposta do aluno à questão 30 do questionário socioeconômico. |
| `TX_RESP_Q031` | STRING | Resposta do aluno à questão 31 do questionário socioeconômico. |
| `TX_RESP_Q032` | STRING | Resposta do aluno à questão 32 do questionário socioeconômico. |
| `TX_RESP_Q033` | STRING | Resposta do aluno à questão 33 do questionário socioeconômico. |
| `TX_RESP_Q034` | STRING | Resposta do aluno à questão 34 do questionário socioeconômico. |
| `TX_RESP_Q035` | STRING | Resposta do aluno à questão 35 do questionário socioeconômico. |
| `TX_RESP_Q036` | STRING | Resposta do aluno à questão 36 do questionário socioeconômico. |
| `TX_RESP_Q037` | STRING | Resposta do aluno à questão 37 do questionário socioeconômico. |
| `TX_RESP_Q038` | STRING | Resposta do aluno à questão 38 do questionário socioeconômico. |
| `TX_RESP_Q039` | STRING | Resposta do aluno à questão 39 do questionário socioeconômico. |
| `TX_RESP_Q040` | STRING | Resposta do aluno à questão 40 do questionário socioeconômico. |
| `TX_RESP_Q041` | STRING | Resposta do aluno à questão 41 do questionário socioeconômico. |
| `TX_RESP_Q042` | STRING | Resposta do aluno à questão 42 do questionário socioeconômico. |
| `TX_RESP_Q043` | STRING | Resposta do aluno à questão 43 do questionário socioeconômico. |
| `TX_RESP_Q044` | STRING | Resposta do aluno à questão 44 do questionário socioeconômico. |
| `TX_RESP_Q045` | STRING | Resposta do aluno à questão 45 do questionário socioeconômico. |
| `TX_RESP_Q046` | STRING | Resposta do aluno à questão 46 do questionário socioeconômico. |
| `TX_RESP_Q047` | STRING | Resposta do aluno à questão 47 do questionário socioeconômico. |
| `TX_RESP_Q048` | STRING | Resposta do aluno à questão 48 do questionário socioeconômico. |
| `TX_RESP_Q049` | STRING | Resposta do aluno à questão 49 do questionário socioeconômico. |
| `TX_RESP_Q050` | STRING | Resposta do aluno à questão 50 do questionário socioeconômico. |
| `TX_RESP_Q051` | STRING | Resposta do aluno à questão 51 do questionário socioeconômico. |
| `TX_RESP_Q052` | STRING | Resposta do aluno à questão 52 do questionário socioeconômico. |
| `TX_RESP_Q053` | STRING | Resposta do aluno à questão 53 do questionário socioeconômico. |
| `TX_RESP_Q054` | STRING | Resposta do aluno à questão 54 do questionário socioeconômico. |
| `TX_RESP_Q055` | STRING | Resposta do aluno à questão 55 do questionário socioeconômico. |
| `TX_RESP_Q056` | STRING | Resposta do aluno à questão 56 do questionário socioeconômico. |
| `TX_RESP_Q057` | STRING | Resposta do aluno à questão 57 do questionário socioeconômico. |
| `TX_RESP_Q058` | STRING | Resposta do aluno à questão 58 do questionário socioeconômico. |
| `TX_RESP_Q059` | STRING | Resposta do aluno à questão 59 do questionário socioeconômico. |
| `TX_RESP_Q060` | STRING | Resposta do aluno à questão 60 do questionário socioeconômico. |

## raw · inep_saeb_aluno_2015

File `raw__inep_saeb_aluno_2015.parquet` · 5,031,032 rows · 94 columns

Tabela de microdados dos alunos participantes da Prova Brasil / SAEB, contendo informações cadastrais da escola, dados de identificação do estudante, respostas aos blocos de provas de Língua Portuguesa e Matemática, proficiências calculadas e respostas ao questionário socioeconômico.

**Built from:** `raw/inep_saeb_microdados_csv_2015_ts_aluno_3em`, `raw/inep_saeb_microdados_csv_2015_ts_aluno_5ef`, `raw/inep_saeb_microdados_csv_2015_ts_aluno_9ef`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de referência da edição da Prova Brasil/SAEB. |
| `ID_REGIAO` | STRING | Código identificador da região geográfica da escola. |
| `ID_UF` | STRING | Código identificador da Unidade da Federação (IBGE) da escola. |
| `ID_MUNICIPIO` | STRING | Código identificador do município (IBGE) da escola. |
| `ID_AREA` | STRING | Código da área de localização da escola (1 para Urbana, 2 para Rural). |
| `ID_ESCOLA` | STRING | Código identificador único da escola no Censo Escolar/INEP. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 para Sim, 0 para Não). |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (Urbana ou Rural). |
| `ID_TURMA` | STRING | Código identificador único da turma do aluno. |
| `ID_SERIE` | STRING | Série ou ano escolar avaliado do aluno (ex: 5 para 5º ano, 9 para 9º ano). |
| `ID_ALUNO` | STRING | Código identificador único do aluno gerado pelo INEP. |
| `IN_SITUACAO_CENSO` | STRING | Indicador da situação de matrícula do aluno no Censo Escolar. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador de preenchimento da prova pelo aluno (1 para preenchida, 0 para em branco). |
| `ID_CADERNO` | STRING | Identificador do caderno de prova (formato do teste) aplicado ao aluno. |
| `ID_BLOCO_1` | STRING | Identificador do primeiro bloco de itens da prova do aluno. |
| `ID_BLOCO_2` | STRING | Identificador do segundo bloco de itens da prova do aluno. |
| `TX_RESP_BLOCO_1_LP` | STRING | Vetor com as respostas do aluno para os itens do Bloco 1 de Língua Portuguesa. |
| `TX_RESP_BLOCO_2_LP` | STRING | Vetor com as respostas do aluno para os itens do Bloco 2 de Língua Portuguesa. |
| `TX_RESP_BLOCO_1_MT` | STRING | Vetor com as respostas do aluno para os itens do Bloco 1 de Matemática. |
| `TX_RESP_BLOCO_2_MT` | STRING | Vetor com as respostas do aluno para os itens do Bloco 2 de Matemática. |
| `IN_PROFICIENCIA` | STRING | Indicador de presença de cálculo de proficiência para o aluno (1 para Sim, 0 para Não). |
| `IN_PROVA_BRASIL` | STRING | Indicador se o aluno pertence ao escopo de divulgação da Prova Brasil. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral do aluno na ANEB. |
| `PESO_ALUNO_LP` | STRING | Peso estatístico do aluno para cálculo de proficiência em Língua Portuguesa. |
| `PESO_ALUNO_MT` | STRING | Peso estatístico do aluno para cálculo de proficiência em Matemática. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência padronizada do aluno em Língua Portuguesa. |
| `DESVIO_PADRAO_LP` | STRING | Desvio padrão da proficiência calculada do aluno em Língua Portuguesa. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota de proficiência do aluno em Língua Portuguesa na escala histórica do SAEB. |
| `DESVIO_PADRAO_LP_SAEB` | STRING | Desvio padrão da proficiência em Língua Portuguesa na escala histórica do SAEB. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência padronizada do aluno em Matemática. |
| `DESVIO_PADRAO_MT` | STRING | Desvio padrão da proficiência calculada do aluno em Matemática. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota de proficiência do aluno em Matemática na escala histórica do SAEB. |
| `DESVIO_PADRAO_MT_SAEB` | STRING | Desvio padrão da proficiência em Matemática na escala histórica do SAEB. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico pelo aluno (1 para Sim, 0 para Não). |
| `TX_RESP_Q001` | STRING | Resposta do aluno à questão 1 do questionário socioeconômico. |
| `TX_RESP_Q002` | STRING | Resposta do aluno à questão 2 do questionário socioeconômico. |
| `TX_RESP_Q003` | STRING | Resposta do aluno à questão 3 do questionário socioeconômico. |
| `TX_RESP_Q004` | STRING | Resposta do aluno à questão 4 do questionário socioeconômico. |
| `TX_RESP_Q005` | STRING | Resposta do aluno à questão 5 do questionário socioeconômico. |
| `TX_RESP_Q006` | STRING | Resposta do aluno à questão 6 do questionário socioeconômico. |
| `TX_RESP_Q007` | STRING | Resposta do aluno à questão 7 do questionário socioeconômico. |
| `TX_RESP_Q008` | STRING | Resposta do aluno à questão 8 do questionário socioeconômico. |
| `TX_RESP_Q009` | STRING | Resposta do aluno à questão 9 do questionário socioeconômico. |
| `TX_RESP_Q010` | STRING | Resposta do aluno à questão 10 do questionário socioeconômico. |
| `TX_RESP_Q011` | STRING | Resposta do aluno à questão 11 do questionário socioeconômico. |
| `TX_RESP_Q012` | STRING | Resposta do aluno à questão 12 do questionário socioeconômico. |
| `TX_RESP_Q013` | STRING | Resposta do aluno à questão 13 do questionário socioeconômico. |
| `TX_RESP_Q014` | STRING | Resposta do aluno à questão 14 do questionário socioeconômico. |
| `TX_RESP_Q015` | STRING | Resposta do aluno à questão 15 do questionário socioeconômico. |
| `TX_RESP_Q016` | STRING | Resposta do aluno à questão 16 do questionário socioeconômico. |
| `TX_RESP_Q017` | STRING | Resposta do aluno à questão 17 do questionário socioeconômico. |
| `TX_RESP_Q018` | STRING | Resposta do aluno à questão 18 do questionário socioeconômico. |
| `TX_RESP_Q019` | STRING | Resposta do aluno à questão 19 do questionário socioeconômico. |
| `TX_RESP_Q020` | STRING | Resposta do aluno à questão 20 do questionário socioeconômico. |
| `TX_RESP_Q021` | STRING | Resposta do aluno à questão 21 do questionário socioeconômico. |
| `TX_RESP_Q022` | STRING | Resposta do aluno à questão 22 do questionário socioeconômico. |
| `TX_RESP_Q023` | STRING | Resposta do aluno à questão 23 do questionário socioeconômico. |
| `TX_RESP_Q024` | STRING | Resposta do aluno à questão 24 do questionário socioeconômico. |
| `TX_RESP_Q025` | STRING | Resposta do aluno à questão 25 do questionário socioeconômico. |
| `TX_RESP_Q026` | STRING | Resposta do aluno à questão 26 do questionário socioeconômico. |
| `TX_RESP_Q027` | STRING | Resposta do aluno à questão 27 do questionário socioeconômico. |
| `TX_RESP_Q028` | STRING | Resposta do aluno à questão 28 do questionário socioeconômico. |
| `TX_RESP_Q029` | STRING | Resposta do aluno à questão 29 do questionário socioeconômico. |
| `TX_RESP_Q030` | STRING | Resposta do aluno à questão 30 do questionário socioeconômico. |
| `TX_RESP_Q031` | STRING | Resposta do aluno à questão 31 do questionário socioeconômico. |
| `TX_RESP_Q032` | STRING | Resposta do aluno à questão 32 do questionário socioeconômico. |
| `TX_RESP_Q033` | STRING | Resposta do aluno à questão 33 do questionário socioeconômico. |
| `TX_RESP_Q034` | STRING | Resposta do aluno à questão 34 do questionário socioeconômico. |
| `TX_RESP_Q035` | STRING | Resposta do aluno à questão 35 do questionário socioeconômico. |
| `TX_RESP_Q036` | STRING | Resposta do aluno à questão 36 do questionário socioeconômico. |
| `TX_RESP_Q037` | STRING | Resposta do aluno à questão 37 do questionário socioeconômico. |
| `TX_RESP_Q038` | STRING | Resposta do aluno à questão 38 do questionário socioeconômico. |
| `TX_RESP_Q039` | STRING | Resposta do aluno à questão 39 do questionário socioeconômico. |
| `TX_RESP_Q040` | STRING | Resposta do aluno à questão 40 do questionário socioeconômico. |
| `TX_RESP_Q041` | STRING | Resposta do aluno à questão 41 do questionário socioeconômico. |
| `TX_RESP_Q042` | STRING | Resposta do aluno à questão 42 do questionário socioeconômico. |
| `TX_RESP_Q043` | STRING | Resposta do aluno à questão 43 do questionário socioeconômico. |
| `TX_RESP_Q044` | STRING | Resposta do aluno à questão 44 do questionário socioeconômico. |
| `TX_RESP_Q045` | STRING | Resposta do aluno à questão 45 do questionário socioeconômico. |
| `TX_RESP_Q046` | STRING | Resposta do aluno à questão 46 do questionário socioeconômico. |
| `TX_RESP_Q047` | STRING | Resposta do aluno à questão 47 do questionário socioeconômico. |
| `TX_RESP_Q048` | STRING | Resposta do aluno à questão 48 do questionário socioeconômico. |
| `TX_RESP_Q049` | STRING | Resposta do aluno à questão 49 do questionário socioeconômico. |
| `TX_RESP_Q050` | STRING | Resposta do aluno à questão 50 do questionário socioeconômico. |
| `TX_RESP_Q051` | STRING | Resposta do aluno à questão 51 do questionário socioeconômico. |
| `TX_RESP_Q052` | STRING | Resposta do aluno à questão 52 do questionário socioeconômico. |
| `TX_RESP_Q053` | STRING | Resposta do aluno à questão 53 do questionário socioeconômico. |
| `TX_RESP_Q054` | STRING | Resposta do aluno à questão 54 do questionário socioeconômico. |
| `TX_RESP_Q055` | STRING | Resposta do aluno à questão 55 do questionário socioeconômico. |
| `TX_RESP_Q056` | STRING | Resposta do aluno à questão 56 do questionário socioeconômico. |
| `TX_RESP_Q057` | STRING | Resposta do aluno à questão 57 do questionário socioeconômico. |
| `TX_RESP_Q058` | STRING | Resposta do aluno à questão 58 do questionário socioeconômico. |
| `TX_RESP_Q059` | STRING | Resposta do aluno à questão 59 do questionário socioeconômico. |
| `TX_RESP_Q060` | STRING | Resposta do aluno à questão 60 do questionário socioeconômico. |

## raw · inep_saeb_aluno_2017

File `raw__inep_saeb_aluno_2017.parquet` · 8,388,310 rows · 95 columns

Microdados dos alunos participantes do SAEB/Prova Brasil, contendo informações cadastrais, proficiências em Língua Portuguesa e Matemática, respostas dos cadernos de prova e respostas ao questionário socioeconômico.

**Built from:** `raw/inep_saeb_microdados_csv_2017_ts_aluno_3em_ag`, `raw/inep_saeb_microdados_csv_2017_ts_aluno_3em_esc`, `raw/inep_saeb_microdados_csv_2017_ts_aluno_5ef`, `raw/inep_saeb_microdados_csv_2017_ts_aluno_9ef`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de referência da edição do SAEB/Prova Brasil. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). |
| `ID_UF` | STRING | Código IBGE do estado (Unidade da Federação) da escola. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. |
| `ID_AREA` | STRING | Código da área de localização da escola (1: Capital, 2: Interior). |
| `ID_ESCOLA` | STRING | Código único de identificação da escola no Censo Escolar (INEP). |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1: Sim, 0: Não/Privada). |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1: Urbana, 2: Rural). |
| `ID_TURMA` | STRING | Código identificador único da turma do aluno. |
| `ID_SERIE` | STRING | Código da série/ano escolar avaliado (ex: 5 para 5º ano EF, 9 para 9º ano EF, 12 para 3º ano EM). |
| `ID_ALUNO` | STRING | Código identificador único do aluno gerado pelo INEP. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação do aluno no Censo Escolar (ex: 1: Regularmente matriculado). |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador de preenchimento do caderno de prova pelo aluno. |
| `IN_PRESENCA_PROVA` | STRING | Indicador de presença do aluno no dia da aplicação da prova (1: Presente, 0: Ausente). |
| `ID_CADERNO` | STRING | Identificador do caderno de prova (combinação de itens) respondido pelo aluno. |
| `ID_BLOCO_1` | STRING | Identificador do primeiro bloco de itens do caderno de prova. |
| `ID_BLOCO_2` | STRING | Identificador do segundo bloco de itens do caderno de prova. |
| `TX_RESP_BLOCO_1_LP` | STRING | String contendo as respostas do aluno para os itens do Bloco 1 de Língua Portuguesa. |
| `TX_RESP_BLOCO_2_LP` | STRING | String contendo as respostas do aluno para os itens do Bloco 2 de Língua Portuguesa. |
| `TX_RESP_BLOCO_1_MT` | STRING | String contendo as respostas do aluno para os itens do Bloco 1 de Matemática. |
| `TX_RESP_BLOCO_2_MT` | STRING | String contendo as respostas do aluno para os itens do Bloco 2 de Matemática. |
| `IN_PROFICIENCIA` | STRING | Indicador se o aluno possui proficiência calculada (1: Sim, 0: Não). |
| `IN_PROVA_BRASIL` | STRING | Indicador se o aluno faz parte da amostra da Prova Brasil. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da Avaliação Nacional da Educação Básica (ANEB). |
| `PESO_ALUNO_LP` | STRING | Fator de expansão (peso amostral) do aluno para Língua Portuguesa. |
| `PESO_ALUNO_MT` | STRING | Fator de expansão (peso amostral) do aluno para Matemática. |
| `PROFICIENCIA_LP` | STRING | Proficiência estimada do aluno em Língua Portuguesa na escala padronizada (Teoria de Resposta ao Item). |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da estimativa de proficiência em Língua Portuguesa na escala padronizada. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência do aluno em Língua Portuguesa convertida para a escala histórica do SAEB (ex: 0 a 500). |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência em Língua Portuguesa na escala histórica do SAEB. |
| `PROFICIENCIA_MT` | STRING | Proficiência estimada do aluno em Matemática na escala padronizada (Teoria de Resposta ao Item). |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da estimativa de proficiência em Matemática na escala padronizada. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência do aluno em Matemática convertida para a escala histórica do SAEB (ex: 0 a 500). |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência em Matemática na escala histórica do SAEB. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico pelo aluno (1: Sim, 0: Não). |
| `TX_RESP_Q001` | STRING | Resposta do aluno à questão 1 do questionário socioeconômico. |
| `TX_RESP_Q002` | STRING | Resposta do aluno à questão 2 do questionário socioeconômico. |
| `TX_RESP_Q003` | STRING | Resposta do aluno à questão 3 do questionário socioeconômico. |
| `TX_RESP_Q004` | STRING | Resposta do aluno à questão 4 do questionário socioeconômico. |
| `TX_RESP_Q005` | STRING | Resposta do aluno à questão 5 do questionário socioeconômico. |
| `TX_RESP_Q006` | STRING | Resposta do aluno à questão 6 do questionário socioeconômico. |
| `TX_RESP_Q007` | STRING | Resposta do aluno à questão 7 do questionário socioeconômico. |
| `TX_RESP_Q008` | STRING | Resposta do aluno à questão 8 do questionário socioeconômico. |
| `TX_RESP_Q009` | STRING | Resposta do aluno à questão 9 do questionário socioeconômico. |
| `TX_RESP_Q010` | STRING | Resposta do aluno à questão 10 do questionário socioeconômico. |
| `TX_RESP_Q011` | STRING | Resposta do aluno à questão 11 do questionário socioeconômico. |
| `TX_RESP_Q012` | STRING | Resposta do aluno à questão 12 do questionário socioeconômico. |
| `TX_RESP_Q013` | STRING | Resposta do aluno à questão 13 do questionário socioeconômico. |
| `TX_RESP_Q014` | STRING | Resposta do aluno à questão 14 do questionário socioeconômico. |
| `TX_RESP_Q015` | STRING | Resposta do aluno à questão 15 do questionário socioeconômico. |
| `TX_RESP_Q016` | STRING | Resposta do aluno à questão 16 do questionário socioeconômico. |
| `TX_RESP_Q017` | STRING | Resposta do aluno à questão 17 do questionário socioeconômico. |
| `TX_RESP_Q018` | STRING | Resposta do aluno à questão 18 do questionário socioeconômico. |
| `TX_RESP_Q019` | STRING | Resposta do aluno à questão 19 do questionário socioeconômico. |
| `TX_RESP_Q020` | STRING | Resposta do aluno à questão 20 do questionário socioeconômico. |
| `TX_RESP_Q021` | STRING | Resposta do aluno à questão 21 do questionário socioeconômico. |
| `TX_RESP_Q022` | STRING | Resposta do aluno à questão 22 do questionário socioeconômico. |
| `TX_RESP_Q023` | STRING | Resposta do aluno à questão 23 do questionário socioeconômico. |
| `TX_RESP_Q024` | STRING | Resposta do aluno à questão 24 do questionário socioeconômico. |
| `TX_RESP_Q025` | STRING | Resposta do aluno à questão 25 do questionário socioeconômico. |
| `TX_RESP_Q026` | STRING | Resposta do aluno à questão 26 do questionário socioeconômico. |
| `TX_RESP_Q027` | STRING | Resposta do aluno à questão 27 do questionário socioeconômico. |
| `TX_RESP_Q028` | STRING | Resposta do aluno à questão 28 do questionário socioeconômico. |
| `TX_RESP_Q029` | STRING | Resposta do aluno à questão 29 do questionário socioeconômico. |
| `TX_RESP_Q030` | STRING | Resposta do aluno à questão 30 do questionário socioeconômico. |
| `TX_RESP_Q031` | STRING | Resposta do aluno à questão 31 do questionário socioeconômico. |
| `TX_RESP_Q032` | STRING | Resposta do aluno à questão 32 do questionário socioeconômico. |
| `TX_RESP_Q033` | STRING | Resposta do aluno à questão 33 do questionário socioeconômico. |
| `TX_RESP_Q034` | STRING | Resposta do aluno à questão 34 do questionário socioeconômico. |
| `TX_RESP_Q035` | STRING | Resposta do aluno à questão 35 do questionário socioeconômico. |
| `TX_RESP_Q036` | STRING | Resposta do aluno à questão 36 do questionário socioeconômico. |
| `TX_RESP_Q037` | STRING | Resposta do aluno à questão 37 do questionário socioeconômico. |
| `TX_RESP_Q038` | STRING | Resposta do aluno à questão 38 do questionário socioeconômico. |
| `TX_RESP_Q039` | STRING | Resposta do aluno à questão 39 do questionário socioeconômico. |
| `TX_RESP_Q040` | STRING | Resposta do aluno à questão 40 do questionário socioeconômico. |
| `TX_RESP_Q041` | STRING | Resposta do aluno à questão 41 do questionário socioeconômico. |
| `TX_RESP_Q042` | STRING | Resposta do aluno à questão 42 do questionário socioeconômico. |
| `TX_RESP_Q043` | STRING | Resposta do aluno à questão 43 do questionário socioeconômico. |
| `TX_RESP_Q044` | STRING | Resposta do aluno à questão 44 do questionário socioeconômico. |
| `TX_RESP_Q045` | STRING | Resposta do aluno à questão 45 do questionário socioeconômico. |
| `TX_RESP_Q046` | STRING | Resposta do aluno à questão 46 do questionário socioeconômico. |
| `TX_RESP_Q047` | STRING | Resposta do aluno à questão 47 do questionário socioeconômico. |
| `TX_RESP_Q048` | STRING | Resposta do aluno à questão 48 do questionário socioeconômico. |
| `TX_RESP_Q049` | STRING | Resposta do aluno à questão 49 do questionário socioeconômico. |
| `TX_RESP_Q050` | STRING | Resposta do aluno à questão 50 do questionário socioeconômico. |
| `TX_RESP_Q051` | STRING | Resposta do aluno à questão 51 do questionário socioeconômico. |
| `TX_RESP_Q052` | STRING | Resposta do aluno à questão 52 do questionário socioeconômico. |
| `TX_RESP_Q053` | STRING | Resposta do aluno à questão 53 do questionário socioeconômico. |
| `TX_RESP_Q054` | STRING | Resposta do aluno à questão 54 do questionário socioeconômico. |
| `TX_RESP_Q055` | STRING | Resposta do aluno à questão 55 do questionário socioeconômico. |
| `TX_RESP_Q056` | STRING | Resposta do aluno à questão 56 do questionário socioeconômico. |
| `TX_RESP_Q057` | STRING | Resposta do aluno à questão 57 do questionário socioeconômico. |
| `TX_RESP_Q058` | STRING | Resposta do aluno à questão 58 do questionário socioeconômico. |
| `TX_RESP_Q059` | STRING | Resposta do aluno à questão 59 do questionário socioeconômico. |
| `TX_RESP_Q060` | STRING | Resposta do aluno à questão 60 do questionário socioeconômico. |

## raw · inep_saeb_aluno_2019

File `raw__inep_saeb_aluno_2019.parquet` · 7,074,919 rows · 143 columns

Microdados dos alunos participantes do SAEB (Sistema de Avaliação da Educação Básica), contendo dados demográficos, respostas aos testes cognitivos, proficiências calculadas e respostas ao questionário socioeconômico.

**Built from:** `raw/inep_saeb_microdados_csv_2019_ts_aluno_2ef`, `raw/inep_saeb_microdados_csv_2019_ts_aluno_34em`, `raw/inep_saeb_microdados_csv_2019_ts_aluno_5ef`, `raw/inep_saeb_microdados_csv_2019_ts_aluno_9ef`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de referência da edição do SAEB (ex: 2019). |
| `ID_REGIAO` | STRING | Código identificador da região geográfica do aluno. |
| `ID_UF` | STRING | Código identificador da Unidade da Federação (UF). |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde se localiza a escola. |
| `ID_AREA` | STRING | Código da área da escola (1 - Capital, 2 - Interior). |
| `ID_ESCOLA` | STRING | Código INEP identificador único da escola. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 - Sim, 0 - Não). |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 - Urbana, 2 - Rural). |
| `ID_TURMA` | STRING | Código identificador único da turma do aluno. |
| `ID_SERIE` | STRING | Código identificador da série/ano escolar avaliado. |
| `ID_ALUNO` | STRING | Código identificador único do aluno no SAEB. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno no Censo Escolar. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento da prova de Língua Portuguesa. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento da prova de Matemática. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença na prova de Língua Portuguesa (1 - Presente, 0 - Ausente). |
| `IN_PRESENCA_MT` | STRING | Indicador de presença na prova de Matemática (1 - Presente, 0 - Ausente). |
| `ID_CADERNO_LP` | STRING | Identificador do caderno de prova de Língua Portuguesa aplicado ao aluno. |
| `ID_BLOCO_1_LP` | STRING | Identificador do primeiro bloco de itens de Língua Portuguesa. |
| `ID_BLOCO_2_LP` | STRING | Identificador do segundo bloco de itens de Língua Portuguesa. |
| `ID_CADERNO_MT` | STRING | Identificador do caderno de prova de Matemática aplicado ao aluno. |
| `ID_BLOCO_1_MT` | STRING | Identificador do primeiro bloco de itens de Matemática. |
| `ID_BLOCO_2_MT` | STRING | Identificador do segundo bloco de itens de Matemática. |
| `TX_RESP_BLOCO1_LP` | STRING | Vetor de respostas do aluno para as questões do bloco 1 de Língua Portuguesa. |
| `TX_RESP_BLOCO2_LP` | STRING | Vetor de respostas do aluno para as questões do bloco 2 de Língua Portuguesa. |
| `TX_RESP_BLOCO1_MT` | STRING | Vetor de respostas do aluno para as questões do bloco 1 de Matemática. |
| `TX_RESP_BLOCO2_MT` | STRING | Vetor de respostas do aluno para as questões do bloco 2 de Matemática. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador de cálculo de proficiência em Língua Portuguesa (1 - Sim, 0 - Não). |
| `IN_PROFICIENCIA_MT` | STRING | Indicador de cálculo de proficiência em Matemática (1 - Sim, 0 - Não). |
| `IN_AMOSTRA` | STRING | Indicador se o aluno faz parte da amostra estatística do SAEB (1 - Sim, 0 - Não). |
| `ESTRATO` | STRING | Código do estrato de amostragem populacional do aluno. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para cálculo de proficiência em Língua Portuguesa. |
| `PROFICIENCIA_LP` | STRING | Proficiência padronizada do aluno em Língua Portuguesa. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da proficiência padronizada em Língua Portuguesa. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência do aluno em Língua Portuguesa na escala SAEB (ex: 0 a 500). |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência em Língua Portuguesa na escala SAEB. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para cálculo de proficiência em Matemática. |
| `PROFICIENCIA_MT` | STRING | Proficiência padronizada do aluno em Matemática. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da proficiência padronizada em Matemática. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência do aluno em Matemática na escala SAEB (ex: 0 a 500). |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência em Matemática na escala SAEB. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico do estudante. |
| `TX_RESP_Q001` | STRING | Resposta do aluno à questão socioeconômica Q001 (ex: escolaridade da mãe). |
| `TX_RESP_Q002` | STRING | Resposta do aluno à questão socioeconômica Q002 (ex: escolaridade do pai). |
| `TX_RESP_Q003A` | STRING | Resposta do aluno à questão socioeconômica Q003A. |
| `TX_RESP_Q003B` | STRING | Resposta do aluno à questão socioeconômica Q003B. |
| `TX_RESP_Q003C` | STRING | Resposta do aluno à questão socioeconômica Q003C. |
| `TX_RESP_Q003D` | STRING | Resposta do aluno à questão socioeconômica Q003D. |
| `TX_RESP_Q003E` | STRING | Resposta do aluno à questão socioeconômica Q003E. |
| `TX_RESP_Q004` | STRING | Resposta do aluno à questão socioeconômica Q004. |
| `TX_RESP_Q005` | STRING | Resposta do aluno à questão socioeconômica Q005. |
| `TX_RESP_Q006A` | STRING | Resposta do aluno à questão socioeconômica Q006A. |
| `TX_RESP_Q006B` | STRING | Resposta do aluno à questão socioeconômica Q006B. |
| `TX_RESP_Q006C` | STRING | Resposta do aluno à questão socioeconômica Q006C. |
| `TX_RESP_Q006D` | STRING | Resposta do aluno à questão socioeconômica Q006D. |
| `TX_RESP_Q006E` | STRING | Resposta do aluno à questão socioeconômica Q006E. |
| `TX_RESP_Q007` | STRING | Resposta do aluno à questão socioeconômica Q007. |
| `TX_RESP_Q008A` | STRING | Resposta do aluno à questão socioeconômica Q008A. |
| `TX_RESP_Q008B` | STRING | Resposta do aluno à questão socioeconômica Q008B. |
| `TX_RESP_Q008C` | STRING | Resposta do aluno à questão socioeconômica Q008C. |
| `TX_RESP_Q009A` | STRING | Resposta do aluno à questão socioeconômica Q009A. |
| `TX_RESP_Q009B` | STRING | Resposta do aluno à questão socioeconômica Q009B. |
| `TX_RESP_Q009C` | STRING | Resposta do aluno à questão socioeconômica Q009C. |
| `TX_RESP_Q009D` | STRING | Resposta do aluno à questão socioeconômica Q009D. |
| `TX_RESP_Q009E` | STRING | Resposta do aluno à questão socioeconômica Q009E. |
| `TX_RESP_Q009F` | STRING | Resposta do aluno à questão socioeconômica Q009F. |
| `TX_RESP_Q009G` | STRING | Resposta do aluno à questão socioeconômica Q009G. |
| `TX_RESP_Q010A` | STRING | Resposta do aluno à questão socioeconômica Q010A. |
| `TX_RESP_Q010B` | STRING | Resposta do aluno à questão socioeconômica Q010B. |
| `TX_RESP_Q010C` | STRING | Resposta do aluno à questão socioeconômica Q010C. |
| `TX_RESP_Q010D` | STRING | Resposta do aluno à questão socioeconômica Q010D. |
| `TX_RESP_Q010E` | STRING | Resposta do aluno à questão socioeconômica Q010E. |
| `TX_RESP_Q010F` | STRING | Resposta do aluno à questão socioeconômica Q010F. |
| `TX_RESP_Q010G` | STRING | Resposta do aluno à questão socioeconômica Q010G. |
| `TX_RESP_Q010H` | STRING | Resposta do aluno à questão socioeconômica Q010H. |
| `TX_RESP_Q010I` | STRING | Resposta do aluno à questão socioeconômica Q010I. |
| `TX_RESP_Q011` | STRING | Resposta do aluno à questão socioeconômica Q011. |
| `TX_RESP_Q012` | STRING | Resposta do aluno à questão socioeconômica Q012. |
| `TX_RESP_Q013` | STRING | Resposta do aluno à questão socioeconômica Q013. |
| `TX_RESP_Q014` | STRING | Resposta do aluno à questão socioeconômica Q014. |
| `TX_RESP_Q015` | STRING | Resposta do aluno à questão socioeconômica Q015. |
| `TX_RESP_Q016` | STRING | Resposta do aluno à questão socioeconômica Q016. |
| `TX_RESP_Q017A` | STRING | Resposta do aluno à questão socioeconômica Q017A. |
| `TX_RESP_Q017B` | STRING | Resposta do aluno à questão socioeconômica Q017B. |
| `TX_RESP_Q017C` | STRING | Resposta do aluno à questão socioeconômica Q017C. |
| `TX_RESP_Q017D` | STRING | Resposta do aluno à questão socioeconômica Q017D. |
| `TX_RESP_Q017E` | STRING | Resposta do aluno à questão socioeconômica Q017E. |
| `TX_RESP_Q018A` | STRING | Resposta do aluno à questão socioeconômica Q018A. |
| `TX_RESP_Q018B` | STRING | Resposta do aluno à questão socioeconômica Q018B. |
| `TX_RESP_Q018C` | STRING | Resposta do aluno à questão socioeconômica Q018C. |
| `TX_RESP_Q019` | STRING | Resposta do aluno à questão socioeconômica Q019. |
| `TX_RESP_Q020` | STRING | Resposta do aluno à questão socioeconômica Q020. |
| `NU_BLOCO_1_ABERTA_LP` | STRING | Número identificador do bloco 1 de questões abertas de Língua Portuguesa. |
| `NU_BLOCO_2_ABERTA_LP` | STRING | Número identificador do bloco 2 de questões abertas de Língua Portuguesa. |
| `NU_BLOCO_1_ABERTA_MT` | STRING | Número identificador do bloco 1 de questões abertas de Matemática. |
| `NU_BLOCO_2_ABERTA_MT` | STRING | Número identificador do bloco 2 de questões abertas de Matemática. |
| `CO_CONCEITO_Q1_LP` | STRING | Conceito atribuído à questão aberta 1 de Língua Portuguesa. |
| `CO_CONCEITO_Q2_LP` | STRING | Conceito atribuído à questão aberta 2 de Língua Portuguesa. |
| `CO_RESPOSTA_TEXTO` | STRING | Código identificador da resposta textual/redação do aluno. |
| `CO_CONCEITO_PROPOSITO` | STRING | Conceito avaliativo sobre o propósito comunicativo do texto produzido. |
| `CO_CONCEITO_ELEMENTO` | STRING | Conceito avaliativo sobre os elementos estruturais do texto produzido. |
| `CO_CONCEITO_SEGMENTACAO` | STRING | Conceito avaliativo sobre a segmentação textual do texto produzido. |
| `CO_TEXTO_GRAFIA` | STRING | Conceito avaliativo sobre os aspectos de grafia e ortografia do texto produzido. |
| `CO_CONCEITO_Q1_MT` | STRING | Conceito atribuído à questão aberta 1 de Matemática. |
| `CO_CONCEITO_Q2_MT` | STRING | Conceito atribuído à questão aberta 2 de Matemática. |
| `IN_PREENCHIMENTO_CH` | STRING | Indicador de preenchimento da prova de Ciências Humanas. |
| `IN_PREENCHIMENTO_CN` | STRING | Indicador de preenchimento da prova de Ciências da Natureza. |
| `IN_PRESENCA_CH` | STRING | Indicador de presença na prova de Ciências Humanas (1 - Presente, 0 - Ausente). |
| `IN_PRESENCA_CN` | STRING | Indicador de presença na prova de Ciências da Natureza (1 - Presente, 0 - Ausente). |
| `ID_CADERNO_CH` | STRING | Identificador do caderno de prova de Ciências Humanas aplicado ao aluno. |
| `ID_BLOCO_1_CH` | STRING | Identificador do primeiro bloco de itens de Ciências Humanas. |
| `ID_BLOCO_2_CH` | STRING | Identificador do segundo bloco de itens de Ciências Humanas. |
| `ID_BLOCO_3_CH` | STRING | Identificador do terceiro bloco de itens de Ciências Humanas. |
| `NU_BLOCO_1_ABERTA_CH` | STRING | Número identificador do bloco 1 de questões abertas de Ciências Humanas. |
| `NU_BLOCO_2_ABERTA_CH` | STRING | Número identificador do bloco 2 de questões abertas de Ciências Humanas. |
| `ID_CADERNO_CN` | STRING | Identificador do caderno de prova de Ciências da Natureza aplicado ao aluno. |
| `ID_BLOCO_1_CN` | STRING | Identificador do primeiro bloco de itens de Ciências da Natureza. |
| `ID_BLOCO_2_CN` | STRING | Identificador do segundo bloco de itens de Ciências da Natureza. |
| `ID_BLOCO_3_CN` | STRING | Identificador do terceiro bloco de itens de Ciências da Natureza. |
| `NU_BLOCO_1_ABERTA_CN` | STRING | Número identificador do bloco 1 de questões abertas de Ciências da Natureza. |
| `NU_BLOCO_2_ABERTA_CN` | STRING | Número identificador do bloco 2 de questões abertas de Ciências da Natureza. |
| `TX_RESP_BLOCO1_CH` | STRING | Vetor de respostas do aluno para as questões do bloco 1 de Ciências Humanas. |
| `TX_RESP_BLOCO2_CH` | STRING | Vetor de respostas do aluno para as questões do bloco 2 de Ciências Humanas. |
| `TX_RESP_BLOCO3_CH` | STRING | Vetor de respostas do aluno para as questões do bloco 3 de Ciências Humanas. |
| `CO_CONCEITO_Q1_CH` | STRING | Conceito atribuído à questão aberta 1 de Ciências Humanas. |
| `CO_CONCEITO_Q2_CH` | STRING | Conceito atribuído à questão aberta 2 de Ciências Humanas. |
| `TX_RESP_BLOCO1_CN` | STRING | Vetor de respostas do aluno para as questões do bloco 1 de Ciências da Natureza. |
| `TX_RESP_BLOCO2_CN` | STRING | Vetor de respostas do aluno para as questões do bloco 2 de Ciências da Natureza. |
| `TX_RESP_BLOCO3_CN` | STRING | Vetor de respostas do aluno para as questões do bloco 3 de Ciências da Natureza. |
| `CO_CONCEITO_Q1_CN` | STRING | Conceito atribuído à questão aberta 1 de Ciências da Natureza. |
| `CO_CONCEITO_Q2_CN` | STRING | Conceito atribuído à questão aberta 2 de Ciências da Natureza. |
| `IN_PROFICIENCIA_CH` | STRING | Indicador de cálculo de proficiência em Ciências Humanas (1 - Sim, 0 - Não). |
| `IN_PROFICIENCIA_CN` | STRING | Indicador de cálculo de proficiência em Ciências da Natureza (1 - Sim, 0 - Não). |
| `ESTRATO_CIENCIAS` | STRING | Código do estrato de amostragem populacional específico para as provas de Ciências. |
| `PESO_ALUNO_CH` | STRING | Peso amostral do aluno para cálculo de proficiência em Ciências Humanas. |
| `PROFICIENCIA_CH` | STRING | Proficiência padronizada do aluno em Ciências Humanas. |
| `ERRO_PADRAO_CH` | STRING | Erro padrão da proficiência padronizada em Ciências Humanas. |
| `PROFICIENCIA_CH_SAEB` | STRING | Proficiência do aluno em Ciências Humanas na escala SAEB. |
| `ERRO_PADRAO_CH_SAEB` | STRING | Erro padrão da proficiência em Ciências Humanas na escala SAEB. |
| `PESO_ALUNO_CN` | STRING | Peso amostral do aluno para cálculo de proficiência em Ciências da Natureza. |
| `PROFICIENCIA_CN` | STRING | Proficiência padronizada do aluno em Ciências da Natureza. |
| `ERRO_PADRAO_CN` | STRING | Erro padrão da proficiência padronizada em Ciências da Natureza. |
| `PROFICIENCIA_CN_SAEB` | STRING | Proficiência do aluno em Ciências da Natureza na escala SAEB. |
| `ERRO_PADRAO_CN_SAEB` | STRING | Erro padrão da proficiência em Ciências da Natureza na escala SAEB. |

## raw · inep_saeb_aluno_2021

File `raw__inep_saeb_aluno_2021.parquet` · 7,464,687 rows · 176 columns

Tabela de microdados dos alunos participantes do SAEB (Sistema de Avaliação da Educação Básica), contendo informações socioeconômicas, respostas aos cadernos de prova (LP, MT, CH, CN) e proficiências calculadas.

**Built from:** `raw/inep_saeb_microdados_csv_2021_ts_aluno_2ef`, `raw/inep_saeb_microdados_csv_2021_ts_aluno_34em`, `raw/inep_saeb_microdados_csv_2021_ts_aluno_5ef`, `raw/inep_saeb_microdados_csv_2021_ts_aluno_9ef`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do SAEB (ex: 2021). |
| `ID_REGIAO` | STRING | Código da região geográfica do Brasil (1 a 5). |
| `ID_UF` | STRING | Código da Unidade da Federação (IBGE). |
| `ID_MUNICIPIO` | STRING | Código do município (IBGE). |
| `ID_AREA` | STRING | Código da área da escola (1 - Urbana, 2 - Rural). |
| `ID_ESCOLA` | STRING | Código de identificação da escola no Censo Escolar (Inep). |
| `IN_PUBLICA` | STRING | Indicador de escola pública (1 - Sim, 0 - Não). |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 - Urbana, 2 - Rural). |
| `ID_TURMA` | STRING | Código de identificação único da turma. |
| `ID_SERIE` | STRING | Código da série/ano escolar avaliado. |
| `ID_ALUNO` | STRING | Código identificador único do aluno. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno no Censo Escolar. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento da prova de Língua Portuguesa (1 - Sim, 0 - Não). |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento da prova de Matemática (1 - Sim, 0 - Não). |
| `IN_PRESENCA_LP` | STRING | Indicador de presença na prova de Língua Portuguesa (1 - Presente, 0 - Ausente). |
| `IN_PRESENCA_MT` | STRING | Indicador de presença na prova de Matemática (1 - Presente, 0 - Ausente). |
| `ID_CADERNO_LP` | STRING | Identificador do caderno de prova de Língua Portuguesa aplicado ao aluno. |
| `ID_BLOCO_1_LP` | STRING | Identificador do primeiro bloco de itens de Língua Portuguesa. |
| `ID_BLOCO_2_LP` | STRING | Identificador do segundo bloco de itens de Língua Portuguesa. |
| `ID_CADERNO_MT` | STRING | Identificador do caderno de prova de Matemática aplicado ao aluno. |
| `ID_BLOCO_1_MT` | STRING | Identificador do primeiro bloco de itens de Matemática. |
| `ID_BLOCO_2_MT` | STRING | Identificador do segundo bloco de itens de Matemática. |
| `TX_RESP_BLOCO1_LP` | STRING | Vetor com as respostas do aluno aos itens do Bloco 1 de Língua Portuguesa. |
| `TX_RESP_BLOCO2_LP` | STRING | Vetor com as respostas do aluno aos itens do Bloco 2 de Língua Portuguesa. |
| `TX_RESP_BLOCO1_MT` | STRING | Vetor com as respostas do aluno aos itens do Bloco 1 de Matemática. |
| `TX_RESP_BLOCO2_MT` | STRING | Vetor com as respostas do aluno aos itens do Bloco 2 de Matemática. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador de proficiência calculada em Língua Portuguesa (1 - Sim, 0 - Não). |
| `IN_PROFICIENCIA_MT` | STRING | Indicador de proficiência calculada em Matemática (1 - Sim, 0 - Não). |
| `IN_AMOSTRA` | STRING | Indicador se o aluno pertence à amostra do SAEB (1 - Sim, 0 - Não). |
| `ESTRATO` | STRING | Código do estrato de amostragem para cálculo de pesos estatísticos. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para a avaliação de Língua Portuguesa. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência padronizada do aluno em Língua Portuguesa. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da proficiência calculada em Língua Portuguesa. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota de proficiência do aluno na escala SAEB para Língua Portuguesa. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência na escala SAEB para Língua Portuguesa. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para a avaliação de Matemática. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência padronizada do aluno em Matemática. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da proficiência calculada em Matemática. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota de proficiência do aluno na escala SAEB para Matemática. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência na escala SAEB para Matemática. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário do estudante (1 - Sim, 0 - Não). |
| `IN_INSE` | STRING | Indicador de cálculo do Indicador de Nível Socioeconômico (INSE) do aluno. |
| `INSE_ALUNO` | STRING | Valor numérico do Indicador de Nível Socioeconômico do aluno. |
| `NU_TIPO_NIVEL_INSE` | STRING | Classificação do nível socioeconômico do aluno em faixas/níveis. |
| `PESO_ALUNO_INSE` | STRING | Peso amostral do aluno para cálculo do INSE. |
| `TX_RESP_Q01` | STRING | Resposta do aluno à questão 1 do questionário socioeconômico. |
| `TX_RESP_Q02` | STRING | Resposta do aluno à questão 2 do questionário socioeconômico. |
| `TX_RESP_Q03` | STRING | Resposta do aluno à questão 3 do questionário socioeconômico. |
| `TX_RESP_Q04` | STRING | Resposta do aluno à questão 4 do questionário socioeconômico. |
| `TX_RESP_Q05` | STRING | Resposta do aluno à questão 5 do questionário socioeconômico. |
| `TX_RESP_Q06a` | STRING | Resposta do aluno à subquestão 6a do questionário socioeconômico. |
| `TX_RESP_Q06b` | STRING | Resposta do aluno à subquestão 6b do questionário socioeconômico. |
| `TX_RESP_Q06c` | STRING | Resposta do aluno à subquestão 6c do questionário socioeconômico. |
| `TX_RESP_Q06d` | STRING | Resposta do aluno à subquestão 6d do questionário socioeconômico. |
| `TX_RESP_Q06e` | STRING | Resposta do aluno à subquestão 6e do questionário socioeconômico. |
| `TX_RESP_Q07` | STRING | Resposta do aluno à questão 7 do questionário socioeconômico. |
| `TX_RESP_Q08` | STRING | Resposta do aluno à questão 8 do questionário socioeconômico. |
| `TX_RESP_Q09a` | STRING | Resposta do aluno à subquestão 9a do questionário socioeconômico. |
| `TX_RESP_Q09b` | STRING | Resposta do aluno à subquestão 9b do questionário socioeconômico. |
| `TX_RESP_Q09c` | STRING | Resposta do aluno à subquestão 9c do questionário socioeconômico. |
| `TX_RESP_Q09d` | STRING | Resposta do aluno à subquestão 9d do questionário socioeconômico. |
| `TX_RESP_Q09e` | STRING | Resposta do aluno à subquestão 9e do questionário socioeconômico. |
| `TX_RESP_Q09f` | STRING | Resposta do aluno à subquestão 9f do questionário socioeconômico. |
| `TX_RESP_Q10a` | STRING | Resposta do aluno à subquestão 10a do questionário socioeconômico. |
| `TX_RESP_Q10b` | STRING | Resposta do aluno à subquestão 10b do questionário socioeconômico. |
| `TX_RESP_Q10c` | STRING | Resposta do aluno à subquestão 10c do questionário socioeconômico. |
| `TX_RESP_Q11a` | STRING | Resposta do aluno à subquestão 11a do questionário socioeconômico. |
| `TX_RESP_Q11b` | STRING | Resposta do aluno à subquestão 11b do questionário socioeconômico. |
| `TX_RESP_Q11c` | STRING | Resposta do aluno à subquestão 11c do questionário socioeconômico. |
| `TX_RESP_Q11d` | STRING | Resposta do aluno à subquestão 11d do questionário socioeconômico. |
| `TX_RESP_Q11e` | STRING | Resposta do aluno à subquestão 11e do questionário socioeconômico. |
| `TX_RESP_Q11f` | STRING | Resposta do aluno à subquestão 11f do questionário socioeconômico. |
| `TX_RESP_Q11g` | STRING | Resposta do aluno à subquestão 11g do questionário socioeconômico. |
| `TX_RESP_Q11h` | STRING | Resposta do aluno à subquestão 11h do questionário socioeconômico. |
| `TX_RESP_Q12a` | STRING | Resposta do aluno à subquestão 12a do questionário socioeconômico. |
| `TX_RESP_Q12b` | STRING | Resposta do aluno à subquestão 12b do questionário socioeconômico. |
| `TX_RESP_Q12c` | STRING | Resposta do aluno à subquestão 12c do questionário socioeconômico. |
| `TX_RESP_Q12d` | STRING | Resposta do aluno à subquestão 12d do questionário socioeconômico. |
| `TX_RESP_Q12e` | STRING | Resposta do aluno à subquestão 12e do questionário socioeconômico. |
| `TX_RESP_Q12f` | STRING | Resposta do aluno à subquestão 12f do questionário socioeconômico. |
| `TX_RESP_Q12g` | STRING | Resposta do aluno à subquestão 12g do questionário socioeconômico. |
| `TX_RESP_Q12h` | STRING | Resposta do aluno à subquestão 12h do questionário socioeconômico. |
| `TX_RESP_Q12i` | STRING | Resposta do aluno à subquestão 12i do questionário socioeconômico. |
| `TX_RESP_Q13` | STRING | Resposta do aluno à questão 13 do questionário socioeconômico. |
| `TX_RESP_Q14` | STRING | Resposta do aluno à questão 14 do questionário socioeconômico. |
| `TX_RESP_Q15` | STRING | Resposta do aluno à questão 15 do questionário socioeconômico. |
| `TX_RESP_Q16` | STRING | Resposta do aluno à questão 16 do questionário socioeconômico. |
| `TX_RESP_Q17` | STRING | Resposta do aluno à questão 17 do questionário socioeconômico. |
| `TX_RESP_Q18` | STRING | Resposta do aluno à questão 18 do questionário socioeconômico. |
| `TX_RESP_Q19` | STRING | Resposta do aluno à questão 19 do questionário socioeconômico. |
| `TX_RESP_Q20a` | STRING | Resposta do aluno à subquestão 20a do questionário socioeconômico. |
| `TX_RESP_Q20b` | STRING | Resposta do aluno à subquestão 20b do questionário socioeconômico. |
| `TX_RESP_Q20c` | STRING | Resposta do aluno à subquestão 20c do questionário socioeconômico. |
| `TX_RESP_Q20d` | STRING | Resposta do aluno à subquestão 20d do questionário socioeconômico. |
| `TX_RESP_Q20e` | STRING | Resposta do aluno à subquestão 20e do questionário socioeconômico. |
| `TX_RESP_Q21` | STRING | Resposta do aluno à questão 21 do questionário socioeconômico. |
| `TX_RESP_Q22` | STRING | Resposta do aluno à questão 22 do questionário socioeconômico. |
| `TX_RESP_Q23a` | STRING | Resposta do aluno à subquestão 23a do questionário socioeconômico. |
| `TX_RESP_Q23b` | STRING | Resposta do aluno à subquestão 23b do questionário socioeconômico. |
| `TX_RESP_Q23c` | STRING | Resposta do aluno à subquestão 23c do questionário socioeconômico. |
| `TX_RESP_Q23d` | STRING | Resposta do aluno à subquestão 23d do questionário socioeconômico. |
| `TX_RESP_Q23e` | STRING | Resposta do aluno à subquestão 23e do questionário socioeconômico. |
| `TX_RESP_Q23f` | STRING | Resposta do aluno à subquestão 23f do questionário socioeconômico. |
| `TX_RESP_Q23g` | STRING | Resposta do aluno à subquestão 23g do questionário socioeconômico. |
| `TX_RESP_Q23h` | STRING | Resposta do aluno à subquestão 23h do questionário socioeconômico. |
| `TX_RESP_Q23i` | STRING | Resposta do aluno à subquestão 23i do questionário socioeconômico. |
| `NU_BLOCO_1_ABERTA_LP` | STRING | Número identificador do bloco de questões abertas de Língua Portuguesa. |
| `NU_BLOCO_2_ABERTA_LP` | STRING | Número identificador do bloco de questões abertas de Língua Portuguesa. |
| `NU_BLOCO_1_ABERTA_MT` | STRING | Número identificador do bloco de questões abertas de Matemática. |
| `NU_BLOCO_2_ABERTA_MT` | STRING | Número identificador do bloco de questões abertas de Matemática. |
| `CO_CONCEITO_Q1_LP` | STRING | Conceito atribuído à questão aberta 1 de Língua Portuguesa. |
| `CO_CONCEITO_Q2_LP` | STRING | Conceito atribuído à questão aberta 2 de Língua Portuguesa. |
| `CO_RESPOSTA_TEXTO` | STRING | Código indicador do tipo de resposta textual fornecida pelo aluno. |
| `CO_CONCEITO_PROPOSITO` | STRING | Conceito atribuído à adequação ao propósito do texto avaliado. |
| `CO_CONCEITO_ELEMENTO` | STRING | Conceito atribuído aos elementos estruturais do texto avaliado. |
| `CO_CONCEITO_SEGMENTACAO` | STRING | Conceito atribuído à segmentação do texto avaliado. |
| `CO_TEXTO_GRAFIA` | STRING | Conceito atribuído à grafia e ortografia do texto avaliado. |
| `CO_CONCEITO_Q1_MT` | STRING | Conceito atribuído à questão aberta 1 de Matemática. |
| `CO_CONCEITO_Q2_MT` | STRING | Conceito atribuído à questão aberta 2 de Matemática. |
| `TX_RESP_Q21a` | STRING | Resposta do aluno à subquestão 21a do questionário socioeconômico. |
| `TX_RESP_Q21b` | STRING | Resposta do aluno à subquestão 21b do questionário socioeconômico. |
| `TX_RESP_Q21c` | STRING | Resposta do aluno à subquestão 21c do questionário socioeconômico. |
| `TX_RESP_Q21d` | STRING | Resposta do aluno à subquestão 21d do questionário socioeconômico. |
| `TX_RESP_Q21e` | STRING | Resposta do aluno à subquestão 21e do questionário socioeconômico. |
| `TX_RESP_Q21f` | STRING | Resposta do aluno à subquestão 21f do questionário socioeconômico. |
| `TX_RESP_Q21g` | STRING | Resposta do aluno à subquestão 21g do questionário socioeconômico. |
| `TX_RESP_Q21h` | STRING | Resposta do aluno à subquestão 21h do questionário socioeconômico. |
| `TX_RESP_Q21i` | STRING | Resposta do aluno à subquestão 21i do questionário socioeconômico. |
| `IN_PREENCHIMENTO_CH` | STRING | Indicador de preenchimento da prova de Ciências Humanas (1 - Sim, 0 - Não). |
| `IN_PREENCHIMENTO_CN` | STRING | Indicador de preenchimento da prova de Ciências da Natureza (1 - Sim, 0 - Não). |
| `IN_PRESENCA_CH` | STRING | Indicador de presença na prova de Ciências Humanas (1 - Presente, 0 - Ausente). |
| `IN_PRESENCA_CN` | STRING | Indicador de presença na prova de Ciências da Natureza (1 - Presente, 0 - Ausente). |
| `ID_CADERNO_CH` | STRING | Identificador do caderno de prova de Ciências Humanas aplicado ao aluno. |
| `ID_BLOCO_1_CH` | STRING | Identificador do primeiro bloco de itens de Ciências Humanas. |
| `ID_BLOCO_2_CH` | STRING | Identificador do segundo bloco de itens de Ciências Humanas. |
| `ID_BLOCO_3_CH` | STRING | Identificador do terceiro bloco de itens de Ciências Humanas. |
| `NU_BLOCO_1_ABERTA_CH` | STRING | Número identificador do bloco de questões abertas de Ciências Humanas. |
| `NU_BLOCO_2_ABERTA_CH` | STRING | Número identificador do bloco de questões abertas de Ciências Humanas. |
| `ID_CADERNO_CN` | STRING | Identificador do caderno de prova de Ciências da Natureza aplicado ao aluno. |
| `ID_BLOCO_1_CN` | STRING | Identificador do primeiro bloco de itens de Ciências da Natureza. |
| `ID_BLOCO_2_CN` | STRING | Identificador do segundo bloco de itens de Ciências da Natureza. |
| `ID_BLOCO_3_CN` | STRING | Identificador do terceiro bloco de itens de Ciências da Natureza. |
| `NU_BLOCO_1_ABERTA_CN` | STRING | Número identificador do bloco de questões abertas de Ciências da Natureza. |
| `NU_BLOCO_2_ABERTA_CN` | STRING | Número identificador do bloco de questões abertas de Ciências da Natureza. |
| `TX_RESP_BLOCO1_CH` | STRING | Vetor com as respostas do aluno aos itens do Bloco 1 de Ciências Humanas. |
| `TX_RESP_BLOCO2_CH` | STRING | Vetor com as respostas do aluno aos itens do Bloco 2 de Ciências Humanas. |
| `TX_RESP_BLOCO3_CH` | STRING | Vetor com as respostas do aluno aos itens do Bloco 3 de Ciências Humanas. |
| `CO_CONCEITO_Q1_CH` | STRING | Conceito atribuído à questão aberta 1 de Ciências Humanas. |
| `CO_CONCEITO_Q2_CH` | STRING | Conceito atribuído à questão aberta 2 de Ciências Humanas. |
| `TX_RESP_BLOCO1_CN` | STRING | Vetor com as respostas do aluno aos itens do Bloco 1 de Ciências da Natureza. |
| `TX_RESP_BLOCO2_CN` | STRING | Vetor com as respostas do aluno aos itens do Bloco 2 de Ciências da Natureza. |
| `TX_RESP_BLOCO3_CN` | STRING | Vetor com as respostas do aluno aos itens do Bloco 3 de Ciências da Natureza. |
| `CO_CONCEITO_Q1_CN` | STRING | Conceito atribuído à questão aberta 1 de Ciências da Natureza. |
| `CO_CONCEITO_Q2_CN` | STRING | Conceito atribuído à questão aberta 2 de Ciências da Natureza. |
| `IN_PROFICIENCIA_CH` | STRING | Indicador de proficiência calculada em Ciências Humanas (1 - Sim, 0 - Não). |
| `IN_PROFICIENCIA_CN` | STRING | Indicador de proficiência calculada em Ciências da Natureza (1 - Sim, 0 - Não). |
| `ESTRATO_CIENCIAS` | STRING | Código do estrato de amostragem para a avaliação de Ciências. |
| `PESO_ALUNO_CH` | STRING | Peso amostral do aluno para a avaliação de Ciências Humanas. |
| `PROFICIENCIA_CH` | STRING | Nota de proficiência padronizada do aluno em Ciências Humanas. |
| `ERRO_PADRAO_CH` | STRING | Erro padrão da proficiência calculada em Ciências Humanas. |
| `PROFICIENCIA_CH_SAEB` | STRING | Nota de proficiência do aluno na escala SAEB para Ciências Humanas. |
| `ERRO_PADRAO_CH_SAEB` | STRING | Erro padrão da proficiência na escala SAEB para Ciências Humanas. |
| `PESO_ALUNO_CN` | STRING | Peso amostral do aluno para a avaliação de Ciências da Natureza. |
| `PROFICIENCIA_CN` | STRING | Nota de proficiência padronizada do aluno em Ciências da Natureza. |
| `ERRO_PADRAO_CN` | STRING | Erro padrão da proficiência calculada em Ciências da Natureza. |
| `PROFICIENCIA_CN_SAEB` | STRING | Nota de proficiência do aluno na escala SAEB para Ciências da Natureza. |
| `ERRO_PADRAO_CN_SAEB` | STRING | Erro padrão da proficiência na escala SAEB para Ciências da Natureza. |
| `TX_RESP_Q22a` | STRING | Resposta do aluno à subquestão 22a do questionário socioeconômico. |
| `TX_RESP_Q22b` | STRING | Resposta do aluno à subquestão 22b do questionário socioeconômico. |
| `TX_RESP_Q22c` | STRING | Resposta do aluno à subquestão 22c do questionário socioeconômico. |
| `TX_RESP_Q22d` | STRING | Resposta do aluno à subquestão 22d do questionário socioeconômico. |
| `TX_RESP_Q22e` | STRING | Resposta do aluno à subquestão 22e do questionário socioeconômico. |
| `TX_RESP_Q22f` | STRING | Resposta do aluno à subquestão 22f do questionário socioeconômico. |
| `TX_RESP_Q22g` | STRING | Resposta do aluno à subquestão 22g do questionário socioeconômico. |
| `TX_RESP_Q22h` | STRING | Resposta do aluno à subquestão 22h do questionário socioeconômico. |
| `TX_RESP_Q22i` | STRING | Resposta do aluno à subquestão 22i do questionário socioeconômico. |

## raw · inep_saeb_aluno_2023

File `raw__inep_saeb_aluno_2023.parquet` · 7,073,491 rows · 169 columns

Microdados dos estudantes avaliados no SAEB (Sistema de Avaliação da Educação Básica), contendo informações socioeconômicas, respostas aos questionários contextuais, cadernos de prova e proficiências em Língua Portuguesa, Matemática, Ciências Humanas e Ciências da Natureza.

**Built from:** `raw/inep_saeb_microdados_csv_2023_ts_aluno_2ef`, `raw/inep_saeb_microdados_csv_2023_ts_aluno_34em`, `raw/inep_saeb_microdados_csv_2023_ts_aluno_5ef`, `raw/inep_saeb_microdados_csv_2023_ts_aluno_9ef`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de referência da edição do SAEB (ex: 2023). |
| `ID_REGIAO` | STRING | Código identificador da região geográfica do Brasil. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação da escola. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. |
| `ID_AREA` | STRING | Código da área de localização da escola (1 - Urbana, 2 - Rural). |
| `ID_ESCOLA` | STRING | Código INEP identificador único da escola. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 - Sim, 0 - Não). |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 - Urbana, 2 - Rural). |
| `ID_TURMA` | STRING | Código identificador único da turma no Censo Escolar. |
| `ID_SERIE` | STRING | Série ou ano escolar avaliado (ex: 5 para 5º ano, 9 para 9º ano). |
| `ID_ALUNO` | STRING | Código identificador único do aluno no SAEB. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno no Censo Escolar. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento da prova de Língua Portuguesa (1 - Sim, 0 - Não). |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento da prova de Matemática (1 - Sim, 0 - Não). |
| `IN_PREENCHIMENTO_CH` | STRING | Indicador de preenchimento da prova de Ciências Humanas (1 - Sim, 0 - Não). |
| `IN_PREENCHIMENTO_CN` | STRING | Indicador de preenchimento da prova de Ciências da Natureza (1 - Sim, 0 - Não). |
| `IN_PRESENCA_LP` | STRING | Indicador de presença do aluno na prova de Língua Portuguesa (1 - Presente, 0 - Ausente). |
| `IN_PRESENCA_MT` | STRING | Indicador de presença do aluno na prova de Matemática (1 - Presente, 0 - Ausente). |
| `IN_PRESENCA_CH` | STRING | Indicador de presença do aluno na prova de Ciências Humanas (1 - Presente, 0 - Ausente). |
| `IN_PRESENCA_CN` | STRING | Indicador de presença do aluno na prova de Ciências da Natureza (1 - Presente, 0 - Ausente). |
| `ID_CADERNO_LP` | STRING | Identificador do caderno de prova de Língua Portuguesa aplicado ao aluno. |
| `ID_BLOCO_1_LP` | STRING | Identificador do primeiro bloco de itens de Língua Portuguesa. |
| `ID_BLOCO_2_LP` | STRING | Identificador do segundo bloco de itens de Língua Portuguesa. |
| `ID_CADERNO_MT` | STRING | Identificador do caderno de prova de Matemática aplicado ao aluno. |
| `ID_BLOCO_1_MT` | STRING | Identificador do primeiro bloco de itens de Matemática. |
| `ID_BLOCO_2_MT` | STRING | Identificador do segundo bloco de itens de Matemática. |
| `ID_CADERNO_CH` | STRING | Identificador do caderno de prova de Ciências Humanas aplicado ao aluno. |
| `ID_BLOCO_1_CH` | STRING | Identificador do primeiro bloco de itens de Ciências Humanas. |
| `ID_BLOCO_2_CH` | STRING | Identificador do segundo bloco de itens de Ciências Humanas. |
| `NU_BLOCO_1_ABERTA_CH` | STRING | Número de questões abertas no bloco 1 de Ciências Humanas. |
| `NU_BLOCO_2_ABERTA_CH` | STRING | Número de questões abertas no bloco 2 de Ciências Humanas. |
| `ID_CADERNO_CN` | STRING | Identificador do caderno de prova de Ciências da Natureza aplicado ao aluno. |
| `ID_BLOCO_1_CN` | STRING | Identificador do primeiro bloco de itens de Ciências da Natureza. |
| `ID_BLOCO_2_CN` | STRING | Identificador do segundo bloco de itens de Ciências da Natureza. |
| `ID_BLOCO_3_CN` | STRING | Identificador do terceiro bloco de itens de Ciências da Natureza. |
| `NU_BLOCO_1_ABERTA_CN` | STRING | Número de questões abertas no bloco 1 de Ciências da Natureza. |
| `NU_BLOCO_2_ABERTA_CN` | STRING | Número de questões abertas no bloco 2 de Ciências da Natureza. |
| `TX_RESP_BLOCO1_LP` | STRING | String contendo as respostas do aluno para os itens do bloco 1 de Língua Portuguesa. |
| `TX_RESP_BLOCO2_LP` | STRING | String contendo as respostas do aluno para os itens do bloco 2 de Língua Portuguesa. |
| `TX_RESP_BLOCO1_MT` | STRING | String contendo as respostas do aluno para os itens do bloco 1 de Matemática. |
| `TX_RESP_BLOCO2_MT` | STRING | String contendo as respostas do aluno para os itens do bloco 2 de Matemática. |
| `TX_RESP_BLOCO1_CH` | STRING | String contendo as respostas do aluno para os itens do bloco 1 de Ciências Humanas. |
| `TX_RESP_BLOCO2_CH` | STRING | String contendo as respostas do aluno para os itens do bloco 2 de Ciências Humanas. |
| `CO_CONCEITO_Q1_CH` | STRING | Conceito atribuído à resposta da questão aberta 1 de Ciências Humanas. |
| `CO_CONCEITO_Q2_CH` | STRING | Conceito atribuído à resposta da questão aberta 2 de Ciências Humanas. |
| `TX_RESP_BLOCO1_CN` | STRING | String contendo as respostas do aluno para os itens do bloco 1 de Ciências da Natureza. |
| `TX_RESP_BLOCO2_CN` | STRING | String contendo as respostas do aluno para os itens do bloco 2 de Ciências da Natureza. |
| `TX_RESP_BLOCO3_CN` | STRING | String contendo as respostas do aluno para os itens do bloco 3 de Ciências da Natureza. |
| `CO_CONCEITO_Q1_CN` | STRING | Conceito atribuído à resposta da questão aberta 1 de Ciências da Natureza. |
| `CO_CONCEITO_Q2_CN` | STRING | Conceito atribuído à resposta da questão aberta 2 de Ciências da Natureza. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador de cálculo de proficiência em Língua Portuguesa (1 - Calculada, 0 - Não). |
| `IN_PROFICIENCIA_MT` | STRING | Indicador de cálculo de proficiência em Matemática (1 - Calculada, 0 - Não). |
| `IN_PROFICIENCIA_CH` | STRING | Indicador de cálculo de proficiência em Ciências Humanas (1 - Calculada, 0 - Não). |
| `IN_PROFICIENCIA_CN` | STRING | Indicador de cálculo de proficiência em Ciências da Natureza (1 - Calculada, 0 - Não). |
| `IN_AMOSTRA` | STRING | Indicador se o aluno pertence à amostra do SAEB (1 - Sim, 0 - Não). |
| `ESTRATO` | STRING | Código do estrato de amostragem do aluno para fins estatísticos. |
| `ESTRATO_CIENCIAS` | STRING | Código do estrato de amostragem específico para a avaliação de Ciências. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para a proficiência de Língua Portuguesa. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência estimada do aluno em Língua Portuguesa. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da proficiência estimada em Língua Portuguesa. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota de proficiência padronizada em Língua Portuguesa na escala SAEB. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência padronizada em Língua Portuguesa na escala SAEB. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para a proficiência de Matemática. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência estimada do aluno em Matemática. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da proficiência estimada em Matemática. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota de proficiência padronizada em Matemática na escala SAEB. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência padronizada em Matemática na escala SAEB. |
| `PESO_ALUNO_CH` | STRING | Peso amostral do aluno para a proficiência de Ciências Humanas. |
| `PROFICIENCIA_CH` | STRING | Nota de proficiência estimada do aluno em Ciências Humanas. |
| `ERRO_PADRAO_CH` | STRING | Erro padrão da proficiência estimada em Ciências Humanas. |
| `PROFICIENCIA_CH_SAEB` | STRING | Nota de proficiência padronizada em Ciências Humanas na escala SAEB. |
| `ERRO_PADRAO_CH_SAEB` | STRING | Erro padrão da proficiência padronizada em Ciências Humanas na escala SAEB. |
| `PESO_ALUNO_CN` | STRING | Peso amostral do aluno para a proficiência de Ciências da Natureza. |
| `PROFICIENCIA_CN` | STRING | Nota de proficiência estimada do aluno em Ciências da Natureza. |
| `ERRO_PADRAO_CN` | STRING | Erro padrão da proficiência estimada em Ciências da Natureza. |
| `PROFICIENCIA_CN_SAEB` | STRING | Nota de proficiência padronizada em Ciências da Natureza na escala SAEB. |
| `ERRO_PADRAO_CN_SAEB` | STRING | Erro padrão da proficiência padronizada em Ciências da Natureza na escala SAEB. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário do estudante (1 - Preenchido, 0 - Não). |
| `IN_INSE` | STRING | Indicador de cálculo do Indicador de Nível Socioeconômico (INSE) do aluno. |
| `INSE_ALUNO` | STRING | Valor numérico do Indicador de Nível Socioeconômico (INSE) do aluno. |
| `NU_TIPO_NIVEL_INSE` | STRING | Classificação do nível socioeconômico do aluno em faixas/níveis. |
| `PESO_ALUNO_INSE` | STRING | Peso amostral do aluno associado ao cálculo do INSE. |
| `TX_RESP_Q01` | STRING | Resposta do aluno à questão 1 do questionário socioeconômico. |
| `TX_RESP_Q02` | STRING | Resposta do aluno à questão 2 do questionário socioeconômico. |
| `TX_RESP_Q03` | STRING | Resposta do aluno à questão 3 do questionário socioeconômico. |
| `TX_RESP_Q04` | STRING | Resposta do aluno à questão 4 do questionário socioeconômico. |
| `TX_RESP_Q05a` | STRING | Resposta do aluno à questão 5a do questionário socioeconômico. |
| `TX_RESP_Q05b` | STRING | Resposta do aluno à questão 5b do questionário socioeconômico. |
| `TX_RESP_Q05c` | STRING | Resposta do aluno à questão 5c do questionário socioeconômico. |
| `TX_RESP_Q06` | STRING | Resposta do aluno à questão 6 do questionário socioeconômico. |
| `TX_RESP_Q07a` | STRING | Resposta do aluno à questão 7a do questionário socioeconômico. |
| `TX_RESP_Q07b` | STRING | Resposta do aluno à questão 7b do questionário socioeconômico. |
| `TX_RESP_Q07c` | STRING | Resposta do aluno à questão 7c do questionário socioeconômico. |
| `TX_RESP_Q07d` | STRING | Resposta do aluno à questão 7d do questionário socioeconômico. |
| `TX_RESP_Q07e` | STRING | Resposta do aluno à questão 7e do questionário socioeconômico. |
| `TX_RESP_Q08` | STRING | Resposta do aluno à questão 8 do questionário socioeconômico. |
| `TX_RESP_Q09` | STRING | Resposta do aluno à questão 9 do questionário socioeconômico. |
| `TX_RESP_Q10a` | STRING | Resposta do aluno à questão 10a do questionário socioeconômico. |
| `TX_RESP_Q10b` | STRING | Resposta do aluno à questão 10b do questionário socioeconômico. |
| `TX_RESP_Q10c` | STRING | Resposta do aluno à questão 10c do questionário socioeconômico. |
| `TX_RESP_Q10d` | STRING | Resposta do aluno à questão 10d do questionário socioeconômico. |
| `TX_RESP_Q10e` | STRING | Resposta do aluno à questão 10e do questionário socioeconômico. |
| `TX_RESP_Q10f` | STRING | Resposta do aluno à questão 10f do questionário socioeconômico. |
| `TX_RESP_Q11a` | STRING | Resposta do aluno à questão 11a do questionário socioeconômico. |
| `TX_RESP_Q11b` | STRING | Resposta do aluno à questão 11b do questionário socioeconômico. |
| `TX_RESP_Q11c` | STRING | Resposta do aluno à questão 11c do questionário socioeconômico. |
| `TX_RESP_Q12a` | STRING | Resposta do aluno à questão 12a do questionário socioeconômico. |
| `TX_RESP_Q12b` | STRING | Resposta do aluno à questão 12b do questionário socioeconômico. |
| `TX_RESP_Q12c` | STRING | Resposta do aluno à questão 12c do questionário socioeconômico. |
| `TX_RESP_Q12d` | STRING | Resposta do aluno à questão 12d do questionário socioeconômico. |
| `TX_RESP_Q12e` | STRING | Resposta do aluno à questão 12e do questionário socioeconômico. |
| `TX_RESP_Q12f` | STRING | Resposta do aluno à questão 12f do questionário socioeconômico. |
| `TX_RESP_Q12g` | STRING | Resposta do aluno à questão 12g do questionário socioeconômico. |
| `TX_RESP_Q13a` | STRING | Resposta do aluno à questão 13a do questionário socioeconômico. |
| `TX_RESP_Q13b` | STRING | Resposta do aluno à questão 13b do questionário socioeconômico. |
| `TX_RESP_Q13c` | STRING | Resposta do aluno à questão 13c do questionário socioeconômico. |
| `TX_RESP_Q13d` | STRING | Resposta do aluno à questão 13d do questionário socioeconômico. |
| `TX_RESP_Q13e` | STRING | Resposta do aluno à questão 13e do questionário socioeconômico. |
| `TX_RESP_Q13f` | STRING | Resposta do aluno à questão 13f do questionário socioeconômico. |
| `TX_RESP_Q13g` | STRING | Resposta do aluno à questão 13g do questionário socioeconômico. |
| `TX_RESP_Q13h` | STRING | Resposta do aluno à questão 13h do questionário socioeconômico. |
| `TX_RESP_Q13i` | STRING | Resposta do aluno à questão 13i do questionário socioeconômico. |
| `TX_RESP_Q14` | STRING | Resposta do aluno à questão 14 do questionário socioeconômico. |
| `TX_RESP_Q15a` | STRING | Resposta do aluno à questão 15a do questionário socioeconômico. |
| `TX_RESP_Q15b` | STRING | Resposta do aluno à questão 15b do questionário socioeconômico. |
| `TX_RESP_Q16` | STRING | Resposta do aluno à questão 16 do questionário socioeconômico. |
| `TX_RESP_Q17` | STRING | Resposta do aluno à questão 17 do questionário socioeconômico. |
| `TX_RESP_Q18` | STRING | Resposta do aluno à questão 18 do questionário socioeconômico. |
| `TX_RESP_Q19` | STRING | Resposta do aluno à questão 19 do questionário socioeconômico. |
| `TX_RESP_Q20` | STRING | Resposta do aluno à questão 20 do questionário socioeconômico. |
| `TX_RESP_Q21a` | STRING | Resposta do aluno à questão 21a do questionário socioeconômico. |
| `TX_RESP_Q21b` | STRING | Resposta do aluno à questão 21b do questionário socioeconômico. |
| `TX_RESP_Q21c` | STRING | Resposta do aluno à questão 21c do questionário socioeconômico. |
| `TX_RESP_Q21d` | STRING | Resposta do aluno à questão 21d do questionário socioeconômico. |
| `TX_RESP_Q21e` | STRING | Resposta do aluno à questão 21e do questionário socioeconômico. |
| `TX_RESP_Q22a` | STRING | Resposta do aluno à questão 22a do questionário socioeconômico. |
| `TX_RESP_Q22b` | STRING | Resposta do aluno à questão 22b do questionário socioeconômico. |
| `TX_RESP_Q22c` | STRING | Resposta do aluno à questão 22c do questionário socioeconômico. |
| `TX_RESP_Q22d` | STRING | Resposta do aluno à questão 22d do questionário socioeconômico. |
| `TX_RESP_Q22e` | STRING | Resposta do aluno à questão 22e do questionário socioeconômico. |
| `TX_RESP_Q22f` | STRING | Resposta do aluno à questão 22f do questionário socioeconômico. |
| `TX_RESP_Q22g` | STRING | Resposta do aluno à questão 22g do questionário socioeconômico. |
| `TX_RESP_Q22h` | STRING | Resposta do aluno à questão 22h do questionário socioeconômico. |
| `TX_RESP_Q23a` | STRING | Resposta do aluno à questão 23a do questionário socioeconômico. |
| `TX_RESP_Q23b` | STRING | Resposta do aluno à questão 23b do questionário socioeconômico. |
| `TX_RESP_Q23c` | STRING | Resposta do aluno à questão 23c do questionário socioeconômico. |
| `TX_RESP_Q23d` | STRING | Resposta do aluno à questão 23d do questionário socioeconômico. |
| `TX_RESP_Q23e` | STRING | Resposta do aluno à questão 23e do questionário socioeconômico. |
| `TX_RESP_Q23f` | STRING | Resposta do aluno à questão 23f do questionário socioeconômico. |
| `TX_RESP_Q23g` | STRING | Resposta do aluno à questão 23g do questionário socioeconômico. |
| `TX_RESP_Q23h` | STRING | Resposta do aluno à questão 23h do questionário socioeconômico. |
| `TX_RESP_Q23i` | STRING | Resposta do aluno à questão 23i do questionário socioeconômico. |
| `TX_RESP_Q24` | STRING | Resposta do aluno à questão 24 do questionário socioeconômico. |
| `TX_RESP_Q25` | STRING | Resposta do aluno à questão 25 do questionário socioeconômico. |
| `NU_BLOCO_1_ABERTA_LP` | STRING | Número de questões abertas no bloco 1 de Língua Portuguesa. |
| `NU_BLOCO_2_ABERTA_LP` | STRING | Número de questões abertas no bloco 2 de Língua Portuguesa. |
| `NU_BLOCO_1_ABERTA_MT` | STRING | Número de questões abertas no bloco 1 de Matemática. |
| `NU_BLOCO_2_ABERTA_MT` | STRING | Número de questões abertas no bloco 2 de Matemática. |
| `CO_CONCEITO_Q1_LP` | STRING | Conceito atribuído à resposta da questão aberta 1 de Língua Portuguesa. |
| `CO_CONCEITO_Q2_LP` | STRING | Conceito atribuído à resposta da questão aberta 2 de Língua Portuguesa. |
| `CO_RESPOSTA_TEXTO` | STRING | Código identificador do tipo de resposta textual ou redação produzida. |
| `CO_CONCEITO_SEQUENCIA` | STRING | Conceito atribuído ao critério de sequência textual na redação. |
| `CO_CONCEITO_COESAO` | STRING | Conceito atribuído ao critério de coesão textual na redação. |
| `CO_CONCEITO_PONTUACAO` | STRING | Conceito atribuído ao critério de pontuação na redação. |
| `CO_CONCEITO_SEGMENTACAO` | STRING | Conceito atribuído ao critério de segmentação textual na redação. |
| `CO_TEXTO_GRAFIA` | STRING | Conceito atribuído ao critério de grafia e ortografia na redação. |
| `CO_CONCEITO_Q1_MT` | STRING | Conceito atribuído à resposta da questão aberta 1 de Matemática. |
| `CO_CONCEITO_Q2_MT` | STRING | Conceito atribuído à resposta da questão aberta 2 de Matemática. |
| `IN_ALFABETIZADO` | STRING | Indicador se o estudante foi classificado como alfabetizado (1 - Sim, 0 - Não). |

## raw · inep_saeb_arquivos

File `raw__inep_saeb_arquivos.parquet` · 64 rows · 19 columns

Catalogo raw dos arquivos oficiais do Saeb baixados do Inep, com hash, status e linhagem.

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano da edicao do Saeb divulgado na pagina oficial. |
| `tipo_arquivo` | STRING | Tipo classificado do arquivo: microdados, resultado_planilha, documento_pdf ou outro. |
| `rotulo_origem` | STRING | Texto do link na pagina oficial do Inep. |
| `pagina_url` | STRING | URL da subpagina oficial de resultados do Saeb. |
| `download_url` | STRING | URL oficial do arquivo baixado. |
| `arquivo` | STRING | Nome do arquivo oficial. |
| `arquivo_local` | STRING | Nome local usado para evitar colisoes de arquivos oficiais com mesmo basename. |
| `extensao` | STRING | Extensao do arquivo oficial. |
| `tamanho_bytes` | INTEGER | Tamanho do arquivo baixado em bytes. |
| `sha256` | STRING | Hash SHA-256 calculado apos download. |
| `status_download` | STRING | Estado da etapa de download do arquivo (ex: 'downloaded'). — descrição gerada por IA. |
| `erro_download` | STRING | Mensagem de erro do download, quando houver. |
| `status_extracao` | STRING | Estado do processo de descompactação (ex: 'extracted', 'listed_not_extracted_disk_guard'). — descrição gerada por IA. |
| `qtd_arquivos_extraidos` | INTEGER | Quantidade total de arquivos gerados após a descompactação. — descrição gerada por IA. |
| `erro_extracao` | STRING | Mensagem de erro de extracao, quando houver. |
| `dt_descoberta_utc` | STRING | Timestamp UTC da descoberta do link. |
| `dt_download_utc` | STRING | Timestamp UTC do download. |
| `dt_extracao_utc` | STRING | Timestamp UTC da extracao/catalogacao. |
| `dt_ingestao_lake` | TIMESTAMP | Data/hora da carga do catalogo no BigQuery. |

## raw · inep_saeb_arquivos_conteudo

File `raw__inep_saeb_arquivos_conteudo.parquet` · 720 rows · 20 columns

Catalogo raw do conteudo encontrado em arquivos oficiais do Saeb, incluindo planilhas, abas e arquivos extraidos.

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano da edicao do Saeb. |
| `tipo_arquivo` | STRING | Tipo classificado do arquivo oficial. |
| `rotulo_origem` | STRING | Texto do link na pagina oficial do Inep. |
| `pagina_url` | STRING | URL da subpagina oficial de resultados do Saeb. |
| `download_url` | STRING | URL oficial do arquivo baixado. |
| `arquivo` | STRING | Nome do arquivo oficial baixado. |
| `arquivo_local` | STRING | Nome local usado para salvar o arquivo baixado sem colidir com outro basename. |
| `status_download` | STRING | Situação da execução do download do arquivo (ex: downloaded, failed). — descrição gerada por IA. |
| `status_extracao` | STRING | Situação do processo de descompactação do arquivo (ex: not_archive, extracted, error). — descrição gerada por IA. |
| `origem_conteudo` | STRING | Indica se o conteudo veio de arquivo direto ou de compactado extraido. |
| `nome_conteudo` | STRING | Nome do arquivo de conteudo perfilado. |
| `extensao_conteudo` | STRING | Extensao do arquivo de conteudo perfilado. |
| `tipo_conteudo` | STRING | Tipo inferido do conteudo: planilha, csv, documento_pdf, arquivo_compactado ou outro. |
| `tamanho_conteudo_bytes` | INTEGER | Tamanho do arquivo de conteudo em bytes. |
| `aba` | STRING | Nome da aba quando o conteudo e uma planilha Excel. |
| `linhas_planilha` | INTEGER | Quantidade total de linhas de dados presentes na planilha analisada. — descrição gerada por IA. |
| `colunas_planilha` | INTEGER | Quantidade total de colunas identificadas no arquivo de planilha analisado. — descrição gerada por IA. |
| `erro_perfil` | STRING | Erro de leitura/perfilamento do conteudo, quando houver. |
| `dt_perfil_utc` | STRING | Timestamp UTC do perfilamento local. |
| `dt_ingestao_lake` | TIMESTAMP | Data/hora da carga do catalogo no BigQuery. |

## raw · inep_saeb_microdados_csv_2011_ts_item

File `raw__inep_saeb_microdados_csv_2011_ts_item.parquet` · 518 rows · 8 columns

Raw do microdado CSV TS_ITEM.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

**Feeds:** `trusted/inep_saeb_microdados_item`

| Column | Type | Description |
|---|---|---|
| `ID_SERIE` | STRING | Código identificador da série/ano escolar avaliado (ex: 5 para 5º ano do Ensino Fundamental). — descrição gerada por IA. |
| `DISCIPLINA` | STRING | Sigla da disciplina avaliada no teste (ex: LP para Língua Portuguesa). — descrição gerada por IA. |
| `ID_SERIE_ITEM` | STRING | Código de relacionamento entre a série escolar e o item da avaliação. — descrição gerada por IA. |
| `ID_BLOCO` | STRING | Número do bloco de questões ao qual o item pertence no caderno de prova. — descrição gerada por IA. |
| `ID_POSICAO` | STRING | Ordem sequencial de exibição do item dentro do bloco de questões. — descrição gerada por IA. |
| `ID_ITEM` | STRING | Identificador único da questão (item) no banco de itens de avaliação. — descrição gerada por IA. |
| `ID_DESCRITOR` | STRING | Código da habilidade/competência avaliada segundo a Matriz de Referência (ex: Matriz SAEB/INEP). — descrição gerada por IA. |
| `GABARITO` | STRING | Letra indicativa da alternativa correta da questão (ex: A, B, C, D). — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2011_ts_pesos

File `raw__inep_saeb_microdados_csv_2011_ts_pesos.parquet` · 184,518 rows · 14 columns

Raw do microdado CSV TS_PESOS.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do SAEB (ex: 2011). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do estado (Unidade Federativa) onde se localiza a escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE de 7 dígitos do município da escola. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação única da escola no Censo Escolar. — descrição gerada por IA. |
| `ID_DEPENDENCIA_ADM` | STRING | Código da dependência administrativa da escola (ex: 2-Estadual, 3-Municipal). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da zona escolar (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_CAPITAL` | STRING | Indicador se o município é a capital do estado (1-Sim, 2-Não). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma na base do SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano do Ensino Fundamental avaliado (ex: 5 para 5º ano, 9 para 9º ano). — descrição gerada por IA. |
| `PARTICIPANTES_ESCOLA` | STRING | Total de alunos que participaram da prova na escola para a respectiva série. — descrição gerada por IA. |
| `PESO_ESCOLA` | STRING | Peso estatístico amostral atribuído à escola pelo INEP. — descrição gerada por IA. |
| `PARTICIPANTES_TURMA` | STRING | Total de alunos que efetivamente realizaram a prova naquela turma específica. — descrição gerada por IA. |
| `PESO_TURMA` | STRING | Peso estatístico amostral atribuído à turma pelo INEP. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2011_ts_quest_diretor

File `raw__inep_saeb_microdados_csv_2011_ts_quest_diretor.parquet` · 58,960 rows · 221 columns

Raw do microdado CSV TS_QUEST_DIRETOR.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização do exame SAEB (ex: 2011). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica do IBGE onde a escola está localizada. — descrição gerada por IA. |
| `ID_UF` | STRING | Código da Unidade Federativa (UF) do IBGE. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código do município no IBGE onde a escola está situada. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (Censo Escolar) de identificação da escola. — descrição gerada por IA. |
| `ID_DEPENDENCIA_ADM` | STRING | Código da dependência administrativa da escola (1-Federal, 2-Estadual, 3-Municipal, 4-Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código do tipo de localização da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_CAPITAL` | STRING | Código indicativo de localização da escola em município capital. — descrição gerada por IA. |
| `IN_PREENCHIMENTO` | STRING | Indicador do status de preenchimento do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta assinalada para a pergunta Q001 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta assinalada para a pergunta Q002 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta assinalada para a pergunta Q003 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta assinalada para a pergunta Q004 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta assinalada para a pergunta Q005 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta assinalada para a pergunta Q006 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta assinalada para a pergunta Q007 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta assinalada para a pergunta Q008 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta assinalada para a pergunta Q009 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta assinalada para a pergunta Q010 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta assinalada para a pergunta Q011 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta assinalada para a pergunta Q012 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta assinalada para a pergunta Q013 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta assinalada para a pergunta Q014 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta assinalada para a pergunta Q015 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta assinalada para a pergunta Q016 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta assinalada para a pergunta Q017 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta assinalada para a pergunta Q018 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta assinalada para a pergunta Q019 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta assinalada para a pergunta Q020 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta assinalada para a pergunta Q021 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta assinalada para a pergunta Q022 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta assinalada para a pergunta Q023 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta assinalada para a pergunta Q024 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta assinalada para a pergunta Q025 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta assinalada para a pergunta Q026 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta assinalada para a pergunta Q027 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta assinalada para a pergunta Q028 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta assinalada para a pergunta Q029 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta assinalada para a pergunta Q030 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta assinalada para a pergunta Q031 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta assinalada para a pergunta Q032 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta assinalada para a pergunta Q033 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta assinalada para a pergunta Q034 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta assinalada para a pergunta Q035 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta assinalada para a pergunta Q036 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta assinalada para a pergunta Q037 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta assinalada para a pergunta Q038 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta assinalada para a pergunta Q039 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta assinalada para a pergunta Q040 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta assinalada para a pergunta Q041 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta assinalada para a pergunta Q042 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta assinalada para a pergunta Q043 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta assinalada para a pergunta Q044 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta assinalada para a pergunta Q045 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta assinalada para a pergunta Q046 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta assinalada para a pergunta Q047 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta assinalada para a pergunta Q048 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta assinalada para a pergunta Q049 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta assinalada para a pergunta Q050 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta assinalada para a pergunta Q051 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta assinalada para a pergunta Q052 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta assinalada para a pergunta Q053 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta assinalada para a pergunta Q054 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta assinalada para a pergunta Q055 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta assinalada para a pergunta Q056 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta assinalada para a pergunta Q057 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta assinalada para a pergunta Q058 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta assinalada para a pergunta Q059 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta assinalada para a pergunta Q060 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta assinalada para a pergunta Q061 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta assinalada para a pergunta Q062 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta assinalada para a pergunta Q063 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta assinalada para a pergunta Q064 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta assinalada para a pergunta Q065 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta assinalada para a pergunta Q066 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta assinalada para a pergunta Q067 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta assinalada para a pergunta Q068 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta assinalada para a pergunta Q069 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta assinalada para a pergunta Q070 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta assinalada para a pergunta Q071 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta assinalada para a pergunta Q072 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta assinalada para a pergunta Q073 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta assinalada para a pergunta Q074 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Resposta assinalada para a pergunta Q075 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Resposta assinalada para a pergunta Q076 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Resposta assinalada para a pergunta Q077 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Resposta assinalada para a pergunta Q078 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Resposta assinalada para a pergunta Q079 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Resposta assinalada para a pergunta Q080 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Resposta assinalada para a pergunta Q081 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Resposta assinalada para a pergunta Q082 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Resposta assinalada para a pergunta Q083 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Resposta assinalada para a pergunta Q084 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Resposta assinalada para a pergunta Q085 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Resposta assinalada para a pergunta Q086 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Resposta assinalada para a pergunta Q087 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Resposta assinalada para a pergunta Q088 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Resposta assinalada para a pergunta Q089 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Resposta assinalada para a pergunta Q090 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Resposta assinalada para a pergunta Q091 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Resposta assinalada para a pergunta Q092 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Resposta assinalada para a pergunta Q093 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Resposta assinalada para a pergunta Q094 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Resposta assinalada para a pergunta Q095 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Resposta assinalada para a pergunta Q096 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Resposta assinalada para a pergunta Q097 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Resposta assinalada para a pergunta Q098 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Resposta assinalada para a pergunta Q099 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Resposta assinalada para a pergunta Q100 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Resposta assinalada para a pergunta Q101 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Resposta assinalada para a pergunta Q102 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Resposta assinalada para a pergunta Q103 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Resposta assinalada para a pergunta Q104 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Resposta assinalada para a pergunta Q105 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Resposta assinalada para a pergunta Q106 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Resposta assinalada para a pergunta Q107 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Resposta assinalada para a pergunta Q108 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Resposta assinalada para a pergunta Q109 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Resposta assinalada para a pergunta Q110 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Resposta assinalada para a pergunta Q111 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Resposta assinalada para a pergunta Q112 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Resposta assinalada para a pergunta Q113 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Resposta assinalada para a pergunta Q114 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Resposta assinalada para a pergunta Q115 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Resposta assinalada para a pergunta Q116 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Resposta assinalada para a pergunta Q117 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Resposta assinalada para a pergunta Q118 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Resposta assinalada para a pergunta Q119 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Resposta assinalada para a pergunta Q120 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Resposta assinalada para a pergunta Q121 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q122` | STRING | Resposta assinalada para a pergunta Q122 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q123` | STRING | Resposta assinalada para a pergunta Q123 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q124` | STRING | Resposta assinalada para a pergunta Q124 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q125` | STRING | Resposta assinalada para a pergunta Q125 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q126` | STRING | Resposta assinalada para a pergunta Q126 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q127` | STRING | Resposta assinalada para a pergunta Q127 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q128` | STRING | Resposta assinalada para a pergunta Q128 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q129` | STRING | Resposta assinalada para a pergunta Q129 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q130` | STRING | Resposta assinalada para a pergunta Q130 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q131` | STRING | Resposta assinalada para a pergunta Q131 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q132` | STRING | Resposta assinalada para a pergunta Q132 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q133` | STRING | Resposta assinalada para a pergunta Q133 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q134` | STRING | Resposta assinalada para a pergunta Q134 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q135` | STRING | Resposta assinalada para a pergunta Q135 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q136` | STRING | Resposta assinalada para a pergunta Q136 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q137` | STRING | Resposta assinalada para a pergunta Q137 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q138` | STRING | Resposta assinalada para a pergunta Q138 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q139` | STRING | Resposta assinalada para a pergunta Q139 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q140` | STRING | Resposta assinalada para a pergunta Q140 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q141` | STRING | Resposta assinalada para a pergunta Q141 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q142` | STRING | Resposta assinalada para a pergunta Q142 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q143` | STRING | Resposta assinalada para a pergunta Q143 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q144` | STRING | Resposta assinalada para a pergunta Q144 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q145` | STRING | Resposta assinalada para a pergunta Q145 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q146` | STRING | Resposta assinalada para a pergunta Q146 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q147` | STRING | Resposta assinalada para a pergunta Q147 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q148` | STRING | Resposta assinalada para a pergunta Q148 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q149` | STRING | Resposta assinalada para a pergunta Q149 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q150` | STRING | Resposta assinalada para a pergunta Q150 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q151` | STRING | Resposta assinalada para a pergunta Q151 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q152` | STRING | Resposta assinalada para a pergunta Q152 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q153` | STRING | Resposta assinalada para a pergunta Q153 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q154` | STRING | Resposta assinalada para a pergunta Q154 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q155` | STRING | Resposta assinalada para a pergunta Q155 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q156` | STRING | Resposta assinalada para a pergunta Q156 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q157` | STRING | Resposta assinalada para a pergunta Q157 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q158` | STRING | Resposta assinalada para a pergunta Q158 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q159` | STRING | Resposta assinalada para a pergunta Q159 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q160` | STRING | Resposta assinalada para a pergunta Q160 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q161` | STRING | Resposta assinalada para a pergunta Q161 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q162` | STRING | Resposta assinalada para a pergunta Q162 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q163` | STRING | Resposta assinalada para a pergunta Q163 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q164` | STRING | Resposta assinalada para a pergunta Q164 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q165` | STRING | Resposta assinalada para a pergunta Q165 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q166` | STRING | Resposta assinalada para a pergunta Q166 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q167` | STRING | Resposta assinalada para a pergunta Q167 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q168` | STRING | Resposta assinalada para a pergunta Q168 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q169` | STRING | Resposta assinalada para a pergunta Q169 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q170` | STRING | Resposta assinalada para a pergunta Q170 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q171` | STRING | Resposta assinalada para a pergunta Q171 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q172` | STRING | Resposta assinalada para a pergunta Q172 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q173` | STRING | Resposta assinalada para a pergunta Q173 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q174` | STRING | Resposta assinalada para a pergunta Q174 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q175` | STRING | Resposta assinalada para a pergunta Q175 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q176` | STRING | Resposta assinalada para a pergunta Q176 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q177` | STRING | Resposta assinalada para a pergunta Q177 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q178` | STRING | Resposta assinalada para a pergunta Q178 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q179` | STRING | Resposta assinalada para a pergunta Q179 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q180` | STRING | Resposta assinalada para a pergunta Q180 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q181` | STRING | Resposta assinalada para a pergunta Q181 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q182` | STRING | Resposta assinalada para a pergunta Q182 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q183` | STRING | Resposta assinalada para a pergunta Q183 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q184` | STRING | Resposta assinalada para a pergunta Q184 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q185` | STRING | Resposta assinalada para a pergunta Q185 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q186` | STRING | Resposta assinalada para a pergunta Q186 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q187` | STRING | Resposta assinalada para a pergunta Q187 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q188` | STRING | Resposta assinalada para a pergunta Q188 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q189` | STRING | Resposta assinalada para a pergunta Q189 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q190` | STRING | Resposta assinalada para a pergunta Q190 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q191` | STRING | Resposta assinalada para a pergunta Q191 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q192` | STRING | Resposta assinalada para a pergunta Q192 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q193` | STRING | Resposta assinalada para a pergunta Q193 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q194` | STRING | Resposta assinalada para a pergunta Q194 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q195` | STRING | Resposta assinalada para a pergunta Q195 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q196` | STRING | Resposta assinalada para a pergunta Q196 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q197` | STRING | Resposta assinalada para a pergunta Q197 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q198` | STRING | Resposta assinalada para a pergunta Q198 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q199` | STRING | Resposta assinalada para a pergunta Q199 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q200` | STRING | Resposta assinalada para a pergunta Q200 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q201` | STRING | Resposta assinalada para a pergunta Q201 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q202` | STRING | Resposta assinalada para a pergunta Q202 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q203` | STRING | Resposta assinalada para a pergunta Q203 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q204` | STRING | Resposta assinalada para a pergunta Q204 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q205` | STRING | Resposta assinalada para a pergunta Q205 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q206` | STRING | Resposta assinalada para a pergunta Q206 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q207` | STRING | Resposta assinalada para a pergunta Q207 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q208` | STRING | Resposta assinalada para a pergunta Q208 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q209` | STRING | Resposta assinalada para a pergunta Q209 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q210` | STRING | Resposta assinalada para a pergunta Q210 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q211` | STRING | Resposta assinalada para a pergunta Q211 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q212` | STRING | Resposta assinalada para a pergunta Q212 do questionário contextual. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2011_ts_quest_escola

File `raw__inep_saeb_microdados_csv_2011_ts_quest_escola.parquet` · 58,960 rows · 75 columns

Raw do microdado CSV TS_QUEST_ESCOLA.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

**Feeds:** `trusted/inep_saeb_microdados_escola`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano/edição do ciclo de avaliação do SAEB (ex: 2011). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico da região geográfica da escola (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE de 2 dígitos do estado (UF) da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE de 7 dígitos do município da escola. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação única da escola. — descrição gerada por IA. |
| `ID_DEPENDENCIA_ADM` | STRING | Código da dependência administrativa da escola (1-Federal, 2-Estadual, 3-Municipal, 4-Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código da localização da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_CAPITAL` | STRING | Indicador se a escola está na capital do estado (1-Capital, 2-Interior). — descrição gerada por IA. |
| `IN_PREENCHIMENTO` | STRING | Indicador de preenchimento do questionário (1-Preenchido, 0-Não preenchido). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta assinalada na Questão 1 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta assinalada na Questão 2 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta assinalada na Questão 3 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta assinalada na Questão 4 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta assinalada na Questão 5 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta assinalada na Questão 6 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta assinalada na Questão 7 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta assinalada na Questão 8 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta assinalada na Questão 9 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta assinalada na Questão 10 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta assinalada na Questão 11 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta assinalada na Questão 12 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta assinalada na Questão 13 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta assinalada na Questão 14 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta assinalada na Questão 15 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta assinalada na Questão 16 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta assinalada na Questão 17 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta assinalada na Questão 18 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta assinalada na Questão 19 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta assinalada na Questão 20 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta assinalada na Questão 21 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta assinalada na Questão 22 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta assinalada na Questão 23 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta assinalada na Questão 24 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta assinalada na Questão 25 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta assinalada na Questão 26 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta assinalada na Questão 27 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta assinalada na Questão 28 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta assinalada na Questão 29 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta assinalada na Questão 30 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta assinalada na Questão 31 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta assinalada na Questão 32 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta assinalada na Questão 33 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta assinalada na Questão 34 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta assinalada na Questão 35 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta assinalada na Questão 36 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta assinalada na Questão 37 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta assinalada na Questão 38 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta assinalada na Questão 39 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta assinalada na Questão 40 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta assinalada na Questão 41 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta assinalada na Questão 42 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta assinalada na Questão 43 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta assinalada na Questão 44 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta assinalada na Questão 45 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta assinalada na Questão 46 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta assinalada na Questão 47 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta assinalada na Questão 48 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta assinalada na Questão 49 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta assinalada na Questão 50 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta assinalada na Questão 51 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta assinalada na Questão 52 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta assinalada na Questão 53 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta assinalada na Questão 54 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta assinalada na Questão 55 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta assinalada na Questão 56 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta assinalada na Questão 57 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta assinalada na Questão 58 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta assinalada na Questão 59 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta assinalada na Questão 60 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta assinalada na Questão 61 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta assinalada na Questão 62 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta assinalada na Questão 63 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta assinalada na Questão 64 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta assinalada na Questão 65 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta assinalada na Questão 66 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2011_ts_quest_professor

File `raw__inep_saeb_microdados_csv_2011_ts_quest_professor.parquet` · 316,668 rows · 163 columns

Raw do microdado CSV TS_QUEST_PROFESSOR.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano/Edição de realização da avaliação do SAEB (ex: 2011). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do estado (Unidade da Federação) da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP/Censo Escolar de identificação da escola. — descrição gerada por IA. |
| `ID_DEPENDENCIA_ADM` | STRING | Código da dependência administrativa da escola (1: Federal, 2: Estadual, 3: Municipal, 4: Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código da localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_CAPITAL` | STRING | Indicador se a escola está localizada na capital do estado (1: Sim, 2: Não). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma avaliada. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código correspondente à série/ano escolar avaliado (ex: 5 para 5º ano do EF). — descrição gerada por IA. |
| `IN_PREENCHIMENTO` | STRING | Indicador de preenchimento do questionário contextual (1: Preenchido, 0: Não preenchido). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta assinalada para a questão 1 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta assinalada para a questão 2 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta assinalada para a questão 3 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta assinalada para a questão 4 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta assinalada para a questão 5 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta assinalada para a questão 6 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta assinalada para a questão 7 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta assinalada para a questão 8 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta assinalada para a questão 9 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta assinalada para a questão 10 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta assinalada para a questão 11 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta assinalada para a questão 12 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta assinalada para a questão 13 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta assinalada para a questão 14 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta assinalada para a questão 15 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta assinalada para a questão 16 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta assinalada para a questão 17 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta assinalada para a questão 18 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta assinalada para a questão 19 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta assinalada para a questão 20 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta assinalada para a questão 21 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta assinalada para a questão 22 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta assinalada para a questão 23 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta assinalada para a questão 24 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta assinalada para a questão 25 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta assinalada para a questão 26 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta assinalada para a questão 27 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta assinalada para a questão 28 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta assinalada para a questão 29 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta assinalada para a questão 30 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta assinalada para a questão 31 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta assinalada para a questão 32 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta assinalada para a questão 33 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta assinalada para a questão 34 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta assinalada para a questão 35 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta assinalada para a questão 36 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta assinalada para a questão 37 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta assinalada para a questão 38 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta assinalada para a questão 39 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta assinalada para a questão 40 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta assinalada para a questão 41 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta assinalada para a questão 42 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta assinalada para a questão 43 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta assinalada para a questão 44 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta assinalada para a questão 45 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta assinalada para a questão 46 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta assinalada para a questão 47 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta assinalada para a questão 48 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta assinalada para a questão 49 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta assinalada para a questão 50 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta assinalada para a questão 51 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta assinalada para a questão 52 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta assinalada para a questão 53 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta assinalada para a questão 54 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta assinalada para a questão 55 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta assinalada para a questão 56 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta assinalada para a questão 57 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta assinalada para a questão 58 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta assinalada para a questão 59 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta assinalada para a questão 60 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta assinalada para a questão 61 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta assinalada para a questão 62 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta assinalada para a questão 63 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta assinalada para a questão 64 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta assinalada para a questão 65 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta assinalada para a questão 66 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta assinalada para a questão 67 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta assinalada para a questão 68 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta assinalada para a questão 69 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta assinalada para a questão 70 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta assinalada para a questão 71 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta assinalada para a questão 72 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta assinalada para a questão 73 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta assinalada para a questão 74 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Resposta assinalada para a questão 75 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Resposta assinalada para a questão 76 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Resposta assinalada para a questão 77 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Resposta assinalada para a questão 78 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Resposta assinalada para a questão 79 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Resposta assinalada para a questão 80 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Resposta assinalada para a questão 81 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Resposta assinalada para a questão 82 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Resposta assinalada para a questão 83 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Resposta assinalada para a questão 84 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Resposta assinalada para a questão 85 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Resposta assinalada para a questão 86 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Resposta assinalada para a questão 87 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Resposta assinalada para a questão 88 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Resposta assinalada para a questão 89 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Resposta assinalada para a questão 90 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Resposta assinalada para a questão 91 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Resposta assinalada para a questão 92 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Resposta assinalada para a questão 93 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Resposta assinalada para a questão 94 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Resposta assinalada para a questão 95 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Resposta assinalada para a questão 96 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Resposta assinalada para a questão 97 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Resposta assinalada para a questão 98 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Resposta assinalada para a questão 99 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Resposta assinalada para a questão 100 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Resposta assinalada para a questão 101 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Resposta assinalada para a questão 102 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Resposta assinalada para a questão 103 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Resposta assinalada para a questão 104 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Resposta assinalada para a questão 105 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Resposta assinalada para a questão 106 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Resposta assinalada para a questão 107 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Resposta assinalada para a questão 108 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Resposta assinalada para a questão 109 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Resposta assinalada para a questão 110 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Resposta assinalada para a questão 111 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Resposta assinalada para a questão 112 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Resposta assinalada para a questão 113 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Resposta assinalada para a questão 114 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Resposta assinalada para a questão 115 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Resposta assinalada para a questão 116 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Resposta assinalada para a questão 117 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Resposta assinalada para a questão 118 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Resposta assinalada para a questão 119 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Resposta assinalada para a questão 120 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Resposta assinalada para a questão 121 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q122` | STRING | Resposta assinalada para a questão 122 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q123` | STRING | Resposta assinalada para a questão 123 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q124` | STRING | Resposta assinalada para a questão 124 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q125` | STRING | Resposta assinalada para a questão 125 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q126` | STRING | Resposta assinalada para a questão 126 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q127` | STRING | Resposta assinalada para a questão 127 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q128` | STRING | Resposta assinalada para a questão 128 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q129` | STRING | Resposta assinalada para a questão 129 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q130` | STRING | Resposta assinalada para a questão 130 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q131` | STRING | Resposta assinalada para a questão 131 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q132` | STRING | Resposta assinalada para a questão 132 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q133` | STRING | Resposta assinalada para a questão 133 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q134` | STRING | Resposta assinalada para a questão 134 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q135` | STRING | Resposta assinalada para a questão 135 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q136` | STRING | Resposta assinalada para a questão 136 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q137` | STRING | Resposta assinalada para a questão 137 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q138` | STRING | Resposta assinalada para a questão 138 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q139` | STRING | Resposta assinalada para a questão 139 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q140` | STRING | Resposta assinalada para a questão 140 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q141` | STRING | Resposta assinalada para a questão 141 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q142` | STRING | Resposta assinalada para a questão 142 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q143` | STRING | Resposta assinalada para a questão 143 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q144` | STRING | Resposta assinalada para a questão 144 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q145` | STRING | Resposta assinalada para a questão 145 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q146` | STRING | Resposta assinalada para a questão 146 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q147` | STRING | Resposta assinalada para a questão 147 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q148` | STRING | Resposta assinalada para a questão 148 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q149` | STRING | Resposta assinalada para a questão 149 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q150` | STRING | Resposta assinalada para a questão 150 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q151` | STRING | Resposta assinalada para a questão 151 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q152` | STRING | Resposta assinalada para a questão 152 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2011_ts_resultado_brasil

File `raw__inep_saeb_microdados_csv_2011_ts_resultado_brasil.parquet` · 162 rows · 10 columns

Raw do microdado CSV TS_RESULTADO_BRASIL.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano ou edição de realização da avaliação do SAEB (ex: 2011). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série ou ano escolar avaliado (ex: 5 para 5º ano do Ensino Fundamental). — descrição gerada por IA. |
| `ID_TIPO_REDE` | STRING | Código do tipo de rede de ensino (ex: pública, privada ou total). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código da localização da escola (ex: urbana, rural ou total). — descrição gerada por IA. |
| `ID_CAPITAL` | STRING | Código indicador de capital ou interior (ex: capital, interior ou total). — descrição gerada por IA. |
| `NU_PARTICIPANTES` | STRING | Quantidade total de estudantes que participaram da avaliação no recorte. — descrição gerada por IA. |
| `MEDIA_LP` | STRING | Nota/proficiência média em Língua Portuguesa na escala SAEB (formato numérico com vírgula). — descrição gerada por IA. |
| `MEDIA_MT` | STRING | Nota/proficiência média em Matemática na escala SAEB (formato numérico com vírgula). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da média de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da média de proficiência em Matemática. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2011_ts_resultado_escola

File `raw__inep_saeb_microdados_csv_2011_ts_resultado_escola.parquet` · 72,808 rows · 15 columns

Raw do microdado CSV TS_RESULTADO_ESCOLA.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do exame SAEB (ex: '2011'). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código IBGE identificador da região geográfica da escola. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação (UF) onde a escola se localiza. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município de localização da escola. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (código de 8 dígitos) que identifica unicamente a escola. — descrição gerada por IA. |
| `ID_DEPENDENCIA_ADM` | STRING | Código da dependência administrativa (1: Federal, 2: Estadual, 3: Municipal, 4: Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_CAPITAL` | STRING | Indicador se a escola fica na capital do estado (1: Sim, 2: Não). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar avaliado na aplicação (ex: 5 para 5º ano, 9 para 9º ano). — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO` | STRING | Número total de alunos matriculados na série de acordo com o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES` | STRING | Número total de alunos que efetivamente compareceram e realizaram a prova. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO` | STRING | Percentual de alunos presentes em relação aos matriculados (em %). — descrição gerada por IA. |
| `ID_DIVULGACAO` | STRING | Indicador de liberação/divulgação pública dos resultados (1: Divulgado, 0: Não divulgado). — descrição gerada por IA. |
| `MEDIA_LP` | STRING | Nota média alcançada pelos alunos da escola na prova de Língua Portuguesa (escala SAEB). — descrição gerada por IA. |
| `MEDIA_MT` | STRING | Nota média alcançada pelos alunos da escola na prova de Matemática (escala SAEB). — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2011_ts_resultado_municipio

File `raw__inep_saeb_microdados_csv_2011_ts_resultado_municipio.parquet` · 60,608 rows · 18 columns

Raw do microdado CSV TS_RESULTADO_MUNICIPIO.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do SAEB (ex: 2011). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código identificador da região geográfica (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `SIGLA_UF` | STRING | Sigla da Unidade Federativa do município. — descrição gerada por IA. |
| `ID_UF` | STRING | Código numérico do IBGE correspondente à Unidade Federativa. — descrição gerada por IA. |
| `NOME_MUNICIPIO` | STRING | Nome do município de referência. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município (7 dígitos). — descrição gerada por IA. |
| `ID_TIPO_REDE` | STRING | Código do tipo de rede administrativa de ensino (ex: 2-Estadual, 3-Municipal, 5-Pública total). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da zona escolar (1-Urbana, 2-Rural, 0-Total). — descrição gerada por IA. |
| `ID_CAPITAL` | STRING | Indicador se o município é capital do estado (1-Sim, 2-Não). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar avaliado (ex: 5 para 5º ano, 9 para 9º ano do Ensino Fundamental). — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO` | STRING | Quantidade total de alunos matriculados na série/ano segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES` | STRING | Quantidade de alunos que realizaram as provas do SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO` | STRING | Percentual de alunos presentes na prova em relação aos matriculados (%). — descrição gerada por IA. |
| `ID_DIVULGACAO` | STRING | Código que indica se o resultado atendeu ao critério mínimo para divulgação oficial (1-Divulgado, 0-Não divulgado). — descrição gerada por IA. |
| `MEDIA_LP` | STRING | Nota média dos alunos na avaliação de Língua Portuguesa (escala SAEB). — descrição gerada por IA. |
| `MEDIA_MT` | STRING | Nota média dos alunos na avaliação de Matemática (escala SAEB). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da média estimada para a prova de Língua Portuguesa. — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da média estimada para a prova de Matemática. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2011_ts_resultado_regiao

File `raw__inep_saeb_microdados_csv_2011_ts_resultado_regiao.parquet` · 810 rows · 11 columns

Raw do microdado CSV TS_RESULTADO_REGIAO.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de edição da avaliação do SAEB (ex: '2011'), utilizado no acompanhamento histórico do desempenho. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico da região geográfica brasileira (ex: '1' para Região Norte), usado para filtros e análises regionais. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código identificador da série/ano escolar avaliado (ex: '12' para o 3º ano do Ensino Médio). — descrição gerada por IA. |
| `ID_TIPO_REDE` | STRING | Código que identifica a dependência administrativa da rede de ensino (pública, privada, estadual, municipal ou total). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código do tipo de localização da escola (ex: urbana, rural ou total). — descrição gerada por IA. |
| `ID_CAPITAL` | STRING | Indicador que sinaliza se o agregado se refere a capitais, interior ou total do estado/região. — descrição gerada por IA. |
| `NU_PARTICIPANTES` | STRING | Quantidade total de estudantes que efetivamente realizaram a prova do SAEB no agrupamento. — descrição gerada por IA. |
| `MEDIA_LP` | STRING | Pontuação média obtida pelos estudantes em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `MEDIA_MT` | STRING | Pontuação média obtida pelos estudantes em Matemática na escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão amostral associado à estimativa da média de Língua Portuguesa. — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão amostral associado à estimativa da média de Matemática. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2011_ts_resultado_uf

File `raw__inep_saeb_microdados_csv_2011_ts_resultado_uf.parquet` · 4,374 rows · 13 columns

Raw do microdado CSV TS_RESULTADO_UF.csv do Saeb 2011, arquivo oficial microdados_saeb_2011.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano ou edição de realização do exame do SAEB (ex: '2011'). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico identificador da região geográfica brasileira (ex: '1' para Norte). — descrição gerada por IA. |
| `SIGLA_UF` | STRING | Sigla de duas letras da Unidade da Federação (ex: 'RO'). — descrição gerada por IA. |
| `ID_UF` | STRING | Código numérico do IBGE/INEP referente ao Estado (ex: '11'). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série ou ano escolar avaliado (ex: '5' para 5º ano, '9' para 9º ano, '12' para 3º ano do Ensino Médio). — descrição gerada por IA. |
| `ID_TIPO_REDE` | STRING | Código numérico da rede de ensino/dependência administrativa (ex: '0' para Total). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código numérico da localização da zona escolar (ex: '0' para Total). — descrição gerada por IA. |
| `ID_CAPITAL` | STRING | Indicador numérico de abrangência da capital (ex: '1' para Capital, '0' para Total/Outros). — descrição gerada por IA. |
| `NU_PARTICIPANTES` | STRING | Número total de alunos participantes que realizaram a prova no agrupamento. — descrição gerada por IA. |
| `MEDIA_LP` | STRING | Média de proficiência dos alunos na prova de Língua Portuguesa (escala SAEB, ex: '184,62'). — descrição gerada por IA. |
| `MEDIA_MT` | STRING | Média de proficiência dos alunos na prova de Matemática (escala SAEB, ex: '202,43'). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da estimativa da média em Língua Portuguesa. — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da estimativa da média em Matemática. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2013_ts_aluno_3em

File `raw__inep_saeb_microdados_csv_2013_ts_aluno_3em.parquet` · 150,429 rows · 94 columns

Raw do microdado CSV TS_ALUNO_3EM.csv do Saeb 2013, arquivo oficial microdados_saeb_2013.zip.

**Feeds:** `raw/inep_saeb_aluno_2013`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de realização da edição da Prova Brasil/SAEB. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico da região geográfica da escola do aluno. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação (Estado). — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código do tipo de área da escola (ex: Capital, Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola pertence à rede pública de ensino (1=Sim, 0=Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código da localização da escola (1=Urbana, 2=Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma do aluno. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código identificador da série/ano escolar avaliado. — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Código identificador único do aluno no exame. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador da situação de matrícula do aluno no Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador de presença/preenchimento da prova pelo aluno (1=Sim, 0=Não). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Identificador do caderno de prova atribuído ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Identificador do primeiro bloco de itens do caderno. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Identificador do segundo bloco de itens do caderno. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | String com a sequência de respostas marcadas no Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | String com a sequência de respostas marcadas no Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | String com a sequência de respostas marcadas no Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | String com a sequência de respostas marcadas no Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador se o aluno obteve cálculo de proficiência válido (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Indicador se a participação do aluno atende aos critérios da Prova Brasil (1=Sim, 0=Não). — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da ANEB/SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostracional do aluno para estatísticas de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostracional do aluno para estatísticas de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência do aluno em Língua Portuguesa na escala Prova Brasil. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP` | STRING | Desvio padrão/erro de medida da proficiência de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota de proficiência do aluno em Língua Portuguesa alinhada à escala SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP_SAEB` | STRING | Desvio padrão da proficiência de Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência do aluno em Matemática na escala Prova Brasil. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT` | STRING | Desvio padrão/erro de medida da proficiência de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota de proficiência do aluno em Matemática alinhada à escala SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT_SAEB` | STRING | Desvio padrão da proficiência de Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário do aluno (1=Sim, 0=Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta do aluno ao item 1 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta do aluno ao item 2 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta do aluno ao item 3 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta do aluno ao item 4 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta do aluno ao item 5 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta do aluno ao item 6 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta do aluno ao item 7 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta do aluno ao item 8 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta do aluno ao item 9 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta do aluno ao item 10 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta do aluno ao item 11 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta do aluno ao item 12 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta do aluno ao item 13 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta do aluno ao item 14 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta do aluno ao item 15 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta do aluno ao item 16 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta do aluno ao item 17 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta do aluno ao item 18 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta do aluno ao item 19 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta do aluno ao item 20 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta do aluno ao item 21 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta do aluno ao item 22 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta do aluno ao item 23 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta do aluno ao item 24 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta do aluno ao item 25 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta do aluno ao item 26 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta do aluno ao item 27 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta do aluno ao item 28 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta do aluno ao item 29 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta do aluno ao item 30 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta do aluno ao item 31 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta do aluno ao item 32 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta do aluno ao item 33 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta do aluno ao item 34 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta do aluno ao item 35 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta do aluno ao item 36 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta do aluno ao item 37 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta do aluno ao item 38 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta do aluno ao item 39 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta do aluno ao item 40 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta do aluno ao item 41 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta do aluno ao item 42 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta do aluno ao item 43 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta do aluno ao item 44 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta do aluno ao item 45 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta do aluno ao item 46 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta do aluno ao item 47 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta do aluno ao item 48 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta do aluno ao item 49 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta do aluno ao item 50 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta do aluno ao item 51 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta do aluno ao item 52 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta do aluno ao item 53 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta do aluno ao item 54 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta do aluno ao item 55 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta do aluno ao item 56 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta do aluno ao item 57 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta do aluno ao item 58 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta do aluno ao item 59 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta do aluno ao item 60 do questionário socioeconômico. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2013_ts_aluno_5ef

File `raw__inep_saeb_microdados_csv_2013_ts_aluno_5ef.parquet` · 2,524,125 rows · 85 columns

Raw do microdado CSV TS_ALUNO_5EF.csv do Saeb 2013, arquivo oficial microdados_saeb_2013.zip.

**Feeds:** `raw/inep_saeb_aluno_2013`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de realização da edição da Prova Brasil / SAEB (ex: 2013). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola do aluno (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do estado (Unidade da Federação) onde a escola está localizada. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola do aluno. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código da área de localização da escola (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola é da rede pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma no Censo Escolar. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar avaliado (ex: 5 para 5º ano do Ensino Fundamental). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único e anonimizado do aluno na avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno conforme o Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador se o aluno preencheu a prova (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Número/código do caderno de teste aplicado ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Código identificador do primeiro bloco de itens de teste do caderno. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Código identificador do segundo bloco de itens de teste do caderno. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | String com as alternativas marcadas pelo aluno no Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | String com as alternativas marcadas pelo aluno no Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | String com as alternativas marcadas pelo aluno no Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | String com as alternativas marcadas pelo aluno no Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador de presença do cálculo de proficiência do aluno (1: Possui proficiência, 0: Não possui). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Indicador de inclusão do aluno na amostra da Prova Brasil (1: Sim, 0: Não). — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da ANEB, quando aplicável. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para a expansão dos dados em Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para a expansão dos dados em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Proficiência estimada do aluno em Língua Portuguesa na escala padronizada (TRI). — descrição gerada por IA. |
| `DESVIO_PADRAO_LP` | STRING | Desvio padrão da estimativa da proficiência do aluno em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência do aluno em Língua Portuguesa transformada para a escala do SAEB (ex: 0 a 500). — descrição gerada por IA. |
| `DESVIO_PADRAO_LP_SAEB` | STRING | Desvio padrão da proficiência de Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Proficiência estimada do aluno em Matemática na escala padronizada (TRI). — descrição gerada por IA. |
| `DESVIO_PADRAO_MT` | STRING | Desvio padrão da estimativa da proficiência do aluno em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência do aluno em Matemática transformada para a escala do SAEB (ex: 0 a 500). — descrição gerada por IA. |
| `DESVIO_PADRAO_MT_SAEB` | STRING | Desvio padrão da proficiência de Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador se o aluno preencheu o questionário socioeconômico (1: Sim, 0: Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta da questão 1 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta da questão 2 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta da questão 3 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta da questão 4 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta da questão 5 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta da questão 6 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da questão 7 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta da questão 8 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta da questão 9 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta da questão 10 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da questão 11 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da questão 12 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da questão 13 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da questão 14 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da questão 15 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da questão 16 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta da questão 17 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta da questão 18 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta da questão 19 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta da questão 20 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta da questão 21 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta da questão 22 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta da questão 23 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta da questão 24 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta da questão 25 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta da questão 26 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta da questão 27 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta da questão 28 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta da questão 29 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta da questão 30 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta da questão 31 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta da questão 32 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta da questão 33 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta da questão 34 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta da questão 35 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta da questão 36 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta da questão 37 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta da questão 38 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta da questão 39 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta da questão 40 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta da questão 41 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta da questão 42 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta da questão 43 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta da questão 44 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta da questão 45 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta da questão 46 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta da questão 47 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta da questão 48 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta da questão 49 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta da questão 50 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta da questão 51 do questionário socioeconômico do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2013_ts_aluno_9ef

File `raw__inep_saeb_microdados_csv_2013_ts_aluno_9ef.parquet` · 2,720,588 rows · 91 columns

Raw do microdado CSV TS_ALUNO_9EF.csv do Saeb 2013, arquivo oficial microdados_saeb_2013.zip.

**Feeds:** `raw/inep_saeb_aluno_2013`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano da edição da Prova Brasil/SAEB (ex: 2013). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade Federativa da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código da área da escola (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de rede pública de ensino (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma no Censo Escolar. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar avaliado (ex: 5 para 5º ano, 9 para 9º ano). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único do aluno na avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação do aluno no Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador de preenchimento da prova pelo aluno (1: Preencheu, 0: Não preencheu). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Número do caderno de prova aplicado ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Identificador do primeiro bloco de itens do caderno. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Identificador do segundo bloco de itens do caderno. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | String com as respostas marcadas pelo aluno no Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | String com as respostas marcadas pelo aluno no Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | String com as respostas marcadas pelo aluno no Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | String com as respostas marcadas pelo aluno no Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador se o aluno possui cálculo de proficiência válido (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Indicador de inclusão no escopo da Prova Brasil (1: Sim, 0: Não). — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da ANEB. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno no teste de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno no teste de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota estimada de proficiência em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP` | STRING | Desvio padrão do erro de medida da proficiência de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência padronizada em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP_SAEB` | STRING | Desvio padrão da proficiência padronizada de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota estimada de proficiência em Matemática na escala SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT` | STRING | Desvio padrão do erro de medida da proficiência de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência padronizada em Matemática na escala SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT_SAEB` | STRING | Desvio padrão da proficiência padronizada de Matemática. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário do aluno (1: Preencheu, 0: Não preencheu). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta da questão 1 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta da questão 2 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta da questão 3 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta da questão 4 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta da questão 5 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta da questão 6 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da questão 7 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta da questão 8 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta da questão 9 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta da questão 10 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da questão 11 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da questão 12 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da questão 13 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da questão 14 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da questão 15 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da questão 16 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta da questão 17 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta da questão 18 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta da questão 19 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta da questão 20 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta da questão 21 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta da questão 22 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta da questão 23 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta da questão 24 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta da questão 25 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta da questão 26 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta da questão 27 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta da questão 28 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta da questão 29 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta da questão 30 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta da questão 31 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta da questão 32 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta da questão 33 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta da questão 34 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta da questão 35 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta da questão 36 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta da questão 37 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta da questão 38 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta da questão 39 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta da questão 40 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta da questão 41 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta da questão 42 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta da questão 43 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta da questão 44 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta da questão 45 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta da questão 46 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta da questão 47 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta da questão 48 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta da questão 49 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta da questão 50 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta da questão 51 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta da questão 52 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta da questão 53 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta da questão 54 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta da questão 55 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta da questão 56 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta da questão 57 do questionário socioeconômico do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2013_ts_diretor

File `raw__inep_saeb_microdados_csv_2013_ts_diretor.parquet` · 56,737 rows · 118 columns

Raw do microdado CSV TS_DIRETOR.csv do Saeb 2013, arquivo oficial microdados_saeb_2013.zip.

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de edição da Prova Brasil/SAEB (ex: 2013). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE de duas letras/dígitos referente à Unidade da Federação da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município de localização da escola. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (Censo Escolar) de identificação única da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador binário de dependência administrativa pública (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento/devolução do questionário contextual (1 = Preenchido, 0 = Não preenchido). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta assinalada para a questão 001 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta assinalada para a questão 002 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta assinalada para a questão 003 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta assinalada para a questão 004 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta assinalada para a questão 005 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta assinalada para a questão 006 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta assinalada para a questão 007 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta assinalada para a questão 008 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta assinalada para a questão 009 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta assinalada para a questão 010 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta assinalada para a questão 011 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta assinalada para a questão 012 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta assinalada para a questão 013 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta assinalada para a questão 014 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta assinalada para a questão 015 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta assinalada para a questão 016 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta assinalada para a questão 017 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta assinalada para a questão 018 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta assinalada para a questão 019 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta assinalada para a questão 020 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta assinalada para a questão 021 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta assinalada para a questão 022 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta assinalada para a questão 023 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta assinalada para a questão 024 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta assinalada para a questão 025 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta assinalada para a questão 026 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta assinalada para a questão 027 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta assinalada para a questão 028 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta assinalada para a questão 029 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta assinalada para a questão 030 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta assinalada para a questão 031 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta assinalada para a questão 032 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta assinalada para a questão 033 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta assinalada para a questão 034 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta assinalada para a questão 035 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta assinalada para a questão 036 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta assinalada para a questão 037 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta assinalada para a questão 038 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta assinalada para a questão 039 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta assinalada para a questão 040 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta assinalada para a questão 041 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta assinalada para a questão 042 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta assinalada para a questão 043 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta assinalada para a questão 044 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta assinalada para a questão 045 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta assinalada para a questão 046 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta assinalada para a questão 047 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta assinalada para a questão 048 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta assinalada para a questão 049 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta assinalada para a questão 050 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta assinalada para a questão 051 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta assinalada para a questão 052 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta assinalada para a questão 053 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta assinalada para a questão 054 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta assinalada para a questão 055 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta assinalada para a questão 056 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta assinalada para a questão 057 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta assinalada para a questão 058 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta assinalada para a questão 059 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta assinalada para a questão 060 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta assinalada para a questão 061 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta assinalada para a questão 062 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta assinalada para a questão 063 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta assinalada para a questão 064 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta assinalada para a questão 065 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta assinalada para a questão 066 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta assinalada para a questão 067 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta assinalada para a questão 068 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta assinalada para a questão 069 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta assinalada para a questão 070 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta assinalada para a questão 071 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta assinalada para a questão 072 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta assinalada para a questão 073 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta assinalada para a questão 074 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Resposta assinalada para a questão 075 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Resposta assinalada para a questão 076 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Resposta assinalada para a questão 077 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Resposta assinalada para a questão 078 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Resposta assinalada para a questão 079 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Resposta assinalada para a questão 080 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Resposta assinalada para a questão 081 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Resposta assinalada para a questão 082 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Resposta assinalada para a questão 083 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Resposta assinalada para a questão 084 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Resposta assinalada para a questão 085 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Resposta assinalada para a questão 086 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Resposta assinalada para a questão 087 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Resposta assinalada para a questão 088 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Resposta assinalada para a questão 089 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Resposta assinalada para a questão 090 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Resposta assinalada para a questão 091 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Resposta assinalada para a questão 092 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Resposta assinalada para a questão 093 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Resposta assinalada para a questão 094 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Resposta assinalada para a questão 095 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Resposta assinalada para a questão 096 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Resposta assinalada para a questão 097 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Resposta assinalada para a questão 098 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Resposta assinalada para a questão 099 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Resposta assinalada para a questão 100 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Resposta assinalada para a questão 101 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Resposta assinalada para a questão 102 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Resposta assinalada para a questão 103 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Resposta assinalada para a questão 104 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Resposta assinalada para a questão 105 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Resposta assinalada para a questão 106 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Resposta assinalada para a questão 107 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Resposta assinalada para a questão 108 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Resposta assinalada para a questão 109 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Resposta assinalada para a questão 110 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Resposta assinalada para a questão 111 do questionário contextual. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2013_ts_escola

File `raw__inep_saeb_microdados_csv_2013_ts_escola.parquet` · 59,251 rows · 127 columns

Raw do microdado CSV TS_ESCOLA.csv do Saeb 2013, arquivo oficial microdados_saeb_2013.zip.

**Feeds:** `trusted/inep_saeb_escola`, `trusted/inep_saeb_microdados_escola`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano ou edição da avaliação Prova Brasil/SAEB. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade Federativa (UF) da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (MEC) de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de escola pública (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_INICIAL` | STRING | Percentual de docentes com formação adequada nos anos iniciais (5º EF). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_FINAL` | STRING | Percentual de docentes com formação adequada nos anos finais (9º EF). — descrição gerada por IA. |
| `NIVEL_SOCIO_ECONOMICO` | STRING | Classificação do Indicador de Nível Socioeconômico (INSE) da escola. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_5EF` | STRING | Quantidade de alunos matriculados no 5º ano EF segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_5EF` | STRING | Quantidade de alunos do 5º ano EF que realizaram a prova. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_5EF` | STRING | Taxa de participação dos alunos do 5º ano EF na prova (0 a 1). — descrição gerada por IA. |
| `ATE_NIVEL_1_LP5` | STRING | Percentual de alunos do 5º ano EF até o Nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP5` | STRING | Percentual de alunos do 5º ano EF no Nível 2 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP5` | STRING | Percentual de alunos do 5º ano EF no Nível 3 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP5` | STRING | Percentual de alunos do 5º ano EF no Nível 4 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP5` | STRING | Percentual de alunos do 5º ano EF no Nível 5 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP5` | STRING | Percentual de alunos do 5º ano EF no Nível 6 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP5` | STRING | Percentual de alunos do 5º ano EF no Nível 7 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP5` | STRING | Percentual de alunos do 5º ano EF no Nível 8 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_9_LP5` | STRING | Percentual de alunos do 5º ano EF no Nível 9 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 0 em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 1 em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 2 em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 3 em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 4 em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 5 em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 6 em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 7 em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 8 em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 9 em Matemática. — descrição gerada por IA. |
| `NIVEL_10_MT5` | STRING | Percentual de alunos do 5º ano EF no Nível 10 em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_9EF` | STRING | Quantidade de alunos matriculados no 9º ano EF segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_9EF` | STRING | Quantidade de alunos do 9º ano EF que realizaram a prova. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_9EF` | STRING | Taxa de participação dos alunos do 9º ano EF na prova (0 a 1). — descrição gerada por IA. |
| `NIVEL_0_LP9` | STRING | Percentual de alunos do 9º ano EF no Nível 0 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP9` | STRING | Percentual de alunos do 9º ano EF no Nível 1 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP9` | STRING | Percentual de alunos do 9º ano EF no Nível 2 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP9` | STRING | Percentual de alunos do 9º ano EF no Nível 3 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP9` | STRING | Percentual de alunos do 9º ano EF no Nível 4 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP9` | STRING | Percentual de alunos do 9º ano EF no Nível 5 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP9` | STRING | Percentual de alunos do 9º ano EF no Nível 6 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP9` | STRING | Percentual de alunos do 9º ano EF no Nível 7 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP9` | STRING | Percentual de alunos do 9º ano EF no Nível 8 em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 0 em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 1 em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 2 em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 3 em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 4 em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 5 em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 6 em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 7 em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 8 em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT9` | STRING | Percentual de alunos do 9º ano EF no Nível 9 em Matemática. — descrição gerada por IA. |
| `MEDIA_5EF_LP` | STRING | Média padronizada da escola em Língua Portuguesa no 5º ano EF. — descrição gerada por IA. |
| `MEDIA_5EF_MT` | STRING | Média padronizada da escola em Matemática no 5º ano EF. — descrição gerada por IA. |
| `MEDIA_9EF_LP` | STRING | Média padronizada da escola em Língua Portuguesa no 9º ano EF. — descrição gerada por IA. |
| `MEDIA_9EF_MT` | STRING | Média padronizada da escola em Matemática no 9º ano EF. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador se o questionário contextual foi preenchido (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da escola/diretor à questão Q007 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta da escola/diretor à questão Q008 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta da escola/diretor à questão Q009 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta da escola/diretor à questão Q010 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da escola/diretor à questão Q011 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da escola/diretor à questão Q012 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da escola/diretor à questão Q013 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da escola/diretor à questão Q014 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da escola/diretor à questão Q015 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da escola/diretor à questão Q016 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta da escola/diretor à questão Q017 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta da escola/diretor à questão Q018 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta da escola/diretor à questão Q019 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta da escola/diretor à questão Q020 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta da escola/diretor à questão Q021 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta da escola/diretor à questão Q022 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta da escola/diretor à questão Q023 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta da escola/diretor à questão Q024 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta da escola/diretor à questão Q025 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta da escola/diretor à questão Q026 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta da escola/diretor à questão Q027 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta da escola/diretor à questão Q028 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta da escola/diretor à questão Q029 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta da escola/diretor à questão Q030 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta da escola/diretor à questão Q031 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta da escola/diretor à questão Q032 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta da escola/diretor à questão Q033 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta da escola/diretor à questão Q034 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta da escola/diretor à questão Q035 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta da escola/diretor à questão Q036 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta da escola/diretor à questão Q037 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta da escola/diretor à questão Q038 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta da escola/diretor à questão Q039 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta da escola/diretor à questão Q040 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta da escola/diretor à questão Q041 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta da escola/diretor à questão Q042 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta da escola/diretor à questão Q043 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta da escola/diretor à questão Q044 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta da escola/diretor à questão Q045 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta da escola/diretor à questão Q046 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta da escola/diretor à questão Q047 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta da escola/diretor à questão Q048 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta da escola/diretor à questão Q049 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta da escola/diretor à questão Q050 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta da escola/diretor à questão Q051 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta da escola/diretor à questão Q052 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta da escola/diretor à questão Q053 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta da escola/diretor à questão Q054 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta da escola/diretor à questão Q055 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta da escola/diretor à questão Q056 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta da escola/diretor à questão Q057 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta da escola/diretor à questão Q058 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta da escola/diretor à questão Q059 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta da escola/diretor à questão Q060 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta da escola/diretor à questão Q061 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta da escola/diretor à questão Q062 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta da escola/diretor à questão Q063 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta da escola/diretor à questão Q064 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta da escola/diretor à questão Q065 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta da escola/diretor à questão Q066 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta da escola/diretor à questão Q067 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta da escola/diretor à questão Q068 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta da escola/diretor à questão Q069 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta da escola/diretor à questão Q070 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta da escola/diretor à questão Q071 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta da escola/diretor à questão Q072 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta da escola/diretor à questão Q073 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta da escola/diretor à questão Q074 do questionário contextual. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2013_ts_item

File `raw__inep_saeb_microdados_csv_2013_ts_item.parquet` · 518 rows · 15 columns

Raw do microdado CSV TS_ITEM.csv do Saeb 2013, arquivo oficial microdados_saeb_2013.zip.

**Feeds:** `trusted/inep_saeb_microdados_item`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização do ciclo de avaliação do SAEB (ex: '2013'). — descrição gerada por IA. |
| `DISCIPLINA` | STRING | Sigla da disciplina avaliada na questão (ex: 'LP' para Língua Portuguesa). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código identificador do ano/série escolar avaliada (ex: '5' para 5º ano do EF). — descrição gerada por IA. |
| `BLOCO` | STRING | Número do bloco do caderno de prova ao qual o item pertence. — descrição gerada por IA. |
| `POSICAO` | STRING | Ordem ou posição da questão dentro do bloco de prova. — descrição gerada por IA. |
| `ID_ITEM` | STRING | Identificador único da questão/item no banco de itens do INEP. — descrição gerada por IA. |
| `NU_DESCRITOR_HABILIDADE` | STRING | Código do descritor da matriz de referência do SAEB que indica a habilidade avaliada (ex: 'D12'). — descrição gerada por IA. |
| `GABARITO` | STRING | Letra indicativa da opção correta do item (ex: 'A'). — descrição gerada por IA. |
| `TIPO_ITEM` | STRING | Formato de resposta da questão (ex: 'Resposta Objetiva'). — descrição gerada por IA. |
| `ITEM_MODELO` | STRING | Modelo psicométrico de TRI utilizado para calibrar a questão (ex: 'M3P' para Modelo de 3 Parâmetros). — descrição gerada por IA. |
| `A` | STRING | Parâmetro de discriminação 'a' da Teoria de Resposta ao Item. — descrição gerada por IA. |
| `B` | STRING | Parâmetro de dificuldade 'b' da Teoria de Resposta ao Item. — descrição gerada por IA. |
| `C` | STRING | Parâmetro 'c' da TRI, que representa a probabilidade de acerto por acaso (chute). — descrição gerada por IA. |
| `B1` | STRING | Primeiro parâmetro do passo de dificuldade em modelos de resposta graduada ou crédito parcial. — descrição gerada por IA. |
| `B2` | STRING | Segundo parâmetro do passo de dificuldade em modelos de resposta graduada ou crédito parcial. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2013_ts_professor

File `raw__inep_saeb_microdados_csv_2013_ts_professor.parquet` · 237,186 rows · 134 columns

Raw do microdado CSV TS_PROFESSOR.csv do Saeb 2013, arquivo oficial microdados_saeb_2013.zip.

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de realização da edição da Prova Brasil/SAEB (ex: 2013). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE de 2 dígitos referente à Unidade da Federação da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE de 7 dígitos referente ao município da escola. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (Censo Escolar) de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola pertence à rede pública (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código da localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma no Censo Escolar/INEP. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série ou ano escolar avaliado (ex: 5 para 5º ano do Ensino Fundamental). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário contextual (1 = Sim/Preenchido, 0 = Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta assinalada (letra da opção) para a questão 1 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta assinalada (letra da opção) para a questão 2 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta assinalada (letra da opção) para a questão 3 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta assinalada (letra da opção) para a questão 4 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta assinalada (letra da opção) para a questão 5 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta assinalada (letra da opção) para a questão 6 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta assinalada (letra da opção) para a questão 7 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta assinalada (letra da opção) para a questão 8 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta assinalada (letra da opção) para a questão 9 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta assinalada (letra da opção) para a questão 10 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta assinalada (letra da opção) para a questão 11 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta assinalada (letra da opção) para a questão 12 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta assinalada (letra da opção) para a questão 13 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta assinalada (letra da opção) para a questão 14 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta assinalada (letra da opção) para a questão 15 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta assinalada (letra da opção) para a questão 16 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta assinalada (letra da opção) para a questão 17 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta assinalada (letra da opção) para a questão 18 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta assinalada (letra da opção) para a questão 19 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta assinalada (letra da opção) para a questão 20 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta assinalada (letra da opção) para a questão 21 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta assinalada (letra da opção) para a questão 22 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta assinalada (letra da opção) para a questão 23 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta assinalada (letra da opção) para a questão 24 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta assinalada (letra da opção) para a questão 25 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta assinalada (letra da opção) para a questão 26 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta assinalada (letra da opção) para a questão 27 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta assinalada (letra da opção) para a questão 28 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta assinalada (letra da opção) para a questão 29 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta assinalada (letra da opção) para a questão 30 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta assinalada (letra da opção) para a questão 31 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta assinalada (letra da opção) para a questão 32 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta assinalada (letra da opção) para a questão 33 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta assinalada (letra da opção) para a questão 34 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta assinalada (letra da opção) para a questão 35 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta assinalada (letra da opção) para a questão 36 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta assinalada (letra da opção) para a questão 37 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta assinalada (letra da opção) para a questão 38 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta assinalada (letra da opção) para a questão 39 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta assinalada (letra da opção) para a questão 40 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta assinalada (letra da opção) para a questão 41 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta assinalada (letra da opção) para a questão 42 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta assinalada (letra da opção) para a questão 43 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta assinalada (letra da opção) para a questão 44 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta assinalada (letra da opção) para a questão 45 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta assinalada (letra da opção) para a questão 46 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta assinalada (letra da opção) para a questão 47 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta assinalada (letra da opção) para a questão 48 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta assinalada (letra da opção) para a questão 49 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta assinalada (letra da opção) para a questão 50 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta assinalada (letra da opção) para a questão 51 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta assinalada (letra da opção) para a questão 52 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta assinalada (letra da opção) para a questão 53 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta assinalada (letra da opção) para a questão 54 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta assinalada (letra da opção) para a questão 55 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta assinalada (letra da opção) para a questão 56 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta assinalada (letra da opção) para a questão 57 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta assinalada (letra da opção) para a questão 58 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta assinalada (letra da opção) para a questão 59 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta assinalada (letra da opção) para a questão 60 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta assinalada (letra da opção) para a questão 61 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta assinalada (letra da opção) para a questão 62 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta assinalada (letra da opção) para a questão 63 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta assinalada (letra da opção) para a questão 64 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta assinalada (letra da opção) para a questão 65 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta assinalada (letra da opção) para a questão 66 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta assinalada (letra da opção) para a questão 67 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta assinalada (letra da opção) para a questão 68 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta assinalada (letra da opção) para a questão 69 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta assinalada (letra da opção) para a questão 70 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta assinalada (letra da opção) para a questão 71 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta assinalada (letra da opção) para a questão 72 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta assinalada (letra da opção) para a questão 73 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta assinalada (letra da opção) para a questão 74 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Resposta assinalada (letra da opção) para a questão 75 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Resposta assinalada (letra da opção) para a questão 76 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Resposta assinalada (letra da opção) para a questão 77 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Resposta assinalada (letra da opção) para a questão 78 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Resposta assinalada (letra da opção) para a questão 79 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Resposta assinalada (letra da opção) para a questão 80 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Resposta assinalada (letra da opção) para a questão 81 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Resposta assinalada (letra da opção) para a questão 82 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Resposta assinalada (letra da opção) para a questão 83 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Resposta assinalada (letra da opção) para a questão 84 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Resposta assinalada (letra da opção) para a questão 85 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Resposta assinalada (letra da opção) para a questão 86 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Resposta assinalada (letra da opção) para a questão 87 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Resposta assinalada (letra da opção) para a questão 88 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Resposta assinalada (letra da opção) para a questão 89 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Resposta assinalada (letra da opção) para a questão 90 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Resposta assinalada (letra da opção) para a questão 91 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Resposta assinalada (letra da opção) para a questão 92 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Resposta assinalada (letra da opção) para a questão 93 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Resposta assinalada (letra da opção) para a questão 94 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Resposta assinalada (letra da opção) para a questão 95 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Resposta assinalada (letra da opção) para a questão 96 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Resposta assinalada (letra da opção) para a questão 97 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Resposta assinalada (letra da opção) para a questão 98 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Resposta assinalada (letra da opção) para a questão 99 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Resposta assinalada (letra da opção) para a questão 100 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Resposta assinalada (letra da opção) para a questão 101 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Resposta assinalada (letra da opção) para a questão 102 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Resposta assinalada (letra da opção) para a questão 103 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Resposta assinalada (letra da opção) para a questão 104 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Resposta assinalada (letra da opção) para a questão 105 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Resposta assinalada (letra da opção) para a questão 106 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Resposta assinalada (letra da opção) para a questão 107 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Resposta assinalada (letra da opção) para a questão 108 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Resposta assinalada (letra da opção) para a questão 109 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Resposta assinalada (letra da opção) para a questão 110 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Resposta assinalada (letra da opção) para a questão 111 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Resposta assinalada (letra da opção) para a questão 112 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Resposta assinalada (letra da opção) para a questão 113 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Resposta assinalada (letra da opção) para a questão 114 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Resposta assinalada (letra da opção) para a questão 115 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Resposta assinalada (letra da opção) para a questão 116 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Resposta assinalada (letra da opção) para a questão 117 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Resposta assinalada (letra da opção) para a questão 118 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Resposta assinalada (letra da opção) para a questão 119 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Resposta assinalada (letra da opção) para a questão 120 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Resposta assinalada (letra da opção) para a questão 121 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q122` | STRING | Resposta assinalada (letra da opção) para a questão 122 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q123` | STRING | Resposta assinalada (letra da opção) para a questão 123 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q124` | STRING | Resposta assinalada (letra da opção) para a questão 124 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q125` | STRING | Resposta assinalada (letra da opção) para a questão 125 do questionário contextual. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2015_ts_aluno_3em

File `raw__inep_saeb_microdados_csv_2015_ts_aluno_3em.parquet` · 114,225 rows · 94 columns

Raw do microdado CSV TS_ALUNO_3EM.csv do Saeb 2015, arquivo oficial microdados_saeb_2015.zip.

**Feeds:** `raw/inep_saeb_aluno_2015`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de edição da avaliação do Prova Brasil/SAEB. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da unidade federativa (UF) da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Indicador de área da escola (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola é da rede pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código de identificação da turma no Censo Escolar/INEP. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série/ano escolar avaliado. — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único criptografado do aluno na avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação do aluno no Censo Escolar na data de referência. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador se o aluno preencheu a prova de avaliação (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Código do caderno de prova atribuído ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Código do primeiro bloco de itens do teste do aluno. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Código do segundo bloco de itens do teste do aluno. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | Vetor de respostas marcadas pelo aluno no Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | Vetor de respostas marcadas pelo aluno no Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | Vetor de respostas marcadas pelo aluno no Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | Vetor de respostas marcadas pelo aluno no Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador se o aluno possui cálculo de proficiência validado (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Indicador de participação do aluno no escopo da Prova Brasil. — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da ANEB/SAEB para ponderação estatística. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para cálculo de estimativas em Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para cálculo de estimativas em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota estimada de proficiência em Língua Portuguesa na escala TRI do SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP` | STRING | Desvio padrão da estimativa de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota padronizada em Língua Portuguesa ajustada à escala comparativa histórica do SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP_SAEB` | STRING | Desvio padrão da proficiência padronizada em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota estimada de proficiência em Matemática na escala TRI do SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT` | STRING | Desvio padrão da estimativa de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota padronizada em Matemática ajustada à escala comparativa histórica do SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT_SAEB` | STRING | Desvio padrão da proficiência padronizada em Matemática. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador se o aluno respondeu ao questionário socioeconômico (1: Sim, 0: Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta da questão 001 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta da questão 002 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta da questão 003 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta da questão 004 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta da questão 005 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta da questão 006 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da questão 007 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta da questão 008 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta da questão 009 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta da questão 010 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da questão 011 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da questão 012 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da questão 013 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da questão 014 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da questão 015 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da questão 016 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta da questão 017 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta da questão 018 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta da questão 019 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta da questão 020 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta da questão 021 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta da questão 022 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta da questão 023 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta da questão 024 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta da questão 025 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta da questão 026 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta da questão 027 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta da questão 028 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta da questão 029 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta da questão 030 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta da questão 031 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta da questão 032 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta da questão 033 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta da questão 034 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta da questão 035 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta da questão 036 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta da questão 037 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta da questão 038 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta da questão 039 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta da questão 040 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta da questão 041 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta da questão 042 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta da questão 043 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta da questão 044 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta da questão 045 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta da questão 046 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta da questão 047 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta da questão 048 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta da questão 049 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta da questão 050 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta da questão 051 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta da questão 052 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta da questão 053 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta da questão 054 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta da questão 055 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta da questão 056 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta da questão 057 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta da questão 058 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta da questão 059 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta da questão 060 do questionário socioeconômico do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2015_ts_aluno_5ef

File `raw__inep_saeb_microdados_csv_2015_ts_aluno_5ef.parquet` · 2,497,431 rows · 85 columns

Raw do microdado CSV TS_ALUNO_5EF.csv do Saeb 2015, arquivo oficial microdados_saeb_2015.zip.

**Feeds:** `raw/inep_saeb_aluno_2015`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano/Edição da aplicação da Prova Brasil/SAEB (ex: 2015). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do Estado (Unidade da Federação) onde a escola está localizada. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área do município (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP único de identificação da escola (Censo Escolar). — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola pertence à rede pública de ensino (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma do aluno na aplicação da avaliação. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/Ano escolar do aluno avaliado (ex: 5 para 5º ano EF, 9 para 9º ano EF). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Código identificador único e anonimizado do aluno na avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação da matrícula do aluno no Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador de presença e preenchimento do caderno de prova pelo aluno (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Código/Número do caderno de teste montado e entregue ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Identificador do primeiro bloco de itens do caderno de teste. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Identificador do segundo bloco de itens do caderno de teste. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | String com as respostas dadas pelo aluno aos itens do Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | String com as respostas dadas pelo aluno aos itens do Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | String com as respostas dadas pelo aluno aos itens do Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | String com as respostas dadas pelo aluno aos itens do Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador de cálculo de proficiência válida para o aluno (1: Possui proficiência calculada, 0: Não possui). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Flag indicando se o aluno compõe a amostra da Prova Brasil (1: Sim, 0: Não). — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código do estrato de amostragem da ANEB para fins estatísticos. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral de expansão do aluno para análises de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral de expansão do aluno para análises de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Pontuação/Proficiência estimada do aluno em Língua Portuguesa na escala TRI. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP` | STRING | Desvio padrão associado à estimativa da proficiência de Língua Portuguesa do aluno. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência padronizada do aluno em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP_SAEB` | STRING | Desvio padrão da proficiência de Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Pontuação/Proficiência estimada do aluno em Matemática na escala TRI. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT` | STRING | Desvio padrão associado à estimativa da proficiência de Matemática do aluno. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência padronizada do aluno em Matemática na escala SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT_SAEB` | STRING | Desvio padrão da proficiência de Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico pelo aluno (1: Sim, 0: Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta da questão 1 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta da questão 2 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta da questão 3 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta da questão 4 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta da questão 5 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta da questão 6 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da questão 7 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta da questão 8 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta da questão 9 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta da questão 10 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da questão 11 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da questão 12 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da questão 13 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da questão 14 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da questão 15 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da questão 16 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta da questão 17 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta da questão 18 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta da questão 19 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta da questão 20 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta da questão 21 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta da questão 22 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta da questão 23 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta da questão 24 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta da questão 25 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta da questão 26 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta da questão 27 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta da questão 28 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta da questão 29 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta da questão 30 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta da questão 31 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta da questão 32 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta da questão 33 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta da questão 34 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta da questão 35 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta da questão 36 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta da questão 37 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta da questão 38 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta da questão 39 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta da questão 40 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta da questão 41 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta da questão 42 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta da questão 43 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta da questão 44 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta da questão 45 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta da questão 46 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta da questão 47 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta da questão 48 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta da questão 49 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta da questão 50 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta da questão 51 do questionário socioeconômico do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2015_ts_aluno_9ef

File `raw__inep_saeb_microdados_csv_2015_ts_aluno_9ef.parquet` · 2,419,376 rows · 91 columns

Raw do microdado CSV TS_ALUNO_9EF.csv do Saeb 2015, arquivo oficial microdados_saeb_2015.zip.

**Feeds:** `raw/inep_saeb_aluno_2015`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano da edição da avaliação Prova Brasil/SAEB. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação onde a escola se localiza. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área do município (1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola é pública (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma no sistema do Censo Escolar/SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar do aluno avaliado (ex: 5 para 5º ano, 9 para 9º ano). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Código de identificação do aluno na base da avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador da situação do aluno no Censo Escolar no momento da amostragem. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador de preenchimento do caderno de prova pelo aluno (1-Preencheu, 0-Não preencheu). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Código do caderno de prova atribuído ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Identificador do primeiro bloco de itens respondido no caderno. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Identificador do segundo bloco de itens respondido no caderno. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | String contendo o vetor de respostas do bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | String contendo o vetor de respostas do bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | String contendo o vetor de respostas do bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | String contendo o vetor de respostas do bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador de cálculo válido da proficiência do aluno (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Indicador se o aluno pertence à amostragem censitária da Prova Brasil. — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da ANEB (Avaliação Nacional da Educação Básica). — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral expandido do aluno para inferências em Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral expandido do aluno para inferências em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Pontuação/proficiência estimada do aluno em Língua Portuguesa na escala TRI. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP` | STRING | Desvio padrão da estimativa de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência calibrada em Língua Portuguesa ajustada à escala histórica do SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_LP_SAEB` | STRING | Desvio padrão da proficiência calibrada de Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Pontuação/proficiência estimada do aluno em Matemática na escala TRI. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT` | STRING | Desvio padrão da estimativa de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência calibrada em Matemática ajustada à escala histórica do SAEB. — descrição gerada por IA. |
| `DESVIO_PADRAO_MT_SAEB` | STRING | Desvio padrão da proficiência calibrada de Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador se o aluno preencheu o questionário socioeconômico (1-Sim, 0-Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta do aluno ao item 1 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta do aluno ao item 2 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta do aluno ao item 3 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta do aluno ao item 4 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta do aluno ao item 5 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta do aluno ao item 6 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta do aluno ao item 7 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta do aluno ao item 8 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta do aluno ao item 9 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta do aluno ao item 10 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta do aluno ao item 11 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta do aluno ao item 12 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta do aluno ao item 13 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta do aluno ao item 14 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta do aluno ao item 15 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta do aluno ao item 16 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta do aluno ao item 17 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta do aluno ao item 18 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta do aluno ao item 19 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta do aluno ao item 20 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta do aluno ao item 21 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta do aluno ao item 22 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta do aluno ao item 23 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta do aluno ao item 24 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta do aluno ao item 25 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta do aluno ao item 26 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta do aluno ao item 27 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta do aluno ao item 28 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta do aluno ao item 29 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta do aluno ao item 30 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta do aluno ao item 31 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta do aluno ao item 32 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta do aluno ao item 33 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta do aluno ao item 34 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta do aluno ao item 35 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta do aluno ao item 36 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta do aluno ao item 37 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta do aluno ao item 38 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta do aluno ao item 39 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta do aluno ao item 40 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta do aluno ao item 41 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta do aluno ao item 42 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta do aluno ao item 43 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta do aluno ao item 44 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta do aluno ao item 45 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta do aluno ao item 46 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta do aluno ao item 47 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta do aluno ao item 48 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta do aluno ao item 49 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta do aluno ao item 50 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta do aluno ao item 51 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta do aluno ao item 52 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta do aluno ao item 53 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta do aluno ao item 54 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta do aluno ao item 55 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta do aluno ao item 56 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta do aluno ao item 57 do questionário socioeconômico. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2015_ts_diretor

File `raw__inep_saeb_microdados_csv_2015_ts_diretor.parquet` · 55,693 rows · 118 columns

Raw do microdado CSV TS_DIRETOR.csv do Saeb 2015, arquivo oficial microdados_saeb_2015.zip.

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano/edição da Prova Brasil ou SAEB (ex: 2015). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE/INEP da Unidade da Federação. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola (Censo Escolar). — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário contextual (1 = Preenchido, 0/null = Não preenchido). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta da questão 1 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta da questão 2 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta da questão 3 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta da questão 4 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta da questão 5 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta da questão 6 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da questão 7 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta da questão 8 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta da questão 9 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta da questão 10 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da questão 11 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da questão 12 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da questão 13 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da questão 14 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da questão 15 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da questão 16 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta da questão 17 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta da questão 18 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta da questão 19 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta da questão 20 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta da questão 21 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta da questão 22 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta da questão 23 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta da questão 24 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta da questão 25 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta da questão 26 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta da questão 27 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta da questão 28 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta da questão 29 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta da questão 30 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta da questão 31 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta da questão 32 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta da questão 33 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta da questão 34 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta da questão 35 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta da questão 36 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta da questão 37 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta da questão 38 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta da questão 39 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta da questão 40 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta da questão 41 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta da questão 42 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta da questão 43 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta da questão 44 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta da questão 45 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta da questão 46 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta da questão 47 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta da questão 48 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta da questão 49 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta da questão 50 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta da questão 51 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta da questão 52 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta da questão 53 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta da questão 54 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta da questão 55 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta da questão 56 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta da questão 57 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta da questão 58 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta da questão 59 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta da questão 60 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta da questão 61 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta da questão 62 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta da questão 63 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta da questão 64 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta da questão 65 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta da questão 66 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta da questão 67 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta da questão 68 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta da questão 69 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta da questão 70 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta da questão 71 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta da questão 72 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta da questão 73 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta da questão 74 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Resposta da questão 75 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Resposta da questão 76 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Resposta da questão 77 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Resposta da questão 78 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Resposta da questão 79 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Resposta da questão 80 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Resposta da questão 81 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Resposta da questão 82 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Resposta da questão 83 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Resposta da questão 84 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Resposta da questão 85 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Resposta da questão 86 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Resposta da questão 87 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Resposta da questão 88 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Resposta da questão 89 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Resposta da questão 90 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Resposta da questão 91 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Resposta da questão 92 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Resposta da questão 93 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Resposta da questão 94 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Resposta da questão 95 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Resposta da questão 96 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Resposta da questão 97 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Resposta da questão 98 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Resposta da questão 99 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Resposta da questão 100 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Resposta da questão 101 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Resposta da questão 102 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Resposta da questão 103 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Resposta da questão 104 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Resposta da questão 105 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Resposta da questão 106 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Resposta da questão 107 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Resposta da questão 108 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Resposta da questão 109 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Resposta da questão 110 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Resposta da questão 111 do questionário contextual (opção codificada em letra). — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2015_ts_escola

File `raw__inep_saeb_microdados_csv_2015_ts_escola.parquet` · 57,744 rows · 128 columns

Raw do microdado CSV TS_ESCOLA.csv do Saeb 2015, arquivo oficial microdados_saeb_2015.zip.

**Feeds:** `trusted/inep_saeb_escola`, `trusted/inep_saeb_microdados_escola`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de realização da edição da Prova Brasil / SAEB (ex: 2015). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE de dois dígitos referente à Unidade da Federação da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE de sete dígitos do município onde a escola está localizada. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP identificador único da escola no Censo Escolar. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 = Escola Pública, 0 = Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_INICIAL` | STRING | Percentual de docentes dos Anos Iniciais (5º ano) com formação acadêmica adequada. — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_FINAL` | STRING | Percentual de docentes dos Anos Finais (9º ano) com formação acadêmica adequada. — descrição gerada por IA. |
| `NIVEL_SOCIO_ECONOMICO` | STRING | Classificação do Nível Socioeconômico (INSE) da comunidade escolar (ex: Alto, Médio). — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_5EF` | STRING | Quantidade total de alunos matriculados no 5º ano do Ensino Fundamental segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_5EF` | STRING | Quantidade de alunos do 5º ano do Ensino Fundamental presentes na aplicação da prova. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_5EF` | STRING | Proporção de participação dos alunos do 5º ano na prova (NU_PRESENTES_5EF / NU_MATRICULADOS_CENSO_5EF). — descrição gerada por IA. |
| `NIVEL_0_LP5` | STRING | Percentual de alunos do 5º ano no Nível 0 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP5` | STRING | Percentual de alunos do 5º ano no Nível 1 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP5` | STRING | Percentual de alunos do 5º ano no Nível 2 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP5` | STRING | Percentual de alunos do 5º ano no Nível 3 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP5` | STRING | Percentual de alunos do 5º ano no Nível 4 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP5` | STRING | Percentual de alunos do 5º ano no Nível 5 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP5` | STRING | Percentual de alunos do 5º ano no Nível 6 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP5` | STRING | Percentual de alunos do 5º ano no Nível 7 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP5` | STRING | Percentual de alunos do 5º ano no Nível 8 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_9_LP5` | STRING | Percentual de alunos do 5º ano no Nível 9 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT5` | STRING | Percentual de alunos do 5º ano no Nível 0 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT5` | STRING | Percentual de alunos do 5º ano no Nível 1 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT5` | STRING | Percentual de alunos do 5º ano no Nível 2 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT5` | STRING | Percentual de alunos do 5º ano no Nível 3 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT5` | STRING | Percentual de alunos do 5º ano no Nível 4 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT5` | STRING | Percentual de alunos do 5º ano no Nível 5 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT5` | STRING | Percentual de alunos do 5º ano no Nível 6 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT5` | STRING | Percentual de alunos do 5º ano no Nível 7 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT5` | STRING | Percentual de alunos do 5º ano no Nível 8 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT5` | STRING | Percentual de alunos do 5º ano no Nível 9 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_10_MT5` | STRING | Percentual de alunos do 5º ano no Nível 10 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_9EF` | STRING | Quantidade total de alunos matriculados no 9º ano do Ensino Fundamental segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_9EF` | STRING | Quantidade de alunos do 9º ano do Ensino Fundamental presentes na aplicação da prova. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_9EF` | STRING | Proporção de participação dos alunos do 9º ano na prova (NU_PRESENTES_9EF / NU_MATRICULADOS_CENSO_9EF). — descrição gerada por IA. |
| `NIVEL_0_LP9` | STRING | Percentual de alunos do 9º ano no Nível 0 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP9` | STRING | Percentual de alunos do 9º ano no Nível 1 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP9` | STRING | Percentual de alunos do 9º ano no Nível 2 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP9` | STRING | Percentual de alunos do 9º ano no Nível 3 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP9` | STRING | Percentual de alunos do 9º ano no Nível 4 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP9` | STRING | Percentual de alunos do 9º ano no Nível 5 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP9` | STRING | Percentual de alunos do 9º ano no Nível 6 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP9` | STRING | Percentual de alunos do 9º ano no Nível 7 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP9` | STRING | Percentual de alunos do 9º ano no Nível 8 da escala de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT9` | STRING | Percentual de alunos do 9º ano no Nível 0 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT9` | STRING | Percentual de alunos do 9º ano no Nível 1 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT9` | STRING | Percentual de alunos do 9º ano no Nível 2 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT9` | STRING | Percentual de alunos do 9º ano no Nível 3 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT9` | STRING | Percentual de alunos do 9º ano no Nível 4 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT9` | STRING | Percentual de alunos do 9º ano no Nível 5 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT9` | STRING | Percentual de alunos do 9º ano no Nível 6 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT9` | STRING | Percentual de alunos do 9º ano no Nível 7 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT9` | STRING | Percentual de alunos do 9º ano no Nível 8 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT9` | STRING | Percentual de alunos do 9º ano no Nível 9 da escala de proficiência em Matemática. — descrição gerada por IA. |
| `MEDIA_5EF_LP` | STRING | Nota média de proficiência em Língua Portuguesa dos alunos do 5º ano. — descrição gerada por IA. |
| `MEDIA_5EF_MT` | STRING | Nota média de proficiência em Matemática dos alunos do 5º ano. — descrição gerada por IA. |
| `MEDIA_9EF_LP` | STRING | Nota média de proficiência em Língua Portuguesa dos alunos do 9º ano. — descrição gerada por IA. |
| `MEDIA_9EF_MT` | STRING | Nota média de proficiência em Matemática dos alunos do 9º ano. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário contextual pela escola/direção (1 = Preenchido, 0 = Não preenchido). — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Opção assinalada na questão 007 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Opção assinalada na questão 008 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Opção assinalada na questão 009 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Opção assinalada na questão 010 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Opção assinalada na questão 011 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Opção assinalada na questão 012 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Opção assinalada na questão 013 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Opção assinalada na questão 014 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Opção assinalada na questão 015 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Opção assinalada na questão 016 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Opção assinalada na questão 017 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Opção assinalada na questão 018 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Opção assinalada na questão 019 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Opção assinalada na questão 020 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Opção assinalada na questão 021 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Opção assinalada na questão 022 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Opção assinalada na questão 023 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Opção assinalada na questão 024 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Opção assinalada na questão 025 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Opção assinalada na questão 026 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Opção assinalada na questão 027 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Opção assinalada na questão 028 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Opção assinalada na questão 029 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Opção assinalada na questão 030 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Opção assinalada na questão 031 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Opção assinalada na questão 032 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Opção assinalada na questão 033 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Opção assinalada na questão 034 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Opção assinalada na questão 035 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Opção assinalada na questão 036 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Opção assinalada na questão 037 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Opção assinalada na questão 038 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Opção assinalada na questão 039 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Opção assinalada na questão 040 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Opção assinalada na questão 041 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Opção assinalada na questão 042 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Opção assinalada na questão 043 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Opção assinalada na questão 044 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Opção assinalada na questão 045 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Opção assinalada na questão 046 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Opção assinalada na questão 047 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Opção assinalada na questão 048 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Opção assinalada na questão 049 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Opção assinalada na questão 050 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Opção assinalada na questão 051 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Opção assinalada na questão 052 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Opção assinalada na questão 053 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Opção assinalada na questão 054 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Opção assinalada na questão 055 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Opção assinalada na questão 056 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Opção assinalada na questão 057 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Opção assinalada na questão 058 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Opção assinalada na questão 059 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Opção assinalada na questão 060 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Opção assinalada na questão 061 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Opção assinalada na questão 062 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Opção assinalada na questão 063 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Opção assinalada na questão 064 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Opção assinalada na questão 065 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Opção assinalada na questão 066 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Opção assinalada na questão 067 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Opção assinalada na questão 068 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Opção assinalada na questão 069 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Opção assinalada na questão 070 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Opção assinalada na questão 071 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Opção assinalada na questão 072 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Opção assinalada na questão 073 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Opção assinalada na questão 074 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2015_ts_item

File `raw__inep_saeb_microdados_csv_2015_ts_item.parquet` · 518 rows · 15 columns

Raw do microdado CSV TS_ITEM.csv do Saeb 2015, arquivo oficial microdados_saeb_2015.zip.

**Feeds:** `trusted/inep_saeb_microdados_item`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do SAEB (ex: '2015'). — descrição gerada por IA. |
| `DISCIPLINA` | STRING | Sigla da disciplina avaliada (ex: 'LP' para Língua Portuguesa). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Identificador da série/ano escolar avaliado (ex: '5' para 5º ano do Ensino Fundamental). — descrição gerada por IA. |
| `BLOCO` | STRING | Número do bloco do caderno de prova em que o item está inserido. — descrição gerada por IA. |
| `POSICAO` | STRING | Ordem ou posição de apresentação do item no bloco de provas. — descrição gerada por IA. |
| `ID_ITEM` | STRING | Código identificador único do item (questão) na base do INEP/SAEB. — descrição gerada por IA. |
| `NU_DESCRITOR_HABILIDADE` | STRING | Código do descritor de habilidade na Matriz de Referência do SAEB (ex: 'D10'). — descrição gerada por IA. |
| `GABARITO` | STRING | Letra que indica a alternativa correta do item. — descrição gerada por IA. |
| `TIPO_ITEM` | STRING | Formato do item na avaliação (ex: 'Resposta Objetiva'). — descrição gerada por IA. |
| `ITEM_MODELO` | STRING | Modelo logístico adotado na Teoria de Resposta ao Item (ex: 'M3P' para Modelo de 3 Parâmetros). — descrição gerada por IA. |
| `A` | STRING | Parâmetro 'a' da TRI: indica a capacidade de discriminação do item. — descrição gerada por IA. |
| `B` | STRING | Parâmetro 'b' da TRI: indica o nível de dificuldade do item. — descrição gerada por IA. |
| `C` | STRING | Parâmetro 'c' da TRI: representa a probabilidade de acerto ao acaso (chute). — descrição gerada por IA. |
| `B1` | STRING | Parâmetro complementar 'b1' de dificuldade para itens de resposta politômica (nulo para dicotômicos). — descrição gerada por IA. |
| `B2` | STRING | Parâmetro complementar 'b2' de dificuldade para itens de resposta politômica (nulo para dicotômicos). — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2015_ts_professor

File `raw__inep_saeb_microdados_csv_2015_ts_professor.parquet` · 274,179 rows · 134 columns

Raw do microdado CSV TS_PROFESSOR.csv do Saeb 2015, arquivo oficial microdados_saeb_2015.zip.

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de edição do exame Prova Brasil/SAEB (ex: 2015). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE de dois dígitos da Unidade da Federação (Estado). — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município de localização da escola. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (Censo Escolar) de identificação única da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador único da turma no sistema do Censo Escolar/INEP. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar avaliado na Prova Brasil (ex: 5 = 5º ano do EF). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador se o questionário de contexto foi respondido (1 = Preenchido, 0 = Não preenchido). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Letra da alternativa selecionada para a questão 1 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Letra da alternativa selecionada para a questão 2 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Letra da alternativa selecionada para a questão 3 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Letra da alternativa selecionada para a questão 4 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Letra da alternativa selecionada para a questão 5 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Letra da alternativa selecionada para a questão 6 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Letra da alternativa selecionada para a questão 7 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Letra da alternativa selecionada para a questão 8 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Letra da alternativa selecionada para a questão 9 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Letra da alternativa selecionada para a questão 10 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Letra da alternativa selecionada para a questão 11 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Letra da alternativa selecionada para a questão 12 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Letra da alternativa selecionada para a questão 13 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Letra da alternativa selecionada para a questão 14 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Letra da alternativa selecionada para a questão 15 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Letra da alternativa selecionada para a questão 16 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Letra da alternativa selecionada para a questão 17 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Letra da alternativa selecionada para a questão 18 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Letra da alternativa selecionada para a questão 19 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Letra da alternativa selecionada para a questão 20 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Letra da alternativa selecionada para a questão 21 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Letra da alternativa selecionada para a questão 22 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Letra da alternativa selecionada para a questão 23 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Letra da alternativa selecionada para a questão 24 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Letra da alternativa selecionada para a questão 25 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Letra da alternativa selecionada para a questão 26 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Letra da alternativa selecionada para a questão 27 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Letra da alternativa selecionada para a questão 28 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Letra da alternativa selecionada para a questão 29 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Letra da alternativa selecionada para a questão 30 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Letra da alternativa selecionada para a questão 31 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Letra da alternativa selecionada para a questão 32 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Letra da alternativa selecionada para a questão 33 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Letra da alternativa selecionada para a questão 34 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Letra da alternativa selecionada para a questão 35 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Letra da alternativa selecionada para a questão 36 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Letra da alternativa selecionada para a questão 37 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Letra da alternativa selecionada para a questão 38 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Letra da alternativa selecionada para a questão 39 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Letra da alternativa selecionada para a questão 40 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Letra da alternativa selecionada para a questão 41 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Letra da alternativa selecionada para a questão 42 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Letra da alternativa selecionada para a questão 43 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Letra da alternativa selecionada para a questão 44 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Letra da alternativa selecionada para a questão 45 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Letra da alternativa selecionada para a questão 46 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Letra da alternativa selecionada para a questão 47 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Letra da alternativa selecionada para a questão 48 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Letra da alternativa selecionada para a questão 49 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Letra da alternativa selecionada para a questão 50 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Letra da alternativa selecionada para a questão 51 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Letra da alternativa selecionada para a questão 52 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Letra da alternativa selecionada para a questão 53 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Letra da alternativa selecionada para a questão 54 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Letra da alternativa selecionada para a questão 55 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Letra da alternativa selecionada para a questão 56 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Letra da alternativa selecionada para a questão 57 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Letra da alternativa selecionada para a questão 58 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Letra da alternativa selecionada para a questão 59 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Letra da alternativa selecionada para a questão 60 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Letra da alternativa selecionada para a questão 61 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Letra da alternativa selecionada para a questão 62 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Letra da alternativa selecionada para a questão 63 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Letra da alternativa selecionada para a questão 64 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Letra da alternativa selecionada para a questão 65 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Letra da alternativa selecionada para a questão 66 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Letra da alternativa selecionada para a questão 67 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Letra da alternativa selecionada para a questão 68 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Letra da alternativa selecionada para a questão 69 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Letra da alternativa selecionada para a questão 70 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Letra da alternativa selecionada para a questão 71 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Letra da alternativa selecionada para a questão 72 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Letra da alternativa selecionada para a questão 73 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Letra da alternativa selecionada para a questão 74 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Letra da alternativa selecionada para a questão 75 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Letra da alternativa selecionada para a questão 76 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Letra da alternativa selecionada para a questão 77 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Letra da alternativa selecionada para a questão 78 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Letra da alternativa selecionada para a questão 79 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Letra da alternativa selecionada para a questão 80 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Letra da alternativa selecionada para a questão 81 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Letra da alternativa selecionada para a questão 82 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Letra da alternativa selecionada para a questão 83 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Letra da alternativa selecionada para a questão 84 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Letra da alternativa selecionada para a questão 85 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Letra da alternativa selecionada para a questão 86 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Letra da alternativa selecionada para a questão 87 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Letra da alternativa selecionada para a questão 88 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Letra da alternativa selecionada para a questão 89 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Letra da alternativa selecionada para a questão 90 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Letra da alternativa selecionada para a questão 91 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Letra da alternativa selecionada para a questão 92 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Letra da alternativa selecionada para a questão 93 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Letra da alternativa selecionada para a questão 94 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Letra da alternativa selecionada para a questão 95 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Letra da alternativa selecionada para a questão 96 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Letra da alternativa selecionada para a questão 97 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Letra da alternativa selecionada para a questão 98 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Letra da alternativa selecionada para a questão 99 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Letra da alternativa selecionada para a questão 100 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Letra da alternativa selecionada para a questão 101 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Letra da alternativa selecionada para a questão 102 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Letra da alternativa selecionada para a questão 103 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Letra da alternativa selecionada para a questão 104 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Letra da alternativa selecionada para a questão 105 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Letra da alternativa selecionada para a questão 106 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Letra da alternativa selecionada para a questão 107 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Letra da alternativa selecionada para a questão 108 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Letra da alternativa selecionada para a questão 109 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Letra da alternativa selecionada para a questão 110 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Letra da alternativa selecionada para a questão 111 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Letra da alternativa selecionada para a questão 112 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Letra da alternativa selecionada para a questão 113 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Letra da alternativa selecionada para a questão 114 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Letra da alternativa selecionada para a questão 115 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Letra da alternativa selecionada para a questão 116 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Letra da alternativa selecionada para a questão 117 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Letra da alternativa selecionada para a questão 118 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Letra da alternativa selecionada para a questão 119 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Letra da alternativa selecionada para a questão 120 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Letra da alternativa selecionada para a questão 121 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q122` | STRING | Letra da alternativa selecionada para a questão 122 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q123` | STRING | Letra da alternativa selecionada para a questão 123 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q124` | STRING | Letra da alternativa selecionada para a questão 124 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |
| `TX_RESP_Q125` | STRING | Letra da alternativa selecionada para a questão 125 do questionário de contexto da Prova Brasil. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2017_ts_aluno_3em_ag

File `raw__inep_saeb_microdados_csv_2017_ts_aluno_3em_ag.parquet` · 1,966,507 rows · 95 columns

Raw do microdado CSV TS_ALUNO_3EM_AG.csv do Saeb 2017, arquivo oficial microdados_saeb_2017.zip.

**Feeds:** `raw/inep_saeb_aluno_2017`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de edição do exame Prova Brasil / SAEB. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Área de localização da escola (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma no Censo Escolar. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/Etapa de ensino avaliada (ex: 5, 9 ou 12). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único e anonimizado do aluno na avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno segundo o Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador de preenchimento suficiente do caderno de teste (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PRESENCA_PROVA` | STRING | Indicador de presença do aluno no dia do exame (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Número do caderno de prova montado para o aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Código do primeiro bloco de itens respondido pelo aluno. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Código do segundo bloco de itens respondido pelo aluno. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | Vetor com as opções marcadas pelo aluno no bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | Vetor com as opções marcadas pelo aluno no bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | Vetor com as opções marcadas pelo aluno no bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | Vetor com as opções marcadas pelo aluno no bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador se o aluno obteve cálculo válido de proficiência (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Indicador de pertencimento ao estrato censitário da Prova Brasil (1: Sim, 0: Não). — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código de estratificação da amostra ANEB. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Fator de expansão amostral do aluno para análises de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Fator de expansão amostral do aluno para análises de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota estimada do aluno em Língua Portuguesa pela Teoria de Resposta ao Item (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência do aluno em Língua Portuguesa ajustada à escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota estimada do aluno em Matemática pela Teoria de Resposta ao Item (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência do aluno em Matemática ajustada à escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência em Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico (1: Sim, 0: Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta da questão 1 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta da questão 2 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta da questão 3 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta da questão 4 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta da questão 5 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta da questão 6 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da questão 7 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta da questão 8 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta da questão 9 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta da questão 10 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da questão 11 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da questão 12 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da questão 13 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da questão 14 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da questão 15 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da questão 16 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta da questão 17 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta da questão 18 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta da questão 19 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta da questão 20 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta da questão 21 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta da questão 22 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta da questão 23 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta da questão 24 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta da questão 25 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta da questão 26 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta da questão 27 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta da questão 28 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta da questão 29 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta da questão 30 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta da questão 31 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta da questão 32 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta da questão 33 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta da questão 34 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta da questão 35 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta da questão 36 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta da questão 37 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta da questão 38 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta da questão 39 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta da questão 40 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta da questão 41 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta da questão 42 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta da questão 43 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta da questão 44 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta da questão 45 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta da questão 46 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta da questão 47 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta da questão 48 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta da questão 49 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta da questão 50 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta da questão 51 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta da questão 52 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta da questão 53 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta da questão 54 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta da questão 55 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta da questão 56 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta da questão 57 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta da questão 58 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta da questão 59 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta da questão 60 do questionário socioeconômico do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2017_ts_aluno_3em_esc

File `raw__inep_saeb_microdados_csv_2017_ts_aluno_3em_esc.parquet` · 1,456,325 rows · 95 columns

Raw do microdado CSV TS_ALUNO_3EM_ESC.csv do Saeb 2017, arquivo oficial microdados_saeb_2017.zip.

**Feeds:** `raw/inep_saeb_aluno_2017`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de realização da edição do SAEB/Prova Brasil (ex: 2017). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área da escola (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de rede escolar pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador único da turma. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série/ano escolar avaliado (ex: 5: 5º ano, 9: 9º ano, 12: 3ª série EM). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Código identificador único do aluno na avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação do aluno no Censo Escolar (1: Matrocinado/Ativo). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador se o aluno preencheu a folha de respostas da prova (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PRESENCA_PROVA` | STRING | Indicador de presença do aluno no dia da aplicação (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Código do caderno do teste/prova respondido pelo aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Código do primeiro bloco de itens respondido no caderno. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Código do segundo bloco de itens respondido no caderno. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | Vetor com as opções assinaladas pelo aluno no Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | Vetor com as opções assinaladas pelo aluno no Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | Vetor com as opções assinaladas pelo aluno no Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | Vetor com as opções assinaladas pelo aluno no Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador se o aluno possui proficiência válida calculada (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Indicador de participação nos critérios de divulgação da Prova Brasil (1: Sim, 0: Não). — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da ANEB/SAEB para ponderação estatística. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostragem do aluno atribuído no cálculo estatístico de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostragem do aluno atribuído no cálculo estatístico de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota do aluno em Língua Portuguesa na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência do aluno em Língua Portuguesa (escala padronizada). — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota/proficiência do aluno em Língua Portuguesa na escala do SAEB (ex: 0 a 500). — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota do aluno em Matemática na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência do aluno em Matemática (escala padronizada). — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota/proficiência do aluno em Matemática na escala do SAEB (ex: 0 a 500). — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência em Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador se o questionário socioeconômico foi preenchido pelo aluno (1: Sim, 0: Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta informada pelo aluno para a questão 1 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta informada pelo aluno para a questão 2 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta informada pelo aluno para a questão 3 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta informada pelo aluno para a questão 4 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta informada pelo aluno para a questão 5 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta informada pelo aluno para a questão 6 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta informada pelo aluno para a questão 7 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta informada pelo aluno para a questão 8 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta informada pelo aluno para a questão 9 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta informada pelo aluno para a questão 10 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta informada pelo aluno para a questão 11 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta informada pelo aluno para a questão 12 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta informada pelo aluno para a questão 13 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta informada pelo aluno para a questão 14 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta informada pelo aluno para a questão 15 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta informada pelo aluno para a questão 16 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta informada pelo aluno para a questão 17 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta informada pelo aluno para a questão 18 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta informada pelo aluno para a questão 19 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta informada pelo aluno para a questão 20 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta informada pelo aluno para a questão 21 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta informada pelo aluno para a questão 22 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta informada pelo aluno para a questão 23 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta informada pelo aluno para a questão 24 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta informada pelo aluno para a questão 25 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta informada pelo aluno para a questão 26 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta informada pelo aluno para a questão 27 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta informada pelo aluno para a questão 28 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta informada pelo aluno para a questão 29 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta informada pelo aluno para a questão 30 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta informada pelo aluno para a questão 31 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta informada pelo aluno para a questão 32 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta informada pelo aluno para a questão 33 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta informada pelo aluno para a questão 34 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta informada pelo aluno para a questão 35 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta informada pelo aluno para a questão 36 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta informada pelo aluno para a questão 37 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta informada pelo aluno para a questão 38 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta informada pelo aluno para a questão 39 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta informada pelo aluno para a questão 40 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta informada pelo aluno para a questão 41 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta informada pelo aluno para a questão 42 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta informada pelo aluno para a questão 43 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta informada pelo aluno para a questão 44 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta informada pelo aluno para a questão 45 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta informada pelo aluno para a questão 46 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta informada pelo aluno para a questão 47 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta informada pelo aluno para a questão 48 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta informada pelo aluno para a questão 49 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta informada pelo aluno para a questão 50 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta informada pelo aluno para a questão 51 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta informada pelo aluno para a questão 52 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta informada pelo aluno para a questão 53 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta informada pelo aluno para a questão 54 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta informada pelo aluno para a questão 55 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta informada pelo aluno para a questão 56 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta informada pelo aluno para a questão 57 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta informada pelo aluno para a questão 58 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta informada pelo aluno para a questão 59 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta informada pelo aluno para a questão 60 do questionário socioeconômico. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2017_ts_aluno_5ef

File `raw__inep_saeb_microdados_csv_2017_ts_aluno_5ef.parquet` · 2,624,019 rows · 86 columns

Raw do microdado CSV TS_ALUNO_5EF.csv do Saeb 2017, arquivo oficial microdados_saeb_2017.zip.

**Feeds:** `raw/inep_saeb_aluno_2017`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de realização da edição da Prova Brasil / SAEB (ex: 2017). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do estado (Unidade da Federação) onde a escola está localizada. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código do tipo de área da escola (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública da escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código de identificação da turma do aluno. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Ano ou série escolar do aluno avaliado (ex: 5 para 5º ano do EF). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único e anonimizado do aluno no sistema da avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno conforme o Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador se o aluno preencheu o caderno de provas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PRESENCA_PROVA` | STRING | Indicador de presença do aluno no dia da aplicação da prova (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Código do caderno de prova atribuído ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Código do primeiro bloco de itens sorteado para a prova do aluno. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Código do segundo bloco de itens sorteado para a prova do aluno. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | String com a sequência de respostas marcadas pelo aluno no Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | String com a sequência de respostas marcadas pelo aluno no Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | String com a sequência de respostas marcadas pelo aluno no Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | String com a sequência de respostas marcadas pelo aluno no Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador se a proficiência do aluno foi calculada com sucesso (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Indicador se o aluno participou da amostra censitária da Prova Brasil (1: Sim, 0: Não). — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da ANEB usado para expansão dos dados. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Fator/peso de expansão estatística do aluno para análises de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Fator/peso de expansão estatística do aluno para análises de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência estimada do aluno em Língua Portuguesa (escala TRI original). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota de proficiência do aluno em Língua Portuguesa padronizada na escala histórica do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da medida de proficiência de Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência estimada do aluno em Matemática (escala TRI original). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota de proficiência do aluno em Matemática padronizada na escala histórica do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da medida de proficiência de Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico do aluno (1: Sim, 0: Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta do aluno à questão 001 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta do aluno à questão 002 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta do aluno à questão 003 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta do aluno à questão 004 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta do aluno à questão 005 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta do aluno à questão 006 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta do aluno à questão 007 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta do aluno à questão 008 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta do aluno à questão 009 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta do aluno à questão 010 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta do aluno à questão 011 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta do aluno à questão 012 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta do aluno à questão 013 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta do aluno à questão 014 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta do aluno à questão 015 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta do aluno à questão 016 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta do aluno à questão 017 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta do aluno à questão 018 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta do aluno à questão 019 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta do aluno à questão 020 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta do aluno à questão 021 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta do aluno à questão 022 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta do aluno à questão 023 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta do aluno à questão 024 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta do aluno à questão 025 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta do aluno à questão 026 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta do aluno à questão 027 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta do aluno à questão 028 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta do aluno à questão 029 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta do aluno à questão 030 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta do aluno à questão 031 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta do aluno à questão 032 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta do aluno à questão 033 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta do aluno à questão 034 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta do aluno à questão 035 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta do aluno à questão 036 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta do aluno à questão 037 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta do aluno à questão 038 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta do aluno à questão 039 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta do aluno à questão 040 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta do aluno à questão 041 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta do aluno à questão 042 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta do aluno à questão 043 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta do aluno à questão 044 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta do aluno à questão 045 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta do aluno à questão 046 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta do aluno à questão 047 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta do aluno à questão 048 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta do aluno à questão 049 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta do aluno à questão 050 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta do aluno à questão 051 do questionário socioeconômico. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2017_ts_aluno_9ef

File `raw__inep_saeb_microdados_csv_2017_ts_aluno_9ef.parquet` · 2,341,459 rows · 92 columns

Raw do microdado CSV TS_ALUNO_9EF.csv do Saeb 2017, arquivo oficial microdados_saeb_2017.zip.

**Feeds:** `raw/inep_saeb_aluno_2017`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de edição da Prova Brasil / SAEB. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade Federativa da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código da área de localização (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1: Pública, 0: Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador único da turma no INEP. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série ou ano escolar avaliado do aluno (ex: 5 para 5º ano, 9 para 9º ano). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único do aluno na edição da avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno no Censo Escolar (1: Regular). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_PROVA` | STRING | Indicador de preenchimento do cartão de respostas da prova (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PRESENCA_PROVA` | STRING | Indicador de presença do aluno na avaliação (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `ID_CADERNO` | STRING | Código do caderno de prova atribuído ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1` | STRING | Código do primeiro bloco de itens aplicado. — descrição gerada por IA. |
| `ID_BLOCO_2` | STRING | Código do segundo bloco de itens aplicado. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_LP` | STRING | String contendo o vetor de respostas do bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_LP` | STRING | String contendo o vetor de respostas do bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO_1_MT` | STRING | String contendo o vetor de respostas do bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO_2_MT` | STRING | String contendo o vetor de respostas do bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA` | STRING | Indicador de proficiência calculada para o aluno (1: Possui proficiência, 0: Não possui). — descrição gerada por IA. |
| `IN_PROVA_BRASIL` | STRING | Indicador de inclusão no estrato da Prova Brasil (1: Sim, 0: Não). — descrição gerada por IA. |
| `ESTRATO_ANEB` | STRING | Código do estrato amostral da ANEB/SAEB para ponderação estatística. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para análises de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para análises de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência estimada do aluno em Língua Portuguesa (Escala TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência do aluno em Língua Portuguesa padronizada na escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência de Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência estimada do aluno em Matemática (Escala TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência do aluno em Matemática padronizada na escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência de Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico (1: Sim, 0: Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta assinalada para a questão 1 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta assinalada para a questão 2 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta assinalada para a questão 3 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta assinalada para a questão 4 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta assinalada para a questão 5 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta assinalada para a questão 6 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta assinalada para a questão 7 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta assinalada para a questão 8 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta assinalada para a questão 9 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta assinalada para a questão 10 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta assinalada para a questão 11 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta assinalada para a questão 12 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta assinalada para a questão 13 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta assinalada para a questão 14 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta assinalada para a questão 15 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta assinalada para a questão 16 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta assinalada para a questão 17 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta assinalada para a questão 18 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta assinalada para a questão 19 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta assinalada para a questão 20 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta assinalada para a questão 21 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta assinalada para a questão 22 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta assinalada para a questão 23 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta assinalada para a questão 24 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta assinalada para a questão 25 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta assinalada para a questão 26 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta assinalada para a questão 27 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta assinalada para a questão 28 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta assinalada para a questão 29 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta assinalada para a questão 30 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta assinalada para a questão 31 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta assinalada para a questão 32 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta assinalada para a questão 33 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta assinalada para a questão 34 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta assinalada para a questão 35 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta assinalada para a questão 36 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta assinalada para a questão 37 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta assinalada para a questão 38 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta assinalada para a questão 39 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta assinalada para a questão 40 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta assinalada para a questão 41 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta assinalada para a questão 42 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta assinalada para a questão 43 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta assinalada para a questão 44 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta assinalada para a questão 45 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta assinalada para a questão 46 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta assinalada para a questão 47 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta assinalada para a questão 48 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta assinalada para a questão 49 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta assinalada para a questão 50 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta assinalada para a questão 51 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta assinalada para a questão 52 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta assinalada para a questão 53 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta assinalada para a questão 54 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta assinalada para a questão 55 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta assinalada para a questão 56 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta assinalada para a questão 57 do questionário socioeconômico do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2017_ts_diretor

File `raw__inep_saeb_microdados_csv_2017_ts_diretor.parquet` · 73,674 rows · 118 columns

Raw do microdado CSV TS_DIRETOR.csv do Saeb 2017, arquivo oficial microdados_saeb_2017.zip.

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de realização da edição da Prova Brasil/SAEB (ex: 2017). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE de 2 dígitos referente à Unidade da Federação da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE referente ao município onde a escola está localizada. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP/Censo Escolar de identificação única da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de rede pública de ensino (1 para Escola Pública, 0 para Não Pública). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código da localização da escola (1 para Urbana, 2 para Rural). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário contextual (1 para preenchido, 0 para não preenchido). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta fornecida (letra da alternativa) para a questão 1 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta fornecida (letra da alternativa) para a questão 2 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta fornecida (letra da alternativa) para a questão 3 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta fornecida (letra da alternativa) para a questão 4 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta fornecida (letra da alternativa) para a questão 5 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta fornecida (letra da alternativa) para a questão 6 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta fornecida (letra da alternativa) para a questão 7 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta fornecida (letra da alternativa) para a questão 8 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta fornecida (letra da alternativa) para a questão 9 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta fornecida (letra da alternativa) para a questão 10 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta fornecida (letra da alternativa) para a questão 11 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta fornecida (letra da alternativa) para a questão 12 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta fornecida (letra da alternativa) para a questão 13 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta fornecida (letra da alternativa) para a questão 14 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta fornecida (letra da alternativa) para a questão 15 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta fornecida (letra da alternativa) para a questão 16 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta fornecida (letra da alternativa) para a questão 17 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta fornecida (letra da alternativa) para a questão 18 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta fornecida (letra da alternativa) para a questão 19 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta fornecida (letra da alternativa) para a questão 20 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta fornecida (letra da alternativa) para a questão 21 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta fornecida (letra da alternativa) para a questão 22 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta fornecida (letra da alternativa) para a questão 23 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta fornecida (letra da alternativa) para a questão 24 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta fornecida (letra da alternativa) para a questão 25 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta fornecida (letra da alternativa) para a questão 26 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta fornecida (letra da alternativa) para a questão 27 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta fornecida (letra da alternativa) para a questão 28 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta fornecida (letra da alternativa) para a questão 29 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta fornecida (letra da alternativa) para a questão 30 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta fornecida (letra da alternativa) para a questão 31 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta fornecida (letra da alternativa) para a questão 32 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta fornecida (letra da alternativa) para a questão 33 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta fornecida (letra da alternativa) para a questão 34 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta fornecida (letra da alternativa) para a questão 35 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta fornecida (letra da alternativa) para a questão 36 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta fornecida (letra da alternativa) para a questão 37 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta fornecida (letra da alternativa) para a questão 38 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta fornecida (letra da alternativa) para a questão 39 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta fornecida (letra da alternativa) para a questão 40 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta fornecida (letra da alternativa) para a questão 41 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta fornecida (letra da alternativa) para a questão 42 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta fornecida (letra da alternativa) para a questão 43 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta fornecida (letra da alternativa) para a questão 44 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta fornecida (letra da alternativa) para a questão 45 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta fornecida (letra da alternativa) para a questão 46 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta fornecida (letra da alternativa) para a questão 47 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta fornecida (letra da alternativa) para a questão 48 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta fornecida (letra da alternativa) para a questão 49 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta fornecida (letra da alternativa) para a questão 50 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta fornecida (letra da alternativa) para a questão 51 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta fornecida (letra da alternativa) para a questão 52 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta fornecida (letra da alternativa) para a questão 53 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta fornecida (letra da alternativa) para a questão 54 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta fornecida (letra da alternativa) para a questão 55 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta fornecida (letra da alternativa) para a questão 56 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta fornecida (letra da alternativa) para a questão 57 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta fornecida (letra da alternativa) para a questão 58 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta fornecida (letra da alternativa) para a questão 59 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta fornecida (letra da alternativa) para a questão 60 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta fornecida (letra da alternativa) para a questão 61 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta fornecida (letra da alternativa) para a questão 62 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta fornecida (letra da alternativa) para a questão 63 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta fornecida (letra da alternativa) para a questão 64 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta fornecida (letra da alternativa) para a questão 65 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta fornecida (letra da alternativa) para a questão 66 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta fornecida (letra da alternativa) para a questão 67 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta fornecida (letra da alternativa) para a questão 68 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta fornecida (letra da alternativa) para a questão 69 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta fornecida (letra da alternativa) para a questão 70 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta fornecida (letra da alternativa) para a questão 71 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta fornecida (letra da alternativa) para a questão 72 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta fornecida (letra da alternativa) para a questão 73 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta fornecida (letra da alternativa) para a questão 74 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Resposta fornecida (letra da alternativa) para a questão 75 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Resposta fornecida (letra da alternativa) para a questão 76 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Resposta fornecida (letra da alternativa) para a questão 77 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Resposta fornecida (letra da alternativa) para a questão 78 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Resposta fornecida (letra da alternativa) para a questão 79 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Resposta fornecida (letra da alternativa) para a questão 80 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Resposta fornecida (letra da alternativa) para a questão 81 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Resposta fornecida (letra da alternativa) para a questão 82 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Resposta fornecida (letra da alternativa) para a questão 83 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Resposta fornecida (letra da alternativa) para a questão 84 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Resposta fornecida (letra da alternativa) para a questão 85 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Resposta fornecida (letra da alternativa) para a questão 86 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Resposta fornecida (letra da alternativa) para a questão 87 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Resposta fornecida (letra da alternativa) para a questão 88 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Resposta fornecida (letra da alternativa) para a questão 89 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Resposta fornecida (letra da alternativa) para a questão 90 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Resposta fornecida (letra da alternativa) para a questão 91 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Resposta fornecida (letra da alternativa) para a questão 92 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Resposta fornecida (letra da alternativa) para a questão 93 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Resposta fornecida (letra da alternativa) para a questão 94 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Resposta fornecida (letra da alternativa) para a questão 95 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Resposta fornecida (letra da alternativa) para a questão 96 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Resposta fornecida (letra da alternativa) para a questão 97 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Resposta fornecida (letra da alternativa) para a questão 98 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Resposta fornecida (letra da alternativa) para a questão 99 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Resposta fornecida (letra da alternativa) para a questão 100 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Resposta fornecida (letra da alternativa) para a questão 101 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Resposta fornecida (letra da alternativa) para a questão 102 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Resposta fornecida (letra da alternativa) para a questão 103 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Resposta fornecida (letra da alternativa) para a questão 104 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Resposta fornecida (letra da alternativa) para a questão 105 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Resposta fornecida (letra da alternativa) para a questão 106 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Resposta fornecida (letra da alternativa) para a questão 107 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Resposta fornecida (letra da alternativa) para a questão 108 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Resposta fornecida (letra da alternativa) para a questão 109 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Resposta fornecida (letra da alternativa) para a questão 110 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Resposta fornecida (letra da alternativa) para a questão 111 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2017_ts_escola

File `raw__inep_saeb_microdados_csv_2017_ts_escola.parquet` · 73,674 rows · 154 columns

Raw do microdado CSV TS_ESCOLA.csv do Saeb 2017, arquivo oficial microdados_saeb_2017.zip.

**Feeds:** `trusted/inep_saeb_escola`, `trusted/inep_saeb_microdados_escola`

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano de realização da Prova Brasil/SAEB. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do Estado (Unidade da Federação) onde a escola está localizada. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do Município onde a escola está localizada. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP/Censo Escolar de identificação única da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola é da rede pública (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_INICIAL` | STRING | Percentual de docentes com formação superior adequada nos anos iniciais do Ensino Fundamental. — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_FINAL` | STRING | Percentual de docentes com formação superior adequada nos anos finais do Ensino Fundamental. — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_MEDIO` | STRING | Percentual de docentes com formação superior adequada no Ensino Médio. — descrição gerada por IA. |
| `NIVEL_SOCIO_ECONOMICO` | STRING | Classificação do Indicador de Nível Socioeconômico (INSE) da escola. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_5EF` | STRING | Número de alunos matriculados no 5º ano do Ensino Fundamental segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_5EF` | STRING | Número de alunos do 5º ano do Ensino Fundamental presentes no dia do exame. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_5EF` | STRING | Proporção de alunos participantes em relação aos matriculados no 5º ano do EF. — descrição gerada por IA. |
| `NIVEL_0_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_9_LP5` | STRING | Percentual de alunos do 5º ano do EF no nível 9 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_10_MT5` | STRING | Percentual de alunos do 5º ano do EF no nível 10 de proficiência em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_9EF` | STRING | Número de alunos matriculados no 9º ano do Ensino Fundamental segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_9EF` | STRING | Número de alunos do 9º ano do Ensino Fundamental presentes no dia do exame. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_9EF` | STRING | Proporção de alunos participantes em relação aos matriculados no 9º ano do EF. — descrição gerada por IA. |
| `NIVEL_0_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP9` | STRING | Percentual de alunos do 9º ano do EF no nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT9` | STRING | Percentual de alunos do 9º ano do EF no nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_3EM` | STRING | Número de alunos matriculados no 3º ano do Ensino Médio segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_3EM` | STRING | Número de alunos do 3º ano do Ensino Médio presentes no dia do exame. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_3EM` | STRING | Proporção de alunos participantes em relação aos matriculados no 3º ano do Ensino Médio. — descrição gerada por IA. |
| `NIVEL_0_LP3` | STRING | Percentual de alunos do 3º ano do EM no nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP3` | STRING | Percentual de alunos do 3º ano do EM no nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP3` | STRING | Percentual de alunos do 3º ano do EM no nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP3` | STRING | Percentual de alunos do 3º ano do EM no nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP3` | STRING | Percentual de alunos do 3º ano do EM no nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP3` | STRING | Percentual de alunos do 3º ano do EM no nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP3` | STRING | Percentual de alunos do 3º ano do EM no nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP3` | STRING | Percentual de alunos do 3º ano do EM no nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP3` | STRING | Percentual de alunos do 3º ano do EM no nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_10_MT3` | STRING | Percentual de alunos do 3º ano do EM no nível 10 de proficiência em Matemática. — descrição gerada por IA. |
| `MEDIA_5EF_LP` | STRING | Nota média padronizada em Língua Portuguesa dos alunos do 5º ano do EF na escala SAEB. — descrição gerada por IA. |
| `MEDIA_5EF_MT` | STRING | Nota média padronizada em Matemática dos alunos do 5º ano do EF na escala SAEB. — descrição gerada por IA. |
| `MEDIA_9EF_LP` | STRING | Nota média padronizada em Língua Portuguesa dos alunos do 9º ano do EF na escala SAEB. — descrição gerada por IA. |
| `MEDIA_9EF_MT` | STRING | Nota média padronizada em Matemática dos alunos do 9º ano do EF na escala SAEB. — descrição gerada por IA. |
| `MEDIA_3EM_LP` | STRING | Nota média padronizada em Língua Portuguesa dos alunos do 3º ano do EM na escala SAEB. — descrição gerada por IA. |
| `MEDIA_3EM_MT` | STRING | Nota média padronizada em Matemática dos alunos do 3º ano do EM na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário do diretor/escola (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Opção assinalada na questão 7 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Opção assinalada na questão 8 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Opção assinalada na questão 9 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Opção assinalada na questão 10 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Opção assinalada na questão 11 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Opção assinalada na questão 12 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Opção assinalada na questão 13 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Opção assinalada na questão 14 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Opção assinalada na questão 15 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Opção assinalada na questão 16 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Opção assinalada na questão 17 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Opção assinalada na questão 18 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Opção assinalada na questão 19 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Opção assinalada na questão 20 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Opção assinalada na questão 21 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Opção assinalada na questão 22 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Opção assinalada na questão 23 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Opção assinalada na questão 24 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Opção assinalada na questão 25 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Opção assinalada na questão 26 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Opção assinalada na questão 27 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Opção assinalada na questão 28 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Opção assinalada na questão 29 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Opção assinalada na questão 30 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Opção assinalada na questão 31 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Opção assinalada na questão 32 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Opção assinalada na questão 33 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Opção assinalada na questão 34 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Opção assinalada na questão 35 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Opção assinalada na questão 36 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Opção assinalada na questão 37 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Opção assinalada na questão 38 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Opção assinalada na questão 39 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Opção assinalada na questão 40 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Opção assinalada na questão 41 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Opção assinalada na questão 42 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Opção assinalada na questão 43 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Opção assinalada na questão 44 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Opção assinalada na questão 45 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Opção assinalada na questão 46 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Opção assinalada na questão 47 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Opção assinalada na questão 48 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Opção assinalada na questão 49 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Opção assinalada na questão 50 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Opção assinalada na questão 51 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Opção assinalada na questão 52 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Opção assinalada na questão 53 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Opção assinalada na questão 54 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Opção assinalada na questão 55 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Opção assinalada na questão 56 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Opção assinalada na questão 57 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Opção assinalada na questão 58 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Opção assinalada na questão 59 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Opção assinalada na questão 60 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Opção assinalada na questão 61 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Opção assinalada na questão 62 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Opção assinalada na questão 63 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Opção assinalada na questão 64 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Opção assinalada na questão 65 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Opção assinalada na questão 66 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Opção assinalada na questão 67 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Opção assinalada na questão 68 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Opção assinalada na questão 69 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Opção assinalada na questão 70 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Opção assinalada na questão 71 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Opção assinalada na questão 72 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Opção assinalada na questão 73 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Opção assinalada na questão 74 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2017_ts_item

File `raw__inep_saeb_microdados_csv_2017_ts_item.parquet` · 518 rows · 15 columns

Raw do microdado CSV TS_ITEM.csv do Saeb 2017, arquivo oficial microdados_saeb_2017.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano ou edicao de realizacao do exame SAEB (ex: '2017'). — descrição gerada por IA. |
| `DISCIPLINA` | STRING | Sigla da disciplina avaliada no exame (ex: 'LP' para Lingua Portuguesa). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Ano ou serie escolar dos alunos avaliados (ex: '5' para o 5º ano do Ensino Fundamental). — descrição gerada por IA. |
| `BLOCO` | STRING | Numero do bloco de questoes no caderno de aplicacao da prova. — descrição gerada por IA. |
| `POSICAO` | STRING | Ordem ou posicao ocupada pela questao dentro do seu bloco correspondente. — descrição gerada por IA. |
| `ID_ITEM` | STRING | Codigo identificador unico do item/questao no banco de dados do INEP. — descrição gerada por IA. |
| `NU_DESCRITOR_HABILIDADE` | STRING | Codigo do descritor da Matriz de Referencia do SAEB associado a habilidade avaliada (ex: 'D1'). — descrição gerada por IA. |
| `GABARITO` | STRING | Letra correspondente a alternativa correta do item (ex: 'A'). — descrição gerada por IA. |
| `TIPO_ITEM` | STRING | Formato de resposta da questao (ex: 'Resposta Objetiva'). — descrição gerada por IA. |
| `ITEM_MODELO` | STRING | Modelo psicometrico de TRI utilizado na calibracao da questao (ex: 'M3P' para Modelo de 3 Parametros). — descrição gerada por IA. |
| `A` | STRING | Parametro de discriminacao da questao na Teoria de Resposta ao Item (TRI). — descrição gerada por IA. |
| `B` | STRING | Parametro de dificuldade da questao na Teoria de Resposta ao Item (TRI). — descrição gerada por IA. |
| `C` | STRING | Parametro de probabilidade de acerto ao acaso (chute) na TRI. — descrição gerada por IA. |
| `B1` | STRING | Parametro de dificuldade da primeira transicao em itens de resposta graduada/politomica. — descrição gerada por IA. |
| `B2` | STRING | Parametro de dificuldade da segunda transicao em itens de resposta graduada/politomica. — descrição gerada por IA. |
