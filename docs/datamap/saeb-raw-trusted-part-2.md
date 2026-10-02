# SAEB assessment (INEP): Raw and Trusted

Dataset: [lucasrangelss/saeb-raw-trusted-part-2](https://www.kaggle.com/datasets/lucasrangelss/saeb-raw-trusted-part-2) · snapshot 2026-10-02 · 40 tables · 24,401,699 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/saeb)

SAEB results: aggregated proficiency indicators, the school report-card API (boletim) for 2011 onward, and the assessment microdata tables released without student-level records.

**Grain and keys:** Indicators: school, municipality, state or Brazil by edition. Boletim: school by edition. The publication format changes between editions, so each edition is validated against the live source.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`inep_saeb_microdados_csv_2017_ts_professor`](#raw-inep-saeb-microdados-csv-2017-ts-professor) | 753,668 | 135 | 135 | source |
| raw | [`inep_saeb_microdados_csv_2019_ts_aluno_2ef`](#raw-inep-saeb-microdados-csv-2019-ts-aluno-2ef) | 85,788 | 53 | 53 | source |
| raw | [`inep_saeb_microdados_csv_2019_ts_aluno_34em`](#raw-inep-saeb-microdados-csv-2019-ts-aluno-34em) | 2,018,515 | 91 | 91 | source |
| raw | [`inep_saeb_microdados_csv_2019_ts_aluno_5ef`](#raw-inep-saeb-microdados-csv-2019-ts-aluno-5ef) | 2,581,685 | 89 | 89 | source |
| raw | [`inep_saeb_microdados_csv_2019_ts_aluno_9ef`](#raw-inep-saeb-microdados-csv-2019-ts-aluno-9ef) | 2,388,931 | 129 | 129 | source |
| raw | [`inep_saeb_microdados_csv_2019_ts_diretor`](#raw-inep-saeb-microdados-csv-2019-ts-diretor) | 74,176 | 262 | 262 | source |
| raw | [`inep_saeb_microdados_csv_2019_ts_escola`](#raw-inep-saeb-microdados-csv-2019-ts-escola) | 70,606 | 137 | 137 | source |
| raw | [`inep_saeb_microdados_csv_2019_ts_item`](#raw-inep-saeb-microdados-csv-2019-ts-item) | 854 | 15 | 15 | source |
| raw | [`inep_saeb_microdados_csv_2019_ts_professor`](#raw-inep-saeb-microdados-csv-2019-ts-professor) | 388,119 | 140 | 140 | source |
| raw | [`inep_saeb_microdados_csv_2019_ts_secretario_municipal`](#raw-inep-saeb-microdados-csv-2019-ts-secretario-municipal) | 5,412 | 204 | 204 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_aluno_2ef`](#raw-inep-saeb-microdados-csv-2021-ts-aluno-2ef) | 29,819 | 53 | 53 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_aluno_34em`](#raw-inep-saeb-microdados-csv-2021-ts-aluno-34em) | 2,288,747 | 106 | 106 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_aluno_5ef`](#raw-inep-saeb-microdados-csv-2021-ts-aluno-5ef) | 2,554,184 | 104 | 104 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_aluno_9ef`](#raw-inep-saeb-microdados-csv-2021-ts-aluno-9ef) | 2,591,937 | 144 | 144 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_diretor`](#raw-inep-saeb-microdados-csv-2021-ts-diretor) | 74,539 | 219 | 219 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_educacao_infantil_2021`](#raw-inep-saeb-microdados-csv-2021-ts-educacao-infantil-2021) | 62,927 | 421 | 421 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_escola`](#raw-inep-saeb-microdados-csv-2021-ts-escola) | 70,897 | 137 | 137 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_item`](#raw-inep-saeb-microdados-csv-2021-ts-item) | 854 | 15 | 15 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_professor`](#raw-inep-saeb-microdados-csv-2021-ts-professor) | 565,640 | 135 | 135 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_secretario_municipal`](#raw-inep-saeb-microdados-csv-2021-ts-secretario-municipal) | 5,568 | 140 | 140 | source |
| raw | [`inep_saeb_microdados_csv_2021_ts_secretario_municipal_2021`](#raw-inep-saeb-microdados-csv-2021-ts-secretario-municipal-2021) | 5,568 | 159 | 159 | source |
| raw | [`inep_saeb_microdados_csv_2023_ts_aluno_2ef`](#raw-inep-saeb-microdados-csv-2023-ts-aluno-2ef) | 37,104 | 55 | 55 | source |
| raw | [`inep_saeb_microdados_csv_2023_ts_aluno_34em`](#raw-inep-saeb-microdados-csv-2023-ts-aluno-34em) | 2,091,337 | 117 | 117 | source |
| raw | [`inep_saeb_microdados_csv_2023_ts_aluno_5ef`](#raw-inep-saeb-microdados-csv-2023-ts-aluno-5ef) | 2,442,143 | 152 | 152 | source |
| raw | [`inep_saeb_microdados_csv_2023_ts_aluno_9ef`](#raw-inep-saeb-microdados-csv-2023-ts-aluno-9ef) | 2,502,907 | 153 | 153 | source |
| raw | [`inep_saeb_microdados_csv_2023_ts_diretor`](#raw-inep-saeb-microdados-csv-2023-ts-diretor) | 107,089 | 237 | 237 | source |
| raw | [`inep_saeb_microdados_csv_2023_ts_escola`](#raw-inep-saeb-microdados-csv-2023-ts-escola) | 70,151 | 137 | 137 | source |
| raw | [`inep_saeb_microdados_csv_2023_ts_item`](#raw-inep-saeb-microdados-csv-2023-ts-item) | 993 | 16 | 16 | source |
| raw | [`inep_saeb_microdados_csv_2023_ts_professor`](#raw-inep-saeb-microdados-csv-2023-ts-professor) | 411,876 | 162 | 162 | source |
| raw | [`inep_saeb_microdados_csv_2023_ts_secretario_municipal`](#raw-inep-saeb-microdados-csv-2023-ts-secretario-municipal) | 5,568 | 182 | 182 | source |
| raw | [`inep_saeb_microdados_csv_tabelas`](#raw-inep-saeb-microdados-csv-tabelas) | 64 | 13 | 13 | source |
| raw | [`inep_saeb_microdados_txt_1997_biologia_03ano_txt`](#raw-inep-saeb-microdados-txt-1997-biologia-03ano-txt) | 8,005 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_ciencias_04serie_txt`](#raw-inep-saeb-microdados-txt-1997-ciencias-04serie-txt) | 23,506 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_ciencias_08serie_txt`](#raw-inep-saeb-microdados-txt-1997-ciencias-08serie-txt) | 18,822 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_diretor_97_txt`](#raw-inep-saeb-microdados-txt-1997-diretor-97-txt) | 2,351 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_docente_97_txt`](#raw-inep-saeb-microdados-txt-1997-docente-97-txt) | 19,339 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_escola_97_txt`](#raw-inep-saeb-microdados-txt-1997-escola-97-txt) | 2,351 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_fisica_03ano_txt`](#raw-inep-saeb-microdados-txt-1997-fisica-03ano-txt) | 7,988 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_matematica_03ano_txt`](#raw-inep-saeb-microdados-txt-1997-matematica-03ano-txt) | 8,136 | 1 | 1 | source |
| raw | [`inep_saeb_microdados_txt_1997_matematica_04serie_txt`](#raw-inep-saeb-microdados-txt-1997-matematica-04serie-txt) | 23,535 | 1 | 1 | source |

## raw · inep_saeb_microdados_csv_2017_ts_professor

File `raw__inep_saeb_microdados_csv_2017_ts_professor.parquet` · 753,668 rows · 135 columns

Raw do microdado CSV TS_PROFESSOR.csv do Saeb 2017, arquivo oficial microdados_saeb_2017.zip.

| Column | Type | Description |
|---|---|---|
| `ID_PROVA_BRASIL` | STRING | Ano da edição da avaliação da Prova Brasil / SAEB. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade Federativa (estado) onde a escola está localizada. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de escola pública (1 para pública, 0 para privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 para Urbana, 2 para Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código de identificação da turma na avaliação. — descrição gerada por IA. |
| `CO_PROFESSOR` | STRING | Código de identificação do docente no sistema do SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código correspondente à série/ano escolar avaliado (ex: 5 para 5º ano, 9 para 9º ano do Ensino Fundamental). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário pelo professor (1 para preenchido, 0 para não preenchido). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta fornecida pelo professor para a questão 001 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta fornecida pelo professor para a questão 002 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta fornecida pelo professor para a questão 003 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta fornecida pelo professor para a questão 004 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta fornecida pelo professor para a questão 005 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta fornecida pelo professor para a questão 006 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta fornecida pelo professor para a questão 007 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta fornecida pelo professor para a questão 008 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta fornecida pelo professor para a questão 009 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta fornecida pelo professor para a questão 010 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta fornecida pelo professor para a questão 011 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta fornecida pelo professor para a questão 012 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta fornecida pelo professor para a questão 013 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta fornecida pelo professor para a questão 014 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta fornecida pelo professor para a questão 015 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta fornecida pelo professor para a questão 016 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta fornecida pelo professor para a questão 017 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta fornecida pelo professor para a questão 018 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta fornecida pelo professor para a questão 019 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta fornecida pelo professor para a questão 020 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta fornecida pelo professor para a questão 021 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta fornecida pelo professor para a questão 022 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta fornecida pelo professor para a questão 023 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta fornecida pelo professor para a questão 024 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta fornecida pelo professor para a questão 025 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta fornecida pelo professor para a questão 026 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta fornecida pelo professor para a questão 027 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta fornecida pelo professor para a questão 028 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta fornecida pelo professor para a questão 029 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta fornecida pelo professor para a questão 030 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta fornecida pelo professor para a questão 031 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta fornecida pelo professor para a questão 032 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta fornecida pelo professor para a questão 033 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta fornecida pelo professor para a questão 034 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta fornecida pelo professor para a questão 035 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta fornecida pelo professor para a questão 036 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta fornecida pelo professor para a questão 037 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta fornecida pelo professor para a questão 038 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta fornecida pelo professor para a questão 039 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta fornecida pelo professor para a questão 040 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta fornecida pelo professor para a questão 041 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta fornecida pelo professor para a questão 042 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta fornecida pelo professor para a questão 043 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta fornecida pelo professor para a questão 044 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta fornecida pelo professor para a questão 045 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta fornecida pelo professor para a questão 046 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta fornecida pelo professor para a questão 047 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta fornecida pelo professor para a questão 048 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta fornecida pelo professor para a questão 049 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta fornecida pelo professor para a questão 050 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta fornecida pelo professor para a questão 051 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta fornecida pelo professor para a questão 052 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta fornecida pelo professor para a questão 053 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta fornecida pelo professor para a questão 054 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta fornecida pelo professor para a questão 055 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta fornecida pelo professor para a questão 056 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta fornecida pelo professor para a questão 057 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta fornecida pelo professor para a questão 058 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta fornecida pelo professor para a questão 059 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta fornecida pelo professor para a questão 060 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta fornecida pelo professor para a questão 061 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta fornecida pelo professor para a questão 062 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta fornecida pelo professor para a questão 063 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta fornecida pelo professor para a questão 064 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta fornecida pelo professor para a questão 065 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta fornecida pelo professor para a questão 066 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta fornecida pelo professor para a questão 067 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta fornecida pelo professor para a questão 068 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta fornecida pelo professor para a questão 069 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta fornecida pelo professor para a questão 070 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta fornecida pelo professor para a questão 071 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta fornecida pelo professor para a questão 072 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta fornecida pelo professor para a questão 073 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta fornecida pelo professor para a questão 074 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Resposta fornecida pelo professor para a questão 075 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Resposta fornecida pelo professor para a questão 076 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Resposta fornecida pelo professor para a questão 077 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Resposta fornecida pelo professor para a questão 078 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Resposta fornecida pelo professor para a questão 079 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Resposta fornecida pelo professor para a questão 080 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Resposta fornecida pelo professor para a questão 081 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Resposta fornecida pelo professor para a questão 082 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Resposta fornecida pelo professor para a questão 083 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Resposta fornecida pelo professor para a questão 084 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Resposta fornecida pelo professor para a questão 085 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Resposta fornecida pelo professor para a questão 086 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Resposta fornecida pelo professor para a questão 087 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Resposta fornecida pelo professor para a questão 088 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Resposta fornecida pelo professor para a questão 089 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Resposta fornecida pelo professor para a questão 090 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Resposta fornecida pelo professor para a questão 091 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Resposta fornecida pelo professor para a questão 092 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Resposta fornecida pelo professor para a questão 093 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Resposta fornecida pelo professor para a questão 094 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Resposta fornecida pelo professor para a questão 095 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Resposta fornecida pelo professor para a questão 096 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Resposta fornecida pelo professor para a questão 097 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Resposta fornecida pelo professor para a questão 098 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Resposta fornecida pelo professor para a questão 099 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Resposta fornecida pelo professor para a questão 100 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Resposta fornecida pelo professor para a questão 101 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Resposta fornecida pelo professor para a questão 102 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Resposta fornecida pelo professor para a questão 103 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Resposta fornecida pelo professor para a questão 104 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Resposta fornecida pelo professor para a questão 105 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Resposta fornecida pelo professor para a questão 106 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Resposta fornecida pelo professor para a questão 107 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Resposta fornecida pelo professor para a questão 108 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Resposta fornecida pelo professor para a questão 109 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Resposta fornecida pelo professor para a questão 110 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Resposta fornecida pelo professor para a questão 111 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Resposta fornecida pelo professor para a questão 112 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Resposta fornecida pelo professor para a questão 113 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Resposta fornecida pelo professor para a questão 114 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Resposta fornecida pelo professor para a questão 115 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Resposta fornecida pelo professor para a questão 116 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Resposta fornecida pelo professor para a questão 117 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Resposta fornecida pelo professor para a questão 118 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Resposta fornecida pelo professor para a questão 119 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Resposta fornecida pelo professor para a questão 120 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Resposta fornecida pelo professor para a questão 121 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q122` | STRING | Resposta fornecida pelo professor para a questão 122 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q123` | STRING | Resposta fornecida pelo professor para a questão 123 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q124` | STRING | Resposta fornecida pelo professor para a questão 124 do questionário do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q125` | STRING | Resposta fornecida pelo professor para a questão 125 do questionário do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2019_ts_aluno_2ef

File `raw__inep_saeb_microdados_csv_2019_ts_aluno_2ef.parquet` · 85,788 rows · 53 columns

Raw do microdado CSV TS_ALUNO_2EF.csv do Saeb 2019, arquivo oficial microdados_saeb_2019.zip.

**Feeds:** `raw/inep_saeb_aluno_2019`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano da edição do exame SAEB (ex: 2019). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica do IBGE onde se localiza a escola. — descrição gerada por IA. |
| `ID_UF` | STRING | Código da Unidade Federativa (UF) do IBGE. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código do tipo de área da escola (1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1-Sim, 0-Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código da localização da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador único da turma no Censo Escolar/SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série ou ano escolar avaliado. — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único e anonimizado do aluno no SAEB. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador da situação de matrícula no Censo Escolar (1-Matriculado). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento do teste de Língua Portuguesa (1-Preenchido, 0-Não preenchido). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento do teste de Matemática (1-Preenchido, 0-Não preenchido). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença do aluno na prova de Língua Portuguesa (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença do aluno na prova de Matemática (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Número do modelo/caderno de prova aplicado de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Identificador do primeiro bloco de itens de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Identificador do segundo bloco de itens de Língua Portuguesa. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_LP` | STRING | Identificador do bloco de questões abertas 1 de Língua Portuguesa. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_LP` | STRING | Identificador do bloco de questões abertas 2 de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Número do modelo/caderno de prova aplicado de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Identificador do primeiro bloco de itens de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Identificador do segundo bloco de itens de Matemática. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_MT` | STRING | Identificador do bloco de questões abertas 1 de Matemática. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_MT` | STRING | Identificador do bloco de questões abertas 2 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Cadeia de caracteres com as alternativas marcadas no Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Cadeia de caracteres com as alternativas marcadas no Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_LP` | STRING | Conceito/nota atribuída à questão aberta 1 de Língua Portuguesa. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_LP` | STRING | Conceito/nota atribuída à questão aberta 2 de Língua Portuguesa. — descrição gerada por IA. |
| `CO_RESPOSTA_TEXTO` | STRING | Código da resposta da produção textual/redação. — descrição gerada por IA. |
| `CO_CONCEITO_PROPOSITO` | STRING | Conceito atribuído ao propósito comunicativo da produção textual. — descrição gerada por IA. |
| `CO_CONCEITO_ELEMENTO` | STRING | Conceito atribuído aos elementos composicionais do texto. — descrição gerada por IA. |
| `CO_CONCEITO_SEGMENTACAO` | STRING | Conceito atribuído à segmentação do texto. — descrição gerada por IA. |
| `CO_TEXTO_GRAFIA` | STRING | Conceito atribuído à grafia e convenções da escrita no texto. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Cadeia de caracteres com as alternativas marcadas no Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Cadeia de caracteres com as alternativas marcadas no Bloco 2 de Matemática. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_MT` | STRING | Conceito/nota atribuída à questão aberta 1 de Matemática. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_MT` | STRING | Conceito/nota atribuída à questão aberta 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador se a proficiência em Língua Portuguesa foi calculada (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador se a proficiência em Matemática foi calculada (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador se a turma/escola pertence à amostra do SAEB (1-Amostra, 0-Censitário). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato de amostragem no desenho do SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral expandido do aluno para Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota estimada de proficiência em Língua Portuguesa na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência em Língua Portuguesa na escala padronizada. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota de proficiência do aluno em Língua Portuguesa convertida para a escala original do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência de Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral expandido do aluno para Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota estimada de proficiência em Matemática na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência em Matemática na escala padronizada. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota de proficiência do aluno em Matemática convertida para a escala original do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência de Matemática na escala SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2019_ts_aluno_34em

File `raw__inep_saeb_microdados_csv_2019_ts_aluno_34em.parquet` · 2,018,515 rows · 91 columns

Raw do microdado CSV TS_ALUNO_34EM.csv do Saeb 2019, arquivo oficial microdados_saeb_2019.zip.

**Feeds:** `raw/inep_saeb_aluno_2019`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do exame SAEB (ex: 2019). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico da região geográfica brasileira da escola (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do Estado (Unidade da Federação) da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área da escola (1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (ID da escola) de 8 dígitos. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de rede pública de ensino (1 = Pública, 0 = Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma no Censo Escolar/SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série/ano escolar avaliado no SAEB. — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único do aluno na edição do SAEB. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno conforme o Censo Escolar (1 = Matriculado). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento do teste de Língua Portuguesa (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento do teste de Matemática (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença na avaliação de Língua Portuguesa (1 = Presente, 0 = Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença na avaliação de Matemática (1 = Presente, 0 = Ausente). — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Código identificador do caderno de prova atribuído para Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Código do primeiro bloco de itens do caderno de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Código do segundo bloco de itens do caderno de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Código identificador do caderno de prova atribuído para Matemática. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Código do primeiro bloco de itens do caderno de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Código do segundo bloco de itens do caderno de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Vetor com as opções marcadas pelo aluno no bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Vetor com as opções marcadas pelo aluno no bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Vetor com as opções marcadas pelo aluno no bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Vetor com as opções marcadas pelo aluno no bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador de presença de cálculo válido de proficiência em Língua Portuguesa (1 = Possui, 0 = Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador de presença de cálculo válido de proficiência em Matemática (1 = Possui, 0 = Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador se a turma do aluno pertence à amostra estatística do SAEB (1 = Sim, 0 = Não/Censo). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato amostral utilizado para ponderação dos dados. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral calculado para o aluno na avaliação de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota padronizada do aluno em Língua Portuguesa (escala normalizada/TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Pontuação final do aluno em Língua Portuguesa na escala oficial do SAEB (ex: 0 a 500). — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência do aluno na escala oficial do SAEB de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral calculado para o aluno na avaliação de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota padronizada do aluno em Matemática (escala normalizada/TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Pontuação final do aluno em Matemática na escala oficial do SAEB (ex: 0 a 500). — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência do aluno na escala oficial do SAEB de Matemática. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico do aluno (1 = Preenchido, 0 = Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta do aluno à questão 1 do questionário socioeconômico (geralmente sobre sexo). — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta do aluno à questão 2 do questionário socioeconômico (geralmente sobre cor/raça). — descrição gerada por IA. |
| `TX_RESP_Q003A` | STRING | Resposta do aluno à questão 3A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003B` | STRING | Resposta do aluno à questão 3B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003C` | STRING | Resposta do aluno à questão 3C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003D` | STRING | Resposta do aluno à questão 3D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003E` | STRING | Resposta do aluno à questão 3E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta do aluno à questão 4 do questionário socioeconômico (geralmente sobre escolaridade da mãe). — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta do aluno à questão 5 do questionário socioeconômico (geralmente sobre escolaridade do pai). — descrição gerada por IA. |
| `TX_RESP_Q006A` | STRING | Resposta do aluno à questão 6A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006B` | STRING | Resposta do aluno à questão 6B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006C` | STRING | Resposta do aluno à questão 6C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006D` | STRING | Resposta do aluno à questão 6D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006E` | STRING | Resposta do aluno à questão 6E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta do aluno à questão 7 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q008A` | STRING | Resposta do aluno à questão 8A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q008B` | STRING | Resposta do aluno à questão 8B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q008C` | STRING | Resposta do aluno à questão 8C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009A` | STRING | Resposta do aluno à questão 9A do questionário socioeconômico (itens de conforto da casa). — descrição gerada por IA. |
| `TX_RESP_Q009B` | STRING | Resposta do aluno à questão 9B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009C` | STRING | Resposta do aluno à questão 9C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009D` | STRING | Resposta do aluno à questão 9D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009E` | STRING | Resposta do aluno à questão 9E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009F` | STRING | Resposta do aluno à questão 9F do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009G` | STRING | Resposta do aluno à questão 9G do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010A` | STRING | Resposta do aluno à questão 10A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010B` | STRING | Resposta do aluno à questão 10B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010C` | STRING | Resposta do aluno à questão 10C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010D` | STRING | Resposta do aluno à questão 10D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010E` | STRING | Resposta do aluno à questão 10E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010F` | STRING | Resposta do aluno à questão 10F do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010G` | STRING | Resposta do aluno à questão 10G do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010H` | STRING | Resposta do aluno à questão 10H do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010I` | STRING | Resposta do aluno à questão 10I do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta do aluno à questão 11 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta do aluno à questão 12 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta do aluno à questão 13 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta do aluno à questão 14 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta do aluno à questão 15 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta do aluno à questão 16 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017A` | STRING | Resposta do aluno à questão 17A do questionário socioeconômico (hábitos de estudo e leitura). — descrição gerada por IA. |
| `TX_RESP_Q017B` | STRING | Resposta do aluno à questão 17B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017C` | STRING | Resposta do aluno à questão 17C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017D` | STRING | Resposta do aluno à questão 17D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017E` | STRING | Resposta do aluno à questão 17E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018A` | STRING | Resposta do aluno à questão 18A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018B` | STRING | Resposta do aluno à questão 18B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018C` | STRING | Resposta do aluno à questão 18C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta do aluno à questão 19 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta do aluno à questão 20 do questionário socioeconômico. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2019_ts_aluno_5ef

File `raw__inep_saeb_microdados_csv_2019_ts_aluno_5ef.parquet` · 2,581,685 rows · 89 columns

Raw do microdado CSV TS_ALUNO_5EF.csv do Saeb 2019, arquivo oficial microdados_saeb_2019.zip.

**Feeds:** `raw/inep_saeb_aluno_2019`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição da avaliação do SAEB (ex: 2019). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código identificador da região geográfica da escola do aluno. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE/INEP do Estado (Unidade da Federação). — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código de localização/área da escola (ex: 1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de escola pública (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Tipo de localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código de identificação da turma no Censo Escolar/SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar avaliado do aluno (ex: 5 para 5º ano). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único e anonimizado do aluno no SAEB. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno segundo o Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento da prova de Língua Portuguesa (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento da prova de Matemática (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença do aluno no dia da prova de Língua Portuguesa. — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença do aluno no dia da prova de Matemática. — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Código identificador do caderno de prova de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Código do primeiro bloco de questões de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Código do segundo bloco de questões de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Código identificador do caderno de prova de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Código do primeiro bloco de questões de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Código do segundo bloco de questões de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Vetor de respostas marcadas pelo aluno no Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Vetor de respostas marcadas pelo aluno no Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Vetor de respostas marcadas pelo aluno no Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Vetor de respostas marcadas pelo aluno no Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador se a proficiência em Língua Portuguesa foi calculada (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador se a proficiência em Matemática foi calculada (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador se o aluno faz parte da amostra estatística do SAEB (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato de amostragem da escola/turma. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para projeções de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Pontuação de proficiência calculada do aluno em Língua Portuguesa. — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão associado à estimativa de proficiência de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência calibrada e padronizada em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para projeções de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Pontuação de proficiência calculada do aluno em Matemática. — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão associado à estimativa de proficiência de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência calibrada e padronizada em Matemática na escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência em Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta da questão 01 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta da questão 02 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003A` | STRING | Resposta da questão 03A do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003B` | STRING | Resposta da questão 03B do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003C` | STRING | Resposta da questão 03C do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003D` | STRING | Resposta da questão 03D do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q003E` | STRING | Resposta da questão 03E do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta da questão 04 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta da questão 05 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006A` | STRING | Resposta da questão 06A do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006B` | STRING | Resposta da questão 06B do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006C` | STRING | Resposta da questão 06C do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006D` | STRING | Resposta da questão 06D do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q006E` | STRING | Resposta da questão 06E do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da questão 07 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q008A` | STRING | Resposta da questão 08A do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q008B` | STRING | Resposta da questão 08B do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q008C` | STRING | Resposta da questão 08C do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009A` | STRING | Resposta da questão 09A do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009B` | STRING | Resposta da questão 09B do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009C` | STRING | Resposta da questão 09C do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009D` | STRING | Resposta da questão 09D do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009E` | STRING | Resposta da questão 09E do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009F` | STRING | Resposta da questão 09F do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q009G` | STRING | Resposta da questão 09G do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010A` | STRING | Resposta da questão 10A do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010B` | STRING | Resposta da questão 10B do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010C` | STRING | Resposta da questão 10C do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010D` | STRING | Resposta da questão 10D do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010E` | STRING | Resposta da questão 10E do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010F` | STRING | Resposta da questão 10F do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010G` | STRING | Resposta da questão 10G do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010H` | STRING | Resposta da questão 10H do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q010I` | STRING | Resposta da questão 10I do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da questão 11 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da questão 12 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da questão 13 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da questão 14 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da questão 15 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da questão 16 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017A` | STRING | Resposta da questão 17A do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017B` | STRING | Resposta da questão 17B do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017C` | STRING | Resposta da questão 17C do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017D` | STRING | Resposta da questão 17D do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q017E` | STRING | Resposta da questão 17E do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q018A` | STRING | Resposta da questão 18A do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q018B` | STRING | Resposta da questão 18B do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q018C` | STRING | Resposta da questão 18C do questionário socioeconômico do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2019_ts_aluno_9ef

File `raw__inep_saeb_microdados_csv_2019_ts_aluno_9ef.parquet` · 2,388,931 rows · 129 columns

Raw do microdado CSV TS_ALUNO_9EF.csv do Saeb 2019, arquivo oficial microdados_saeb_2019.zip.

**Feeds:** `raw/inep_saeb_aluno_2019`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do SAEB (ex: 2019). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade Federativa (estado) da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código de localização da escola segundo critérios de área (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP/Censo Escolar identificador da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola pertence à rede pública de ensino (1-Sim, 0-Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador da turma do aluno na avaliação do SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar avaliado do aluno (ex: 5, 9, 12). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único e anonimizado do aluno na avaliação SAEB. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação cadastral do aluno no Censo Escolar no momento do SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento do caderno de Língua Portuguesa (1-Preenchido, 0-Não preenchido). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento do caderno de Matemática (1-Preenchido, 0-Não preenchido). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_CH` | STRING | Indicador de preenchimento do caderno de Ciências Humanas (1-Preenchido, 0-Não preenchido). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_CN` | STRING | Indicador de preenchimento do caderno de Ciências da Natureza (1-Preenchido, 0-Não preenchido). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença do aluno no dia da prova de Língua Portuguesa (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença do aluno no dia da prova de Matemática (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_CH` | STRING | Indicador de presença do aluno no dia da prova de Ciências Humanas (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_CN` | STRING | Indicador de presença do aluno no dia da prova de Ciências da Natureza (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Número do caderno de prova de Língua Portuguesa respondido pelo aluno. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Identificador do primeiro bloco de itens de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Identificador do segundo bloco de itens de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Número do caderno de prova de Matemática respondido pelo aluno. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Identificador do primeiro bloco de itens de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Identificador do segundo bloco de itens de Matemática. — descrição gerada por IA. |
| `ID_CADERNO_CH` | STRING | Número do caderno de prova de Ciências Humanas respondido pelo aluno. — descrição gerada por IA. |
| `ID_BLOCO_1_CH` | STRING | Identificador do primeiro bloco de itens de Ciências Humanas. — descrição gerada por IA. |
| `ID_BLOCO_2_CH` | STRING | Identificador do segundo bloco de itens de Ciências Humanas. — descrição gerada por IA. |
| `ID_BLOCO_3_CH` | STRING | Identificador do terceiro bloco de itens de Ciências Humanas. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_CH` | STRING | Número de itens abertos no bloco 1 de Ciências Humanas. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_CH` | STRING | Número de itens abertos no bloco 2 de Ciências Humanas. — descrição gerada por IA. |
| `ID_CADERNO_CN` | STRING | Número do caderno de prova de Ciências da Natureza respondido pelo aluno. — descrição gerada por IA. |
| `ID_BLOCO_1_CN` | STRING | Identificador do primeiro bloco de itens de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_2_CN` | STRING | Identificador do segundo bloco de itens de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_3_CN` | STRING | Identificador do terceiro bloco de itens de Ciências da Natureza. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_CN` | STRING | Número de itens abertos no bloco 1 de Ciências da Natureza. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_CN` | STRING | Número de itens abertos no bloco 2 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Vetor com as opções de respostas assinaladas no bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Vetor com as opções de respostas assinaladas no bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Vetor com as opções de respostas assinaladas no bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Vetor com as opções de respostas assinaladas no bloco 2 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_CH` | STRING | Vetor com as opções de respostas assinaladas no bloco 1 de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_CH` | STRING | Vetor com as opções de respostas assinaladas no bloco 2 de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO3_CH` | STRING | Vetor com as opções de respostas assinaladas no bloco 3 de Ciências Humanas. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_CH` | STRING | Conceito/nota atribuído à questão aberta 1 de Ciências Humanas. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_CH` | STRING | Conceito/nota atribuído à questão aberta 2 de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_CN` | STRING | Vetor com as opções de respostas assinaladas no bloco 1 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_CN` | STRING | Vetor com as opções de respostas assinaladas no bloco 2 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO3_CN` | STRING | Vetor com as opções de respostas assinaladas no bloco 3 de Ciências da Natureza. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_CN` | STRING | Conceito/nota atribuído à questão aberta 1 de Ciências da Natureza. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_CN` | STRING | Conceito/nota atribuído à questão aberta 2 de Ciências da Natureza. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador de validade/presença de proficiência estimada em Língua Portuguesa (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador de validade/presença de proficiência estimada em Matemática (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_CH` | STRING | Indicador de validade/presença de proficiência estimada em Ciências Humanas (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_CN` | STRING | Indicador de validade/presença de proficiência estimada em Ciências da Natureza (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador se a turma/escola pertence à amostra do SAEB (1-Amostral, 0-Censitária). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código identificador do estrato de amostragem da escola/turma. — descrição gerada por IA. |
| `ESTRATO_CIENCIAS` | STRING | Código do estrato de amostragem específico para as avaliações de Ciências. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Fator de expansão/peso amostral do aluno para análises de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Pontuação estimada de proficiência em Língua Portuguesa na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão associado à estimativa de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Pontuação de proficiência de Língua Portuguesa transformada na escala SAEB (ex: 0-500). — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência de Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Fator de expansão/peso amostral do aluno para análises de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Pontuação estimada de proficiência em Matemática na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão associado à estimativa de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Pontuação de proficiência de Matemática transformada na escala SAEB (ex: 0-500). — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência de Matemática na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_CH` | STRING | Fator de expansão/peso amostral do aluno para análises de Ciências Humanas. — descrição gerada por IA. |
| `PROFICIENCIA_CH` | STRING | Pontuação estimada de proficiência em Ciências Humanas na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_CH` | STRING | Erro padrão associado à estimativa de proficiência em Ciências Humanas. — descrição gerada por IA. |
| `PROFICIENCIA_CH_SAEB` | STRING | Pontuação de proficiência de Ciências Humanas transformada na escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_CH_SAEB` | STRING | Erro padrão da proficiência de Ciências Humanas na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_CN` | STRING | Fator de expansão/peso amostral do aluno para análises de Ciências da Natureza. — descrição gerada por IA. |
| `PROFICIENCIA_CN` | STRING | Pontuação estimada de proficiência em Ciências da Natureza na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_CN` | STRING | Erro padrão associado à estimativa de proficiência em Ciências da Natureza. — descrição gerada por IA. |
| `PROFICIENCIA_CN_SAEB` | STRING | Pontuação de proficiência de Ciências da Natureza transformada na escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_CN_SAEB` | STRING | Erro padrão da proficiência de Ciências da Natureza na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico pelo aluno (1-Sim, 0-Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta do aluno à questão 1 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta do aluno à questão 2 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q003A` | STRING | Resposta do aluno à questão 3A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003B` | STRING | Resposta do aluno à questão 3B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003C` | STRING | Resposta do aluno à questão 3C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003D` | STRING | Resposta do aluno à questão 3D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q003E` | STRING | Resposta do aluno à questão 3E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta do aluno à questão 4 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta do aluno à questão 5 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q006A` | STRING | Resposta do aluno à questão 6A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006B` | STRING | Resposta do aluno à questão 6B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006C` | STRING | Resposta do aluno à questão 6C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006D` | STRING | Resposta do aluno à questão 6D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q006E` | STRING | Resposta do aluno à questão 6E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta do aluno à questão 7 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008A` | STRING | Resposta do aluno à questão 8A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q008B` | STRING | Resposta do aluno à questão 8B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q008C` | STRING | Resposta do aluno à questão 8C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009A` | STRING | Resposta do aluno à questão 9A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009B` | STRING | Resposta do aluno à questão 9B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009C` | STRING | Resposta do aluno à questão 9C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009D` | STRING | Resposta do aluno à questão 9D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009E` | STRING | Resposta do aluno à questão 9E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009F` | STRING | Resposta do aluno à questão 9F do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q009G` | STRING | Resposta do aluno à questão 9G do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010A` | STRING | Resposta do aluno à questão 10A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010B` | STRING | Resposta do aluno à questão 10B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010C` | STRING | Resposta do aluno à questão 10C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010D` | STRING | Resposta do aluno à questão 10D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010E` | STRING | Resposta do aluno à questão 10E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010F` | STRING | Resposta do aluno à questão 10F do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010G` | STRING | Resposta do aluno à questão 10G do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010H` | STRING | Resposta do aluno à questão 10H do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q010I` | STRING | Resposta do aluno à questão 10I do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta do aluno à questão 11 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta do aluno à questão 12 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta do aluno à questão 13 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta do aluno à questão 14 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta do aluno à questão 15 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta do aluno à questão 16 do questionário socioeconômico do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017A` | STRING | Resposta do aluno à questão 17A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017B` | STRING | Resposta do aluno à questão 17B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017C` | STRING | Resposta do aluno à questão 17C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017D` | STRING | Resposta do aluno à questão 17D do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q017E` | STRING | Resposta do aluno à questão 17E do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018A` | STRING | Resposta do aluno à questão 18A do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018B` | STRING | Resposta do aluno à questão 18B do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q018C` | STRING | Resposta do aluno à questão 18C do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta do aluno à questão 19 do questionário socioeconômico do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2019_ts_diretor

File `raw__inep_saeb_microdados_csv_2019_ts_diretor.parquet` · 74,176 rows · 262 columns

Raw do microdado CSV TS_DIRETOR.csv do Saeb 2019, arquivo oficial microdados_saeb_2019.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de edição do exame SAEB (ex: 2019). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código IBGE da região geográfica da escola. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação (UF) da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código da área de localização da escola (ex: capital ou interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola (8 dígitos). — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de rede pública de ensino (1 = Pública, 0 = Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário da escola/gestor (1 = Preenchido, 0 = Não preenchido). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Alternativa assinalada na questão 001 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Alternativa assinalada na questão 002 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Alternativa assinalada na questão 003 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Alternativa assinalada na questão 004 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Alternativa assinalada na questão 005 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Alternativa assinalada na questão 006 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Alternativa assinalada na questão 007 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Alternativa assinalada na questão 008 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Alternativa assinalada na questão 009 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Alternativa assinalada na questão 010 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Alternativa assinalada na questão 011 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Alternativa assinalada na questão 012 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Alternativa assinalada na questão 013 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Alternativa assinalada na questão 014 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Alternativa assinalada na questão 015 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Alternativa assinalada na questão 016 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Alternativa assinalada na questão 017 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Alternativa assinalada na questão 018 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Alternativa assinalada na questão 019 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Alternativa assinalada na questão 020 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Alternativa assinalada na questão 021 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Alternativa assinalada na questão 022 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Alternativa assinalada na questão 023 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Alternativa assinalada na questão 024 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Alternativa assinalada na questão 025 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Alternativa assinalada na questão 026 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Alternativa assinalada na questão 027 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Alternativa assinalada na questão 028 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Alternativa assinalada na questão 029 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Alternativa assinalada na questão 030 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Alternativa assinalada na questão 031 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Alternativa assinalada na questão 032 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Alternativa assinalada na questão 033 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Alternativa assinalada na questão 034 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Alternativa assinalada na questão 035 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Alternativa assinalada na questão 036 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Alternativa assinalada na questão 037 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Alternativa assinalada na questão 038 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Alternativa assinalada na questão 039 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Alternativa assinalada na questão 040 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Alternativa assinalada na questão 041 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Alternativa assinalada na questão 042 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Alternativa assinalada na questão 043 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Alternativa assinalada na questão 044 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Alternativa assinalada na questão 045 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Alternativa assinalada na questão 046 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Alternativa assinalada na questão 047 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Alternativa assinalada na questão 048 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Alternativa assinalada na questão 049 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Alternativa assinalada na questão 050 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Alternativa assinalada na questão 051 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Alternativa assinalada na questão 052 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Alternativa assinalada na questão 053 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Alternativa assinalada na questão 054 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Alternativa assinalada na questão 055 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Alternativa assinalada na questão 056 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Alternativa assinalada na questão 057 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Alternativa assinalada na questão 058 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Alternativa assinalada na questão 059 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Alternativa assinalada na questão 060 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Alternativa assinalada na questão 061 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Alternativa assinalada na questão 062 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Alternativa assinalada na questão 063 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Alternativa assinalada na questão 064 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Alternativa assinalada na questão 065 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Alternativa assinalada na questão 066 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Alternativa assinalada na questão 067 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Alternativa assinalada na questão 068 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Alternativa assinalada na questão 069 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Alternativa assinalada na questão 070 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Alternativa assinalada na questão 071 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Alternativa assinalada na questão 072 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Alternativa assinalada na questão 073 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Alternativa assinalada na questão 074 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Alternativa assinalada na questão 075 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Alternativa assinalada na questão 076 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Alternativa assinalada na questão 077 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Alternativa assinalada na questão 078 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Alternativa assinalada na questão 079 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Alternativa assinalada na questão 080 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Alternativa assinalada na questão 081 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Alternativa assinalada na questão 082 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Alternativa assinalada na questão 083 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Alternativa assinalada na questão 084 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Alternativa assinalada na questão 085 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Alternativa assinalada na questão 086 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Alternativa assinalada na questão 087 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Alternativa assinalada na questão 088 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Alternativa assinalada na questão 089 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Alternativa assinalada na questão 090 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Alternativa assinalada na questão 091 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Alternativa assinalada na questão 092 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Alternativa assinalada na questão 093 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Alternativa assinalada na questão 094 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Alternativa assinalada na questão 095 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Alternativa assinalada na questão 096 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Alternativa assinalada na questão 097 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Alternativa assinalada na questão 098 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Alternativa assinalada na questão 099 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Alternativa assinalada na questão 100 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Alternativa assinalada na questão 101 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Alternativa assinalada na questão 102 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Alternativa assinalada na questão 103 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Alternativa assinalada na questão 104 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Alternativa assinalada na questão 105 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Alternativa assinalada na questão 106 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Alternativa assinalada na questão 107 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Alternativa assinalada na questão 108 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Alternativa assinalada na questão 109 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Alternativa assinalada na questão 110 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Alternativa assinalada na questão 111 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Alternativa assinalada na questão 112 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Alternativa assinalada na questão 113 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Alternativa assinalada na questão 114 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Alternativa assinalada na questão 115 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Alternativa assinalada na questão 116 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Alternativa assinalada na questão 117 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Alternativa assinalada na questão 118 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Alternativa assinalada na questão 119 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Alternativa assinalada na questão 120 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Alternativa assinalada na questão 121 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q122` | STRING | Alternativa assinalada na questão 122 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q123` | STRING | Alternativa assinalada na questão 123 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q124` | STRING | Alternativa assinalada na questão 124 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q125` | STRING | Alternativa assinalada na questão 125 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q126` | STRING | Alternativa assinalada na questão 126 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q127` | STRING | Alternativa assinalada na questão 127 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q128` | STRING | Alternativa assinalada na questão 128 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q129` | STRING | Alternativa assinalada na questão 129 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q130` | STRING | Alternativa assinalada na questão 130 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q131` | STRING | Alternativa assinalada na questão 131 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q132` | STRING | Alternativa assinalada na questão 132 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q133` | STRING | Alternativa assinalada na questão 133 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q134` | STRING | Alternativa assinalada na questão 134 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q135` | STRING | Alternativa assinalada na questão 135 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q136` | STRING | Alternativa assinalada na questão 136 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q137` | STRING | Alternativa assinalada na questão 137 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q138` | STRING | Alternativa assinalada na questão 138 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q139` | STRING | Alternativa assinalada na questão 139 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q140` | STRING | Alternativa assinalada na questão 140 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q141` | STRING | Alternativa assinalada na questão 141 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q142` | STRING | Alternativa assinalada na questão 142 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q143` | STRING | Alternativa assinalada na questão 143 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q144` | STRING | Alternativa assinalada na questão 144 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q145` | STRING | Alternativa assinalada na questão 145 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q146` | STRING | Alternativa assinalada na questão 146 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q147` | STRING | Alternativa assinalada na questão 147 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q148` | STRING | Alternativa assinalada na questão 148 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q149` | STRING | Alternativa assinalada na questão 149 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q150` | STRING | Alternativa assinalada na questão 150 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q151` | STRING | Alternativa assinalada na questão 151 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q152` | STRING | Alternativa assinalada na questão 152 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q153` | STRING | Alternativa assinalada na questão 153 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q154` | STRING | Alternativa assinalada na questão 154 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q155` | STRING | Alternativa assinalada na questão 155 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q156` | STRING | Alternativa assinalada na questão 156 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q157` | STRING | Alternativa assinalada na questão 157 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q158` | STRING | Alternativa assinalada na questão 158 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q159` | STRING | Alternativa assinalada na questão 159 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q160` | STRING | Alternativa assinalada na questão 160 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q161` | STRING | Alternativa assinalada na questão 161 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q162` | STRING | Alternativa assinalada na questão 162 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q163` | STRING | Alternativa assinalada na questão 163 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q164` | STRING | Alternativa assinalada na questão 164 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q165` | STRING | Alternativa assinalada na questão 165 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q166` | STRING | Alternativa assinalada na questão 166 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q167` | STRING | Alternativa assinalada na questão 167 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q168` | STRING | Alternativa assinalada na questão 168 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q169` | STRING | Alternativa assinalada na questão 169 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q170` | STRING | Alternativa assinalada na questão 170 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q171` | STRING | Alternativa assinalada na questão 171 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q172` | STRING | Alternativa assinalada na questão 172 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q173` | STRING | Alternativa assinalada na questão 173 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q174` | STRING | Alternativa assinalada na questão 174 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q175` | STRING | Alternativa assinalada na questão 175 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q176` | STRING | Alternativa assinalada na questão 176 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q177` | STRING | Alternativa assinalada na questão 177 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q178` | STRING | Alternativa assinalada na questão 178 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q179` | STRING | Alternativa assinalada na questão 179 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q180` | STRING | Alternativa assinalada na questão 180 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q181` | STRING | Alternativa assinalada na questão 181 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q182` | STRING | Alternativa assinalada na questão 182 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q183` | STRING | Alternativa assinalada na questão 183 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q184` | STRING | Alternativa assinalada na questão 184 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q185` | STRING | Alternativa assinalada na questão 185 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q186` | STRING | Alternativa assinalada na questão 186 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q187` | STRING | Alternativa assinalada na questão 187 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q188` | STRING | Alternativa assinalada na questão 188 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q189` | STRING | Alternativa assinalada na questão 189 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q190` | STRING | Alternativa assinalada na questão 190 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q191` | STRING | Alternativa assinalada na questão 191 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q192` | STRING | Alternativa assinalada na questão 192 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q193` | STRING | Alternativa assinalada na questão 193 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q194` | STRING | Alternativa assinalada na questão 194 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q195` | STRING | Alternativa assinalada na questão 195 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q196` | STRING | Alternativa assinalada na questão 196 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q197` | STRING | Alternativa assinalada na questão 197 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q198` | STRING | Alternativa assinalada na questão 198 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q199` | STRING | Alternativa assinalada na questão 199 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q200` | STRING | Alternativa assinalada na questão 200 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q201` | STRING | Alternativa assinalada na questão 201 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q202` | STRING | Alternativa assinalada na questão 202 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q203` | STRING | Alternativa assinalada na questão 203 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q204` | STRING | Alternativa assinalada na questão 204 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q205` | STRING | Alternativa assinalada na questão 205 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q206` | STRING | Alternativa assinalada na questão 206 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q207` | STRING | Alternativa assinalada na questão 207 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q208` | STRING | Alternativa assinalada na questão 208 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q209` | STRING | Alternativa assinalada na questão 209 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q210` | STRING | Alternativa assinalada na questão 210 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q211` | STRING | Alternativa assinalada na questão 211 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q212` | STRING | Alternativa assinalada na questão 212 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q213` | STRING | Alternativa assinalada na questão 213 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q214` | STRING | Alternativa assinalada na questão 214 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q215` | STRING | Alternativa assinalada na questão 215 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q216` | STRING | Alternativa assinalada na questão 216 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q217` | STRING | Alternativa assinalada na questão 217 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q218` | STRING | Alternativa assinalada na questão 218 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q219` | STRING | Alternativa assinalada na questão 219 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q220` | STRING | Alternativa assinalada na questão 220 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q221` | STRING | Alternativa assinalada na questão 221 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q222` | STRING | Alternativa assinalada na questão 222 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q223` | STRING | Alternativa assinalada na questão 223 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q224` | STRING | Alternativa assinalada na questão 224 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q225` | STRING | Alternativa assinalada na questão 225 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q226` | STRING | Alternativa assinalada na questão 226 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q227` | STRING | Alternativa assinalada na questão 227 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q228` | STRING | Alternativa assinalada na questão 228 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q229` | STRING | Alternativa assinalada na questão 229 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q230` | STRING | Alternativa assinalada na questão 230 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q231` | STRING | Alternativa assinalada na questão 231 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q232` | STRING | Alternativa assinalada na questão 232 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q233` | STRING | Alternativa assinalada na questão 233 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q234` | STRING | Alternativa assinalada na questão 234 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q235` | STRING | Alternativa assinalada na questão 235 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q236` | STRING | Alternativa assinalada na questão 236 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q237` | STRING | Alternativa assinalada na questão 237 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q238` | STRING | Alternativa assinalada na questão 238 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q239` | STRING | Alternativa assinalada na questão 239 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q240` | STRING | Alternativa assinalada na questão 240 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q241` | STRING | Alternativa assinalada na questão 241 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q242` | STRING | Alternativa assinalada na questão 242 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q243` | STRING | Alternativa assinalada na questão 243 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q244` | STRING | Alternativa assinalada na questão 244 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q245` | STRING | Alternativa assinalada na questão 245 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q246` | STRING | Alternativa assinalada na questão 246 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q247` | STRING | Alternativa assinalada na questão 247 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q248` | STRING | Alternativa assinalada na questão 248 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q249` | STRING | Alternativa assinalada na questão 249 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q250` | STRING | Alternativa assinalada na questão 250 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q251` | STRING | Alternativa assinalada na questão 251 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q252` | STRING | Alternativa assinalada na questão 252 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q253` | STRING | Alternativa assinalada na questão 253 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2019_ts_escola

File `raw__inep_saeb_microdados_csv_2019_ts_escola.parquet` · 70,606 rows · 137 columns

Raw do microdado CSV TS_ESCOLA.csv do Saeb 2019, arquivo oficial microdados_saeb_2019.zip.

**Feeds:** `trusted/inep_saeb_escola`, `trusted/inep_saeb_microdados_escola`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do SAEB (ex: 2019). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código de identificação da região geográfica do IBGE (1 a 5). — descrição gerada por IA. |
| `ID_UF` | STRING | Código numérico IBGE da Unidade Federativa da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código de 7 dígitos do município no IBGE. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código do tipo de área do município (1 para Capital, 2 para Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP único de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 para Pública, 0 para Privada/Outros). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código da localização da escola (1 para Urbana, 2 para Rural). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_INICIAL` | STRING | Percentual de docentes com formação adequada nos Anos Iniciais do Ensino Fundamental (0 a 100%). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_FINAL` | STRING | Percentual de docentes com formação adequada nos Anos Finais do Ensino Fundamental (0 a 100%). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_MEDIO` | STRING | Percentual de docentes com formação adequada no Ensino Médio (0 a 100%). — descrição gerada por IA. |
| `NIVEL_SOCIO_ECONOMICO` | STRING | Classificação do Indicador de Nível Socioeconômico (INSE) da escola. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_5EF` | STRING | Número de alunos matriculados no 5º ano do Ensino Fundamental segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_5EF` | STRING | Número de alunos do 5º ano do Ensino Fundamental presentes na aplicação do SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_5EF` | STRING | Taxa de participação dos alunos do 5º ano do EF na prova do SAEB. — descrição gerada por IA. |
| `Nivel_0_LP5` | STRING | Percentual de alunos do 5º EF no Nível 0 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_1_LP5` | STRING | Percentual de alunos do 5º EF no Nível 1 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_2_LP5` | STRING | Percentual de alunos do 5º EF no Nível 2 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_3_LP5` | STRING | Percentual de alunos do 5º EF no Nível 3 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_4_LP5` | STRING | Percentual de alunos do 5º EF no Nível 4 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_5_LP5` | STRING | Percentual de alunos do 5º EF no Nível 5 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_6_LP5` | STRING | Percentual de alunos do 5º EF no Nível 6 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_7_LP5` | STRING | Percentual de alunos do 5º EF no Nível 7 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_8_LP5` | STRING | Percentual de alunos do 5º EF no Nível 8 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_9_LP5` | STRING | Percentual de alunos do 5º EF no Nível 9 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_0_MT5` | STRING | Percentual de alunos do 5º EF no Nível 0 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_1_MT5` | STRING | Percentual de alunos do 5º EF no Nível 1 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_2_MT5` | STRING | Percentual de alunos do 5º EF no Nível 2 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_3_MT5` | STRING | Percentual de alunos do 5º EF no Nível 3 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_4_MT5` | STRING | Percentual de alunos do 5º EF no Nível 4 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_5_MT5` | STRING | Percentual de alunos do 5º EF no Nível 5 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_6_MT5` | STRING | Percentual de alunos do 5º EF no Nível 6 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_7_MT5` | STRING | Percentual de alunos do 5º EF no Nível 7 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_8_MT5` | STRING | Percentual de alunos do 5º EF no Nível 8 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_9_MT5` | STRING | Percentual de alunos do 5º EF no Nível 9 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_10_MT5` | STRING | Percentual de alunos do 5º EF no Nível 10 de proficiência em Matemática (%). — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_9EF` | STRING | Número de alunos matriculados no 9º ano do Ensino Fundamental segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_9EF` | STRING | Número de alunos do 9º ano do Ensino Fundamental presentes na aplicação do SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_9EF` | STRING | Taxa de participação dos alunos do 9º ano do EF na prova do SAEB. — descrição gerada por IA. |
| `Nivel_0_LP9` | STRING | Percentual de alunos do 9º EF no Nível 0 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_1_LP9` | STRING | Percentual de alunos do 9º EF no Nível 1 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_2_LP9` | STRING | Percentual de alunos do 9º EF no Nível 2 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_3_LP9` | STRING | Percentual de alunos do 9º EF no Nível 3 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_4_LP9` | STRING | Percentual de alunos do 9º EF no Nível 4 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_5_LP9` | STRING | Percentual de alunos do 9º EF no Nível 5 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_6_LP9` | STRING | Percentual de alunos do 9º EF no Nível 6 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_7_LP9` | STRING | Percentual de alunos do 9º EF no Nível 7 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_8_LP9` | STRING | Percentual de alunos do 9º EF no Nível 8 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_0_MT9` | STRING | Percentual de alunos do 9º EF no Nível 0 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_1_MT9` | STRING | Percentual de alunos do 9º EF no Nível 1 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_2_MT9` | STRING | Percentual de alunos do 9º EF no Nível 2 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_3_MT9` | STRING | Percentual de alunos do 9º EF no Nível 3 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_4_MT9` | STRING | Percentual de alunos do 9º EF no Nível 4 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_5_MT9` | STRING | Percentual de alunos do 9º EF no Nível 5 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_6_MT9` | STRING | Percentual de alunos do 9º EF no Nível 6 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_7_MT9` | STRING | Percentual de alunos do 9º EF no Nível 7 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_8_MT9` | STRING | Percentual de alunos do 9º EF no Nível 8 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_9_MT9` | STRING | Percentual de alunos do 9º EF no Nível 9 de proficiência em Matemática (%). — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_EMT` | STRING | Número de alunos matriculados no Ensino Médio Tradicional segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_EMT` | STRING | Número de alunos do Ensino Médio Tradicional presentes no SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_EMT` | STRING | Taxa de participação dos alunos do Ensino Médio Tradicional no SAEB. — descrição gerada por IA. |
| `Nivel_0_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 0 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_1_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 1 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_2_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 2 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_3_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 3 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_4_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 4 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_5_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 5 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_6_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 6 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_7_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 7 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_8_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 8 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_0_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 0 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_1_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 1 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_2_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 2 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_3_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 3 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_4_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 4 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_5_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 5 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_6_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 6 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_7_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 7 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_8_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 8 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_9_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 9 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_10_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no Nível 10 de proficiência em Matemática (%). — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_EMI` | STRING | Número de alunos matriculados no Ensino Médio Integrado segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_EMI` | STRING | Número de alunos do Ensino Médio Integrado presentes no SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_EMI` | STRING | Taxa de participação dos alunos do Ensino Médio Integrado no SAEB. — descrição gerada por IA. |
| `Nivel_0_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 0 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_1_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 1 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_2_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 2 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_3_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 3 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_4_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 4 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_5_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 5 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_6_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 6 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_7_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 7 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_8_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 8 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_0_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 0 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_1_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 1 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_2_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 2 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_3_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 3 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_4_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 4 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_5_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 5 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_6_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 6 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_7_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 7 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_8_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 8 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_9_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 9 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_10_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no Nível 10 de proficiência em Matemática (%). — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_EM` | STRING | Número total de alunos matriculados no Ensino Médio segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_EM` | STRING | Número total de alunos do Ensino Médio presentes no SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_EM` | STRING | Taxa total de participação dos alunos do Ensino Médio no SAEB. — descrição gerada por IA. |
| `Nivel_0_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 0 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_1_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 1 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_2_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 2 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_3_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 3 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_4_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 4 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_5_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 5 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_6_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 6 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_7_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 7 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_8_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 8 de proficiência em Língua Portuguesa (%). — descrição gerada por IA. |
| `Nivel_0_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 0 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_1_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 1 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_2_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 2 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_3_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 3 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_4_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 4 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_5_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 5 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_6_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 6 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_7_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 7 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_8_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 8 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_9_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 9 de proficiência em Matemática (%). — descrição gerada por IA. |
| `Nivel_10_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 10 de proficiência em Matemática (%). — descrição gerada por IA. |
| `MEDIA_5EF_LP` | STRING | Nota média de proficiência em Língua Portuguesa no 5º ano do Ensino Fundamental na escala SAEB. — descrição gerada por IA. |
| `MEDIA_5EF_MT` | STRING | Nota média de proficiência em Matemática no 5º ano do Ensino Fundamental na escala SAEB. — descrição gerada por IA. |
| `MEDIA_9EF_LP` | STRING | Nota média de proficiência em Língua Portuguesa no 9º ano do Ensino Fundamental na escala SAEB. — descrição gerada por IA. |
| `MEDIA_9EF_MT` | STRING | Nota média de proficiência em Matemática no 9º ano do Ensino Fundamental na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EMT_LP` | STRING | Nota média de proficiência em Língua Portuguesa no Ensino Médio Tradicional na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EMT_MT` | STRING | Nota média de proficiência em Matemática no Ensino Médio Tradicional na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EMI_LP` | STRING | Nota média de proficiência em Língua Portuguesa no Ensino Médio Integrado na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EMI_MT` | STRING | Nota média de proficiência em Matemática no Ensino Médio Integrado na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EM_LP` | STRING | Nota média geral de proficiência em Língua Portuguesa no Ensino Médio na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EM_MT` | STRING | Nota média geral de proficiência em Matemática no Ensino Médio na escala SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2019_ts_item

File `raw__inep_saeb_microdados_csv_2019_ts_item.parquet` · 854 rows · 15 columns

Raw do microdado CSV TS_ITEM.csv do Saeb 2019, arquivo oficial microdados_saeb_2019.zip.

**Feeds:** `trusted/inep_saeb_microdados_item`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano da edição da avaliação do SAEB (ex: 2019). — descrição gerada por IA. |
| `DISCIPLINA` | STRING | Sigla da disciplina avaliada (ex: LP para Língua Portuguesa, MT para Matemática). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Identificador ou número correspondente à série/ano escolar avaliado (ex: 2 para 2º ano). — descrição gerada por IA. |
| `BLOCO` | STRING | Número do bloco de testes do caderno de prova em que o item está localizado. — descrição gerada por IA. |
| `POSICAO` | STRING | Posição sequencial em que o item aparece dentro do seu bloco. — descrição gerada por IA. |
| `ID_ITEM` | STRING | Identificador único do item (questão) no cadastro do INEP/SAEB. — descrição gerada por IA. |
| `NU_DESCRITOR_HABILIDADE` | STRING | Código do descritor de habilidade da Matriz de Referência do SAEB associado ao item (ex: H10, H1.1). — descrição gerada por IA. |
| `GABARITO` | STRING | Alternativa ou critério de resposta correta da questão (ex: A, B, A/B). — descrição gerada por IA. |
| `TIPO_ITEM` | STRING | Classificação do formato do item (ex: Resposta Objetiva, Resposta Construída, Produção Textual). — descrição gerada por IA. |
| `ITEM_MODELO` | STRING | Modelo de calibração psicométrica da Teoria de Resposta ao Item (ex: M3PL para 3 Parâmetros Logísticos, MRG para Resposta Graduada). — descrição gerada por IA. |
| `A` | STRING | Parâmetro 'a' da TRI: indica o poder de discriminação do item (valor numérico continuo). — descrição gerada por IA. |
| `B` | STRING | Parâmetro 'b' da TRI: indica o parâmetro de dificuldade geral do item em itens objetiva (escala logit). — descrição gerada por IA. |
| `C` | STRING | Parâmetro 'c' da TRI: indica a probabilidade de acerto ao acaso / adivinhação (valor entre 0 e 1). — descrição gerada por IA. |
| `B1` | STRING | Parâmetro de dificuldade 'b1' para a primeira transição de categoria em modelos politômicos (ex: MRG). — descrição gerada por IA. |
| `B2` | STRING | Parâmetro de dificuldade 'b2' para a segunda transição de categoria em modelos politômicos (ex: MRG). — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2019_ts_professor

File `raw__inep_saeb_microdados_csv_2019_ts_professor.parquet` · 388,119 rows · 140 columns

Raw do microdado CSV TS_PROFESSOR.csv do Saeb 2019, arquivo oficial microdados_saeb_2019.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de edição do exame SAEB. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do estado (Unidade da Federação) onde a escola está localizada. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área de localização da escola (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola é de rede pública (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Zona de localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador da turma avaliada. — descrição gerada por IA. |
| `CO_PROFESSOR` | STRING | Código de identificação do professor respondente. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série ou ano escolar avaliado na turma. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário pelo professor (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta da questão 1 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta da questão 2 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta da questão 3 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta da questão 4 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta da questão 5 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta da questão 6 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da questão 7 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta da questão 8 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta da questão 9 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta da questão 10 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da questão 11 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da questão 12 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da questão 13 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da questão 14 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da questão 15 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da questão 16 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta da questão 17 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta da questão 18 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta da questão 19 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta da questão 20 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta da questão 21 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta da questão 22 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta da questão 23 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta da questão 24 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta da questão 25 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta da questão 26 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta da questão 27 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta da questão 28 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta da questão 29 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta da questão 30 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta da questão 31 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta da questão 32 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta da questão 33 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta da questão 34 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta da questão 35 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta da questão 36 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta da questão 37 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta da questão 38 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta da questão 39 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta da questão 40 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta da questão 41 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta da questão 42 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta da questão 43 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta da questão 44 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta da questão 45 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta da questão 46 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta da questão 47 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta da questão 48 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta da questão 49 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta da questão 50 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta da questão 51 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta da questão 52 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta da questão 53 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta da questão 54 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta da questão 55 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta da questão 56 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta da questão 57 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta da questão 58 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta da questão 59 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta da questão 60 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta da questão 61 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta da questão 62 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta da questão 63 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta da questão 64 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta da questão 65 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta da questão 66 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta da questão 67 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta da questão 68 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta da questão 69 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta da questão 70 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta da questão 71 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta da questão 72 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta da questão 73 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta da questão 74 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Resposta da questão 75 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Resposta da questão 76 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Resposta da questão 77 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Resposta da questão 78 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Resposta da questão 79 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Resposta da questão 80 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Resposta da questão 81 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Resposta da questão 82 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Resposta da questão 83 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Resposta da questão 84 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Resposta da questão 85 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Resposta da questão 86 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Resposta da questão 87 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Resposta da questão 88 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Resposta da questão 89 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Resposta da questão 90 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Resposta da questão 91 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Resposta da questão 92 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Resposta da questão 93 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Resposta da questão 94 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Resposta da questão 95 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Resposta da questão 96 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Resposta da questão 97 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Resposta da questão 98 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Resposta da questão 99 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Resposta da questão 100 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Resposta da questão 101 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Resposta da questão 102 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Resposta da questão 103 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Resposta da questão 104 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Resposta da questão 105 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Resposta da questão 106 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Resposta da questão 107 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Resposta da questão 108 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Resposta da questão 109 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Resposta da questão 110 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Resposta da questão 111 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Resposta da questão 112 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Resposta da questão 113 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Resposta da questão 114 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Resposta da questão 115 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Resposta da questão 116 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Resposta da questão 117 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Resposta da questão 118 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Resposta da questão 119 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Resposta da questão 120 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Resposta da questão 121 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q122` | STRING | Resposta da questão 122 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q123` | STRING | Resposta da questão 123 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q124` | STRING | Resposta da questão 124 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q125` | STRING | Resposta da questão 125 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q126` | STRING | Resposta da questão 126 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q127` | STRING | Resposta da questão 127 do questionário do professor no SAEB. — descrição gerada por IA. |
| `TX_RESP_Q128` | STRING | Resposta da questão 128 do questionário do professor no SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2019_ts_secretario_municipal

File `raw__inep_saeb_microdados_csv_2019_ts_secretario_municipal.parquet` · 5,412 rows · 204 columns

Raw do microdado CSV TS_SECRETARIO_MUNICIPAL.csv do Saeb 2019, arquivo oficial microdados_saeb_2019.zip.

**Feeds:** `trusted/inep_saeb_secretario`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de edição da aplicação da avaliação do SAEB/INEP (ex: 2019). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico identificador da região geográfica brasileira (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE correspondente à Unidade da Federação (UF) da escola ou participante. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município de localização da escola ou participante. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código identificador do tipo de área da escola (ex: 1-Urbana, 2-Rural). — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Código da resposta selecionada para a questão 19 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Código da resposta selecionada para a questão 20 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Código da resposta selecionada para a questão 21 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Código ou valor preenchido na questão 22 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Código da resposta selecionada para a questão 23 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Código da resposta selecionada para a questão 24 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Código da resposta selecionada para a questão 25 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Código da resposta selecionada para a questão 26 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Código da resposta selecionada para a questão 27 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Código da resposta selecionada para a questão 28 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Código da resposta selecionada para a questão 29 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Código da resposta selecionada para a questão 30 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Código da resposta selecionada para a questão 31 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Código da resposta selecionada para a questão 32 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Código da resposta selecionada para a questão 33 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Código da resposta selecionada para a questão 34 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Código da resposta selecionada para a questão 35 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Código da resposta selecionada para a questão 36 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Código da resposta selecionada para a questão 37 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Código da resposta selecionada para a questão 38 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Código da resposta selecionada para a questão 39 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Código da resposta selecionada para a questão 40 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Código da resposta selecionada para a questão 41 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Código da resposta selecionada para a questão 42 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Código da resposta selecionada para a questão 43 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Código da resposta selecionada para a questão 44 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Código da resposta selecionada para a questão 45 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Código da resposta selecionada para a questão 46 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Código da resposta selecionada para a questão 47 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Código da resposta selecionada para a questão 48 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Código da resposta selecionada para a questão 49 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Código da resposta selecionada para a questão 50 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Código da resposta selecionada para a questão 51 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Código da resposta selecionada para a questão 52 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Código da resposta selecionada para a questão 53 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Código da resposta selecionada para a questão 54 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Código da resposta selecionada para a questão 55 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Código da resposta selecionada para a questão 56 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Código da resposta selecionada para a questão 57 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Código da resposta selecionada para a questão 58 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Código ou indicador selecionado para a questão 59 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Código ou indicador selecionado para a questão 60 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Código ou indicador selecionado para a questão 61 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Código ou indicador selecionado para a questão 62 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Código ou indicador selecionado para a questão 63 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Código ou indicador selecionado para a questão 64 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Código ou indicador selecionado para a questão 65 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Código ou indicador selecionado para a questão 66 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Código ou indicador selecionado para a questão 67 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Código ou indicador selecionado para a questão 68 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Código ou indicador selecionado para a questão 69 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Código ou indicador selecionado para a questão 70 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Código ou indicador selecionado para a questão 71 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Código ou indicador selecionado para a questão 72 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Código da resposta selecionada para a questão 73 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Código ou valor preenchido na questão 74 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Código da resposta selecionada para a questão 75 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Código da resposta selecionada para a questão 76 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Código da resposta selecionada para a questão 77 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Código da resposta selecionada para a questão 78 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Código da resposta selecionada para a questão 79 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Código da resposta selecionada para a questão 80 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Código da resposta selecionada para a questão 81 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Código da resposta selecionada para a questão 82 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Código da resposta selecionada para a questão 83 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Código da resposta selecionada para a questão 84 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Código da resposta selecionada para a questão 85 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Código da resposta selecionada para a questão 86 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Código da resposta selecionada para a questão 87 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Código da resposta selecionada para a questão 88 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Código da resposta selecionada para a questão 89 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Código da resposta selecionada para a questão 90 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Código da resposta selecionada para a questão 91 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Código da resposta selecionada para a questão 92 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Código da resposta selecionada para a questão 93 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Código da resposta selecionada para a questão 94 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Código da resposta selecionada para a questão 95 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Código da resposta selecionada para a questão 96 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Código da resposta selecionada para a questão 97 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Código da resposta selecionada para a questão 98 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Código da resposta selecionada para a questão 99 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Código da resposta selecionada para a questão 100 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Código da resposta selecionada para a questão 101 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Código da resposta selecionada para a questão 102 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Código da resposta selecionada para a questão 103 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Código da resposta selecionada para a questão 104 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Código da resposta selecionada para a questão 105 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Código da resposta selecionada para a questão 106 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Código da resposta selecionada para a questão 107 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Código da resposta selecionada para a questão 108 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Código da resposta selecionada para a questão 109 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Código da resposta selecionada para a questão 110 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Código da resposta selecionada para a questão 111 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Código da resposta selecionada para a questão 112 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Código da resposta selecionada para a questão 113 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Código da resposta selecionada para a questão 114 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Código da resposta selecionada para a questão 115 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Código da resposta selecionada para a questão 116 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Código da resposta selecionada para a questão 117 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Código da resposta selecionada para a questão 118 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Código da resposta selecionada para a questão 119 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Código da resposta selecionada para a questão 120 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Código da resposta selecionada para a questão 121 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q122` | STRING | Código da resposta selecionada para a questão 122 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q123` | STRING | Código da resposta selecionada para a questão 123 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q124` | STRING | Código da resposta selecionada para a questão 124 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q125` | STRING | Código da resposta selecionada para a questão 125 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q126` | STRING | Código da resposta selecionada para a questão 126 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q127` | STRING | Código da resposta selecionada para a questão 127 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q128` | STRING | Código da resposta selecionada para a questão 128 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q129` | STRING | Código da resposta selecionada para a questão 129 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q130` | STRING | Código da resposta selecionada para a questão 130 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q131` | STRING | Código da resposta selecionada para a questão 131 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q132` | STRING | Código da resposta selecionada para a questão 132 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q133` | STRING | Código da resposta selecionada para a questão 133 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q134` | STRING | Código da resposta selecionada para a questão 134 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q135` | STRING | Código da resposta selecionada para a questão 135 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q136` | STRING | Código da resposta selecionada para a questão 136 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q137` | STRING | Código da resposta selecionada para a questão 137 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q138` | STRING | Código da resposta selecionada para a questão 138 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q139` | STRING | Código da resposta selecionada para a questão 139 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q140` | STRING | Código da resposta selecionada para a questão 140 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q141` | STRING | Código da resposta selecionada para a questão 141 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q142` | STRING | Código da resposta selecionada para a questão 142 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q143` | STRING | Código da resposta selecionada para a questão 143 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q144` | STRING | Código da resposta selecionada para a questão 144 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q145` | STRING | Código da resposta selecionada para a questão 145 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q146` | STRING | Código da resposta selecionada para a questão 146 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q147` | STRING | Código da resposta selecionada para a questão 147 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q148` | STRING | Código da resposta selecionada para a questão 148 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q149` | STRING | Código da resposta selecionada para a questão 149 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q150` | STRING | Código da resposta selecionada para a questão 150 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q151` | STRING | Código da resposta selecionada para a questão 151 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q152` | STRING | Código da resposta selecionada para a questão 152 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q153` | STRING | Código da resposta selecionada para a questão 153 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q154` | STRING | Código da resposta selecionada para a questão 154 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q155` | STRING | Código da resposta selecionada para a questão 155 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q156` | STRING | Código da resposta selecionada para a questão 156 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q157` | STRING | Código da resposta selecionada para a questão 157 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q158` | STRING | Código da resposta selecionada para a questão 158 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q159` | STRING | Código da resposta selecionada para a questão 159 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q160` | STRING | Código da resposta selecionada para a questão 160 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q161` | STRING | Código da resposta selecionada para a questão 161 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q162` | STRING | Código da resposta selecionada para a questão 162 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q163` | STRING | Código da resposta selecionada para a questão 163 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q164` | STRING | Código da resposta selecionada para a questão 164 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q165` | STRING | Código da resposta selecionada para a questão 165 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q166` | STRING | Código da resposta selecionada para a questão 166 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q167` | STRING | Código da resposta selecionada para a questão 167 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q168` | STRING | Código da resposta selecionada para a questão 168 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q169` | STRING | Código da resposta selecionada para a questão 169 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q170` | STRING | Código da resposta selecionada para a questão 170 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q171` | STRING | Código da resposta selecionada para a questão 171 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q172` | STRING | Código da resposta selecionada para a questão 172 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q173` | STRING | Código da resposta selecionada para a questão 173 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q174` | STRING | Código da resposta selecionada para a questão 174 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q175` | STRING | Código da resposta selecionada para a questão 175 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q176` | STRING | Código da resposta selecionada para a questão 176 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q177` | STRING | Código da resposta selecionada para a questão 177 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q178` | STRING | Código da resposta selecionada para a questão 178 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q179` | STRING | Código da resposta selecionada para a questão 179 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q180` | STRING | Código da resposta selecionada para a questão 180 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q181` | STRING | Código da resposta selecionada para a questão 181 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q182` | STRING | Código da resposta selecionada para a questão 182 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q183` | STRING | Código da resposta selecionada para a questão 183 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q184` | STRING | Código da resposta selecionada para a questão 184 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q185` | STRING | Código da resposta selecionada para a questão 185 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q186` | STRING | Código da resposta selecionada para a questão 186 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q187` | STRING | Código da resposta selecionada para a questão 187 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q188` | STRING | Código da resposta selecionada para a questão 188 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q189` | STRING | Código da resposta selecionada para a questão 189 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q190` | STRING | Código da resposta selecionada para a questão 190 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q191` | STRING | Código da resposta selecionada para a questão 191 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q192` | STRING | Código da resposta selecionada para a questão 192 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q193` | STRING | Código da resposta selecionada para a questão 193 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q194` | STRING | Código da resposta selecionada para a questão 194 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q195` | STRING | Código da resposta selecionada para a questão 195 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q196` | STRING | Código da resposta selecionada para a questão 196 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q197` | STRING | Código da resposta selecionada para a questão 197 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q198` | STRING | Código da resposta selecionada para a questão 198 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q199` | STRING | Código da resposta selecionada para a questão 199 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q200` | STRING | Código da resposta selecionada para a questão 200 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q201` | STRING | Código da resposta selecionada para a questão 201 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q202` | STRING | Código da resposta selecionada para a questão 202 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q203` | STRING | Código da resposta selecionada para a questão 203 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q204` | STRING | Código da resposta selecionada para a questão 204 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q205` | STRING | Código da resposta selecionada para a questão 205 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q206` | STRING | Código da resposta selecionada para a questão 206 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q207` | STRING | Código da resposta selecionada para a questão 207 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q208` | STRING | Código da resposta selecionada para a questão 208 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q209` | STRING | Código da resposta selecionada para a questão 209 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q210` | STRING | Código da resposta selecionada para a questão 210 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q211` | STRING | Código da resposta selecionada para a questão 211 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q212` | STRING | Código da resposta selecionada para a questão 212 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q213` | STRING | Código da resposta selecionada para a questão 213 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q214` | STRING | Código da resposta selecionada para a questão 214 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q215` | STRING | Código da resposta selecionada para a questão 215 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q216` | STRING | Código da resposta selecionada para a questão 216 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q217` | STRING | Código da resposta selecionada para a questão 217 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_aluno_2ef

File `raw__inep_saeb_microdados_csv_2021_ts_aluno_2ef.parquet` · 29,819 rows · 53 columns

Raw do microdado CSV TS_ALUNO_2EF.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_ensino_fundamental_e_medio.zip.

**Feeds:** `raw/inep_saeb_aluno_2021`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição da avaliação do SAEB. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (ex: 1-Norte, 2-Nordeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área do município da escola (1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador único da turma no Censo Escolar/SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série ou ano escolar avaliado do aluno. — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único e anonimizado do aluno. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação do aluno segundo o Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador se o aluno preencheu a prova de Língua Portuguesa suficiente para correção (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador se o aluno preencheu a prova de Matemática suficiente para correção (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença do aluno no dia da prova de Língua Portuguesa (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença do aluno no dia da prova de Matemática (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Código de identificação do caderno de prova de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Código do primeiro bloco de itens de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Código do segundo bloco de itens de Língua Portuguesa. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_LP` | STRING | Número de itens abertos/discursivos no bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_LP` | STRING | Número de itens abertos/discursivos no bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Código de identificação do caderno de prova de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Código do primeiro bloco de itens de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Código do segundo bloco de itens de Matemática. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_MT` | STRING | Número de itens abertos/discursivos no bloco 1 de Matemática. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_MT` | STRING | Número de itens abertos/discursivos no bloco 2 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Sequência de respostas assinaladas pelo aluno no bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Sequência de respostas assinaladas pelo aluno no bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_LP` | STRING | Conceito atribuído à questão aberta 1 de Língua Portuguesa. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_LP` | STRING | Conceito atribuído à questão aberta 2 de Língua Portuguesa. — descrição gerada por IA. |
| `CO_RESPOSTA_TEXTO` | STRING | Código da situação de preenchimento/resposta da produção de texto (ex: BR para em branco). — descrição gerada por IA. |
| `CO_CONCEITO_PROPOSITO` | STRING | Conceito atribuído ao propósito comunicativo do texto produzido pelo aluno. — descrição gerada por IA. |
| `CO_CONCEITO_ELEMENTO` | STRING | Conceito atribuído aos elementos e estrutura do texto produzido. — descrição gerada por IA. |
| `CO_CONCEITO_SEGMENTACAO` | STRING | Conceito atribuído à segmentação do texto na correção discursiva. — descrição gerada por IA. |
| `CO_TEXTO_GRAFIA` | STRING | Conceito atribuído à grafia e ortografia na redação do aluno. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Sequência de respostas assinaladas pelo aluno no bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Sequência de respostas assinaladas pelo aluno no bloco 2 de Matemática. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_MT` | STRING | Conceito atribuído à questão aberta 1 de Matemática. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_MT` | STRING | Conceito atribuído à questão aberta 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador se a proficiência em Língua Portuguesa foi calculada para o aluno (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador se a proficiência em Matemática foi calculada para o aluno (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador de pertencimento da turma à amostra estatística do SAEB (1-Sim, 0-Não). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato amostral utilizado no plano de amostragem. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno aplicado aos cálculos de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Proficiência estimada do aluno em Língua Portuguesa na escala padronizada TRI. — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão de medida da proficiência do aluno em Língua Portuguesa na escala padronizada. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência final do aluno em Língua Portuguesa na escala histórica do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão de medida da proficiência em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno aplicado aos cálculos de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Proficiência estimada do aluno em Matemática na escala padronizada TRI. — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão de medida da proficiência do aluno em Matemática na escala padronizada. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência final do aluno em Matemática na escala histórica do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão de medida da proficiência em Matemática na escala SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_aluno_34em

File `raw__inep_saeb_microdados_csv_2021_ts_aluno_34em.parquet` · 2,288,747 rows · 106 columns

Raw do microdado CSV TS_ALUNO_34EM.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_ensino_fundamental_e_medio.zip.

**Feeds:** `raw/inep_saeb_aluno_2021`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição da avaliação do SAEB (ex: 2021). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico da região geográfica do aluno/escola (1-Norte, 2-Nordeste, etc.). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação onde a escola se localiza. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área da escola (1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (Censo Escolar) identificador da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de rede pública de ensino (1=Pública, 0=Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador da turma do aluno no Censo Escolar/SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série/ano escolar avaliado (ex: 12 indica 3ª série do Ensino Médio). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único do aluno no SAEB. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador da situação do aluno na matrícula do Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador se o caderno de Língua Portuguesa foi preenchido (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador se o caderno de Matemática foi preenchido (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença do aluno na avaliação de Língua Portuguesa (1=Presente, 0=Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença do aluno na avaliação de Matemática (1=Presente, 0=Ausente). — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Número do caderno de prova de Língua Portuguesa respondido. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Identificador do Bloco 1 da prova de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Identificador do Bloco 2 da prova de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Número do caderno de prova de Matemática respondido. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Identificador do Bloco 1 da prova de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Identificador do Bloco 2 da prova de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Sequência de respostas dadas às questões do Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Sequência de respostas dadas às questões do Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Sequência de respostas dadas às questões do Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Sequência de respostas dadas às questões do Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador se a proficiência do aluno em Língua Portuguesa foi calculada (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador se a proficiência do aluno em Matemática foi calculada (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador se a turma/aluno faz parte do desenho amostral do SAEB (1=Sim, 0=Não). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato amostral da escola para expansão estatística. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno associado à avaliação de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência do aluno em Língua Portuguesa na escala do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência do aluno em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência padronizada do aluno em Língua Portuguesa. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência padronizada de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno associado à avaliação de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência do aluno em Matemática na escala do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência do aluno em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência padronizada do aluno em Matemática. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência padronizada de Matemática. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador se o questionário do aluno foi preenchido (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_INSE` | STRING | Indicador se o aluno possui cálculo de Nível Socioeconômico (1=Sim, 0=Não). — descrição gerada por IA. |
| `INSE_ALUNO` | STRING | Pontuação numérica do Indicador de Nível Socioeconômico (INSE) do aluno. — descrição gerada por IA. |
| `NU_TIPO_NIVEL_INSE` | STRING | Nível ordinal do INSE do aluno (categoria socioeconômica). — descrição gerada por IA. |
| `PESO_ALUNO_INSE` | STRING | Peso amostral do aluno para cálculo e expansão do INSE. — descrição gerada por IA. |
| `TX_RESP_Q01` | STRING | Resposta do aluno à questão 1 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q02` | STRING | Resposta do aluno à questão 2 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q03` | STRING | Resposta do aluno à questão 3 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q04` | STRING | Resposta do aluno à questão 4 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q05` | STRING | Resposta do aluno à questão 5 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q06a` | STRING | Resposta do aluno ao item 6a do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q06b` | STRING | Resposta do aluno ao item 6b do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q06c` | STRING | Resposta do aluno ao item 6c do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q06d` | STRING | Resposta do aluno ao item 6d do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q06e` | STRING | Resposta do aluno ao item 6e do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q07` | STRING | Resposta do aluno à questão 7 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q08` | STRING | Resposta do aluno à questão 8 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q09a` | STRING | Resposta do aluno ao item 9a do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q09b` | STRING | Resposta do aluno ao item 9b do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q09c` | STRING | Resposta do aluno ao item 9c do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q09d` | STRING | Resposta do aluno ao item 9d do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q09e` | STRING | Resposta do aluno ao item 9e do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q09f` | STRING | Resposta do aluno ao item 9f do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q10a` | STRING | Resposta do aluno ao item 10a do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q10b` | STRING | Resposta do aluno ao item 10b do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q10c` | STRING | Resposta do aluno ao item 10c do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q11a` | STRING | Resposta do aluno ao item 11a do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q11b` | STRING | Resposta do aluno ao item 11b do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q11c` | STRING | Resposta do aluno ao item 11c do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q11d` | STRING | Resposta do aluno ao item 11d do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q11e` | STRING | Resposta do aluno ao item 11e do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q11f` | STRING | Resposta do aluno ao item 11f do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q11g` | STRING | Resposta do aluno ao item 11g do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q11h` | STRING | Resposta do aluno ao item 11h do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q12a` | STRING | Resposta do aluno ao item 12a do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q12b` | STRING | Resposta do aluno ao item 12b do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q12c` | STRING | Resposta do aluno ao item 12c do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q12d` | STRING | Resposta do aluno ao item 12d do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q12e` | STRING | Resposta do aluno ao item 12e do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q12f` | STRING | Resposta do aluno ao item 12f do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q12g` | STRING | Resposta do aluno ao item 12g do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q12h` | STRING | Resposta do aluno ao item 12h do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q12i` | STRING | Resposta do aluno ao item 12i do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q13` | STRING | Resposta do aluno à questão 13 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q14` | STRING | Resposta do aluno à questão 14 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q15` | STRING | Resposta do aluno à questão 15 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q16` | STRING | Resposta do aluno à questão 16 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q17` | STRING | Resposta do aluno à questão 17 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q18` | STRING | Resposta do aluno à questão 18 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q19` | STRING | Resposta do aluno à questão 19 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q20a` | STRING | Resposta do aluno ao item 20a do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q20b` | STRING | Resposta do aluno ao item 20b do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q20c` | STRING | Resposta do aluno ao item 20c do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q20d` | STRING | Resposta do aluno ao item 20d do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q20e` | STRING | Resposta do aluno ao item 20e do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q21` | STRING | Resposta do aluno à questão 21 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q22` | STRING | Resposta do aluno à questão 22 do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q23a` | STRING | Resposta do aluno ao item 23a do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q23b` | STRING | Resposta do aluno ao item 23b do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q23c` | STRING | Resposta do aluno ao item 23c do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q23d` | STRING | Resposta do aluno ao item 23d do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q23e` | STRING | Resposta do aluno ao item 23e do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q23f` | STRING | Resposta do aluno ao item 23f do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q23g` | STRING | Resposta do aluno ao item 23g do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q23h` | STRING | Resposta do aluno ao item 23h do questionário contextual. — descrição gerada por IA. |
| `TX_RESP_Q23i` | STRING | Resposta do aluno ao item 23i do questionário contextual. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_aluno_5ef

File `raw__inep_saeb_microdados_csv_2021_ts_aluno_5ef.parquet` · 2,554,184 rows · 104 columns

Raw do microdado CSV TS_ALUNO_5EF.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_ensino_fundamental_e_medio.zip.

**Feeds:** `raw/inep_saeb_aluno_2021`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do exame SAEB (ex: 2021). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico da região geográfica do aluno/escola. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código de identificação da turma do aluno. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série ou ano escolar avaliado (ex: 5 para 5º ano do Ensino Fundamental). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único do aluno na base da avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador da situação de matrícula do aluno no Censo Escolar (1: Presente/Ativo). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento mínimo do caderno de Língua Portuguesa (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento mínimo do caderno de Matemática (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença do aluno no dia da prova de Língua Portuguesa (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença do aluno no dia da prova de Matemática (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Código de identificação do caderno de prova de Língua Portuguesa aplicado. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Identificador do primeiro bloco de itens da prova de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Identificador do segundo bloco de itens da prova de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Código de identificação do caderno de prova de Matemática aplicado. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Identificador do primeiro bloco de itens da prova de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Identificador do segundo bloco de itens da prova de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | String com a sequência de respostas marcadas pelo aluno no Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | String com a sequência de respostas marcadas pelo aluno no Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | String com a sequência de respostas marcadas pelo aluno no Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | String com a sequência de respostas marcadas pelo aluno no Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador se o aluno obteve cálculo de proficiência em Língua Portuguesa (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador se o aluno obteve cálculo de proficiência em Matemática (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador se a turma/escola faz parte da amostra estatística do SAEB (1: Sim, 0: Censo/Não). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato amostral utilizado no plano de amostragem do SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral expandido do aluno para análises de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Escore de proficiência estimado do aluno em Língua Portuguesa na escala logística (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência em Língua Portuguesa (escala logística). — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Pontuação final de proficiência do aluno em Língua Portuguesa na escala padronizada do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência de Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral expandido do aluno para análises de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Escore de proficiência estimado do aluno em Matemática na escala logística (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência em Matemática (escala logística). — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Pontuação final de proficiência do aluno em Matemática na escala padronizada do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência de Matemática na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico do aluno (1: Preenchido, 0: Não preenchido). — descrição gerada por IA. |
| `IN_INSE` | STRING | Indicador de disponibilidade do Indicador do Nível Socioeconômico do aluno (1: Sim, 0: Não). — descrição gerada por IA. |
| `INSE_ALUNO` | STRING | Valor numérico contínuo do Indicador de Nível Socioeconômico (INSE) do aluno. — descrição gerada por IA. |
| `NU_TIPO_NIVEL_INSE` | STRING | Categoria do nível socioeconômico do aluno (ex: Nível I a VIII). — descrição gerada por IA. |
| `PESO_ALUNO_INSE` | STRING | Peso amostral do aluno utilizado na expansão estatística do INSE. — descrição gerada por IA. |
| `TX_RESP_Q01` | STRING | Resposta da questão 1 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q02` | STRING | Resposta da questão 2 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q03` | STRING | Resposta da questão 3 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q04` | STRING | Resposta da questão 4 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q05` | STRING | Resposta da questão 5 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q06a` | STRING | Resposta da subquestão 6a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q06b` | STRING | Resposta da subquestão 6b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q06c` | STRING | Resposta da subquestão 6c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q06d` | STRING | Resposta da subquestão 6d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q06e` | STRING | Resposta da subquestão 6e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07` | STRING | Resposta da questão 7 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q08` | STRING | Resposta da questão 8 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q09a` | STRING | Resposta da subquestão 9a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q09b` | STRING | Resposta da subquestão 9b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q09c` | STRING | Resposta da subquestão 9c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q09d` | STRING | Resposta da subquestão 9d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q09e` | STRING | Resposta da subquestão 9e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q09f` | STRING | Resposta da subquestão 9f do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10a` | STRING | Resposta da subquestão 10a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10b` | STRING | Resposta da subquestão 10b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10c` | STRING | Resposta da subquestão 10c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11a` | STRING | Resposta da subquestão 11a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11b` | STRING | Resposta da subquestão 11b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11c` | STRING | Resposta da subquestão 11c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11d` | STRING | Resposta da subquestão 11d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11e` | STRING | Resposta da subquestão 11e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11f` | STRING | Resposta da subquestão 11f do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11g` | STRING | Resposta da subquestão 11g do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11h` | STRING | Resposta da subquestão 11h do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12a` | STRING | Resposta da subquestão 12a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12b` | STRING | Resposta da subquestão 12b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12c` | STRING | Resposta da subquestão 12c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12d` | STRING | Resposta da subquestão 12d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12e` | STRING | Resposta da subquestão 12e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12f` | STRING | Resposta da subquestão 12f do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12g` | STRING | Resposta da subquestão 12g do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12h` | STRING | Resposta da subquestão 12h do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12i` | STRING | Resposta da subquestão 12i do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13` | STRING | Resposta da questão 13 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q14` | STRING | Resposta da questão 14 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q15` | STRING | Resposta da questão 15 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q16` | STRING | Resposta da questão 16 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q17` | STRING | Resposta da questão 17 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q18` | STRING | Resposta da questão 18 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q19` | STRING | Resposta da questão 19 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q20a` | STRING | Resposta da subquestão 20a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q20b` | STRING | Resposta da subquestão 20b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q20c` | STRING | Resposta da subquestão 20c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q20d` | STRING | Resposta da subquestão 20d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q20e` | STRING | Resposta da subquestão 20e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21a` | STRING | Resposta da subquestão 21a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21b` | STRING | Resposta da subquestão 21b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21c` | STRING | Resposta da subquestão 21c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21d` | STRING | Resposta da subquestão 21d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21e` | STRING | Resposta da subquestão 21e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21f` | STRING | Resposta da subquestão 21f do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21g` | STRING | Resposta da subquestão 21g do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21h` | STRING | Resposta da subquestão 21h do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21i` | STRING | Resposta da subquestão 21i do questionário socioeconômico do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_aluno_9ef

File `raw__inep_saeb_microdados_csv_2021_ts_aluno_9ef.parquet` · 2,591,937 rows · 144 columns

Raw do microdado CSV TS_ALUNO_9EF.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_ensino_fundamental_e_medio.zip.

**Feeds:** `raw/inep_saeb_aluno_2021`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano da edição da avaliação do SAEB (ex: 2021). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do Estado/Unidade Federativa da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. — descrição gerada por IA. |
| `ID_AREA` | STRING | Área geográfica da escola (1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP/Censo Escolar da unidade de ensino. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de rede pública (1 para pública, 0 para privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador único da turma no Censo Escolar/SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar avaliado (ex: 5, 9, 12). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador do aluno participante no SAEB. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno segundo o Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento do teste de Língua Portuguesa (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento do teste de Matemática (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_CH` | STRING | Indicador de preenchimento do teste de Ciências Humanas (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_CN` | STRING | Indicador de preenchimento do teste de Ciências da Natureza (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença no dia do teste de Língua Portuguesa (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença no dia do teste de Matemática (1-Presente, 0-Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_CH` | STRING | Indicador de presença na prova de Ciências Humanas. — descrição gerada por IA. |
| `IN_PRESENCA_CN` | STRING | Indicador de presença na prova de Ciências da Natureza. — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Código do caderno de prova de Língua Portuguesa respondido pelo aluno. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Código do bloco 1 do caderno de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Código do bloco 2 do caderno de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Código do caderno de prova de Matemática respondido pelo aluno. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Código do bloco 1 do caderno de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Código do bloco 2 do caderno de Matemática. — descrição gerada por IA. |
| `ID_CADERNO_CH` | STRING | Código do caderno de prova de Ciências Humanas. — descrição gerada por IA. |
| `ID_BLOCO_1_CH` | STRING | Código do bloco 1 de Ciências Humanas. — descrição gerada por IA. |
| `ID_BLOCO_2_CH` | STRING | Código do bloco 2 de Ciências Humanas. — descrição gerada por IA. |
| `ID_BLOCO_3_CH` | STRING | Código do bloco 3 de Ciências Humanas. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_CH` | STRING | Número do item aberto/discursivo do bloco 1 de Ciências Humanas. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_CH` | STRING | Número do item aberto/discursivo do bloco 2 de Ciências Humanas. — descrição gerada por IA. |
| `ID_CADERNO_CN` | STRING | Código do caderno de prova de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_1_CN` | STRING | Código do bloco 1 de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_2_CN` | STRING | Código do bloco 2 de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_3_CN` | STRING | Código do bloco 3 de Ciências da Natureza. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_CN` | STRING | Número do item aberto/discursivo do bloco 1 de Ciências da Natureza. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_CN` | STRING | Número do item aberto/discursivo do bloco 2 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Vetor com as opções assinaladas pelo aluno no bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Vetor com as opções assinaladas pelo aluno no bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Vetor com as opções assinaladas pelo aluno no bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Vetor com as opções assinaladas pelo aluno no bloco 2 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_CH` | STRING | Vetor com as respostas do aluno no bloco 1 de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_CH` | STRING | Vetor com as respostas do aluno no bloco 2 de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO3_CH` | STRING | Vetor com as respostas do aluno no bloco 3 de Ciências Humanas. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_CH` | STRING | Conceito/nota atribuída à primeira questão aberta de Ciências Humanas. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_CH` | STRING | Conceito/nota atribuída à segunda questão aberta de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_CN` | STRING | Vetor com as respostas do aluno no bloco 1 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_CN` | STRING | Vetor com as respostas do aluno no bloco 2 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO3_CN` | STRING | Vetor com as respostas do aluno no bloco 3 de Ciências da Natureza. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_CN` | STRING | Conceito/nota atribuída à primeira questão aberta de Ciências da Natureza. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_CN` | STRING | Conceito/nota atribuída à segunda questão aberta de Ciências da Natureza. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador de proficiência calculada em Língua Portuguesa (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador de proficiência calculada em Matemática (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_CH` | STRING | Indicador de proficiência calculada em Ciências Humanas (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_CN` | STRING | Indicador de proficiência calculada em Ciências da Natureza (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador de pertencimento do aluno à amostra estatística do SAEB. — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato de amostragem do aluno. — descrição gerada por IA. |
| `ESTRATO_CIENCIAS` | STRING | Código do estrato amostral específico para a prova de Ciências. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para cálculos de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota/proficiência do aluno em Língua Portuguesa na escala do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão do cálculo da proficiência de Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência em Língua Portuguesa padronizada para métricas oficiais SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência padronizada de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para cálculos de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota/proficiência do aluno em Matemática na escala do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão do cálculo da proficiência de Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência em Matemática padronizada para métricas oficiais SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência padronizada de Matemática. — descrição gerada por IA. |
| `PESO_ALUNO_CH` | STRING | Peso amostral do aluno para cálculos de Ciências Humanas. — descrição gerada por IA. |
| `PROFICIENCIA_CH` | STRING | Nota/proficiência do aluno em Ciências Humanas. — descrição gerada por IA. |
| `ERRO_PADRAO_CH` | STRING | Erro padrão do cálculo da proficiência de Ciências Humanas. — descrição gerada por IA. |
| `PROFICIENCIA_CH_SAEB` | STRING | Proficiência em Ciências Humanas padronizada para o SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_CH_SAEB` | STRING | Erro padrão da proficiência padronizada de Ciências Humanas. — descrição gerada por IA. |
| `PESO_ALUNO_CN` | STRING | Peso amostral do aluno para cálculos de Ciências da Natureza. — descrição gerada por IA. |
| `PROFICIENCIA_CN` | STRING | Nota/proficiência do aluno em Ciências da Natureza. — descrição gerada por IA. |
| `ERRO_PADRAO_CN` | STRING | Erro padrão do cálculo da proficiência de Ciências da Natureza. — descrição gerada por IA. |
| `PROFICIENCIA_CN_SAEB` | STRING | Proficiência em Ciências da Natureza padronizada para o SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_CN_SAEB` | STRING | Erro padrão da proficiência padronizada de Ciências da Natureza. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_INSE` | STRING | Indicador de cálculo do Indicador do Nível Socioeconômico do aluno (1-Sim, 0-Não). — descrição gerada por IA. |
| `INSE_ALUNO` | STRING | Escore numérico do Nível Socioeconômico (INSE) do aluno. — descrição gerada por IA. |
| `NU_TIPO_NIVEL_INSE` | STRING | Nível/categoria do INSE atribuído ao aluno. — descrição gerada por IA. |
| `PESO_ALUNO_INSE` | STRING | Peso amostral do aluno utilizado no cálculo de estatísticas do INSE. — descrição gerada por IA. |
| `TX_RESP_Q01` | STRING | Resposta da questão socioeconômica 1 (ex: sexo do aluno). — descrição gerada por IA. |
| `TX_RESP_Q02` | STRING | Resposta da questão socioeconômica 2 (ex: cor/raça). — descrição gerada por IA. |
| `TX_RESP_Q03` | STRING | Resposta da questão socioeconômica 3 (ex: data de nascimento). — descrição gerada por IA. |
| `TX_RESP_Q04` | STRING | Resposta da questão socioeconômica 4 (ex: escolaridade da mãe). — descrição gerada por IA. |
| `TX_RESP_Q05` | STRING | Resposta da questão socioeconômica 5 (ex: escolaridade do pai). — descrição gerada por IA. |
| `TX_RESP_Q06a` | STRING | Resposta do item socioeconômico 6a (posse de itens em casa). — descrição gerada por IA. |
| `TX_RESP_Q06b` | STRING | Resposta do item socioeconômico 6b (posse de itens em casa). — descrição gerada por IA. |
| `TX_RESP_Q06c` | STRING | Resposta do item socioeconômico 6c (posse de itens em casa). — descrição gerada por IA. |
| `TX_RESP_Q06d` | STRING | Resposta do item socioeconômico 6d (posse de itens em casa). — descrição gerada por IA. |
| `TX_RESP_Q06e` | STRING | Resposta do item socioeconômico 6e (posse de itens em casa). — descrição gerada por IA. |
| `TX_RESP_Q07` | STRING | Resposta da questão socioeconômica 7 (ex: hábito de leitura). — descrição gerada por IA. |
| `TX_RESP_Q08` | STRING | Resposta da questão socioeconômica 8. — descrição gerada por IA. |
| `TX_RESP_Q09a` | STRING | Resposta do subitem 9a do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q09b` | STRING | Resposta do subitem 9b do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q09c` | STRING | Resposta do subitem 9c do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q09d` | STRING | Resposta do subitem 9d do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q09e` | STRING | Resposta do subitem 9e do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q09f` | STRING | Resposta do subitem 9f do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q10a` | STRING | Resposta do subitem 10a do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q10b` | STRING | Resposta do subitem 10b do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q10c` | STRING | Resposta do subitem 10c do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q11a` | STRING | Resposta do subitem 11a do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q11b` | STRING | Resposta do subitem 11b do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q11c` | STRING | Resposta do subitem 11c do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q11d` | STRING | Resposta do subitem 11d do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q11e` | STRING | Resposta do subitem 11e do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q11f` | STRING | Resposta do subitem 11f do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q11g` | STRING | Resposta do subitem 11g do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q11h` | STRING | Resposta do subitem 11h do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q12a` | STRING | Resposta do subitem 12a do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q12b` | STRING | Resposta do subitem 12b do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q12c` | STRING | Resposta do subitem 12c do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q12d` | STRING | Resposta do subitem 12d do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q12e` | STRING | Resposta do subitem 12e do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q12f` | STRING | Resposta do subitem 12f do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q12g` | STRING | Resposta do subitem 12g do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q12h` | STRING | Resposta do subitem 12h do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q12i` | STRING | Resposta do subitem 12i do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q13` | STRING | Resposta da questão 13 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q14` | STRING | Resposta da questão 14 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q15` | STRING | Resposta da questão 15 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q16` | STRING | Resposta da questão 16 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q17` | STRING | Resposta da questão 17 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q18` | STRING | Resposta da questão 18 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q19` | STRING | Resposta da questão 19 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q20a` | STRING | Resposta do subitem 20a do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q20b` | STRING | Resposta do subitem 20b do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q20c` | STRING | Resposta do subitem 20c do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q20d` | STRING | Resposta do subitem 20d do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q20e` | STRING | Resposta do subitem 20e do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q21` | STRING | Resposta da questão 21 do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q22a` | STRING | Resposta do subitem 22a do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q22b` | STRING | Resposta do subitem 22b do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q22c` | STRING | Resposta do subitem 22c do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q22d` | STRING | Resposta do subitem 22d do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q22e` | STRING | Resposta do subitem 22e do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q22f` | STRING | Resposta do subitem 22f do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q22g` | STRING | Resposta do subitem 22g do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q22h` | STRING | Resposta do subitem 22h do questionário socioeconômico. — descrição gerada por IA. |
| `TX_RESP_Q22i` | STRING | Resposta do subitem 22i do questionário socioeconômico. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_diretor

File `raw__inep_saeb_microdados_csv_2021_ts_diretor.parquet` · 74,539 rows · 219 columns

Raw do microdado CSV TS_DIRETOR.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_ensino_fundamental_e_medio.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de edição do exame SAEB (ex: 2021). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica brasileira (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do Estado (Unidade da Federação) onde se localiza a escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está situada. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código da área de localização (ex: 1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (Censo Escolar) de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola é da rede pública (1=Pública, 0=Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Tipo de localização da escola (1=Urbana, 2=Rural). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador se o questionário foi preenchido (1=Sim, 0=Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Resposta da questão 001 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Resposta da questão 002 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Resposta da questão 003 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Resposta da questão 004 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Resposta da questão 005 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Resposta da questão 006 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Resposta da questão 007 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Resposta da questão 008 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Resposta da questão 009 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Resposta da questão 010 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Resposta da questão 011 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Resposta da questão 012 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Resposta da questão 013 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Resposta da questão 014 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Resposta da questão 015 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Resposta da questão 016 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Resposta da questão 017 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Resposta da questão 018 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Resposta da questão 019 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Resposta da questão 020 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Resposta da questão 021 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Resposta da questão 022 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Resposta da questão 023 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Resposta da questão 024 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Resposta da questão 025 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Resposta da questão 026 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Resposta da questão 027 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Resposta da questão 028 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Resposta da questão 029 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Resposta da questão 030 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Resposta da questão 031 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Resposta da questão 032 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Resposta da questão 033 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Resposta da questão 034 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Resposta da questão 035 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Resposta da questão 036 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Resposta da questão 037 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Resposta da questão 038 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Resposta da questão 039 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Resposta da questão 040 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Resposta da questão 041 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Resposta da questão 042 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Resposta da questão 043 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Resposta da questão 044 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Resposta da questão 045 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Resposta da questão 046 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Resposta da questão 047 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Resposta da questão 048 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Resposta da questão 049 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Resposta da questão 050 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Resposta da questão 051 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Resposta da questão 052 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Resposta da questão 053 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Resposta da questão 054 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Resposta da questão 055 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Resposta da questão 056 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Resposta da questão 057 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Resposta da questão 058 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Resposta da questão 059 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Resposta da questão 060 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Resposta da questão 061 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Resposta da questão 062 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Resposta da questão 063 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Resposta da questão 064 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Resposta da questão 065 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Resposta da questão 066 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Resposta da questão 067 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Resposta da questão 068 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Resposta da questão 069 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Resposta da questão 070 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Resposta da questão 071 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Resposta da questão 072 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Resposta da questão 073 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Resposta da questão 074 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Resposta da questão 075 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Resposta da questão 076 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Resposta da questão 077 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Resposta da questão 078 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Resposta da questão 079 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Resposta da questão 080 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Resposta da questão 081 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Resposta da questão 082 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Resposta da questão 083 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Resposta da questão 084 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Resposta da questão 085 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Resposta da questão 086 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Resposta da questão 087 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Resposta da questão 088 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Resposta da questão 089 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Resposta da questão 090 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Resposta da questão 091 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Resposta da questão 092 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Resposta da questão 093 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Resposta da questão 094 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Resposta da questão 095 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Resposta da questão 096 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Resposta da questão 097 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Resposta da questão 098 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Resposta da questão 099 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Resposta da questão 100 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Resposta da questão 101 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Resposta da questão 102 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Resposta da questão 103 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Resposta da questão 104 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Resposta da questão 105 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Resposta da questão 106 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Resposta da questão 107 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Resposta da questão 108 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Resposta da questão 109 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Resposta da questão 110 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Resposta da questão 111 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Resposta da questão 112 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Resposta da questão 113 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Resposta da questão 114 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Resposta da questão 115 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Resposta da questão 116 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Resposta da questão 117 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Resposta da questão 118 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Resposta da questão 119 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Resposta da questão 120 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Resposta da questão 121 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q122` | STRING | Resposta da questão 122 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q123` | STRING | Resposta da questão 123 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q124` | STRING | Resposta da questão 124 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q125` | STRING | Resposta da questão 125 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q126` | STRING | Resposta da questão 126 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q127` | STRING | Resposta da questão 127 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q128` | STRING | Resposta da questão 128 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q129` | STRING | Resposta da questão 129 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q130` | STRING | Resposta da questão 130 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q131` | STRING | Resposta da questão 131 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q132` | STRING | Resposta da questão 132 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q133` | STRING | Resposta da questão 133 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q134` | STRING | Resposta da questão 134 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q135` | STRING | Resposta da questão 135 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q136` | STRING | Resposta da questão 136 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q137` | STRING | Resposta da questão 137 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q138` | STRING | Resposta da questão 138 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q139` | STRING | Resposta da questão 139 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q140` | STRING | Resposta da questão 140 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q141` | STRING | Resposta da questão 141 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q142` | STRING | Resposta da questão 142 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q143` | STRING | Resposta da questão 143 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q144` | STRING | Resposta da questão 144 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q145` | STRING | Resposta da questão 145 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q146` | STRING | Resposta da questão 146 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q147` | STRING | Resposta da questão 147 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q148` | STRING | Resposta da questão 148 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q149` | STRING | Resposta da questão 149 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q150` | STRING | Resposta da questão 150 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q151` | STRING | Resposta da questão 151 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q152` | STRING | Resposta da questão 152 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q153` | STRING | Resposta da questão 153 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q154` | STRING | Resposta da questão 154 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q155` | STRING | Resposta da questão 155 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q156` | STRING | Resposta da questão 156 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q157` | STRING | Resposta da questão 157 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q158` | STRING | Resposta da questão 158 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q159` | STRING | Resposta da questão 159 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q160` | STRING | Resposta da questão 160 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q161` | STRING | Resposta da questão 161 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q162` | STRING | Resposta da questão 162 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q163` | STRING | Resposta da questão 163 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q164` | STRING | Resposta da questão 164 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q165` | STRING | Resposta da questão 165 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q166` | STRING | Resposta da questão 166 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q167` | STRING | Resposta da questão 167 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q168` | STRING | Resposta da questão 168 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q169` | STRING | Resposta da questão 169 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q170` | STRING | Resposta da questão 170 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q171` | STRING | Resposta da questão 171 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q172` | STRING | Resposta da questão 172 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q173` | STRING | Resposta da questão 173 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q174` | STRING | Resposta da questão 174 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q175` | STRING | Resposta da questão 175 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q176` | STRING | Resposta da questão 176 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q177` | STRING | Resposta da questão 177 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q178` | STRING | Resposta da questão 178 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q179` | STRING | Resposta da questão 179 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q180` | STRING | Resposta da questão 180 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q181` | STRING | Resposta da questão 181 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q182` | STRING | Resposta da questão 182 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q183` | STRING | Resposta da questão 183 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q184` | STRING | Resposta da questão 184 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q185` | STRING | Resposta da questão 185 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q186` | STRING | Resposta da questão 186 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q187` | STRING | Resposta da questão 187 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q188` | STRING | Resposta da questão 188 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q189` | STRING | Resposta da questão 189 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q190` | STRING | Resposta da questão 190 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q191` | STRING | Resposta da questão 191 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q192` | STRING | Resposta da questão 192 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q193` | STRING | Resposta da questão 193 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q194` | STRING | Resposta da questão 194 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q195` | STRING | Resposta da questão 195 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q196` | STRING | Resposta da questão 196 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q197` | STRING | Resposta da questão 197 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q198` | STRING | Resposta da questão 198 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q199` | STRING | Resposta da questão 199 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q200` | STRING | Resposta da questão 200 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q201` | STRING | Resposta da questão 201 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q202` | STRING | Resposta da questão 202 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q203` | STRING | Resposta da questão 203 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q204` | STRING | Resposta da questão 204 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q205` | STRING | Resposta da questão 205 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q206` | STRING | Resposta da questão 206 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q207` | STRING | Resposta da questão 207 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q208` | STRING | Resposta da questão 208 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q209` | STRING | Resposta da questão 209 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_RESP_Q210` | STRING | Resposta da questão 210 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_educacao_infantil_2021

File `raw__inep_saeb_microdados_csv_2021_ts_educacao_infantil_2021.parquet` · 62,927 rows · 421 columns

Raw do microdado CSV TS_EDUCACAO_INFANTIL_2021.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_educacao_infantil.zip.

| Column | Type | Description |
|---|---|---|
| `NU_ANO_SAEB` | STRING | Ano de realização da edição do SAEB (ex: 2021). — descrição gerada por IA. |
| `CO_UF` | STRING | Código IBGE da Unidade da Federação da escola. — descrição gerada por IA. |
| `CO_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `IN_CAPITAL` | STRING | Indicador se a escola está localizada em uma capital (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `TP_LOCALIZACAO` | STRING | Tipo de localização da escola (1 = Urbana, 2 = Rural). — descrição gerada por IA. |
| `ID_EDUCACAO_INFANTIL` | STRING | Identificador da unidade de amostragem da Educação Infantil no SAEB. — descrição gerada por IA. |
| `TP_EDUCACAO_INFANTIL` | STRING | Tipo de etapa de atendimento da Educação Infantil (ex: Creche, Pré-escola). — descrição gerada por IA. |
| `TP_DEPENDENCIA_ADM_ESTRT` | STRING | Código da dependência administrativa da escola (1=Federal, 2=Estadual, 3=Municipal, 4=Privada). — descrição gerada por IA. |
| `NU_DOMINIO` | STRING | Código do domínio de amostragem estatística. — descrição gerada por IA. |
| `NU_ESTRATO` | STRING | Código do estrato amostral da escola no SAEB. — descrição gerada por IA. |
| `VALIDO_P` | STRING | Indicador de questionário do professor considerado válido (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `DT_PREENCHIMENTO_P` | STRING | Data e hora do preenchimento do questionário do professor. — descrição gerada por IA. |
| `VALIDO_D` | STRING | Indicador de questionário do diretor considerado válido (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `DT_PREENCHIMENTO_D` | STRING | Data e hora do preenchimento do questionário do diretor. — descrição gerada por IA. |
| `IN_DUP_T` | STRING | Indicador de duplicidade no registro da turma (1 = Duplicado, 0 = Não). — descrição gerada por IA. |
| `IN_DUP_P` | STRING | Indicador de duplicidade no registro do professor (1 = Duplicado, 0 = Não). — descrição gerada por IA. |
| `IN_DUP_E` | STRING | Indicador de duplicidade no registro da escola (1 = Duplicado, 0 = Não). — descrição gerada por IA. |
| `IN_DUP_D` | STRING | Indicador de duplicidade no registro do diretor (1 = Duplicado, 0 = Não). — descrição gerada por IA. |
| `IN_ELEGIVEL` | STRING | Indicador de elegibilidade da unidade/turma na amostra do SAEB (1 = Elegível, 0 = Não). — descrição gerada por IA. |
| `NAO_RESPOSTA` | STRING | Indicador de não resposta ao questionário (1 = Não respondeu, 0 = Respondeu). — descrição gerada por IA. |
| `PESO_AMOSTRAL` | STRING | Peso de expansão amostral do registro para inferência estatística. — descrição gerada por IA. |
| `TG1Q01` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 1). — descrição gerada por IA. |
| `TG1Q02` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 2). — descrição gerada por IA. |
| `TG1Q03` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 3). — descrição gerada por IA. |
| `TG1Q04` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 4). — descrição gerada por IA. |
| `TG1Q05` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 5). — descrição gerada por IA. |
| `TG1Q06` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 6). — descrição gerada por IA. |
| `TG1Q07` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 7). — descrição gerada por IA. |
| `TG1Q08` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 8). — descrição gerada por IA. |
| `TG1Q09` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 9). — descrição gerada por IA. |
| `TG1Q10` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 10). — descrição gerada por IA. |
| `TG1Q11` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 11). — descrição gerada por IA. |
| `TG1Q12` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 12). — descrição gerada por IA. |
| `TG1Q13` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 13). — descrição gerada por IA. |
| `TG1Q14` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 14). — descrição gerada por IA. |
| `TG1Q15` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 15). — descrição gerada por IA. |
| `TG1Q16` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 16). — descrição gerada por IA. |
| `TG1Q17` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 17). — descrição gerada por IA. |
| `TG1Q18` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 18). — descrição gerada por IA. |
| `TG1Q19` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 19). — descrição gerada por IA. |
| `TG1Q20` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 20). — descrição gerada por IA. |
| `TG1Q21` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 21). — descrição gerada por IA. |
| `TG1Q22` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 22). — descrição gerada por IA. |
| `TG1Q23` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 23). — descrição gerada por IA. |
| `TG1Q24` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 24). — descrição gerada por IA. |
| `TG1Q25` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 25). — descrição gerada por IA. |
| `TG1Q26` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 26). — descrição gerada por IA. |
| `TG1Q27` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 27). — descrição gerada por IA. |
| `TG1Q28` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 28). — descrição gerada por IA. |
| `TG1Q29` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 29). — descrição gerada por IA. |
| `TG1Q30` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 30). — descrição gerada por IA. |
| `TG1Q31` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 1, Questão 31). — descrição gerada por IA. |
| `TG2Q01` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 1). — descrição gerada por IA. |
| `TG2Q02` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 2). — descrição gerada por IA. |
| `TG2Q03` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 3). — descrição gerada por IA. |
| `TG2Q04` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 4). — descrição gerada por IA. |
| `TG2Q05` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 5). — descrição gerada por IA. |
| `TG2Q06` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 6). — descrição gerada por IA. |
| `TG2Q07` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 7). — descrição gerada por IA. |
| `TG2Q08` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 8). — descrição gerada por IA. |
| `TG2Q09` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 9). — descrição gerada por IA. |
| `TG2Q10` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 10). — descrição gerada por IA. |
| `TG2Q11` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 11). — descrição gerada por IA. |
| `TG2Q12` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 12). — descrição gerada por IA. |
| `TG2Q13` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 13). — descrição gerada por IA. |
| `TG2Q14` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 14). — descrição gerada por IA. |
| `TG2Q15` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 15). — descrição gerada por IA. |
| `TG2Q16` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 16). — descrição gerada por IA. |
| `TG2Q17` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 17). — descrição gerada por IA. |
| `TG2Q18` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 18). — descrição gerada por IA. |
| `TG2Q19` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 2, Questão 19). — descrição gerada por IA. |
| `TG3Q01` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 1). — descrição gerada por IA. |
| `TG3Q02` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 2). — descrição gerada por IA. |
| `TG3Q03` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 3). — descrição gerada por IA. |
| `TG3Q04` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 4). — descrição gerada por IA. |
| `TG3Q05` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 5). — descrição gerada por IA. |
| `TG3Q06` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 6). — descrição gerada por IA. |
| `TG3Q07` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 7). — descrição gerada por IA. |
| `TG3Q08` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 8). — descrição gerada por IA. |
| `TG3Q09` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 9). — descrição gerada por IA. |
| `TG3Q10` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 10). — descrição gerada por IA. |
| `TG3Q11` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 11). — descrição gerada por IA. |
| `TG3Q12` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 12). — descrição gerada por IA. |
| `TG3Q13` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 13). — descrição gerada por IA. |
| `TG3Q14` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 14). — descrição gerada por IA. |
| `TG3Q15` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 15). — descrição gerada por IA. |
| `TG3Q16` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 16). — descrição gerada por IA. |
| `TG3Q17` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 17). — descrição gerada por IA. |
| `TG3Q18` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 3, Questão 18). — descrição gerada por IA. |
| `TG4Q01` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 1). — descrição gerada por IA. |
| `TG4Q02` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 2). — descrição gerada por IA. |
| `TG4Q03` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 3). — descrição gerada por IA. |
| `TG4Q04` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 4). — descrição gerada por IA. |
| `TG4Q05` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 5). — descrição gerada por IA. |
| `TG4Q06` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 6). — descrição gerada por IA. |
| `TG4Q07` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 7). — descrição gerada por IA. |
| `TG4Q08` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 8). — descrição gerada por IA. |
| `TG4Q09` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 9). — descrição gerada por IA. |
| `TG4Q10` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 10). — descrição gerada por IA. |
| `TG4Q11` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 11). — descrição gerada por IA. |
| `TG4Q12` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 12). — descrição gerada por IA. |
| `TG4Q13_A` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item A). — descrição gerada por IA. |
| `TG4Q13_B` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item B). — descrição gerada por IA. |
| `TG4Q13_C` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item C). — descrição gerada por IA. |
| `TG4Q13_D` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item D). — descrição gerada por IA. |
| `TG4Q13_E` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item E). — descrição gerada por IA. |
| `TG4Q13_F` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item F). — descrição gerada por IA. |
| `TG4Q13_G` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item G). — descrição gerada por IA. |
| `TG4Q13_H` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item H). — descrição gerada por IA. |
| `TG4Q13_I` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item I). — descrição gerada por IA. |
| `TG4Q13_J` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item J). — descrição gerada por IA. |
| `TG4Q13_K` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item K). — descrição gerada por IA. |
| `TG4Q13_L` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item L). — descrição gerada por IA. |
| `TG4Q13_M` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item M). — descrição gerada por IA. |
| `TG4Q13_N` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item N). — descrição gerada por IA. |
| `TG4Q13_O` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item O). — descrição gerada por IA. |
| `TG4Q13_P` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item P). — descrição gerada por IA. |
| `TG4Q13_Q` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 13, Item Q). — descrição gerada por IA. |
| `TG4Q14_A` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item A). — descrição gerada por IA. |
| `TG4Q14_B` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item B). — descrição gerada por IA. |
| `TG4Q14_C` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item C). — descrição gerada por IA. |
| `TG4Q14_D` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item D). — descrição gerada por IA. |
| `TG4Q14_E` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item E). — descrição gerada por IA. |
| `TG4Q14_F` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item F). — descrição gerada por IA. |
| `TG4Q14_G` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item G). — descrição gerada por IA. |
| `TG4Q14_H` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item H). — descrição gerada por IA. |
| `TG4Q14_I` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item I). — descrição gerada por IA. |
| `TG4Q14_J` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item J). — descrição gerada por IA. |
| `TG4Q14_K` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item K). — descrição gerada por IA. |
| `TG4Q14_L` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item L). — descrição gerada por IA. |
| `TG4Q14_M` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 14, Item M). — descrição gerada por IA. |
| `TG4Q15_A` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item A). — descrição gerada por IA. |
| `TG4Q15_B` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item B). — descrição gerada por IA. |
| `TG4Q15_C` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item C). — descrição gerada por IA. |
| `TG4Q15_D` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item D). — descrição gerada por IA. |
| `TG4Q15_E` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item E). — descrição gerada por IA. |
| `TG4Q15_F` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item F). — descrição gerada por IA. |
| `TG4Q15_G` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item G). — descrição gerada por IA. |
| `TG4Q15_H` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item H). — descrição gerada por IA. |
| `TG4Q15_I` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item I). — descrição gerada por IA. |
| `TG4Q15_J` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item J). — descrição gerada por IA. |
| `TG4Q15_K` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item K). — descrição gerada por IA. |
| `TG4Q15_L` | STRING | Resposta do questionário do professor/turma (Bloco 4, Questão 15, Item L). — descrição gerada por IA. |
| `TG4Q16` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 16). — descrição gerada por IA. |
| `TG4Q17` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 17). — descrição gerada por IA. |
| `TG4Q18` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 18). — descrição gerada por IA. |
| `TG4Q19` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 19). — descrição gerada por IA. |
| `TG4Q20` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 20). — descrição gerada por IA. |
| `TG4Q21` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 21). — descrição gerada por IA. |
| `TG4Q22` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 22). — descrição gerada por IA. |
| `TG4Q23` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 23). — descrição gerada por IA. |
| `TG4Q24` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 24). — descrição gerada por IA. |
| `TG4Q25` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 25). — descrição gerada por IA. |
| `TG4Q26` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 26). — descrição gerada por IA. |
| `TG4Q27` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 27). — descrição gerada por IA. |
| `TG4Q28` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 28). — descrição gerada por IA. |
| `TG4Q29` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 29). — descrição gerada por IA. |
| `TG4Q30` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 4, Questão 30). — descrição gerada por IA. |
| `TG5Q01` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 1). — descrição gerada por IA. |
| `TG5Q02` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 2). — descrição gerada por IA. |
| `TG5Q03` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 3). — descrição gerada por IA. |
| `TG5Q04` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 4). — descrição gerada por IA. |
| `TG5Q05` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 5). — descrição gerada por IA. |
| `TG5Q06` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 6). — descrição gerada por IA. |
| `TG5Q07` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 7). — descrição gerada por IA. |
| `TG5Q08` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 8). — descrição gerada por IA. |
| `TG5Q09` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 9). — descrição gerada por IA. |
| `TG5Q10` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 10). — descrição gerada por IA. |
| `TG5Q11` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 11). — descrição gerada por IA. |
| `TG5Q12` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 12). — descrição gerada por IA. |
| `TG5Q13` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 13). — descrição gerada por IA. |
| `TG5Q14` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 14). — descrição gerada por IA. |
| `TG5Q15` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 15). — descrição gerada por IA. |
| `TG5Q16` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 16). — descrição gerada por IA. |
| `TG5Q17` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 17). — descrição gerada por IA. |
| `TG5Q18` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 18). — descrição gerada por IA. |
| `TG5Q19_A` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 19, Item A). — descrição gerada por IA. |
| `TG5Q19_B` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 19, Item B). — descrição gerada por IA. |
| `TG5Q19_C` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 19, Item C). — descrição gerada por IA. |
| `TG5Q19_D` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 19, Item D). — descrição gerada por IA. |
| `TG5Q19_E` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 19, Item E). — descrição gerada por IA. |
| `TG5Q20_A` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 20, Item A). — descrição gerada por IA. |
| `TG5Q20_B` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 20, Item B). — descrição gerada por IA. |
| `TG5Q20_C` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 20, Item C). — descrição gerada por IA. |
| `TG5Q20_D` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 20, Item D). — descrição gerada por IA. |
| `TG5Q20_E` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 20, Item E). — descrição gerada por IA. |
| `TG5Q20_F` | STRING | Resposta do questionário do professor/turma (Bloco 5, Questão 20, Item F). — descrição gerada por IA. |
| `TG5Q21` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 21). — descrição gerada por IA. |
| `TG5Q22` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 22). — descrição gerada por IA. |
| `TG5Q23` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 23). — descrição gerada por IA. |
| `TG5Q24` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 24). — descrição gerada por IA. |
| `TG5Q25` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 25). — descrição gerada por IA. |
| `TG5Q26` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 26). — descrição gerada por IA. |
| `TG5Q27` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 27). — descrição gerada por IA. |
| `TG5Q28` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 28). — descrição gerada por IA. |
| `TG5Q29` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 29). — descrição gerada por IA. |
| `TG5Q30` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 30). — descrição gerada por IA. |
| `TG5Q31` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 31). — descrição gerada por IA. |
| `TG5Q32` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 32). — descrição gerada por IA. |
| `TG5Q33` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 33). — descrição gerada por IA. |
| `TG5Q34` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 34). — descrição gerada por IA. |
| `TG5Q35` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 35). — descrição gerada por IA. |
| `TG5Q36` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 36). — descrição gerada por IA. |
| `TG5Q37` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 37). — descrição gerada por IA. |
| `TG5Q38` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 38). — descrição gerada por IA. |
| `TG5Q39` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 39). — descrição gerada por IA. |
| `TG5Q40` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 40). — descrição gerada por IA. |
| `TG5Q41` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 41). — descrição gerada por IA. |
| `TG5Q42` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 42). — descrição gerada por IA. |
| `TG5Q43` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 5, Questão 43). — descrição gerada por IA. |
| `TG6Q01` | STRING | Resposta do questionário do professor/turma da Educação Infantil (Bloco 6, Questão 1). — descrição gerada por IA. |
| `EG1Q01` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 1, Questão 1). — descrição gerada por IA. |
| `EG1Q02` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 1, Questão 2). — descrição gerada por IA. |
| `EG1Q03` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 1, Questão 3). — descrição gerada por IA. |
| `EG1Q04` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 1, Questão 4). — descrição gerada por IA. |
| `EG1Q05` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 1, Questão 5). — descrição gerada por IA. |
| `EG1Q06` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 1, Questão 6). — descrição gerada por IA. |
| `EG2Q01` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 1). — descrição gerada por IA. |
| `EG2Q02` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 2). — descrição gerada por IA. |
| `EG2Q03` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 3). — descrição gerada por IA. |
| `EG2Q04` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 4). — descrição gerada por IA. |
| `EG2Q05` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 5). — descrição gerada por IA. |
| `EG2Q06` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 6). — descrição gerada por IA. |
| `EG2Q07` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 7). — descrição gerada por IA. |
| `EG2Q08` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 8). — descrição gerada por IA. |
| `EG2Q09` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 9). — descrição gerada por IA. |
| `EG2Q10` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 10). — descrição gerada por IA. |
| `EG2Q11` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 11). — descrição gerada por IA. |
| `EG2Q12` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 12). — descrição gerada por IA. |
| `EG2Q13` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 13). — descrição gerada por IA. |
| `EG2Q14` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 14). — descrição gerada por IA. |
| `EG2Q15` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 15). — descrição gerada por IA. |
| `EG2Q16` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 16). — descrição gerada por IA. |
| `EG2Q17` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 17). — descrição gerada por IA. |
| `EG2Q18` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 18). — descrição gerada por IA. |
| `EG2Q19` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 2, Questão 19). — descrição gerada por IA. |
| `EG3Q01` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 1). — descrição gerada por IA. |
| `EG3Q02` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 2). — descrição gerada por IA. |
| `EG3Q03` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 3). — descrição gerada por IA. |
| `EG3Q04` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 4). — descrição gerada por IA. |
| `EG3Q05` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 5). — descrição gerada por IA. |
| `EG3Q06` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 6). — descrição gerada por IA. |
| `EG3Q07` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 7). — descrição gerada por IA. |
| `EG3Q08` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 8). — descrição gerada por IA. |
| `EG3Q09` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 9). — descrição gerada por IA. |
| `EG3Q10` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 10). — descrição gerada por IA. |
| `EG3Q11` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 11). — descrição gerada por IA. |
| `EG3Q12` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 12). — descrição gerada por IA. |
| `EG3Q13` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 13). — descrição gerada por IA. |
| `EG3Q14` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 14). — descrição gerada por IA. |
| `EG3Q15` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 15). — descrição gerada por IA. |
| `EG3Q16` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 16). — descrição gerada por IA. |
| `EG3Q17` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 17). — descrição gerada por IA. |
| `EG3Q18` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 18). — descrição gerada por IA. |
| `EG3Q19` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 19). — descrição gerada por IA. |
| `EG3Q20` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 20). — descrição gerada por IA. |
| `EG3Q21` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 21). — descrição gerada por IA. |
| `EG3Q22` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 22). — descrição gerada por IA. |
| `EG3Q23` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 23). — descrição gerada por IA. |
| `EG3Q24` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 24). — descrição gerada por IA. |
| `EG3Q25` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 25). — descrição gerada por IA. |
| `EG3Q26` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 26). — descrição gerada por IA. |
| `EG3Q27` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 27). — descrição gerada por IA. |
| `EG3Q28` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 28). — descrição gerada por IA. |
| `EG3Q29` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 29). — descrição gerada por IA. |
| `EG3Q30` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 30). — descrição gerada por IA. |
| `EG3Q31` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 31). — descrição gerada por IA. |
| `EG3Q32` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 32). — descrição gerada por IA. |
| `EG3Q33` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 33). — descrição gerada por IA. |
| `EG3Q34` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 34). — descrição gerada por IA. |
| `EG3Q35` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 35). — descrição gerada por IA. |
| `EG3Q36` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 36). — descrição gerada por IA. |
| `EG3Q37` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 37). — descrição gerada por IA. |
| `EG3Q38` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 38). — descrição gerada por IA. |
| `EG3Q39` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 39). — descrição gerada por IA. |
| `EG3Q40` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 40). — descrição gerada por IA. |
| `EG3Q41` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 41). — descrição gerada por IA. |
| `EG3Q42` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 42). — descrição gerada por IA. |
| `EG3Q43` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 43). — descrição gerada por IA. |
| `EG3Q44` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 44). — descrição gerada por IA. |
| `EG3Q45` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 45). — descrição gerada por IA. |
| `EG3Q46` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 46). — descrição gerada por IA. |
| `EG3Q47` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 47). — descrição gerada por IA. |
| `EG3Q48` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 48). — descrição gerada por IA. |
| `EG3Q49` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 49). — descrição gerada por IA. |
| `EG3Q50` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 50). — descrição gerada por IA. |
| `EG3Q51` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 51). — descrição gerada por IA. |
| `EG3Q52` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 52). — descrição gerada por IA. |
| `EG3Q53` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 53). — descrição gerada por IA. |
| `EG3Q54` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 54). — descrição gerada por IA. |
| `EG3Q55` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 55). — descrição gerada por IA. |
| `EG3Q56` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 56). — descrição gerada por IA. |
| `EG3Q57` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 57). — descrição gerada por IA. |
| `EG3Q58` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 58). — descrição gerada por IA. |
| `EG3Q59` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 59). — descrição gerada por IA. |
| `EG3Q60` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 60). — descrição gerada por IA. |
| `EG3Q61` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 61). — descrição gerada por IA. |
| `EG3Q62` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 62). — descrição gerada por IA. |
| `EG3Q63` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 63). — descrição gerada por IA. |
| `EG3Q64` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 64). — descrição gerada por IA. |
| `EG3Q65` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 65). — descrição gerada por IA. |
| `EG3Q66` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 66). — descrição gerada por IA. |
| `EG3Q67` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 67). — descrição gerada por IA. |
| `EG3Q68` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 68). — descrição gerada por IA. |
| `EG3Q69` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 3, Questão 69). — descrição gerada por IA. |
| `EG4Q01` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 1). — descrição gerada por IA. |
| `EG4Q02` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 2). — descrição gerada por IA. |
| `EG4Q03` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 3). — descrição gerada por IA. |
| `EG4Q04` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 4). — descrição gerada por IA. |
| `EG4Q05` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 5). — descrição gerada por IA. |
| `EG4Q06` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 6). — descrição gerada por IA. |
| `EG4Q07_A` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 7, Item A). — descrição gerada por IA. |
| `EG4Q07_B` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 7, Item B). — descrição gerada por IA. |
| `EG4Q07_C` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 7, Item C). — descrição gerada por IA. |
| `EG4Q07_D` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 7, Item D). — descrição gerada por IA. |
| `EG4Q07_E` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 7, Item E). — descrição gerada por IA. |
| `EG4Q07_F` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 7, Item F). — descrição gerada por IA. |
| `EG4Q08` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 8). — descrição gerada por IA. |
| `EG4Q09` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 9). — descrição gerada por IA. |
| `EG4Q10` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 10). — descrição gerada por IA. |
| `EG4Q11` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 11). — descrição gerada por IA. |
| `EG4Q12` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 12). — descrição gerada por IA. |
| `EG4Q13` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 13). — descrição gerada por IA. |
| `EG4Q14` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 14). — descrição gerada por IA. |
| `EG4Q15` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 15). — descrição gerada por IA. |
| `EG4Q16_A` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 16, Item A). — descrição gerada por IA. |
| `EG4Q16_B` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 16, Item B). — descrição gerada por IA. |
| `EG4Q16_C` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 16, Item C). — descrição gerada por IA. |
| `EG4Q17_A` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 17, Item A). — descrição gerada por IA. |
| `EG4Q17_B` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 17, Item B). — descrição gerada por IA. |
| `EG4Q17_C` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 17, Item C). — descrição gerada por IA. |
| `EG4Q18_A` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 18, Item A). — descrição gerada por IA. |
| `EG4Q18_B` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 18, Item B). — descrição gerada por IA. |
| `EG4Q18_C` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 18, Item C). — descrição gerada por IA. |
| `EG4Q19` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 19). — descrição gerada por IA. |
| `EG4Q20` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 20). — descrição gerada por IA. |
| `EG4Q21` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 21). — descrição gerada por IA. |
| `EG4Q22` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 22). — descrição gerada por IA. |
| `EG4Q23` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 23). — descrição gerada por IA. |
| `EG4Q24` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 24). — descrição gerada por IA. |
| `EG4Q25` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 25). — descrição gerada por IA. |
| `EG4Q26` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 26). — descrição gerada por IA. |
| `EG4Q27` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 27). — descrição gerada por IA. |
| `EG4Q28` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 28). — descrição gerada por IA. |
| `EG4Q29` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 29). — descrição gerada por IA. |
| `EG4Q30` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 30). — descrição gerada por IA. |
| `EG4Q31` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 31). — descrição gerada por IA. |
| `EG4Q32` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 32). — descrição gerada por IA. |
| `EG4Q33` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 33). — descrição gerada por IA. |
| `EG4Q34` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 34). — descrição gerada por IA. |
| `EG4Q35` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 35). — descrição gerada por IA. |
| `EG4Q36` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 36). — descrição gerada por IA. |
| `EG4Q37` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 37). — descrição gerada por IA. |
| `EG4Q38` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 38). — descrição gerada por IA. |
| `EG4Q39` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 39). — descrição gerada por IA. |
| `EG4Q40_A` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 40, Item A). — descrição gerada por IA. |
| `EG4Q40_B` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 40, Item B). — descrição gerada por IA. |
| `EG4Q40_C` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 40, Item C). — descrição gerada por IA. |
| `EG4Q40_D` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 40, Item D). — descrição gerada por IA. |
| `EG4Q40_E` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 40, Item E). — descrição gerada por IA. |
| `EG4Q40_F` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 40, Item F). — descrição gerada por IA. |
| `EG4Q40_G` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 40, Item G). — descrição gerada por IA. |
| `EG4Q40_H` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 40, Item H). — descrição gerada por IA. |
| `EG4Q41` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 41). — descrição gerada por IA. |
| `EG4Q42_A` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 42, Item A). — descrição gerada por IA. |
| `EG4Q42_B` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 42, Item B). — descrição gerada por IA. |
| `EG4Q42_C` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 42, Item C). — descrição gerada por IA. |
| `EG4Q42_D` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 42, Item D). — descrição gerada por IA. |
| `EG4Q42_E` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 42, Item E). — descrição gerada por IA. |
| `EG4Q42_F` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 42, Item F). — descrição gerada por IA. |
| `EG4Q42_G` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 42, Item G). — descrição gerada por IA. |
| `EG4Q43` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 43). — descrição gerada por IA. |
| `EG4Q44` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 44). — descrição gerada por IA. |
| `EG4Q45` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 45). — descrição gerada por IA. |
| `EG4Q46` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 46). — descrição gerada por IA. |
| `EG4Q47` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 47). — descrição gerada por IA. |
| `EG4Q48` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 48). — descrição gerada por IA. |
| `EG4Q49` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 49). — descrição gerada por IA. |
| `EG4Q50` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 50). — descrição gerada por IA. |
| `EG4Q51` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 51). — descrição gerada por IA. |
| `EG4Q52` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 52). — descrição gerada por IA. |
| `EG4Q53` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 53). — descrição gerada por IA. |
| `EG4Q54` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 54). — descrição gerada por IA. |
| `EG4Q55` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 55). — descrição gerada por IA. |
| `EG4Q56` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 56). — descrição gerada por IA. |
| `EG4Q57` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 57). — descrição gerada por IA. |
| `EG4Q58` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 58). — descrição gerada por IA. |
| `EG4Q59` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 59). — descrição gerada por IA. |
| `EG4Q60_A` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item A). — descrição gerada por IA. |
| `EG4Q60_B` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item B). — descrição gerada por IA. |
| `EG4Q60_C` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item C). — descrição gerada por IA. |
| `EG4Q60_D` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item D). — descrição gerada por IA. |
| `EG4Q60_E` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item E). — descrição gerada por IA. |
| `EG4Q60_F` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item F). — descrição gerada por IA. |
| `EG4Q60_G` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item G). — descrição gerada por IA. |
| `EG4Q60_H` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item H). — descrição gerada por IA. |
| `EG4Q60_I` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item I). — descrição gerada por IA. |
| `EG4Q60_J` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item J). — descrição gerada por IA. |
| `EG4Q60_K` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item K). — descrição gerada por IA. |
| `EG4Q60_L` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item L). — descrição gerada por IA. |
| `EG4Q60_M` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item M). — descrição gerada por IA. |
| `EG4Q60_N` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item N). — descrição gerada por IA. |
| `EG4Q60_O` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item O). — descrição gerada por IA. |
| `EG4Q60_P` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item P). — descrição gerada por IA. |
| `EG4Q60_Q` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item Q). — descrição gerada por IA. |
| `EG4Q60_R` | STRING | Resposta do questionário do diretor/escola (Bloco 4, Questão 60, Item R). — descrição gerada por IA. |
| `EG4Q61` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 61). — descrição gerada por IA. |
| `EG4Q62` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 62). — descrição gerada por IA. |
| `EG4Q63` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 63). — descrição gerada por IA. |
| `EG4Q64` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 64). — descrição gerada por IA. |
| `EG4Q65` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 65). — descrição gerada por IA. |
| `EG4Q66` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 66). — descrição gerada por IA. |
| `EG4Q67` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 67). — descrição gerada por IA. |
| `EG4Q68` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 68). — descrição gerada por IA. |
| `EG4Q69` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 69). — descrição gerada por IA. |
| `EG4Q70` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 70). — descrição gerada por IA. |
| `EG4Q71` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 71). — descrição gerada por IA. |
| `EG4Q72` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 72). — descrição gerada por IA. |
| `EG4Q73` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 73). — descrição gerada por IA. |
| `EG4Q74` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 4, Questão 74). — descrição gerada por IA. |
| `EG5Q01` | STRING | Resposta do questionário do diretor/escola da Educação Infantil (Bloco 5, Questão 1). — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_escola

File `raw__inep_saeb_microdados_csv_2021_ts_escola.parquet` · 70,897 rows · 137 columns

Raw do microdado CSV TS_ESCOLA.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_ensino_fundamental_e_medio.zip.

**Feeds:** `trusted/inep_saeb_escola`, `trusted/inep_saeb_microdados_escola`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição da avaliação do SAEB. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico de identificação da região geográfica da escola (1 a 5). — descrição gerada por IA. |
| `ID_UF` | STRING | Código numérico do IBGE correspondente à Unidade Federativa da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE de 7 dígitos do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código da área de localização da escola (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (8 dígitos) de identificação única da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código do tipo de localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_INICIAL` | STRING | Percentual de docentes com formação superior adequada nos anos iniciais do Ensino Fundamental (0 a 100%). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_FINAL` | STRING | Percentual de docentes com formação superior adequada nos anos finais do Ensino Fundamental (0 a 100%). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_MEDIO` | STRING | Percentual de docentes com formação superior adequada no Ensino Médio (0 a 100%). — descrição gerada por IA. |
| `NIVEL_SOCIO_ECONOMICO` | STRING | Classificação do Indicador de Nível Socioeconômico (INSE) da escola segundo o INEP. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_5EF` | STRING | Número total de alunos matriculados no 5º ano do Ensino Fundamental segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_5EF` | STRING | Número de alunos do 5º ano do Ensino Fundamental presentes nas provas do SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_5EF` | STRING | Proporção de alunos participantes do 5º ano do Ensino Fundamental no SAEB (0 a 1). — descrição gerada por IA. |
| `NIVEL_0_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_9_LP5` | STRING | Percentual de alunos do 5º ano EF no nível 9 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_10_MT5` | STRING | Percentual de alunos do 5º ano EF no nível 10 de proficiência em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_9EF` | STRING | Número total de alunos matriculados no 9º ano do Ensino Fundamental no Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_9EF` | STRING | Número de alunos do 9º ano do Ensino Fundamental presentes nas provas do SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_9EF` | STRING | Proporção de alunos participantes do 9º ano do Ensino Fundamental no SAEB (0 a 1). — descrição gerada por IA. |
| `NIVEL_0_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP9` | STRING | Percentual de alunos do 9º ano EF no nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT9` | STRING | Percentual de alunos do 9º ano EF no nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_EMT` | STRING | Número de alunos matriculados no Ensino Médio Tradicional/Regular no Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_EMT` | STRING | Número de alunos do Ensino Médio Tradicional/Regular presentes no SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_EMT` | STRING | Taxa de participação dos alunos do Ensino Médio Tradicional/Regular no SAEB (0 a 1). — descrição gerada por IA. |
| `NIVEL_0_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LPEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_10_MTEMT` | STRING | Percentual de alunos do Ensino Médio Tradicional no nível 10 de proficiência em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_EMI` | STRING | Número de alunos matriculados no Ensino Médio Integrado no Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_EMI` | STRING | Número de alunos do Ensino Médio Integrado presentes no SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_EMI` | STRING | Taxa de participação dos alunos do Ensino Médio Integrado no SAEB (0 a 1). — descrição gerada por IA. |
| `NIVEL_0_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LPEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_10_MTEMI` | STRING | Percentual de alunos do Ensino Médio Integrado no nível 10 de proficiência em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_EM` | STRING | Número total de alunos matriculados no Ensino Médio (todas as modalidades) no Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_EM` | STRING | Número total de alunos do Ensino Médio presentes no SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_EM` | STRING | Taxa global de participação dos alunos do Ensino Médio no SAEB (0 a 1). — descrição gerada por IA. |
| `NIVEL_0_LPEM` | STRING | Percentual total de alunos do Ensino Médio no nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LPEM` | STRING | Percentual total de alunos do Ensino Médio no nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LPEM` | STRING | Percentual total de alunos do Ensino Médio no nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LPEM` | STRING | Percentual total de alunos do Ensino Médio no nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LPEM` | STRING | Percentual total de alunos do Ensino Médio no nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LPEM` | STRING | Percentual total de alunos do Ensino Médio no nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LPEM` | STRING | Percentual total de alunos do Ensino Médio no nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LPEM` | STRING | Percentual total de alunos do Ensino Médio no nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LPEM` | STRING | Percentual total de alunos do Ensino Médio no nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_10_MTEM` | STRING | Percentual total de alunos do Ensino Médio no nível 10 de proficiência em Matemática. — descrição gerada por IA. |
| `MEDIA_5EF_LP` | STRING | Nota média padronizada em Língua Portuguesa obtida pelos alunos do 5º ano do Ensino Fundamental na escala SAEB. — descrição gerada por IA. |
| `MEDIA_5EF_MT` | STRING | Nota média padronizada em Matemática obtida pelos alunos do 5º ano do Ensino Fundamental na escala SAEB. — descrição gerada por IA. |
| `MEDIA_9EF_LP` | STRING | Nota média padronizada em Língua Portuguesa obtida pelos alunos do 9º ano do Ensino Fundamental na escala SAEB. — descrição gerada por IA. |
| `MEDIA_9EF_MT` | STRING | Nota média padronizada em Matemática obtida pelos alunos do 9º ano do Ensino Fundamental na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EMT_LP` | STRING | Nota média padronizada em Língua Portuguesa obtida pelos alunos do Ensino Médio Tradicional na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EMT_MT` | STRING | Nota média padronizada em Matemática obtida pelos alunos do Ensino Médio Tradicional na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EMI_LP` | STRING | Nota média padronizada em Língua Portuguesa obtida pelos alunos do Ensino Médio Integrado na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EMI_MT` | STRING | Nota média padronizada em Matemática obtida pelos alunos do Ensino Médio Integrado na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EM_LP` | STRING | Nota média padronizada total em Língua Portuguesa obtida pelos alunos do Ensino Médio na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EM_MT` | STRING | Nota média padronizada total em Matemática obtida pelos alunos do Ensino Médio na escala SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_item

File `raw__inep_saeb_microdados_csv_2021_ts_item.parquet` · 854 rows · 15 columns

Raw do microdado CSV TS_ITEM.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_ensino_fundamental_e_medio.zip.

**Feeds:** `trusted/inep_saeb_microdados_item`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano ou edição da avaliação nacional do SAEB (ex: 2021). — descrição gerada por IA. |
| `DISCIPLINA` | STRING | Sigla da disciplina avaliada na prova (ex: 'LP' para Língua Portuguesa, 'MT' para Matemática). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série ou ano escolar avaliado (ex: '2' para o 2º ano do Ensino Fundamental). — descrição gerada por IA. |
| `BLOCO` | STRING | Número do bloco de questões no caderno de teste em que o item foi apresentado. — descrição gerada por IA. |
| `POSICAO` | STRING | Número de ordem/posição da questão dentro do bloco de prova. — descrição gerada por IA. |
| `ID_ITEM` | STRING | Código identificador único do item (questão) no banco de itens do INEP/SAEB. — descrição gerada por IA. |
| `NU_DESCRITOR_HABILIDADE` | STRING | Código do descritor de habilidade ou competência avaliada segundo a Matriz de Referência do SAEB (ex: 'H1.1'). — descrição gerada por IA. |
| `GABARITO` | STRING | Resposta correta ou padrão de pontuação do item (ex: 'A', 'B', 'A/B'). — descrição gerada por IA. |
| `TIPO_ITEM` | STRING | Classificação do formato de resposta da questão (ex: 'Resposta Objetiva', 'Resposta Construída', 'Produção Textual'). — descrição gerada por IA. |
| `ITEM_MODELO` | STRING | Modelo estatístico/psicométrico da Teoria de Resposta ao Item (TRI) aplicado (ex: 'M3PL' para modelo de 3 parâmetros, 'MRG' para resposta graduada). — descrição gerada por IA. |
| `A` | STRING | Parâmetro 'a' de discriminação do item na TRI (valor decimal). — descrição gerada por IA. |
| `B` | STRING | Parâmetro 'b' de dificuldade geral do item na TRI para questões dicotômicas (valor decimal). — descrição gerada por IA. |
| `C` | STRING | Parâmetro 'c' de probabilidade de acerto ao acaso (chute) na TRI (valor decimal). — descrição gerada por IA. |
| `B1` | STRING | Parâmetro de dificuldade 'b1' da TRI para a primeira categoria de resposta em itens politômicos ou de crédito parcial. — descrição gerada por IA. |
| `B2` | STRING | Parâmetro de dificuldade 'b2' da TRI para a segunda categoria de resposta em itens politômicos ou de crédito parcial. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_professor

File `raw__inep_saeb_microdados_csv_2021_ts_professor.parquet` · 565,640 rows · 135 columns

Raw do microdado CSV TS_PROFESSOR.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_ensino_fundamental_e_medio.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de edição do exame SAEB (ex: 2021). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do estado (Unidade da Federação) da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código de localização/área da escola segundo o INEP (ex: Capital, Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP/Censo Escolar de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1: Pública, 0: Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código da localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código de identificação da turma no SAEB. — descrição gerada por IA. |
| `ID_PROFESSOR` | STRING | Código identificador único do professor no cadastro do SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série ou ano escolar avaliado (ex: 5 para 5º ano, 9 para 9º ano). — descrição gerada por IA. |
| `SQ_QUESTIONARIO` | STRING | Sequencial ou versão do modelo do questionário aplicado ao professor. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento efetivo do questionário (1: Preenchido, 0: Não preenchido). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_OUTRA_TURMA` | STRING | Indicador se o professor já preencheu o questionário para outra turma (1: Sim, 0: Não). — descrição gerada por IA. |
| `TX_RESP_Q001` | STRING | Opção de resposta selecionada pelo professor na questão 001 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q002` | STRING | Opção de resposta selecionada pelo professor na questão 002 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q003` | STRING | Opção de resposta selecionada pelo professor na questão 003 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q004` | STRING | Opção de resposta selecionada pelo professor na questão 004 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q005` | STRING | Opção de resposta selecionada pelo professor na questão 005 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q006` | STRING | Opção de resposta selecionada pelo professor na questão 006 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q007` | STRING | Opção de resposta selecionada pelo professor na questão 007 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q008` | STRING | Opção de resposta selecionada pelo professor na questão 008 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q009` | STRING | Opção de resposta selecionada pelo professor na questão 009 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q010` | STRING | Opção de resposta selecionada pelo professor na questão 010 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q011` | STRING | Opção de resposta selecionada pelo professor na questão 011 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q012` | STRING | Opção de resposta selecionada pelo professor na questão 012 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q013` | STRING | Opção de resposta selecionada pelo professor na questão 013 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q014` | STRING | Opção de resposta selecionada pelo professor na questão 014 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q015` | STRING | Opção de resposta selecionada pelo professor na questão 015 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q016` | STRING | Opção de resposta selecionada pelo professor na questão 016 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q017` | STRING | Opção de resposta selecionada pelo professor na questão 017 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q018` | STRING | Opção de resposta selecionada pelo professor na questão 018 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q019` | STRING | Opção de resposta selecionada pelo professor na questão 019 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q020` | STRING | Opção de resposta selecionada pelo professor na questão 020 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q021` | STRING | Opção de resposta selecionada pelo professor na questão 021 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q022` | STRING | Opção de resposta selecionada pelo professor na questão 022 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q023` | STRING | Opção de resposta selecionada pelo professor na questão 023 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q024` | STRING | Opção de resposta selecionada pelo professor na questão 024 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q025` | STRING | Opção de resposta selecionada pelo professor na questão 025 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q026` | STRING | Opção de resposta selecionada pelo professor na questão 026 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q027` | STRING | Opção de resposta selecionada pelo professor na questão 027 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q028` | STRING | Opção de resposta selecionada pelo professor na questão 028 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q029` | STRING | Opção de resposta selecionada pelo professor na questão 029 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q030` | STRING | Opção de resposta selecionada pelo professor na questão 030 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q031` | STRING | Opção de resposta selecionada pelo professor na questão 031 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q032` | STRING | Opção de resposta selecionada pelo professor na questão 032 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q033` | STRING | Opção de resposta selecionada pelo professor na questão 033 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q034` | STRING | Opção de resposta selecionada pelo professor na questão 034 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q035` | STRING | Opção de resposta selecionada pelo professor na questão 035 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q036` | STRING | Opção de resposta selecionada pelo professor na questão 036 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q037` | STRING | Opção de resposta selecionada pelo professor na questão 037 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q038` | STRING | Opção de resposta selecionada pelo professor na questão 038 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q039` | STRING | Opção de resposta selecionada pelo professor na questão 039 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q040` | STRING | Opção de resposta selecionada pelo professor na questão 040 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q041` | STRING | Opção de resposta selecionada pelo professor na questão 041 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q042` | STRING | Opção de resposta selecionada pelo professor na questão 042 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q043` | STRING | Opção de resposta selecionada pelo professor na questão 043 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q044` | STRING | Opção de resposta selecionada pelo professor na questão 044 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q045` | STRING | Opção de resposta selecionada pelo professor na questão 045 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q046` | STRING | Opção de resposta selecionada pelo professor na questão 046 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q047` | STRING | Opção de resposta selecionada pelo professor na questão 047 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q048` | STRING | Opção de resposta selecionada pelo professor na questão 048 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q049` | STRING | Opção de resposta selecionada pelo professor na questão 049 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q050` | STRING | Opção de resposta selecionada pelo professor na questão 050 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q051` | STRING | Opção de resposta selecionada pelo professor na questão 051 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q052` | STRING | Opção de resposta selecionada pelo professor na questão 052 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q053` | STRING | Opção de resposta selecionada pelo professor na questão 053 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q054` | STRING | Opção de resposta selecionada pelo professor na questão 054 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q055` | STRING | Opção de resposta selecionada pelo professor na questão 055 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q056` | STRING | Opção de resposta selecionada pelo professor na questão 056 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q057` | STRING | Opção de resposta selecionada pelo professor na questão 057 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q058` | STRING | Opção de resposta selecionada pelo professor na questão 058 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q059` | STRING | Opção de resposta selecionada pelo professor na questão 059 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q060` | STRING | Opção de resposta selecionada pelo professor na questão 060 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q061` | STRING | Opção de resposta selecionada pelo professor na questão 061 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q062` | STRING | Opção de resposta selecionada pelo professor na questão 062 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q063` | STRING | Opção de resposta selecionada pelo professor na questão 063 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q064` | STRING | Opção de resposta selecionada pelo professor na questão 064 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q065` | STRING | Opção de resposta selecionada pelo professor na questão 065 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q066` | STRING | Opção de resposta selecionada pelo professor na questão 066 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q067` | STRING | Opção de resposta selecionada pelo professor na questão 067 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q068` | STRING | Opção de resposta selecionada pelo professor na questão 068 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q069` | STRING | Opção de resposta selecionada pelo professor na questão 069 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q070` | STRING | Opção de resposta selecionada pelo professor na questão 070 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q071` | STRING | Opção de resposta selecionada pelo professor na questão 071 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q072` | STRING | Opção de resposta selecionada pelo professor na questão 072 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q073` | STRING | Opção de resposta selecionada pelo professor na questão 073 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q074` | STRING | Opção de resposta selecionada pelo professor na questão 074 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q075` | STRING | Opção de resposta selecionada pelo professor na questão 075 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q076` | STRING | Opção de resposta selecionada pelo professor na questão 076 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q077` | STRING | Opção de resposta selecionada pelo professor na questão 077 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q078` | STRING | Opção de resposta selecionada pelo professor na questão 078 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q079` | STRING | Opção de resposta selecionada pelo professor na questão 079 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q080` | STRING | Opção de resposta selecionada pelo professor na questão 080 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q081` | STRING | Opção de resposta selecionada pelo professor na questão 081 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q082` | STRING | Opção de resposta selecionada pelo professor na questão 082 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q083` | STRING | Opção de resposta selecionada pelo professor na questão 083 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q084` | STRING | Opção de resposta selecionada pelo professor na questão 084 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q085` | STRING | Opção de resposta selecionada pelo professor na questão 085 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q086` | STRING | Opção de resposta selecionada pelo professor na questão 086 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q087` | STRING | Opção de resposta selecionada pelo professor na questão 087 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q088` | STRING | Opção de resposta selecionada pelo professor na questão 088 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q089` | STRING | Opção de resposta selecionada pelo professor na questão 089 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q090` | STRING | Opção de resposta selecionada pelo professor na questão 090 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q091` | STRING | Opção de resposta selecionada pelo professor na questão 091 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q092` | STRING | Opção de resposta selecionada pelo professor na questão 092 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q093` | STRING | Opção de resposta selecionada pelo professor na questão 093 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q094` | STRING | Opção de resposta selecionada pelo professor na questão 094 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q095` | STRING | Opção de resposta selecionada pelo professor na questão 095 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q096` | STRING | Opção de resposta selecionada pelo professor na questão 096 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q097` | STRING | Opção de resposta selecionada pelo professor na questão 097 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q098` | STRING | Opção de resposta selecionada pelo professor na questão 098 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q099` | STRING | Opção de resposta selecionada pelo professor na questão 099 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q100` | STRING | Opção de resposta selecionada pelo professor na questão 100 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q101` | STRING | Opção de resposta selecionada pelo professor na questão 101 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q102` | STRING | Opção de resposta selecionada pelo professor na questão 102 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q103` | STRING | Opção de resposta selecionada pelo professor na questão 103 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q104` | STRING | Opção de resposta selecionada pelo professor na questão 104 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q105` | STRING | Opção de resposta selecionada pelo professor na questão 105 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q106` | STRING | Opção de resposta selecionada pelo professor na questão 106 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q107` | STRING | Opção de resposta selecionada pelo professor na questão 107 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q108` | STRING | Opção de resposta selecionada pelo professor na questão 108 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q109` | STRING | Opção de resposta selecionada pelo professor na questão 109 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q110` | STRING | Opção de resposta selecionada pelo professor na questão 110 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q111` | STRING | Opção de resposta selecionada pelo professor na questão 111 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q112` | STRING | Opção de resposta selecionada pelo professor na questão 112 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q113` | STRING | Opção de resposta selecionada pelo professor na questão 113 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q114` | STRING | Opção de resposta selecionada pelo professor na questão 114 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q115` | STRING | Opção de resposta selecionada pelo professor na questão 115 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q116` | STRING | Opção de resposta selecionada pelo professor na questão 116 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q117` | STRING | Opção de resposta selecionada pelo professor na questão 117 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q118` | STRING | Opção de resposta selecionada pelo professor na questão 118 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q119` | STRING | Opção de resposta selecionada pelo professor na questão 119 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q120` | STRING | Opção de resposta selecionada pelo professor na questão 120 do questionário SAEB. — descrição gerada por IA. |
| `TX_RESP_Q121` | STRING | Opção de resposta selecionada pelo professor na questão 121 do questionário SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_secretario_municipal

File `raw__inep_saeb_microdados_csv_2021_ts_secretario_municipal.parquet` · 5,568 rows · 140 columns

Raw do microdado CSV TS_SECRETARIO_MUNICIPAL.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_ensino_fundamental_e_medio.zip.

**Feeds:** `trusted/inep_saeb_secretario`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano da edição do SAEB (ex: 2021). — descrição gerada por IA. |
| `CO_UF` | STRING | Código IBGE do Estado (Unidade da Federação). — descrição gerada por IA. |
| `CO_MUNICIPIO` | STRING | Código IBGE do município. — descrição gerada por IA. |
| `IN_CAPITAL` | STRING | Indicador se o município é capital do Estado (1 = Sim, 0 = Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO` | STRING | Indicador de preenchimento do questionário pelo dirigente municipal (1 = Preenchido, 0 = Não preenchido). — descrição gerada por IA. |
| `CO_TRATAMENTO` | STRING | Código de tratamento/consistência dos dados adotado pelo INEP. — descrição gerada por IA. |
| `DT_PREENCHIMENTO` | STRING | Data de preenchimento do questionário pelo secretário municipal. — descrição gerada por IA. |
| `MG2Q01` | STRING | Resposta do Secretário Municipal de Educação à Questão 01 do Bloco 2. — descrição gerada por IA. |
| `MG2Q02` | STRING | Resposta do Secretário Municipal de Educação à Questão 02 do Bloco 2. — descrição gerada por IA. |
| `MG2Q03` | STRING | Resposta do Secretário Municipal de Educação à Questão 03 do Bloco 2. — descrição gerada por IA. |
| `MG2Q04` | STRING | Resposta do Secretário Municipal de Educação à Questão 04 do Bloco 2. — descrição gerada por IA. |
| `MG2Q05` | STRING | Resposta do Secretário Municipal de Educação à Questão 05 do Bloco 2. — descrição gerada por IA. |
| `MG2Q06` | STRING | Resposta do Secretário Municipal de Educação à Questão 06 do Bloco 2. — descrição gerada por IA. |
| `MG2Q07` | STRING | Resposta do Secretário Municipal de Educação à Questão 07 do Bloco 2. — descrição gerada por IA. |
| `MG2Q08` | STRING | Resposta do Secretário Municipal de Educação à Questão 08 do Bloco 2. — descrição gerada por IA. |
| `MG2Q09` | STRING | Resposta do Secretário Municipal de Educação à Questão 09 do Bloco 2. — descrição gerada por IA. |
| `MG2Q10` | STRING | Resposta do Secretário Municipal de Educação à Questão 10 do Bloco 2. — descrição gerada por IA. |
| `MG2Q11` | STRING | Resposta do Secretário Municipal de Educação à Questão 11 do Bloco 2. — descrição gerada por IA. |
| `MG2Q12` | STRING | Resposta do Secretário Municipal de Educação à Questão 12 do Bloco 2. — descrição gerada por IA. |
| `MG2Q13` | STRING | Resposta do Secretário Municipal de Educação à Questão 13 do Bloco 2. — descrição gerada por IA. |
| `MG2Q14` | STRING | Resposta do Secretário Municipal de Educação à Questão 14 do Bloco 2. — descrição gerada por IA. |
| `MG2Q15` | STRING | Resposta do Secretário Municipal de Educação à Questão 15 do Bloco 2. — descrição gerada por IA. |
| `MG2Q16` | STRING | Resposta do Secretário Municipal de Educação à Questão 16 do Bloco 2. — descrição gerada por IA. |
| `MG2Q17` | STRING | Resposta do Secretário Municipal de Educação à Questão 17 do Bloco 2. — descrição gerada por IA. |
| `MG2Q18` | STRING | Resposta do Secretário Municipal de Educação à Questão 18 do Bloco 2. — descrição gerada por IA. |
| `MG2Q19` | STRING | Resposta do Secretário Municipal de Educação à Questão 19 do Bloco 2. — descrição gerada por IA. |
| `MG2Q20` | STRING | Resposta do Secretário Municipal de Educação à Questão 20 do Bloco 2. — descrição gerada por IA. |
| `MG2Q21` | STRING | Resposta do Secretário Municipal de Educação à Questão 21 do Bloco 2. — descrição gerada por IA. |
| `MG2Q22` | STRING | Resposta do Secretário Municipal de Educação à Questão 22 do Bloco 2. — descrição gerada por IA. |
| `MG2Q23` | STRING | Resposta do Secretário Municipal de Educação à Questão 23 do Bloco 2. — descrição gerada por IA. |
| `MG2Q24` | STRING | Resposta do Secretário Municipal de Educação à Questão 24 do Bloco 2. — descrição gerada por IA. |
| `MG2Q25` | STRING | Resposta do Secretário Municipal de Educação à Questão 25 do Bloco 2. — descrição gerada por IA. |
| `MG2Q26` | STRING | Resposta do Secretário Municipal de Educação à Questão 26 do Bloco 2. — descrição gerada por IA. |
| `MG2Q27` | STRING | Resposta do Secretário Municipal de Educação à Questão 27 do Bloco 2. — descrição gerada por IA. |
| `MG2Q28` | STRING | Resposta do Secretário Municipal de Educação à Questão 28 do Bloco 2. — descrição gerada por IA. |
| `MG2Q29` | STRING | Resposta do Secretário Municipal de Educação à Questão 29 do Bloco 2. — descrição gerada por IA. |
| `MG2Q30` | STRING | Resposta do Secretário Municipal de Educação à Questão 30 do Bloco 2. — descrição gerada por IA. |
| `MG2Q31` | STRING | Resposta do Secretário Municipal de Educação à Questão 31 do Bloco 2. — descrição gerada por IA. |
| `MG2Q32` | STRING | Resposta do Secretário Municipal de Educação à Questão 32 do Bloco 2. — descrição gerada por IA. |
| `MG2Q33` | STRING | Resposta do Secretário Municipal de Educação à Questão 33 do Bloco 2. — descrição gerada por IA. |
| `MG2Q34` | STRING | Resposta do Secretário Municipal de Educação à Questão 34 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_A` | STRING | Resposta do item A da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_B` | STRING | Resposta do item B da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_C` | STRING | Resposta do item C da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_D` | STRING | Resposta do item D da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_E` | STRING | Resposta do item E da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_F` | STRING | Resposta do item F da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_G` | STRING | Resposta do item G da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_H` | STRING | Resposta do item H da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_I` | STRING | Resposta do item I da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q35_J` | STRING | Resposta do item J da Questão 35 do Bloco 2. — descrição gerada por IA. |
| `MG2Q36` | STRING | Resposta do Secretário Municipal de Educação à Questão 36 do Bloco 2. — descrição gerada por IA. |
| `MG2Q37` | STRING | Resposta do Secretário Municipal de Educação à Questão 37 do Bloco 2. — descrição gerada por IA. |
| `MG2Q38` | STRING | Resposta do Secretário Municipal de Educação à Questão 38 do Bloco 2. — descrição gerada por IA. |
| `MG2Q39` | STRING | Resposta do Secretário Municipal de Educação à Questão 39 do Bloco 2. — descrição gerada por IA. |
| `MG2Q40` | STRING | Resposta do Secretário Municipal de Educação à Questão 40 do Bloco 2. — descrição gerada por IA. |
| `MG2Q41` | STRING | Resposta do Secretário Municipal de Educação à Questão 41 do Bloco 2. — descrição gerada por IA. |
| `MG2Q42` | STRING | Resposta do Secretário Municipal de Educação à Questão 42 do Bloco 2. — descrição gerada por IA. |
| `MG3Q01` | STRING | Resposta do Secretário Municipal de Educação à Questão 01 do Bloco 3. — descrição gerada por IA. |
| `MG3Q02` | STRING | Resposta do Secretário Municipal de Educação à Questão 02 do Bloco 3. — descrição gerada por IA. |
| `MG3Q03` | STRING | Resposta do Secretário Municipal de Educação à Questão 03 do Bloco 3. — descrição gerada por IA. |
| `MG3Q04` | STRING | Resposta do Secretário Municipal de Educação à Questão 04 do Bloco 3. — descrição gerada por IA. |
| `MG3Q05` | STRING | Resposta do Secretário Municipal de Educação à Questão 05 do Bloco 3. — descrição gerada por IA. |
| `MG3Q06` | STRING | Resposta do Secretário Municipal de Educação à Questão 06 do Bloco 3. — descrição gerada por IA. |
| `MG3Q07` | STRING | Resposta do Secretário Municipal de Educação à Questão 07 do Bloco 3. — descrição gerada por IA. |
| `MG3Q08` | STRING | Resposta do Secretário Municipal de Educação à Questão 08 do Bloco 3. — descrição gerada por IA. |
| `MG3Q09` | STRING | Resposta do Secretário Municipal de Educação à Questão 09 do Bloco 3. — descrição gerada por IA. |
| `MG3Q10` | STRING | Resposta do Secretário Municipal de Educação à Questão 10 do Bloco 3. — descrição gerada por IA. |
| `MG3Q11` | STRING | Resposta do Secretário Municipal de Educação à Questão 11 do Bloco 3. — descrição gerada por IA. |
| `MG3Q12` | STRING | Resposta do Secretário Municipal de Educação à Questão 12 do Bloco 3. — descrição gerada por IA. |
| `MG3Q13` | STRING | Resposta do Secretário Municipal de Educação à Questão 13 do Bloco 3. — descrição gerada por IA. |
| `MG3Q14` | STRING | Resposta do Secretário Municipal de Educação à Questão 14 do Bloco 3. — descrição gerada por IA. |
| `MG3Q15` | STRING | Resposta do Secretário Municipal de Educação à Questão 15 do Bloco 3. — descrição gerada por IA. |
| `MG3Q16` | STRING | Resposta do Secretário Municipal de Educação à Questão 16 do Bloco 3. — descrição gerada por IA. |
| `MG3Q17` | STRING | Resposta do Secretário Municipal de Educação à Questão 17 do Bloco 3. — descrição gerada por IA. |
| `MG3Q18` | STRING | Resposta do Secretário Municipal de Educação à Questão 18 do Bloco 3. — descrição gerada por IA. |
| `MG3Q19` | STRING | Resposta do Secretário Municipal de Educação à Questão 19 do Bloco 3. — descrição gerada por IA. |
| `MG3Q20` | STRING | Resposta do Secretário Municipal de Educação à Questão 20 do Bloco 3. — descrição gerada por IA. |
| `MG3Q21` | STRING | Resposta do Secretário Municipal de Educação à Questão 21 do Bloco 3. — descrição gerada por IA. |
| `MG4Q01` | STRING | Resposta do Secretário Municipal de Educação à Questão 01 do Bloco 4. — descrição gerada por IA. |
| `MG4Q02` | STRING | Resposta do Secretário Municipal de Educação à Questão 02 do Bloco 4. — descrição gerada por IA. |
| `MG4Q03` | STRING | Resposta do Secretário Municipal de Educação à Questão 03 do Bloco 4. — descrição gerada por IA. |
| `MG4Q04` | STRING | Resposta do Secretário Municipal de Educação à Questão 04 do Bloco 4. — descrição gerada por IA. |
| `MG4Q05` | STRING | Resposta do Secretário Municipal de Educação à Questão 05 do Bloco 4. — descrição gerada por IA. |
| `MG4Q06` | STRING | Resposta do Secretário Municipal de Educação à Questão 06 do Bloco 4. — descrição gerada por IA. |
| `MG4Q07` | STRING | Resposta do Secretário Municipal de Educação à Questão 07 do Bloco 4. — descrição gerada por IA. |
| `MG4Q08` | STRING | Resposta do Secretário Municipal de Educação à Questão 08 do Bloco 4. — descrição gerada por IA. |
| `MG4Q09` | STRING | Resposta do Secretário Municipal de Educação à Questão 09 do Bloco 4. — descrição gerada por IA. |
| `MG4Q10` | STRING | Resposta do Secretário Municipal de Educação à Questão 10 do Bloco 4. — descrição gerada por IA. |
| `MG5Q01` | STRING | Resposta do Secretário Municipal de Educação à Questão 01 do Bloco 5. — descrição gerada por IA. |
| `MG5Q02_A` | STRING | Resposta do item A da Questão 02 do Bloco 5. — descrição gerada por IA. |
| `MG5Q02_B` | STRING | Resposta do item B da Questão 02 do Bloco 5. — descrição gerada por IA. |
| `MG5Q02_C` | STRING | Resposta do item C da Questão 02 do Bloco 5. — descrição gerada por IA. |
| `MG5Q02_D` | STRING | Resposta do item D da Questão 02 do Bloco 5. — descrição gerada por IA. |
| `MG5Q02_E` | STRING | Resposta do item E da Questão 02 do Bloco 5. — descrição gerada por IA. |
| `MG5Q02_F` | STRING | Resposta do item F da Questão 02 do Bloco 5. — descrição gerada por IA. |
| `MG5Q02_G` | STRING | Resposta do item G da Questão 02 do Bloco 5. — descrição gerada por IA. |
| `MG5Q03` | STRING | Resposta do Secretário Municipal de Educação à Questão 03 do Bloco 5. — descrição gerada por IA. |
| `MG5Q04_A` | STRING | Resposta do item A da Questão 04 do Bloco 5. — descrição gerada por IA. |
| `MG5Q04_B` | STRING | Resposta do item B da Questão 04 do Bloco 5. — descrição gerada por IA. |
| `MG5Q04_C` | STRING | Resposta do item C da Questão 04 do Bloco 5. — descrição gerada por IA. |
| `MG5Q05_A` | STRING | Resposta do item A da Questão 05 do Bloco 5. — descrição gerada por IA. |
| `MG5Q05_B` | STRING | Resposta do item B da Questão 05 do Bloco 5. — descrição gerada por IA. |
| `MG5Q05_C` | STRING | Resposta do item C da Questão 05 do Bloco 5. — descrição gerada por IA. |
| `MG5Q05_D` | STRING | Resposta do item D da Questão 05 do Bloco 5. — descrição gerada por IA. |
| `MG5Q05_E` | STRING | Resposta do item E da Questão 05 do Bloco 5. — descrição gerada por IA. |
| `MG5Q05_F` | STRING | Resposta do item F da Questão 05 do Bloco 5. — descrição gerada por IA. |
| `MG5Q05_G` | STRING | Resposta do item G da Questão 05 do Bloco 5. — descrição gerada por IA. |
| `MG5Q06` | STRING | Resposta do Secretário Municipal de Educação à Questão 06 do Bloco 5. — descrição gerada por IA. |
| `MG5Q07_A` | STRING | Resposta do item A da Questão 07 do Bloco 5. — descrição gerada por IA. |
| `MG5Q07_B` | STRING | Resposta do item B da Questão 07 do Bloco 5. — descrição gerada por IA. |
| `MG5Q07_C` | STRING | Resposta do item C da Questão 07 do Bloco 5. — descrição gerada por IA. |
| `MG5Q07_D` | STRING | Resposta do item D da Questão 07 do Bloco 5. — descrição gerada por IA. |
| `MG5Q07_E` | STRING | Resposta do item E da Questão 07 do Bloco 5. — descrição gerada por IA. |
| `MG5Q07_F` | STRING | Resposta do item F da Questão 07 do Bloco 5. — descrição gerada por IA. |
| `MG5Q07_G` | STRING | Resposta do item G da Questão 07 do Bloco 5. — descrição gerada por IA. |
| `MG5Q07_H` | STRING | Resposta do item H da Questão 07 do Bloco 5. — descrição gerada por IA. |
| `MG5Q07_I` | STRING | Resposta do item I da Questão 07 do Bloco 5. — descrição gerada por IA. |
| `MG5Q08` | STRING | Resposta do Secretário Municipal de Educação à Questão 08 do Bloco 5. — descrição gerada por IA. |
| `MG6Q01` | STRING | Resposta do Secretário Municipal de Educação à Questão 01 do Bloco 6. — descrição gerada por IA. |
| `MG6Q02` | STRING | Resposta do Secretário Municipal de Educação à Questão 02 do Bloco 6. — descrição gerada por IA. |
| `MG6Q03` | STRING | Resposta do Secretário Municipal de Educação à Questão 03 do Bloco 6. — descrição gerada por IA. |
| `MG6Q04` | STRING | Resposta do Secretário Municipal de Educação à Questão 04 do Bloco 6. — descrição gerada por IA. |
| `MG6Q05_A` | STRING | Resposta do item A da Questão 05 do Bloco 6. — descrição gerada por IA. |
| `MG6Q05_B` | STRING | Resposta do item B da Questão 05 do Bloco 6. — descrição gerada por IA. |
| `MG6Q05_C` | STRING | Resposta do item C da Questão 05 do Bloco 6. — descrição gerada por IA. |
| `MG6Q05_D` | STRING | Resposta do item D da Questão 05 do Bloco 6. — descrição gerada por IA. |
| `MG6Q06` | STRING | Resposta do Secretário Municipal de Educação à Questão 06 do Bloco 6. — descrição gerada por IA. |
| `MG6Q07` | STRING | Resposta do Secretário Municipal de Educação à Questão 07 do Bloco 6. — descrição gerada por IA. |
| `MG6Q08_A` | STRING | Resposta do item A da Questão 08 do Bloco 6. — descrição gerada por IA. |
| `MG6Q08_B` | STRING | Resposta do item B da Questão 08 do Bloco 6. — descrição gerada por IA. |
| `MG6Q08_C` | STRING | Resposta do item C da Questão 08 do Bloco 6. — descrição gerada por IA. |
| `MG6Q08_D` | STRING | Resposta do item D da Questão 08 do Bloco 6. — descrição gerada por IA. |
| `MG6Q08_E` | STRING | Resposta do item E da Questão 08 do Bloco 6. — descrição gerada por IA. |
| `MG6Q08_F` | STRING | Resposta do item F da Questão 08 do Bloco 6. — descrição gerada por IA. |
| `MG6Q08_G` | STRING | Resposta do item G da Questão 08 do Bloco 6. — descrição gerada por IA. |
| `MG6Q08_H` | STRING | Resposta do item H da Questão 08 do Bloco 6. — descrição gerada por IA. |
| `MG6Q09` | STRING | Resposta do Secretário Municipal de Educação à Questão 09 do Bloco 6. — descrição gerada por IA. |
| `MG6Q10` | STRING | Resposta do Secretário Municipal de Educação à Questão 10 do Bloco 6. — descrição gerada por IA. |
| `MG7Q01` | STRING | Resposta do Secretário Municipal de Educação à Questão 01 do Bloco 7. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2021_ts_secretario_municipal_2021

File `raw__inep_saeb_microdados_csv_2021_ts_secretario_municipal_2021.parquet` · 5,568 rows · 159 columns

Raw do microdado CSV TS_SECRETARIO_MUNICIPAL_2021.csv do Saeb 2021, arquivo oficial microdados_saeb_2021_educacao_infantil.zip.

| Column | Type | Description |
|---|---|---|
| `NU_ANO_SAEB` | STRING | Ano de realização da edição do SAEB (ex: 2021). — descrição gerada por IA. |
| `CO_UF` | STRING | Código IBGE da Unidade Federativa da escola. — descrição gerada por IA. |
| `CO_MUNICIPIO` | STRING | Código IBGE do município onde a escola está localizada. — descrição gerada por IA. |
| `IN_CAPITAL` | STRING | Indicador se a escola está localizada em uma capital (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO` | STRING | Indicador de preenchimento do questionário pelo gestor (1=Sim, 0=Não). — descrição gerada por IA. |
| `CO_TRATAMENTO` | STRING | Código do status do tratamento do questionário na base de dados do INEP. — descrição gerada por IA. |
| `DT_PREENCHIMENTO` | STRING | Data de preenchimento do questionário pelo gestor escolar (formato DDMMMYYYY). — descrição gerada por IA. |
| `MG1Q01` | STRING | Resposta da questão 01 do Bloco 1 (Perfil e dados demográficos do gestor). — descrição gerada por IA. |
| `MG1Q02` | STRING | Resposta da questão 02 do Bloco 1 (Idade ou perfil do gestor). — descrição gerada por IA. |
| `MG1Q03` | STRING | Resposta da questão 03 do Bloco 1 (Cor/raça do gestor). — descrição gerada por IA. |
| `MG1Q04` | STRING | Resposta da questão 04 do Bloco 1 (Sexo/gênero do gestor). — descrição gerada por IA. |
| `MG1Q05` | STRING | Resposta da questão 05 do Bloco 1 (Escolaridade/grau de instrução). — descrição gerada por IA. |
| `MG1Q06` | STRING | Resposta da questão 06 do Bloco 1 (Área de formação superior). — descrição gerada por IA. |
| `MG1Q07` | STRING | Resposta da questão 07 do Bloco 1 (Posse de pós-graduação/especialização). — descrição gerada por IA. |
| `MG1Q08_A` | STRING | Resposta do item A da questão 08 do Bloco 1 (Atividades de formação continuada). — descrição gerada por IA. |
| `MG1Q08_B` | STRING | Resposta do item B da questão 08 do Bloco 1 (Atividades de formação continuada). — descrição gerada por IA. |
| `MG1Q08_C` | STRING | Resposta do item C da questão 08 do Bloco 1 (Atividades de formação continuada). — descrição gerada por IA. |
| `MG1Q08_D` | STRING | Resposta do item D da questão 08 do Bloco 1 (Atividades de formação continuada). — descrição gerada por IA. |
| `MG1Q08_E` | STRING | Resposta do item E da questão 08 do Bloco 1 (Atividades de formação continuada). — descrição gerada por IA. |
| `MG1Q08_F` | STRING | Resposta do item F da questão 08 do Bloco 1 (Atividades de formação continuada). — descrição gerada por IA. |
| `MG1Q08_G` | STRING | Resposta do item G da questão 08 do Bloco 1 (Atividades de formação continuada). — descrição gerada por IA. |
| `MG1Q09` | STRING | Resposta da questão 09 do Bloco 1 (Renda ou aspectos socioeconômicos). — descrição gerada por IA. |
| `MG1Q10` | STRING | Resposta da questão 10 do Bloco 1 (Tempo de atuação na educação em anos). — descrição gerada por IA. |
| `MG1Q11` | STRING | Resposta da questão 11 do Bloco 1 (Tempo de atuação na gestão desta escola). — descrição gerada por IA. |
| `MG1Q12` | STRING | Resposta da questão 12 do Bloco 1 (Forma de provimento/seleção para o cargo de gestor). — descrição gerada por IA. |
| `MG1Q13` | STRING | Resposta da questão 13 do Bloco 1 (Tipo de vínculo empregatício com a rede). — descrição gerada por IA. |
| `MG2Q01` | STRING | Resposta da questão 01 do Bloco 2 (Condições de trabalho e infraestrutura da escola). — descrição gerada por IA. |
| `MG2Q02` | STRING | Resposta da questão 02 do Bloco 2 (Disponibilidade de equipamentos e recursos na escola). — descrição gerada por IA. |
| `MG2Q03` | STRING | Resposta da questão 03 do Bloco 2 (Acesso à internet e recursos de TIC na escola). — descrição gerada por IA. |
| `MG2Q04` | STRING | Resposta da questão 04 do Bloco 2 (Conservação das instalações físicas). — descrição gerada por IA. |
| `MG2Q05` | STRING | Resposta da questão 05 do Bloco 2 (Segurança do ambiente escolar). — descrição gerada por IA. |
| `MG2Q06` | STRING | Resposta da questão 06 do Bloco 2 (Número de turmas ou turnos da escola). — descrição gerada por IA. |
| `MG2Q07` | STRING | Resposta da questão 07 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q08` | STRING | Resposta da questão 08 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q09` | STRING | Resposta da questão 09 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q10` | STRING | Resposta da questão 10 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q11` | STRING | Resposta da questão 11 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q12` | STRING | Resposta da questão 12 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q13` | STRING | Resposta da questão 13 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q14` | STRING | Resposta da questão 14 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q15` | STRING | Resposta da questão 15 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q16` | STRING | Resposta da questão 16 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q17` | STRING | Resposta da questão 17 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q18` | STRING | Resposta da questão 18 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q19` | STRING | Resposta da questão 19 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q20` | STRING | Resposta da questão 20 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q21` | STRING | Resposta da questão 21 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q22` | STRING | Resposta da questão 22 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q23` | STRING | Resposta da questão 23 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q24` | STRING | Resposta da questão 24 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q25` | STRING | Resposta da questão 25 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q26` | STRING | Resposta da questão 26 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q27` | STRING | Resposta da questão 27 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q28` | STRING | Resposta da questão 28 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q29` | STRING | Resposta da questão 29 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q30` | STRING | Resposta da questão 30 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q31` | STRING | Resposta da questão 31 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q32` | STRING | Resposta da questão 32 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q33` | STRING | Resposta da questão 33 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q34` | STRING | Resposta da questão 34 do Bloco 2 (Infraestrutura e recursos pedagógicos). — descrição gerada por IA. |
| `MG2Q35_A` | STRING | Resposta do item A da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q35_B` | STRING | Resposta do item B da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q35_C` | STRING | Resposta do item C da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q35_D` | STRING | Resposta do item D da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q35_E` | STRING | Resposta do item E da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q35_F` | STRING | Resposta do item F da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q35_G` | STRING | Resposta do item G da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q35_H` | STRING | Resposta do item H da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q35_I` | STRING | Resposta do item I da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q35_J` | STRING | Resposta do item J da questão 35 do Bloco 2 (Equipamentos e materiais disponíveis). — descrição gerada por IA. |
| `MG2Q36` | STRING | Resposta da questão 36 do Bloco 2 (Aspectos de infraestrutura escolar). — descrição gerada por IA. |
| `MG2Q37` | STRING | Resposta da questão 37 do Bloco 2 (Aspectos de infraestrutura escolar). — descrição gerada por IA. |
| `MG2Q38` | STRING | Resposta da questão 38 do Bloco 2 (Aspectos de infraestrutura escolar). — descrição gerada por IA. |
| `MG2Q39` | STRING | Resposta da questão 39 do Bloco 2 (Aspectos de infraestrutura escolar). — descrição gerada por IA. |
| `MG2Q40` | STRING | Resposta da questão 40 do Bloco 2 (Aspectos de infraestrutura escolar). — descrição gerada por IA. |
| `MG2Q41` | STRING | Resposta da questão 41 do Bloco 2 (Aspectos de infraestrutura escolar). — descrição gerada por IA. |
| `MG2Q42` | STRING | Resposta da questão 42 do Bloco 2 (Aspectos de infraestrutura escolar). — descrição gerada por IA. |
| `MG3Q01` | STRING | Resposta da questão 01 do Bloco 3 (Práticas de gestão pedagógica e liderança). — descrição gerada por IA. |
| `MG3Q02` | STRING | Resposta da questão 02 do Bloco 3 (Acompanhamento das atividades de ensino). — descrição gerada por IA. |
| `MG3Q03` | STRING | Resposta da questão 03 do Bloco 3 (Elaboração do Projeto Político Pedagógico - PPP). — descrição gerada por IA. |
| `MG3Q04` | STRING | Resposta da questão 04 do Bloco 3 (Planejamento de aulas e diretrizes curriculares). — descrição gerada por IA. |
| `MG3Q05` | STRING | Resposta da questão 05 do Bloco 3 (Frequência de reuniões pedagógicas). — descrição gerada por IA. |
| `MG3Q06` | STRING | Resposta da questão 06 do Bloco 3 (Uso de resultados de avaliações externas como o SAEB). — descrição gerada por IA. |
| `MG3Q07` | STRING | Resposta da questão 07 do Bloco 3 (Estratégias de combate à evasão escolar). — descrição gerada por IA. |
| `MG3Q08` | STRING | Resposta da questão 08 do Bloco 3 (Práticas e políticas de inclusão de alunos com deficiência). — descrição gerada por IA. |
| `MG3Q09` | STRING | Resposta da questão 09 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q10` | STRING | Resposta da questão 10 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q11` | STRING | Resposta da questão 11 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q12` | STRING | Resposta da questão 12 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q13` | STRING | Resposta da questão 13 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q14` | STRING | Resposta da questão 14 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q15` | STRING | Resposta da questão 15 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q16` | STRING | Resposta da questão 16 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q17` | STRING | Resposta da questão 17 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q18` | STRING | Resposta da questão 18 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q19` | STRING | Resposta da questão 19 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q20` | STRING | Resposta da questão 20 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG3Q21` | STRING | Resposta da questão 21 do Bloco 3 (Práticas pedagógicas e gestão escolar). — descrição gerada por IA. |
| `MG4Q01` | STRING | Resposta da questão 01 do Bloco 4 (Clima escolar, convivência e disciplina). — descrição gerada por IA. |
| `MG4Q02` | STRING | Resposta da questão 02 do Bloco 4 (Frequência de problemas de indisciplina). — descrição gerada por IA. |
| `MG4Q03` | STRING | Resposta da questão 03 do Bloco 4 (Casos de bullying ou violência na escola). — descrição gerada por IA. |
| `MG4Q04` | STRING | Resposta da questão 04 do Bloco 4 (Absenteísmo docente/faltas de professores). — descrição gerada por IA. |
| `MG4Q05` | STRING | Resposta da questão 05 do Bloco 4 (Estratégias para substituição de professores ausentes). — descrição gerada por IA. |
| `MG4Q06` | STRING | Resposta da questão 06 do Bloco 4 (Relação entre gestão e corpo docente). — descrição gerada por IA. |
| `MG4Q07` | STRING | Resposta da questão 07 do Bloco 4 (Aspectos de convivência e clima escolar). — descrição gerada por IA. |
| `MG4Q08` | STRING | Resposta da questão 08 do Bloco 4 (Aspectos de convivência e clima escolar). — descrição gerada por IA. |
| `MG4Q09` | STRING | Resposta da questão 09 do Bloco 4 (Aspectos de convivência e clima escolar). — descrição gerada por IA. |
| `MG4Q10` | STRING | Resposta da questão 10 do Bloco 4 (Aspectos de convivência e clima escolar). — descrição gerada por IA. |
| `MG5Q01` | STRING | Resposta da questão 01 do Bloco 5 (Participação da comunidade e Conselho Escolar). — descrição gerada por IA. |
| `MG5Q02_A` | STRING | Resposta do item A da questão 02 do Bloco 5 (Atuação do Conselho Escolar). — descrição gerada por IA. |
| `MG5Q02_B` | STRING | Resposta do item B da questão 02 do Bloco 5 (Atuação do Conselho Escolar). — descrição gerada por IA. |
| `MG5Q02_C` | STRING | Resposta do item C da questão 02 do Bloco 5 (Atuação do Conselho Escolar). — descrição gerada por IA. |
| `MG5Q02_D` | STRING | Resposta do item D da questão 02 do Bloco 5 (Atuação do Conselho Escolar). — descrição gerada por IA. |
| `MG5Q02_E` | STRING | Resposta do item E da questão 02 do Bloco 5 (Atuação do Conselho Escolar). — descrição gerada por IA. |
| `MG5Q02_F` | STRING | Resposta do item F da questão 02 do Bloco 5 (Atuação do Conselho Escolar). — descrição gerada por IA. |
| `MG5Q02_G` | STRING | Resposta do item G da questão 02 do Bloco 5 (Atuação do Conselho Escolar). — descrição gerada por IA. |
| `MG5Q03` | STRING | Resposta da questão 03 do Bloco 5 (Atividades de integração com famílias dos alunos). — descrição gerada por IA. |
| `MG5Q04_A` | STRING | Resposta do item A da questão 04 do Bloco 5 (Formas de comunicação com os pais). — descrição gerada por IA. |
| `MG5Q04_B` | STRING | Resposta do item B da questão 04 do Bloco 5 (Formas de comunicação com os pais). — descrição gerada por IA. |
| `MG5Q04_C` | STRING | Resposta do item C da questão 04 do Bloco 5 (Formas de comunicação com os pais). — descrição gerada por IA. |
| `MG5Q05_A` | STRING | Resposta do item A da questão 05 do Bloco 5 (Programas educacionais governamentais). — descrição gerada por IA. |
| `MG5Q05_B` | STRING | Resposta do item B da questão 05 do Bloco 5 (Programas educacionais governamentais). — descrição gerada por IA. |
| `MG5Q05_C` | STRING | Resposta do item C da questão 05 do Bloco 5 (Programas educacionais governamentais). — descrição gerada por IA. |
| `MG5Q05_D` | STRING | Resposta do item D da questão 05 do Bloco 5 (Programas educacionais governamentais). — descrição gerada por IA. |
| `MG5Q05_E` | STRING | Resposta do item E da questão 05 do Bloco 5 (Programas educacionais governamentais). — descrição gerada por IA. |
| `MG5Q05_F` | STRING | Resposta do item F da questão 05 do Bloco 5 (Programas educacionais governamentais). — descrição gerada por IA. |
| `MG5Q05_G` | STRING | Resposta do item G da questão 05 do Bloco 5 (Programas educacionais governamentais). — descrição gerada por IA. |
| `MG5Q06` | STRING | Resposta da questão 06 do Bloco 5 (Apoio pedagógico ou programas suplementares). — descrição gerada por IA. |
| `MG5Q07_A` | STRING | Resposta do item A da questão 07 do Bloco 5 (Apoio e recursos financeiros externos/PDDE). — descrição gerada por IA. |
| `MG5Q07_B` | STRING | Resposta do item B da questão 07 do Bloco 5 (Apoio e recursos financeiros externos/PDDE). — descrição gerada por IA. |
| `MG5Q07_C` | STRING | Resposta do item C da questão 07 do Bloco 5 (Apoio e recursos financeiros externos/PDDE). — descrição gerada por IA. |
| `MG5Q07_D` | STRING | Resposta do item D da questão 07 do Bloco 5 (Apoio e recursos financeiros externos/PDDE). — descrição gerada por IA. |
| `MG5Q07_E` | STRING | Resposta do item E da questão 07 do Bloco 5 (Apoio e recursos financeiros externos/PDDE). — descrição gerada por IA. |
| `MG5Q07_F` | STRING | Resposta do item F da questão 07 do Bloco 5 (Apoio e recursos financeiros externos/PDDE). — descrição gerada por IA. |
| `MG5Q07_G` | STRING | Resposta do item G da questão 07 do Bloco 5 (Apoio e recursos financeiros externos/PDDE). — descrição gerada por IA. |
| `MG5Q07_H` | STRING | Resposta do item H da questão 07 do Bloco 5 (Apoio e recursos financeiros externos/PDDE). — descrição gerada por IA. |
| `MG5Q07_I` | STRING | Resposta do item I da questão 07 do Bloco 5 (Apoio e recursos financeiros externos/PDDE). — descrição gerada por IA. |
| `MG5Q08` | STRING | Resposta da questão 08 do Bloco 5 (Avaliação geral de recursos e programas). — descrição gerada por IA. |
| `MG6Q01` | STRING | Resposta da questão 01 do Bloco 6 (Impactos do contexto de ensino e adaptações). — descrição gerada por IA. |
| `MG6Q02` | STRING | Resposta da questão 02 do Bloco 6 (Uso de estratégias e ferramentas pedagógicas de apoio). — descrição gerada por IA. |
| `MG6Q03` | STRING | Resposta da questão 03 do Bloco 6 (Acompanhamento da aprendizagem dos estudantes). — descrição gerada por IA. |
| `MG6Q04` | STRING | Resposta da questão 04 do Bloco 6 (Atividades de reforço e recomposição de aprendizagem). — descrição gerada por IA. |
| `MG6Q05_A` | STRING | Resposta do item A da questão 05 do Bloco 6 (Ações pedagógicas emergenciais ou de apoio). — descrição gerada por IA. |
| `MG6Q05_B` | STRING | Resposta do item B da questão 05 do Bloco 6 (Ações pedagógicas emergenciais ou de apoio). — descrição gerada por IA. |
| `MG6Q05_C` | STRING | Resposta do item C da questão 05 do Bloco 6 (Ações pedagógicas emergenciais ou de apoio). — descrição gerada por IA. |
| `MG6Q05_D` | STRING | Resposta do item D da questão 05 do Bloco 6 (Ações pedagógicas emergenciais ou de apoio). — descrição gerada por IA. |
| `MG6Q06` | STRING | Resposta da questão 06 do Bloco 6 (Recursos tecnológicos e de conectividade utilizados). — descrição gerada por IA. |
| `MG6Q07` | STRING | Resposta da questão 07 do Bloco 6 (Nível de satisfação com o suporte da secretaria de educação). — descrição gerada por IA. |
| `MG6Q08_A` | STRING | Resposta do item A da questão 08 do Bloco 6 (Desafios enfrentados pela gestão). — descrição gerada por IA. |
| `MG6Q08_B` | STRING | Resposta do item B da questão 08 do Bloco 6 (Desafios enfrentados pela gestão). — descrição gerada por IA. |
| `MG6Q08_C` | STRING | Resposta do item C da questão 08 do Bloco 6 (Desafios enfrentados pela gestão). — descrição gerada por IA. |
| `MG6Q08_D` | STRING | Resposta do item D da questão 08 do Bloco 6 (Desafios enfrentados pela gestão). — descrição gerada por IA. |
| `MG6Q08_E` | STRING | Resposta do item E da questão 08 do Bloco 6 (Desafios enfrentados pela gestão). — descrição gerada por IA. |
| `MG6Q08_F` | STRING | Resposta do item F da questão 08 do Bloco 6 (Desafios enfrentados pela gestão). — descrição gerada por IA. |
| `MG6Q08_G` | STRING | Resposta do item G da questão 08 do Bloco 6 (Desafios enfrentados pela gestão). — descrição gerada por IA. |
| `MG6Q08_H` | STRING | Resposta do item H da questão 08 do Bloco 6 (Desafios enfrentados pela gestão). — descrição gerada por IA. |
| `MG6Q09_A` | STRING | Resposta do item A da questão 09 do Bloco 6 (Suporte pedagógico e de infraestrutura suplementar). — descrição gerada por IA. |
| `MG6Q10` | STRING | Resposta da questão 10 do Bloco 6 (Avaliação final da gestão escolar e contexto educacional). — descrição gerada por IA. |
| `MG7Q01` | STRING | Resposta da questão 01 do Bloco 7 (Percepções gerais adicionais sobre a instituição e a rede escolar). — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2023_ts_aluno_2ef

File `raw__inep_saeb_microdados_csv_2023_ts_aluno_2ef.parquet` · 37,104 rows · 55 columns

Raw do microdado CSV TS_ALUNO_2EF.csv do Saeb 2023, arquivo oficial microdados_saeb_2023.zip.

**Feeds:** `raw/inep_saeb_aluno_2023`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de edição da avaliação do SAEB (ex: 2023). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico da região geográfica do Brasil onde a escola se localiza. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE de duas letras ou dígitos da Unidade da Federação. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área da localização da escola (1=Urbana, 2=Rural). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (8 dígitos) de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública da escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código de localização da escola (1=Urbana, 2=Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador único da turma no Censo Escolar/SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série/ano escolar avaliado (ex: 2 para 2º ano, 5 para 5º ano). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador único criptografado do aluno na avaliação SAEB. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação da matrícula do aluno informada no Censo Escolar (1=Ativo). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento do caderno de prova de Língua Portuguesa (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento do caderno de prova de Matemática (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença do aluno no dia da prova de Língua Portuguesa (1=Presente, 0=Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença do aluno no dia da prova de Matemática (1=Presente, 0=Ausente). — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Identificador do caderno de prova aplicado em Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Identificador do primeiro bloco de itens de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Identificador do segundo bloco de itens de Língua Portuguesa. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_LP` | STRING | Número de itens com resposta aberta contidos no bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_LP` | STRING | Número de itens com resposta aberta contidos no bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Identificador do caderno de prova aplicado em Matemática. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Identificador do primeiro bloco de itens de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Identificador do segundo bloco de itens de Matemática. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_MT` | STRING | Número de itens com resposta aberta contidos no bloco 1 de Matemática. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_MT` | STRING | Número de itens com resposta aberta contidos no bloco 2 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Sequência das alternativas marcadas pelo aluno no bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Sequência das alternativas marcadas pelo aluno no bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_LP` | STRING | Código de avaliação/conceito obtido na questão aberta 1 de Língua Portuguesa. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_LP` | STRING | Código de avaliação/conceito obtido na questão aberta 2 de Língua Portuguesa. — descrição gerada por IA. |
| `CO_RESPOSTA_TEXTO` | STRING | Código de situação/validade da produção textual do aluno (ex: BR=Branco, anulação, etc.). — descrição gerada por IA. |
| `CO_CONCEITO_SEQUENCIA` | STRING | Conceito atribuído à competência de coerência/sequência lógica na redação. — descrição gerada por IA. |
| `CO_CONCEITO_COESAO` | STRING | Conceito atribuído à competência de coesão textual na redação. — descrição gerada por IA. |
| `CO_CONCEITO_PONTUACAO` | STRING | Conceito atribuído ao uso adequado de pontuação na redação. — descrição gerada por IA. |
| `CO_CONCEITO_SEGMENTACAO` | STRING | Conceito atribuído à segmentação correta de palavras e frases. — descrição gerada por IA. |
| `CO_TEXTO_GRAFIA` | STRING | Conceito atribuído ao domínio ortográfico/grafia do texto. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Sequência das alternativas marcadas pelo aluno no bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Sequência das alternativas marcadas pelo aluno no bloco 2 de Matemática. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_MT` | STRING | Código de avaliação/conceito obtido na questão aberta 1 de Matemática. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_MT` | STRING | Código de avaliação/conceito obtido na questão aberta 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador de proficiência calculada em Língua Portuguesa (1=Válida, 0=Não calculada). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador de proficiência calculada em Matemática (1=Válida, 0=Não calculada). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador de inclusão do aluno no cálculo da amostra estatística do SAEB (1=Sim, 0=Não). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código identificador do estrato amostral da aplicação do SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Fator de ponderação/peso amostral do aluno para cálculo populacional em Língua Portuguesa. — descrição gerada por IA. |
| `IN_ALFABETIZADO` | STRING | Indicador de atingimento dos critérios de alfabetização do aluno (1=Sim, 0=Não). — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Escore estimado do aluno em Língua Portuguesa na escala padronizada da TRI (escala theta). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da estimativa de proficiência em Língua Portuguesa na escala padronizada. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Nota/Proficiência final do aluno em Língua Portuguesa na escala oficial do SAEB (ex: 0 a 500). — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da medida de proficiência em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Fator de ponderação/peso amostral do aluno para cálculo populacional em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Escore estimado do aluno em Matemática na escala padronizada da TRI (escala theta). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da estimativa de proficiência em Matemática na escala padronizada. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Nota/Proficiência final do aluno em Matemática na escala oficial do SAEB (ex: 0 a 500). — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da medida de proficiência em Matemática na escala SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2023_ts_aluno_34em

File `raw__inep_saeb_microdados_csv_2023_ts_aluno_34em.parquet` · 2,091,337 rows · 117 columns

Raw do microdado CSV TS_ALUNO_34EM.csv do Saeb 2023, arquivo oficial microdados_saeb_2023.zip.

**Feeds:** `raw/inep_saeb_aluno_2023`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de edição da avaliação do SAEB (ex: 2023). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola do aluno. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação da escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área do município (1 - Capital, 2 - Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP/Censo Escolar da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 - Sim, 0 - Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1 - Urbana, 2 - Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador da turma do aluno no Censo/SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar avaliado (ex: 5, 9, 12 para o 3º ano do Ensino Médio). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Código identificador do aluno na avaliação SAEB. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno no Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento da prova de Língua Portuguesa (1 - Sim, 0 - Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento da prova de Matemática (1 - Sim, 0 - Não). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença na prova de Língua Portuguesa (1 - Presente, 0 - Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença na prova de Matemática (1 - Presente, 0 - Ausente). — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Código do caderno de prova de Língua Portuguesa atribuído ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Código do 1º bloco de itens de Língua Portuguesa no caderno do aluno. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Código do 2º bloco de itens de Língua Portuguesa no caderno do aluno. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Código do caderno de prova de Matemática atribuído ao aluno. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Código do 1º bloco de itens de Matemática no caderno do aluno. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Código do 2º bloco de itens de Matemática no caderno do aluno. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Vetor de respostas dadas pelo aluno nas questões do Bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Vetor de respostas dadas pelo aluno nas questões do Bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Vetor de respostas dadas pelo aluno nas questões do Bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Vetor de respostas dadas pelo aluno nas questões do Bloco 2 de Matemática. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador se a proficiência de Língua Portuguesa foi calculada (1 - Sim, 0 - Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador se a proficiência de Matemática foi calculada (1 - Sim, 0 - Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador de pertencimento da turma/escola à amostra do SAEB (1 - Amostra, 0 - Censitário). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato amostral da escola/turma no desenho amostral do SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno aplicado ao cálculo em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência do aluno na escala do SAEB para Língua Portuguesa. — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência padronizada do aluno em Língua Portuguesa. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência padronizada em Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno aplicado ao cálculo em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência do aluno na escala do SAEB para Matemática. — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência padronizada do aluno em Matemática. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência padronizada em Matemática. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário do aluno (1 - Sim, 0 - Não). — descrição gerada por IA. |
| `IN_INSE` | STRING | Indicador de cálculo do Indicador de Nível Socioeconômico do aluno (1 - Sim, 0 - Não). — descrição gerada por IA. |
| `INSE_ALUNO` | STRING | Pontuação contínua do Nível Socioeconômico (INSE) do aluno. — descrição gerada por IA. |
| `NU_TIPO_NIVEL_INSE` | STRING | Nível de classificação socioeconômica do aluno (faixa/estrato INSE). — descrição gerada por IA. |
| `PESO_ALUNO_INSE` | STRING | Peso amostral do aluno utilizado no cálculo do INSE. — descrição gerada por IA. |
| `TX_RESP_Q01` | STRING | Resposta da questão socioeconômica 01 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q02` | STRING | Resposta da questão socioeconômica 02 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q03` | STRING | Resposta da questão socioeconômica 03 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q04` | STRING | Resposta da questão socioeconômica 04 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q05a` | STRING | Resposta da questão socioeconômica 05a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q05b` | STRING | Resposta da questão socioeconômica 05b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q05c` | STRING | Resposta da questão socioeconômica 05c do aluno. — descrição gerada por IA. |
| `TX_RESP_Q06` | STRING | Resposta da questão socioeconômica 06 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07a` | STRING | Resposta da questão socioeconômica 07a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07b` | STRING | Resposta da questão socioeconômica 07b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07c` | STRING | Resposta da questão socioeconômica 07c do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07d` | STRING | Resposta da questão socioeconômica 07d do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07e` | STRING | Resposta da questão socioeconômica 07e do aluno. — descrição gerada por IA. |
| `TX_RESP_Q08` | STRING | Resposta da questão socioeconômica 08 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q09` | STRING | Resposta da questão socioeconômica 09 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10a` | STRING | Resposta da questão socioeconômica 10a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10b` | STRING | Resposta da questão socioeconômica 10b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10c` | STRING | Resposta da questão socioeconômica 10c do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10d` | STRING | Resposta da questão socioeconômica 10d do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10e` | STRING | Resposta da questão socioeconômica 10e do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10f` | STRING | Resposta da questão socioeconômica 10f do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11a` | STRING | Resposta da questão socioeconômica 11a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11b` | STRING | Resposta da questão socioeconômica 11b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11c` | STRING | Resposta da questão socioeconômica 11c do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12a` | STRING | Resposta da questão socioeconômica 12a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12b` | STRING | Resposta da questão socioeconômica 12b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12c` | STRING | Resposta da questão socioeconômica 12c do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12d` | STRING | Resposta da questão socioeconômica 12d do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12e` | STRING | Resposta da questão socioeconômica 12e do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12f` | STRING | Resposta da questão socioeconômica 12f do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12g` | STRING | Resposta da questão socioeconômica 12g do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13a` | STRING | Resposta da questão socioeconômica 13a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13b` | STRING | Resposta da questão socioeconômica 13b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13c` | STRING | Resposta da questão socioeconômica 13c do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13d` | STRING | Resposta da questão socioeconômica 13d do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13e` | STRING | Resposta da questão socioeconômica 13e do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13f` | STRING | Resposta da questão socioeconômica 13f do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13g` | STRING | Resposta da questão socioeconômica 13g do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13h` | STRING | Resposta da questão socioeconômica 13h do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13i` | STRING | Resposta da questão socioeconômica 13i do aluno. — descrição gerada por IA. |
| `TX_RESP_Q14` | STRING | Resposta da questão socioeconômica 14 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q15a` | STRING | Resposta da questão socioeconômica 15a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q15b` | STRING | Resposta da questão socioeconômica 15b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q16` | STRING | Resposta da questão socioeconômica 16 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q17` | STRING | Resposta da questão socioeconômica 17 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q18` | STRING | Resposta da questão socioeconômica 18 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q19` | STRING | Resposta da questão socioeconômica 19 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q20` | STRING | Resposta da questão socioeconômica 20 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21a` | STRING | Resposta da questão socioeconômica 21a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21b` | STRING | Resposta da questão socioeconômica 21b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21c` | STRING | Resposta da questão socioeconômica 21c do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21d` | STRING | Resposta da questão socioeconômica 21d do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21e` | STRING | Resposta da questão socioeconômica 21e do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22a` | STRING | Resposta da questão socioeconômica 22a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22b` | STRING | Resposta da questão socioeconômica 22b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22c` | STRING | Resposta da questão socioeconômica 22c do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22d` | STRING | Resposta da questão socioeconômica 22d do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22e` | STRING | Resposta da questão socioeconômica 22e do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22f` | STRING | Resposta da questão socioeconômica 22f do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22g` | STRING | Resposta da questão socioeconômica 22g do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22h` | STRING | Resposta da questão socioeconômica 22h do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23a` | STRING | Resposta da questão socioeconômica 23a do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23b` | STRING | Resposta da questão socioeconômica 23b do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23c` | STRING | Resposta da questão socioeconômica 23c do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23d` | STRING | Resposta da questão socioeconômica 23d do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23e` | STRING | Resposta da questão socioeconômica 23e do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23f` | STRING | Resposta da questão socioeconômica 23f do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23g` | STRING | Resposta da questão socioeconômica 23g do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23h` | STRING | Resposta da questão socioeconômica 23h do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23i` | STRING | Resposta da questão socioeconômica 23i do aluno. — descrição gerada por IA. |
| `TX_RESP_Q24` | STRING | Resposta da questão socioeconômica 24 do aluno. — descrição gerada por IA. |
| `TX_RESP_Q25` | STRING | Resposta da questão socioeconômica 25 do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2023_ts_aluno_5ef

File `raw__inep_saeb_microdados_csv_2023_ts_aluno_5ef.parquet` · 2,442,143 rows · 152 columns

Raw do microdado CSV TS_ALUNO_5EF.csv do Saeb 2023, arquivo oficial microdados_saeb_2023.zip.

**Feeds:** `raw/inep_saeb_aluno_2023`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano/edição da realização da avaliação do SAEB (ex: 2023). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do Estado/Unidade Federativa onde se localiza a escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola do aluno. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código de área de localização da escola (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (Censo Escolar) de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa da escola (1: Pública, 0: Privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código identificador único da turma no SAEB. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Etapa de ensino/série avaliada (ex: 5 para 5º ano do Ensino Fundamental). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Código identificador único do aluno na avaliação. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno segundo o Censo Escolar (1: Ativo/Regular). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento mínimo do teste de Língua Portuguesa (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento mínimo do teste de Matemática (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_CH` | STRING | Indicador de preenchimento mínimo do teste de Ciências Humanas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_CN` | STRING | Indicador de preenchimento mínimo do teste de Ciências da Natureza (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença do aluno na prova de Língua Portuguesa (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença do aluno na prova de Matemática (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_CH` | STRING | Indicador de presença do aluno na prova de Ciências Humanas (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `IN_PRESENCA_CN` | STRING | Indicador de presença do aluno na prova de Ciências da Natureza (1: Presente, 0: Ausente). — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Identificador do caderno de prova aplicado ao aluno para Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Código do primeiro bloco de itens do teste de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Código do segundo bloco de itens do teste de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Identificador do caderno de prova aplicado ao aluno para Matemática. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Código do primeiro bloco de itens do teste de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Código do segundo bloco de itens do teste de Matemática. — descrição gerada por IA. |
| `ID_CADERNO_CH` | STRING | Identificador do caderno de prova aplicado ao aluno para Ciências Humanas. — descrição gerada por IA. |
| `ID_BLOCO_1_CH` | STRING | Código do primeiro bloco de itens de Ciências Humanas. — descrição gerada por IA. |
| `ID_BLOCO_2_CH` | STRING | Código do segundo bloco de itens de Ciências Humanas. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_CH` | STRING | Número de itens abertos contidos no bloco 1 de Ciências Humanas. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_CH` | STRING | Número de itens abertos contidos no bloco 2 de Ciências Humanas. — descrição gerada por IA. |
| `ID_CADERNO_CN` | STRING | Identificador do caderno de prova aplicado ao aluno para Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_1_CN` | STRING | Código do primeiro bloco de itens de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_2_CN` | STRING | Código do segundo bloco de itens de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_3_CN` | STRING | Código do terceiro bloco de itens de Ciências da Natureza. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_CN` | STRING | Número de itens abertos contidos no bloco 1 de Ciências da Natureza. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_CN` | STRING | Número de itens abertos contidos no bloco 2 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Vetor com os gabaritos/respostas marcadas pelo aluno no bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Vetor com os gabaritos/respostas marcadas pelo aluno no bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Vetor com os gabaritos/respostas marcadas pelo aluno no bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Vetor com os gabaritos/respostas marcadas pelo aluno no bloco 2 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_CH` | STRING | Vetor com os gabaritos/respostas marcadas pelo aluno no bloco 1 de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_CH` | STRING | Vetor com os gabaritos/respostas marcadas pelo aluno no bloco 2 de Ciências Humanas. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_CH` | STRING | Conceito/nota atribuída à questão discursiva 1 de Ciências Humanas. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_CH` | STRING | Conceito/nota atribuída à questão discursiva 2 de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_CN` | STRING | Vetor com os gabaritos/respostas marcadas pelo aluno no bloco 1 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_CN` | STRING | Vetor com os gabaritos/respostas marcadas pelo aluno no bloco 2 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO3_CN` | STRING | Vetor com os gabaritos/respostas marcadas pelo aluno no bloco 3 de Ciências da Natureza. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_CN` | STRING | Conceito/nota atribuída à questão discursiva 1 de Ciências da Natureza. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_CN` | STRING | Conceito/nota atribuída à questão discursiva 2 de Ciências da Natureza. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador de proficiência calculada para Língua Portuguesa (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador de proficiência calculada para Matemática (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_CH` | STRING | Indicador de proficiência calculada para Ciências Humanas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_CN` | STRING | Indicador de proficiência calculada para Ciências da Natureza (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador se o aluno faz parte da amostra estatística do SAEB (1: Amostral, 0: Censitário). — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato amostral da turma/escola. — descrição gerada por IA. |
| `ESTRATO_CIENCIAS` | STRING | Código do estrato amostral específico para avaliação de Ciências. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral do aluno para cálculos agregados em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota estimada do aluno em Língua Portuguesa na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão do cálculo de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Pontuação final do aluno em Língua Portuguesa na escala SAEB (ex: 0-500). — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da pontuação em Língua Portuguesa na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral do aluno para cálculos agregados em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota estimada do aluno em Matemática na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão do cálculo de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Pontuação final do aluno em Matemática na escala SAEB (ex: 0-500). — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da pontuação em Matemática na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_CH` | STRING | Peso amostral do aluno para cálculos agregados em Ciências Humanas. — descrição gerada por IA. |
| `PROFICIENCIA_CH` | STRING | Nota estimada do aluno em Ciências Humanas na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_CH` | STRING | Erro padrão do cálculo de proficiência em Ciências Humanas. — descrição gerada por IA. |
| `PROFICIENCIA_CH_SAEB` | STRING | Pontuação final do aluno em Ciências Humanas na escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_CH_SAEB` | STRING | Erro padrão da pontuação em Ciências Humanas na escala SAEB. — descrição gerada por IA. |
| `PESO_ALUNO_CN` | STRING | Peso amostral do aluno para cálculos agregados em Ciências da Natureza. — descrição gerada por IA. |
| `PROFICIENCIA_CN` | STRING | Nota estimada do aluno em Ciências da Natureza na escala padronizada (TRI). — descrição gerada por IA. |
| `ERRO_PADRAO_CN` | STRING | Erro padrão do cálculo de proficiência em Ciências da Natureza. — descrição gerada por IA. |
| `PROFICIENCIA_CN_SAEB` | STRING | Pontuação final do aluno em Ciências da Natureza na escala SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_CN_SAEB` | STRING | Erro padrão da pontuação em Ciências da Natureza na escala SAEB. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário socioeconômico do aluno (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_INSE` | STRING | Indicador se o Nível Socioeconômico (INSE) foi calculado para o aluno (1: Sim, 0: Não). — descrição gerada por IA. |
| `INSE_ALUNO` | STRING | Valor contínuo do Nível Socioeconômico (INSE) calculado para o aluno. — descrição gerada por IA. |
| `NU_TIPO_NIVEL_INSE` | STRING | Classificação do nível socioeconômico do aluno em categorias/faixas numéricas. — descrição gerada por IA. |
| `PESO_ALUNO_INSE` | STRING | Peso de expansão amostral associado ao cálculo do INSE do aluno. — descrição gerada por IA. |
| `TX_RESP_Q01` | STRING | Resposta do aluno à questão socioeconômica Q01. — descrição gerada por IA. |
| `TX_RESP_Q02` | STRING | Resposta do aluno à questão socioeconômica Q02. — descrição gerada por IA. |
| `TX_RESP_Q03` | STRING | Resposta do aluno à questão socioeconômica Q03. — descrição gerada por IA. |
| `TX_RESP_Q04` | STRING | Resposta do aluno à questão socioeconômica Q04. — descrição gerada por IA. |
| `TX_RESP_Q05a` | STRING | Resposta do aluno à subquestão socioeconômica Q05a. — descrição gerada por IA. |
| `TX_RESP_Q05b` | STRING | Resposta do aluno à subquestão socioeconômica Q05b. — descrição gerada por IA. |
| `TX_RESP_Q05c` | STRING | Resposta do aluno à subquestão socioeconômica Q05c. — descrição gerada por IA. |
| `TX_RESP_Q06` | STRING | Resposta do aluno à questão socioeconômica Q06. — descrição gerada por IA. |
| `TX_RESP_Q07a` | STRING | Resposta do aluno à subquestão socioeconômica Q07a. — descrição gerada por IA. |
| `TX_RESP_Q07b` | STRING | Resposta do aluno à subquestão socioeconômica Q07b. — descrição gerada por IA. |
| `TX_RESP_Q07c` | STRING | Resposta do aluno à subquestão socioeconômica Q07c. — descrição gerada por IA. |
| `TX_RESP_Q07d` | STRING | Resposta do aluno à subquestão socioeconômica Q07d. — descrição gerada por IA. |
| `TX_RESP_Q07e` | STRING | Resposta do aluno à subquestão socioeconômica Q07e. — descrição gerada por IA. |
| `TX_RESP_Q08` | STRING | Resposta do aluno à questão socioeconômica Q08. — descrição gerada por IA. |
| `TX_RESP_Q09` | STRING | Resposta do aluno à questão socioeconômica Q09. — descrição gerada por IA. |
| `TX_RESP_Q10a` | STRING | Resposta do aluno à subquestão socioeconômica Q10a. — descrição gerada por IA. |
| `TX_RESP_Q10b` | STRING | Resposta do aluno à subquestão socioeconômica Q10b. — descrição gerada por IA. |
| `TX_RESP_Q10c` | STRING | Resposta do aluno à subquestão socioeconômica Q10c. — descrição gerada por IA. |
| `TX_RESP_Q10d` | STRING | Resposta do aluno à subquestão socioeconômica Q10d. — descrição gerada por IA. |
| `TX_RESP_Q10e` | STRING | Resposta do aluno à subquestão socioeconômica Q10e. — descrição gerada por IA. |
| `TX_RESP_Q10f` | STRING | Resposta do aluno à subquestão socioeconômica Q10f. — descrição gerada por IA. |
| `TX_RESP_Q11a` | STRING | Resposta do aluno à subquestão socioeconômica Q11a. — descrição gerada por IA. |
| `TX_RESP_Q11b` | STRING | Resposta do aluno à subquestão socioeconômica Q11b. — descrição gerada por IA. |
| `TX_RESP_Q11c` | STRING | Resposta do aluno à subquestão socioeconômica Q11c. — descrição gerada por IA. |
| `TX_RESP_Q12a` | STRING | Resposta do aluno à subquestão socioeconômica Q12a. — descrição gerada por IA. |
| `TX_RESP_Q12b` | STRING | Resposta do aluno à subquestão socioeconômica Q12b. — descrição gerada por IA. |
| `TX_RESP_Q12c` | STRING | Resposta do aluno à subquestão socioeconômica Q12c. — descrição gerada por IA. |
| `TX_RESP_Q12d` | STRING | Resposta do aluno à subquestão socioeconômica Q12d. — descrição gerada por IA. |
| `TX_RESP_Q12e` | STRING | Resposta do aluno à subquestão socioeconômica Q12e. — descrição gerada por IA. |
| `TX_RESP_Q12f` | STRING | Resposta do aluno à subquestão socioeconômica Q12f. — descrição gerada por IA. |
| `TX_RESP_Q12g` | STRING | Resposta do aluno à subquestão socioeconômica Q12g. — descrição gerada por IA. |
| `TX_RESP_Q13a` | STRING | Resposta do aluno à subquestão socioeconômica Q13a. — descrição gerada por IA. |
| `TX_RESP_Q13b` | STRING | Resposta do aluno à subquestão socioeconômica Q13b. — descrição gerada por IA. |
| `TX_RESP_Q13c` | STRING | Resposta do aluno à subquestão socioeconômica Q13c. — descrição gerada por IA. |
| `TX_RESP_Q13d` | STRING | Resposta do aluno à subquestão socioeconômica Q13d. — descrição gerada por IA. |
| `TX_RESP_Q13e` | STRING | Resposta do aluno à subquestão socioeconômica Q13e. — descrição gerada por IA. |
| `TX_RESP_Q13f` | STRING | Resposta do aluno à subquestão socioeconômica Q13f. — descrição gerada por IA. |
| `TX_RESP_Q13g` | STRING | Resposta do aluno à subquestão socioeconômica Q13g. — descrição gerada por IA. |
| `TX_RESP_Q13h` | STRING | Resposta do aluno à subquestão socioeconômica Q13h. — descrição gerada por IA. |
| `TX_RESP_Q13i` | STRING | Resposta do aluno à subquestão socioeconômica Q13i. — descrição gerada por IA. |
| `TX_RESP_Q14` | STRING | Resposta do aluno à questão socioeconômica Q14. — descrição gerada por IA. |
| `TX_RESP_Q15a` | STRING | Resposta do aluno à subquestão socioeconômica Q15a. — descrição gerada por IA. |
| `TX_RESP_Q15b` | STRING | Resposta do aluno à subquestão socioeconômica Q15b. — descrição gerada por IA. |
| `TX_RESP_Q16` | STRING | Resposta do aluno à questão socioeconômica Q16. — descrição gerada por IA. |
| `TX_RESP_Q17` | STRING | Resposta do aluno à questão socioeconômica Q17. — descrição gerada por IA. |
| `TX_RESP_Q18` | STRING | Resposta do aluno à questão socioeconômica Q18. — descrição gerada por IA. |
| `TX_RESP_Q19` | STRING | Resposta do aluno à questão socioeconômica Q19. — descrição gerada por IA. |
| `TX_RESP_Q20` | STRING | Resposta do aluno à questão socioeconômica Q20. — descrição gerada por IA. |
| `TX_RESP_Q21a` | STRING | Resposta do aluno à subquestão socioeconômica Q21a. — descrição gerada por IA. |
| `TX_RESP_Q21b` | STRING | Resposta do aluno à subquestão socioeconômica Q21b. — descrição gerada por IA. |
| `TX_RESP_Q21c` | STRING | Resposta do aluno à subquestão socioeconômica Q21c. — descrição gerada por IA. |
| `TX_RESP_Q21d` | STRING | Resposta do aluno à subquestão socioeconômica Q21d. — descrição gerada por IA. |
| `TX_RESP_Q21e` | STRING | Resposta do aluno à subquestão socioeconômica Q21e. — descrição gerada por IA. |
| `TX_RESP_Q22a` | STRING | Resposta do aluno à subquestão socioeconômica Q22a. — descrição gerada por IA. |
| `TX_RESP_Q22b` | STRING | Resposta do aluno à subquestão socioeconômica Q22b. — descrição gerada por IA. |
| `TX_RESP_Q22c` | STRING | Resposta do aluno à subquestão socioeconômica Q22c. — descrição gerada por IA. |
| `TX_RESP_Q22d` | STRING | Resposta do aluno à subquestão socioeconômica Q22d. — descrição gerada por IA. |
| `TX_RESP_Q22e` | STRING | Resposta do aluno à subquestão socioeconômica Q22e. — descrição gerada por IA. |
| `TX_RESP_Q22f` | STRING | Resposta do aluno à subquestão socioeconômica Q22f. — descrição gerada por IA. |
| `TX_RESP_Q22g` | STRING | Resposta do aluno à subquestão socioeconômica Q22g. — descrição gerada por IA. |
| `TX_RESP_Q22h` | STRING | Resposta do aluno à subquestão socioeconômica Q22h. — descrição gerada por IA. |
| `TX_RESP_Q23a` | STRING | Resposta do aluno à subquestão socioeconômica Q23a. — descrição gerada por IA. |
| `TX_RESP_Q23b` | STRING | Resposta do aluno à subquestão socioeconômica Q23b. — descrição gerada por IA. |
| `TX_RESP_Q23c` | STRING | Resposta do aluno à subquestão socioeconômica Q23c. — descrição gerada por IA. |
| `TX_RESP_Q23d` | STRING | Resposta do aluno à subquestão socioeconômica Q23d. — descrição gerada por IA. |
| `TX_RESP_Q23e` | STRING | Resposta do aluno à subquestão socioeconômica Q23e. — descrição gerada por IA. |
| `TX_RESP_Q23f` | STRING | Resposta do aluno à subquestão socioeconômica Q23f. — descrição gerada por IA. |
| `TX_RESP_Q23g` | STRING | Resposta do aluno à subquestão socioeconômica Q23g. — descrição gerada por IA. |
| `TX_RESP_Q23h` | STRING | Resposta do aluno à subquestão socioeconômica Q23h. — descrição gerada por IA. |
| `TX_RESP_Q23i` | STRING | Resposta do aluno à subquestão socioeconômica Q23i. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2023_ts_aluno_9ef

File `raw__inep_saeb_microdados_csv_2023_ts_aluno_9ef.parquet` · 2,502,907 rows · 153 columns

Raw do microdado CSV TS_ALUNO_9EF.csv do Saeb 2023, arquivo oficial microdados_saeb_2023.zip.

**Feeds:** `raw/inep_saeb_aluno_2023`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de edição do SAEB (ex: 2023). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica da escola (1-Norte, 2-Nordeste, 3-Sudeste, 4-Sul, 5-Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do estado (UF) onde a escola está localizada. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área do município (1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1-Sim, 0-Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Identificador único da turma no Censo Escolar. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série/ano escolar do aluno avaliado (ex: 5, 9, 12). — descrição gerada por IA. |
| `ID_ALUNO` | STRING | Identificador do aluno no SAEB. — descrição gerada por IA. |
| `IN_SITUACAO_CENSO` | STRING | Indicador de situação de matrícula do aluno no Censo Escolar. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_LP` | STRING | Indicador de preenchimento do teste de Língua Portuguesa (1-Preenchido, 0-Em branco/Não preenchido). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_MT` | STRING | Indicador de preenchimento do teste de Matemática (1-Preenchido, 0-Em branco/Não preenchido). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_CH` | STRING | Indicador de preenchimento do teste de Ciências Humanas. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_CN` | STRING | Indicador de preenchimento do teste de Ciências da Natureza. — descrição gerada por IA. |
| `IN_PRESENCA_LP` | STRING | Indicador de presença no dia do teste de Língua Portuguesa. — descrição gerada por IA. |
| `IN_PRESENCA_MT` | STRING | Indicador de presença no dia do teste de Matemática. — descrição gerada por IA. |
| `IN_PRESENCA_CH` | STRING | Indicador de presença no dia do teste de Ciências Humanas. — descrição gerada por IA. |
| `IN_PRESENCA_CN` | STRING | Indicador de presença no dia do teste de Ciências da Natureza. — descrição gerada por IA. |
| `ID_CADERNO_LP` | STRING | Número do caderno de prova de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_1_LP` | STRING | Identificador do bloco 1 do caderno de Língua Portuguesa. — descrição gerada por IA. |
| `ID_BLOCO_2_LP` | STRING | Identificador do bloco 2 do caderno de Língua Portuguesa. — descrição gerada por IA. |
| `ID_CADERNO_MT` | STRING | Número do caderno de prova de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_1_MT` | STRING | Identificador do bloco 1 do caderno de Matemática. — descrição gerada por IA. |
| `ID_BLOCO_2_MT` | STRING | Identificador do bloco 2 do caderno de Matemática. — descrição gerada por IA. |
| `ID_CADERNO_CH` | STRING | Número do caderno de prova de Ciências Humanas. — descrição gerada por IA. |
| `ID_BLOCO_1_CH` | STRING | Identificador do bloco 1 do caderno de Ciências Humanas. — descrição gerada por IA. |
| `ID_BLOCO_2_CH` | STRING | Identificador do bloco 2 do caderno de Ciências Humanas. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_CH` | STRING | Número do bloco 1 com questões abertas/discursivas de Ciências Humanas. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_CH` | STRING | Número do bloco 2 com questões abertas/discursivas de Ciências Humanas. — descrição gerada por IA. |
| `ID_CADERNO_CN` | STRING | Número do caderno de prova de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_1_CN` | STRING | Identificador do bloco 1 do caderno de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_2_CN` | STRING | Identificador do bloco 2 do caderno de Ciências da Natureza. — descrição gerada por IA. |
| `ID_BLOCO_3_CN` | STRING | Identificador do bloco 3 do caderno de Ciências da Natureza. — descrição gerada por IA. |
| `NU_BLOCO_1_ABERTA_CN` | STRING | Número do bloco 1 com questões abertas/discursivas de Ciências da Natureza. — descrição gerada por IA. |
| `NU_BLOCO_2_ABERTA_CN` | STRING | Número do bloco 2 com questões abertas/discursivas de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_LP` | STRING | Vetor de respostas dadas pelo aluno para os itens do bloco 1 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_LP` | STRING | Vetor de respostas dadas pelo aluno para os itens do bloco 2 de Língua Portuguesa. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_MT` | STRING | Vetor de respostas dadas pelo aluno para os itens do bloco 1 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_MT` | STRING | Vetor de respostas dadas pelo aluno para os itens do bloco 2 de Matemática. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_CH` | STRING | Vetor de respostas dadas pelo aluno para os itens do bloco 1 de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_CH` | STRING | Vetor de respostas dadas pelo aluno para os itens do bloco 2 de Ciências Humanas. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_CH` | STRING | Código do conceito atribuído à resposta discursiva da questão 1 de Ciências Humanas. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_CH` | STRING | Código do conceito atribuído à resposta discursiva da questão 2 de Ciências Humanas. — descrição gerada por IA. |
| `TX_RESP_BLOCO1_CN` | STRING | Vetor de respostas dadas pelo aluno para os itens do bloco 1 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO2_CN` | STRING | Vetor de respostas dadas pelo aluno para os itens do bloco 2 de Ciências da Natureza. — descrição gerada por IA. |
| `TX_RESP_BLOCO3_CN` | STRING | Vetor de respostas dadas pelo aluno para os itens do bloco 3 de Ciências da Natureza. — descrição gerada por IA. |
| `CO_CONCEITO_Q1_CN` | STRING | Código do conceito atribuído à resposta discursiva da questão 1 de Ciências da Natureza. — descrição gerada por IA. |
| `CO_CONCEITO_Q2_CN` | STRING | Código do conceito atribuído à resposta discursiva da questão 2 de Ciências da Natureza. — descrição gerada por IA. |
| `IN_PROFICIENCIA_LP` | STRING | Indicador de geração de nota de proficiência válida em Língua Portuguesa (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_MT` | STRING | Indicador de geração de nota de proficiência válida em Matemática (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_PROFICIENCIA_CH` | STRING | Indicador de geração de nota de proficiência válida em Ciências Humanas. — descrição gerada por IA. |
| `IN_PROFICIENCIA_CN` | STRING | Indicador de geração de nota de proficiência válida em Ciências da Natureza. — descrição gerada por IA. |
| `IN_AMOSTRA` | STRING | Indicador se a turma/aluno faz parte da amostra censitária ou amostral. — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato amostral do aluno para cálculos estatísticos. — descrição gerada por IA. |
| `ESTRATO_CIENCIAS` | STRING | Código do estrato amostral específico para Ciências. — descrição gerada por IA. |
| `PESO_ALUNO_LP` | STRING | Peso amostral de expansão do aluno para Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP` | STRING | Nota de proficiência estimada do aluno em Língua Portuguesa (escala SAEB). — descrição gerada por IA. |
| `ERRO_PADRAO_LP` | STRING | Erro padrão da medida de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `PROFICIENCIA_LP_SAEB` | STRING | Proficiência padronizada em Língua Portuguesa para relatórios do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_LP_SAEB` | STRING | Erro padrão da proficiência padronizada de Língua Portuguesa. — descrição gerada por IA. |
| `PESO_ALUNO_MT` | STRING | Peso amostral de expansão do aluno para Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT` | STRING | Nota de proficiência estimada do aluno em Matemática (escala SAEB). — descrição gerada por IA. |
| `ERRO_PADRAO_MT` | STRING | Erro padrão da medida de proficiência em Matemática. — descrição gerada por IA. |
| `PROFICIENCIA_MT_SAEB` | STRING | Proficiência padronizada em Matemática para relatórios do SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_MT_SAEB` | STRING | Erro padrão da proficiência padronizada de Matemática. — descrição gerada por IA. |
| `PESO_ALUNO_CH` | STRING | Peso amostral de expansão do aluno para Ciências Humanas. — descrição gerada por IA. |
| `PROFICIENCIA_CH` | STRING | Nota de proficiência estimada do aluno em Ciências Humanas (escala SAEB). — descrição gerada por IA. |
| `ERRO_PADRAO_CH` | STRING | Erro padrão da medida de proficiência em Ciências Humanas. — descrição gerada por IA. |
| `PROFICIENCIA_CH_SAEB` | STRING | Proficiência padronizada em Ciências Humanas para o SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_CH_SAEB` | STRING | Erro padrão da proficiência padronizada de Ciências Humanas. — descrição gerada por IA. |
| `PESO_ALUNO_CN` | STRING | Peso amostral de expansão do aluno para Ciências da Natureza. — descrição gerada por IA. |
| `PROFICIENCIA_CN` | STRING | Nota de proficiência estimada do aluno em Ciências da Natureza (escala SAEB). — descrição gerada por IA. |
| `ERRO_PADRAO_CN` | STRING | Erro padrão da medida de proficiência em Ciências da Natureza. — descrição gerada por IA. |
| `PROFICIENCIA_CN_SAEB` | STRING | Proficiência padronizada em Ciências da Natureza para o SAEB. — descrição gerada por IA. |
| `ERRO_PADRAO_CN_SAEB` | STRING | Erro padrão da proficiência padronizada de Ciências da Natureza. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador de preenchimento do questionário do aluno (1-Sim, 0-Não). — descrição gerada por IA. |
| `IN_INSE` | STRING | Indicador de disponibilidade do Nível Socioeconômico do Aluno (1-Possui, 0-Não possui). — descrição gerada por IA. |
| `INSE_ALUNO` | STRING | Escore do Indicador de Nível Socioeconômico (INSE) do aluno. — descrição gerada por IA. |
| `NU_TIPO_NIVEL_INSE` | STRING | Nível/classificação do INSE do aluno. — descrição gerada por IA. |
| `PESO_ALUNO_INSE` | STRING | Peso amostral aplicado ao cálculo do INSE. — descrição gerada por IA. |
| `TX_RESP_Q01` | STRING | Resposta da questão 01 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q02` | STRING | Resposta da questão 02 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q03` | STRING | Resposta da questão 03 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q04` | STRING | Resposta da questão 04 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q05a` | STRING | Resposta da subquestão 05a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q05b` | STRING | Resposta da subquestão 05b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q05c` | STRING | Resposta da subquestão 05c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q06` | STRING | Resposta da questão 06 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07a` | STRING | Resposta da subquestão 07a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07b` | STRING | Resposta da subquestão 07b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07c` | STRING | Resposta da subquestão 07c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07d` | STRING | Resposta da subquestão 07d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q07e` | STRING | Resposta da subquestão 07e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q08` | STRING | Resposta da questão 08 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q09` | STRING | Resposta da questão 09 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10a` | STRING | Resposta da subquestão 10a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10b` | STRING | Resposta da subquestão 10b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10c` | STRING | Resposta da subquestão 10c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10d` | STRING | Resposta da subquestão 10d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10e` | STRING | Resposta da subquestão 10e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q10f` | STRING | Resposta da subquestão 10f do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11a` | STRING | Resposta da subquestão 11a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11b` | STRING | Resposta da subquestão 11b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q11c` | STRING | Resposta da subquestão 11c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12a` | STRING | Resposta da subquestão 12a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12b` | STRING | Resposta da subquestão 12b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12c` | STRING | Resposta da subquestão 12c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12d` | STRING | Resposta da subquestão 12d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12e` | STRING | Resposta da subquestão 12e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12f` | STRING | Resposta da subquestão 12f do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q12g` | STRING | Resposta da subquestão 12g do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13a` | STRING | Resposta da subquestão 13a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13b` | STRING | Resposta da subquestão 13b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13c` | STRING | Resposta da subquestão 13c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13d` | STRING | Resposta da subquestão 13d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13e` | STRING | Resposta da subquestão 13e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13f` | STRING | Resposta da subquestão 13f do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13g` | STRING | Resposta da subquestão 13g do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13h` | STRING | Resposta da subquestão 13h do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q13i` | STRING | Resposta da subquestão 13i do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q14` | STRING | Resposta da questão 14 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q15a` | STRING | Resposta da subquestão 15a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q15b` | STRING | Resposta da subquestão 15b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q16` | STRING | Resposta da questão 16 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q17` | STRING | Resposta da questão 17 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q18` | STRING | Resposta da questão 18 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q19` | STRING | Resposta da questão 19 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q20` | STRING | Resposta da questão 20 do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21a` | STRING | Resposta da subquestão 21a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21b` | STRING | Resposta da subquestão 21b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21c` | STRING | Resposta da subquestão 21c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21d` | STRING | Resposta da subquestão 21d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q21e` | STRING | Resposta da subquestão 21e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22a` | STRING | Resposta da subquestão 22a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22b` | STRING | Resposta da subquestão 22b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22c` | STRING | Resposta da subquestão 22c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22d` | STRING | Resposta da subquestão 22d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22e` | STRING | Resposta da subquestão 22e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22f` | STRING | Resposta da subquestão 22f do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22g` | STRING | Resposta da subquestão 22g do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q22h` | STRING | Resposta da subquestão 22h do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23a` | STRING | Resposta da subquestão 23a do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23b` | STRING | Resposta da subquestão 23b do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23c` | STRING | Resposta da subquestão 23c do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23d` | STRING | Resposta da subquestão 23d do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23e` | STRING | Resposta da subquestão 23e do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23f` | STRING | Resposta da subquestão 23f do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23g` | STRING | Resposta da subquestão 23g do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23h` | STRING | Resposta da subquestão 23h do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q23i` | STRING | Resposta da subquestão 23i do questionário socioeconômico do aluno. — descrição gerada por IA. |
| `TX_RESP_Q24` | STRING | Resposta da questão 24 do questionário socioeconômico do aluno. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2023_ts_diretor

File `raw__inep_saeb_microdados_csv_2023_ts_diretor.parquet` · 107,089 rows · 237 columns

Raw do microdado CSV TS_DIRETOR.csv do Saeb 2023, arquivo oficial microdados_saeb_2023.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano da edição da avaliação do SAEB (ex: 2023). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código da região geográfica do IBGE (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código da Unidade Federativa (UF) no padrão IBGE. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código do município de localização da escola no padrão IBGE. — descrição gerada por IA. |
| `ID_AREA` | STRING | Tipo de área do município (1: Capital, 2: Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código único de identificação da escola no Censo Escolar/INEP. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador se a escola pertence à rede pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador se o questionário contextual foi preenchido (1: Sim, 0: Não). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série/ano escolar avaliado no SAEB. — descrição gerada por IA. |
| `ESTRATO` | STRING | Código do estrato amostral da escola definido pelo INEP. — descrição gerada por IA. |
| `VL_PESO_ESCOLA` | STRING | Peso amostral da escola para expansão estatística dos resultados. — descrição gerada por IA. |
| `TX_Q001` | STRING | Resposta fornecida à questão 1 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q002` | STRING | Resposta fornecida à questão 2 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q003` | STRING | Resposta fornecida à questão 3 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q004` | STRING | Resposta fornecida à questão 4 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q005` | STRING | Resposta fornecida à questão 5 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q006` | STRING | Resposta fornecida à questão 6 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q007` | STRING | Resposta fornecida à questão 7 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q008` | STRING | Resposta fornecida à questão 8 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q009` | STRING | Resposta fornecida à questão 9 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q010` | STRING | Resposta fornecida à questão 10 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q011` | STRING | Resposta fornecida à questão 11 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q012` | STRING | Resposta fornecida à questão 12 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q013` | STRING | Resposta fornecida à questão 13 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q014` | STRING | Resposta fornecida à questão 14 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q015_A` | STRING | Resposta fornecida ao item A da questão 15 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q015_B` | STRING | Resposta fornecida ao item B da questão 15 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q016` | STRING | Resposta fornecida à questão 16 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q017` | STRING | Resposta fornecida à questão 17 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q018` | STRING | Resposta fornecida à questão 18 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q019` | STRING | Resposta fornecida à questão 19 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q020` | STRING | Resposta fornecida à questão 20 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q021` | STRING | Resposta fornecida à questão 21 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q022` | STRING | Resposta fornecida à questão 22 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q023` | STRING | Resposta fornecida à questão 23 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q024` | STRING | Resposta fornecida à questão 24 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q025` | STRING | Resposta fornecida à questão 25 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q026` | STRING | Resposta fornecida à questão 26 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q027` | STRING | Resposta fornecida à questão 27 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q028` | STRING | Resposta fornecida à questão 28 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q029` | STRING | Resposta fornecida à questão 29 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q030` | STRING | Resposta fornecida à questão 30 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q031` | STRING | Resposta fornecida à questão 31 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q032` | STRING | Resposta fornecida à questão 32 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q033` | STRING | Resposta fornecida à questão 33 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q034` | STRING | Resposta fornecida à questão 34 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q035` | STRING | Resposta fornecida à questão 35 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q036` | STRING | Resposta fornecida à questão 36 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q037` | STRING | Resposta fornecida à questão 37 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q038` | STRING | Resposta fornecida à questão 38 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q039` | STRING | Resposta fornecida à questão 39 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q040` | STRING | Resposta fornecida à questão 40 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q041` | STRING | Resposta fornecida à questão 41 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q042` | STRING | Resposta fornecida à questão 42 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q043` | STRING | Resposta fornecida à questão 43 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q044` | STRING | Resposta fornecida à questão 44 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q045` | STRING | Resposta fornecida à questão 45 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q046` | STRING | Resposta fornecida à questão 46 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q047` | STRING | Resposta fornecida à questão 47 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q048` | STRING | Resposta fornecida à questão 48 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q049` | STRING | Resposta fornecida à questão 49 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q050` | STRING | Resposta fornecida à questão 50 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q051` | STRING | Resposta fornecida à questão 51 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q052` | STRING | Resposta fornecida à questão 52 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q053` | STRING | Resposta fornecida à questão 53 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q054` | STRING | Resposta fornecida à questão 54 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q055` | STRING | Resposta fornecida à questão 55 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q056` | STRING | Resposta fornecida à questão 56 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q057` | STRING | Resposta fornecida à questão 57 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q058` | STRING | Resposta fornecida à questão 58 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q059` | STRING | Resposta fornecida à questão 59 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q060` | STRING | Resposta fornecida à questão 60 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q061` | STRING | Resposta fornecida à questão 61 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q062` | STRING | Resposta fornecida à questão 62 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q063` | STRING | Resposta fornecida à questão 63 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q064` | STRING | Resposta fornecida à questão 64 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q065` | STRING | Resposta fornecida à questão 65 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q066` | STRING | Resposta fornecida à questão 66 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q067` | STRING | Resposta fornecida à questão 67 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q068` | STRING | Resposta fornecida à questão 68 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q069` | STRING | Resposta fornecida à questão 69 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q070` | STRING | Resposta fornecida à questão 70 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q071` | STRING | Resposta fornecida à questão 71 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q072` | STRING | Resposta fornecida à questão 72 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q073` | STRING | Resposta fornecida à questão 73 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q074` | STRING | Resposta fornecida à questão 74 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q075` | STRING | Resposta fornecida à questão 75 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q076` | STRING | Resposta fornecida à questão 76 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q077` | STRING | Resposta fornecida à questão 77 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q078` | STRING | Resposta fornecida à questão 78 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q079` | STRING | Resposta fornecida à questão 79 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q080` | STRING | Resposta fornecida à questão 80 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q081` | STRING | Resposta fornecida à questão 81 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q082` | STRING | Resposta fornecida à questão 82 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q083` | STRING | Resposta fornecida à questão 83 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q084` | STRING | Resposta fornecida à questão 84 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q085` | STRING | Resposta fornecida à questão 85 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q086` | STRING | Resposta fornecida à questão 86 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q087` | STRING | Resposta fornecida à questão 87 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q088` | STRING | Resposta fornecida à questão 88 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q089` | STRING | Resposta fornecida à questão 89 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q090` | STRING | Resposta fornecida à questão 90 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q091` | STRING | Resposta fornecida à questão 91 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q092` | STRING | Resposta fornecida à questão 92 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q093` | STRING | Resposta fornecida à questão 93 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q094` | STRING | Resposta fornecida à questão 94 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q095` | STRING | Resposta fornecida à questão 95 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q096` | STRING | Resposta fornecida à questão 96 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q097` | STRING | Resposta fornecida à questão 97 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q098` | STRING | Resposta fornecida à questão 98 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q099` | STRING | Resposta fornecida à questão 99 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q100` | STRING | Resposta fornecida à questão 100 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q101` | STRING | Resposta fornecida à questão 101 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q102` | STRING | Resposta fornecida à questão 102 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q103` | STRING | Resposta fornecida à questão 103 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q104` | STRING | Resposta fornecida à questão 104 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q105` | STRING | Resposta fornecida à questão 105 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q106` | STRING | Resposta fornecida à questão 106 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q107` | STRING | Resposta fornecida à questão 107 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q108` | STRING | Resposta fornecida à questão 108 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q109` | STRING | Resposta fornecida à questão 109 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q110` | STRING | Resposta fornecida à questão 110 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q111` | STRING | Resposta fornecida à questão 111 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q112` | STRING | Resposta fornecida à questão 112 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q113` | STRING | Resposta fornecida à questão 113 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q114` | STRING | Resposta fornecida à questão 114 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q115` | STRING | Resposta fornecida à questão 115 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q116` | STRING | Resposta fornecida à questão 116 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q117` | STRING | Resposta fornecida à questão 117 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q118` | STRING | Resposta fornecida à questão 118 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q119` | STRING | Resposta fornecida à questão 119 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q120` | STRING | Resposta fornecida à questão 120 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q121` | STRING | Resposta fornecida à questão 121 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q122` | STRING | Resposta fornecida à questão 122 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q123` | STRING | Resposta fornecida à questão 123 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q124` | STRING | Resposta fornecida à questão 124 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q125` | STRING | Resposta fornecida à questão 125 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q126` | STRING | Resposta fornecida à questão 126 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q127` | STRING | Resposta fornecida à questão 127 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q128` | STRING | Resposta fornecida à questão 128 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q129` | STRING | Resposta fornecida à questão 129 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q130` | STRING | Resposta fornecida à questão 130 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q131` | STRING | Resposta fornecida à questão 131 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q132` | STRING | Resposta fornecida à questão 132 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q133` | STRING | Resposta fornecida à questão 133 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q134` | STRING | Resposta fornecida à questão 134 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q135` | STRING | Resposta fornecida à questão 135 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q136` | STRING | Resposta fornecida à questão 136 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q137` | STRING | Resposta fornecida à questão 137 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q138` | STRING | Resposta fornecida à questão 138 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q139` | STRING | Resposta fornecida à questão 139 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q140` | STRING | Resposta fornecida à questão 140 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q141` | STRING | Resposta fornecida à questão 141 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q142` | STRING | Resposta fornecida à questão 142 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q143` | STRING | Resposta fornecida à questão 143 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q144` | STRING | Resposta fornecida à questão 144 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q145` | STRING | Resposta fornecida à questão 145 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q146` | STRING | Resposta fornecida à questão 146 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q147` | STRING | Resposta fornecida à questão 147 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q148` | STRING | Resposta fornecida à questão 148 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q149` | STRING | Resposta fornecida à questão 149 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q150` | STRING | Resposta fornecida à questão 150 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q151` | STRING | Resposta fornecida à questão 151 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q152` | STRING | Resposta fornecida à questão 152 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q153` | STRING | Resposta fornecida à questão 153 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q154` | STRING | Resposta fornecida à questão 154 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q155` | STRING | Resposta fornecida à questão 155 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q156` | STRING | Resposta fornecida à questão 156 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q157` | STRING | Resposta fornecida à questão 157 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q158` | STRING | Resposta fornecida à questão 158 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q159` | STRING | Resposta fornecida à questão 159 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q160` | STRING | Resposta fornecida à questão 160 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q161` | STRING | Resposta fornecida à questão 161 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q162` | STRING | Resposta fornecida à questão 162 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q163` | STRING | Resposta fornecida à questão 163 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q164` | STRING | Resposta fornecida à questão 164 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q165` | STRING | Resposta fornecida à questão 165 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q166` | STRING | Resposta fornecida à questão 166 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q167` | STRING | Resposta fornecida à questão 167 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q168` | STRING | Resposta fornecida à questão 168 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q169` | STRING | Resposta fornecida à questão 169 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q170` | STRING | Resposta fornecida à questão 170 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q171` | STRING | Resposta fornecida à questão 171 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q172` | STRING | Resposta fornecida à questão 172 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q173` | STRING | Resposta fornecida à questão 173 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q174` | STRING | Resposta fornecida à questão 174 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q175` | STRING | Resposta fornecida à questão 175 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q176` | STRING | Resposta fornecida à questão 176 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q177` | STRING | Resposta fornecida à questão 177 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q178` | STRING | Resposta fornecida à questão 178 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q179` | STRING | Resposta fornecida à questão 179 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q180` | STRING | Resposta fornecida à questão 180 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q181` | STRING | Resposta fornecida à questão 181 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q182` | STRING | Resposta fornecida à questão 182 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q183` | STRING | Resposta fornecida à questão 183 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q184` | STRING | Resposta fornecida à questão 184 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q185` | STRING | Resposta fornecida à questão 185 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q186` | STRING | Resposta fornecida à questão 186 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q187` | STRING | Resposta fornecida à questão 187 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q188` | STRING | Resposta fornecida à questão 188 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q189` | STRING | Resposta fornecida à questão 189 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q190` | STRING | Resposta fornecida à questão 190 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q191` | STRING | Resposta fornecida à questão 191 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q192` | STRING | Resposta fornecida à questão 192 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q193` | STRING | Resposta fornecida à questão 193 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q194` | STRING | Resposta fornecida à questão 194 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q195` | STRING | Resposta fornecida à questão 195 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q196` | STRING | Resposta fornecida à questão 196 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q197` | STRING | Resposta fornecida à questão 197 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q198` | STRING | Resposta fornecida à questão 198 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q199` | STRING | Resposta fornecida à questão 199 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q200` | STRING | Resposta fornecida à questão 200 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q201` | STRING | Resposta fornecida à questão 201 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q202` | STRING | Resposta fornecida à questão 202 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q203` | STRING | Resposta fornecida à questão 203 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q204` | STRING | Resposta fornecida à questão 204 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q205` | STRING | Resposta fornecida à questão 205 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q206` | STRING | Resposta fornecida à questão 206 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q207` | STRING | Resposta fornecida à questão 207 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q208` | STRING | Resposta fornecida à questão 208 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q209` | STRING | Resposta fornecida à questão 209 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q210` | STRING | Resposta fornecida à questão 210 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q211` | STRING | Resposta fornecida à questão 211 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q212` | STRING | Resposta fornecida à questão 212 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q213` | STRING | Resposta fornecida à questão 213 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q214` | STRING | Resposta fornecida à questão 214 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q215` | STRING | Resposta fornecida à questão 215 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q216` | STRING | Resposta fornecida à questão 216 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q217` | STRING | Resposta fornecida à questão 217 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q218` | STRING | Resposta fornecida à questão 218 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q219` | STRING | Resposta fornecida à questão 219 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q220` | STRING | Resposta fornecida à questão 220 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q221` | STRING | Resposta fornecida à questão 221 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q222` | STRING | Resposta fornecida à questão 222 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q223` | STRING | Resposta fornecida à questão 223 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q224` | STRING | Resposta fornecida à questão 224 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2023_ts_escola

File `raw__inep_saeb_microdados_csv_2023_ts_escola.parquet` · 70,151 rows · 137 columns

Raw do microdado CSV TS_ESCOLA.csv do Saeb 2023, arquivo oficial microdados_saeb_2023.zip.

**Feeds:** `trusted/inep_saeb_escola`, `trusted/inep_saeb_microdados_escola`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do SAEB (ex: 2023). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código identificador da região geográfica da escola (1-Norte, 2-Nordeste, etc.). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE da Unidade da Federação onde a escola está localizada. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município da escola. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código de localização da área da escola (1-Capital, 2-Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP (Censo Escolar) de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de rede pública de ensino (1 para SIM, 0 para NÃO). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Localização da escola (1 para Urbana, 2 para Rural). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_INICIAL` | STRING | Percentual de docentes com formação superior adequada nos Anos Iniciais do EF (0 a 100%). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_FINAL` | STRING | Percentual de docentes com formação superior adequada nos Anos Finais do EF (0 a 100%). — descrição gerada por IA. |
| `PC_FORMACAO_DOCENTE_MEDIO` | STRING | Percentual de docentes com formação superior adequada no Ensino Médio (0 a 100%). — descrição gerada por IA. |
| `NIVEL_SOCIO_ECONOMICO` | STRING | Classificação do Nível Socioeconômico (NSE) da escola segundo o INEP (ex: Nível IV). — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_5EF` | STRING | Número de alunos matriculados no 5º ano do EF segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_5EF` | STRING | Número de alunos do 5º ano do EF presentes na aplicação do SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_5EF` | STRING | Taxa de participação (%) dos alunos do 5º ano do EF na avaliação do SAEB. — descrição gerada por IA. |
| `NIVEL_0_LP5` | STRING | Percentual de alunos do 5º EF no Nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP5` | STRING | Percentual de alunos do 5º EF no Nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP5` | STRING | Percentual de alunos do 5º EF no Nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP5` | STRING | Percentual de alunos do 5º EF no Nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP5` | STRING | Percentual de alunos do 5º EF no Nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP5` | STRING | Percentual de alunos do 5º EF no Nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP5` | STRING | Percentual de alunos do 5º EF no Nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP5` | STRING | Percentual de alunos do 5º EF no Nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP5` | STRING | Percentual de alunos do 5º EF no Nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_9_LP5` | STRING | Percentual de alunos do 5º EF no Nível 9 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT5` | STRING | Percentual de alunos do 5º EF no Nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT5` | STRING | Percentual de alunos do 5º EF no Nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT5` | STRING | Percentual de alunos do 5º EF no Nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT5` | STRING | Percentual de alunos do 5º EF no Nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT5` | STRING | Percentual de alunos do 5º EF no Nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT5` | STRING | Percentual de alunos do 5º EF no Nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT5` | STRING | Percentual de alunos do 5º EF no Nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT5` | STRING | Percentual de alunos do 5º EF no Nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT5` | STRING | Percentual de alunos do 5º EF no Nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT5` | STRING | Percentual de alunos do 5º EF no Nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_10_MT5` | STRING | Percentual de alunos do 5º EF no Nível 10 de proficiência em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_9EF` | STRING | Número de alunos matriculados no 9º ano do EF segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_9EF` | STRING | Número de alunos do 9º ano do EF presentes na aplicação do SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_9EF` | STRING | Taxa de participação (%) dos alunos do 9º ano do EF na avaliação do SAEB. — descrição gerada por IA. |
| `NIVEL_0_LP9` | STRING | Percentual de alunos do 9º EF no Nível 0 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LP9` | STRING | Percentual de alunos do 9º EF no Nível 1 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LP9` | STRING | Percentual de alunos do 9º EF no Nível 2 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LP9` | STRING | Percentual de alunos do 9º EF no Nível 3 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LP9` | STRING | Percentual de alunos do 9º EF no Nível 4 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LP9` | STRING | Percentual de alunos do 9º EF no Nível 5 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LP9` | STRING | Percentual de alunos do 9º EF no Nível 6 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LP9` | STRING | Percentual de alunos do 9º EF no Nível 7 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LP9` | STRING | Percentual de alunos do 9º EF no Nível 8 de proficiência em Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MT9` | STRING | Percentual de alunos do 9º EF no Nível 0 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_1_MT9` | STRING | Percentual de alunos do 9º EF no Nível 1 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_2_MT9` | STRING | Percentual de alunos do 9º EF no Nível 2 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_3_MT9` | STRING | Percentual de alunos do 9º EF no Nível 3 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_4_MT9` | STRING | Percentual de alunos do 9º EF no Nível 4 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_5_MT9` | STRING | Percentual de alunos do 9º EF no Nível 5 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_6_MT9` | STRING | Percentual de alunos do 9º EF no Nível 6 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_7_MT9` | STRING | Percentual de alunos do 9º EF no Nível 7 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_8_MT9` | STRING | Percentual de alunos do 9º EF no Nível 8 de proficiência em Matemática. — descrição gerada por IA. |
| `NIVEL_9_MT9` | STRING | Percentual de alunos do 9º EF no Nível 9 de proficiência em Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_EMT` | STRING | Número de matriculados no Ensino Médio Tradicional/Regular no Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_EMT` | STRING | Número de alunos do Ensino Médio Tradicional presentes na prova do SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_EMT` | STRING | Taxa de participação (%) dos alunos do Ensino Médio Tradicional no SAEB. — descrição gerada por IA. |
| `NIVEL_0_LPEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 0 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LPEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 1 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LPEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 2 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LPEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 3 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LPEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 4 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LPEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 5 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LPEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 6 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LPEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 7 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LPEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 8 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 0 de Matemática. — descrição gerada por IA. |
| `NIVEL_1_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 1 de Matemática. — descrição gerada por IA. |
| `NIVEL_2_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 2 de Matemática. — descrição gerada por IA. |
| `NIVEL_3_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 3 de Matemática. — descrição gerada por IA. |
| `NIVEL_4_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 4 de Matemática. — descrição gerada por IA. |
| `NIVEL_5_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 5 de Matemática. — descrição gerada por IA. |
| `NIVEL_6_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 6 de Matemática. — descrição gerada por IA. |
| `NIVEL_7_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 7 de Matemática. — descrição gerada por IA. |
| `NIVEL_8_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 8 de Matemática. — descrição gerada por IA. |
| `NIVEL_9_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 9 de Matemática. — descrição gerada por IA. |
| `NIVEL_10_MTEMT` | STRING | Percentual de alunos do EM Tradicional no Nível 10 de Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_EMI` | STRING | Número de matriculados no Ensino Médio Integrado segundo o Censo Escolar. — descrição gerada por IA. |
| `NU_PRESENTES_EMI` | STRING | Número de alunos do Ensino Médio Integrado presentes no SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_EMI` | STRING | Taxa de participação (%) do Ensino Médio Integrado no SAEB. — descrição gerada por IA. |
| `NIVEL_0_LPEMI` | STRING | Percentual de alunos do EM Integrado no Nível 0 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LPEMI` | STRING | Percentual de alunos do EM Integrado no Nível 1 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LPEMI` | STRING | Percentual de alunos do EM Integrado no Nível 2 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LPEMI` | STRING | Percentual de alunos do EM Integrado no Nível 3 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LPEMI` | STRING | Percentual de alunos do EM Integrado no Nível 4 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LPEMI` | STRING | Percentual de alunos do EM Integrado no Nível 5 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LPEMI` | STRING | Percentual de alunos do EM Integrado no Nível 6 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LPEMI` | STRING | Percentual de alunos do EM Integrado no Nível 7 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LPEMI` | STRING | Percentual de alunos do EM Integrado no Nível 8 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 0 de Matemática. — descrição gerada por IA. |
| `NIVEL_1_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 1 de Matemática. — descrição gerada por IA. |
| `NIVEL_2_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 2 de Matemática. — descrição gerada por IA. |
| `NIVEL_3_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 3 de Matemática. — descrição gerada por IA. |
| `NIVEL_4_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 4 de Matemática. — descrição gerada por IA. |
| `NIVEL_5_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 5 de Matemática. — descrição gerada por IA. |
| `NIVEL_6_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 6 de Matemática. — descrição gerada por IA. |
| `NIVEL_7_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 7 de Matemática. — descrição gerada por IA. |
| `NIVEL_8_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 8 de Matemática. — descrição gerada por IA. |
| `NIVEL_9_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 9 de Matemática. — descrição gerada por IA. |
| `NIVEL_10_MTEMI` | STRING | Percentual de alunos do EM Integrado no Nível 10 de Matemática. — descrição gerada por IA. |
| `NU_MATRICULADOS_CENSO_EM` | STRING | Número total de matriculados no Ensino Médio geral segundo o Censo. — descrição gerada por IA. |
| `NU_PRESENTES_EM` | STRING | Número total de alunos do Ensino Médio geral presentes no SAEB. — descrição gerada por IA. |
| `TAXA_PARTICIPACAO_EM` | STRING | Taxa total de participação (%) do Ensino Médio geral no SAEB. — descrição gerada por IA. |
| `NIVEL_0_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 0 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_1_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 1 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_2_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 2 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_3_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 3 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_4_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 4 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_5_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 5 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_6_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 6 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_7_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 7 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_8_LPEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 8 de Língua Portuguesa. — descrição gerada por IA. |
| `NIVEL_0_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 0 de Matemática. — descrição gerada por IA. |
| `NIVEL_1_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 1 de Matemática. — descrição gerada por IA. |
| `NIVEL_2_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 2 de Matemática. — descrição gerada por IA. |
| `NIVEL_3_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 3 de Matemática. — descrição gerada por IA. |
| `NIVEL_4_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 4 de Matemática. — descrição gerada por IA. |
| `NIVEL_5_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 5 de Matemática. — descrição gerada por IA. |
| `NIVEL_6_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 6 de Matemática. — descrição gerada por IA. |
| `NIVEL_7_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 7 de Matemática. — descrição gerada por IA. |
| `NIVEL_8_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 8 de Matemática. — descrição gerada por IA. |
| `NIVEL_9_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 9 de Matemática. — descrição gerada por IA. |
| `NIVEL_10_MTEM` | STRING | Percentual de alunos do Ensino Médio geral no Nível 10 de Matemática. — descrição gerada por IA. |
| `MEDIA_5EF_LP` | STRING | Nota média de proficiência em Língua Portuguesa no 5º ano do EF na escala SAEB. — descrição gerada por IA. |
| `MEDIA_5EF_MT` | STRING | Nota média de proficiência em Matemática no 5º ano do EF na escala SAEB. — descrição gerada por IA. |
| `MEDIA_9EF_LP` | STRING | Nota média de proficiência em Língua Portuguesa no 9º ano do EF na escala SAEB. — descrição gerada por IA. |
| `MEDIA_9EF_MT` | STRING | Nota média de proficiência em Matemática no 9º ano do EF na escala SAEB. — descrição gerada por IA. |
| `MEDIA_EMT_LP` | STRING | Nota média em Língua Portuguesa dos alunos do Ensino Médio Tradicional. — descrição gerada por IA. |
| `MEDIA_EMT_MT` | STRING | Nota média em Matemática dos alunos do Ensino Médio Tradicional. — descrição gerada por IA. |
| `MEDIA_EMI_LP` | STRING | Nota média em Língua Portuguesa dos alunos do Ensino Médio Integrado. — descrição gerada por IA. |
| `MEDIA_EMI_MT` | STRING | Nota média em Matemática dos alunos do Ensino Médio Integrado. — descrição gerada por IA. |
| `MEDIA_EM_LP` | STRING | Nota média consolidada em Língua Portuguesa do Ensino Médio geral. — descrição gerada por IA. |
| `MEDIA_EM_MT` | STRING | Nota média consolidada em Matemática do Ensino Médio geral. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2023_ts_item

File `raw__inep_saeb_microdados_csv_2023_ts_item.parquet` · 993 rows · 16 columns

Raw do microdado CSV TS_ITEM.csv do Saeb 2023, arquivo oficial microdados_saeb_2023.zip.

**Feeds:** `trusted/inep_saeb_microdados_item`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano ou edição de realização do exame SAEB (ex: 2023). — descrição gerada por IA. |
| `ID_SERIE` | STRING | Código da série/ano escolar avaliado (ex: 2 para 2º ano do Ensino Fundamental). — descrição gerada por IA. |
| `TP_DISCIPLINA` | STRING | Sigla da disciplina/área do conhecimento avaliada (ex: LP para Língua Portuguesa). — descrição gerada por IA. |
| `NU_BLOCO` | STRING | Número do bloco de itens na estrutura do caderno de teste. — descrição gerada por IA. |
| `NU_POSICAO` | STRING | Posição de ordem do item dentro do seu respectivo bloco. — descrição gerada por IA. |
| `ID_ITEM` | STRING | Identificador único do item no banco de questões do INEP/SAEB. — descrição gerada por IA. |
| `NU_DESCRITOR_HABILIDADE` | STRING | Código da habilidade/descritor avaliado do item segundo a Matriz de Referência do SAEB. — descrição gerada por IA. |
| `TX_GABARITO` | STRING | Gabarito correto da questão objetiva ou chave de correção do item construído/textual. — descrição gerada por IA. |
| `TP_ITEM` | STRING | Tipo de formato da questão (ex: Resposta Objetiva, Resposta Construída, Produção Textual). — descrição gerada por IA. |
| `TP_ITEM_MODELO` | STRING | Modelo de TRI aplicado na calibração (ex: M3PL para Logístico de 3 Parâmetros, MRG para Modelo de Resposta Graduada). — descrição gerada por IA. |
| `A` | STRING | Parâmetro de discriminação (a) do item segundo a Teoria de Resposta ao Item (TRI). — descrição gerada por IA. |
| `B` | STRING | Parâmetro de dificuldade (b) do item para modelos de resposta dicotômica. — descrição gerada por IA. |
| `C` | STRING | Parâmetro de probabilidade de acerto ao acaso / pseudochute (c) na TRI. — descrição gerada por IA. |
| `B1` | STRING | Primeiro limiar de dificuldade (b1) para itens politômicos calibrados via Modelo de Resposta Graduada (MRG). — descrição gerada por IA. |
| `B2` | STRING | Segundo limiar de dificuldade (b2) para itens politômicos em modelos de resposta graduada. — descrição gerada por IA. |
| `B3` | STRING | Terceiro limiar de dificuldade (b3) para itens politômicos em modelos de resposta graduada. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2023_ts_professor

File `raw__inep_saeb_microdados_csv_2023_ts_professor.parquet` · 411,876 rows · 162 columns

Raw do microdado CSV TS_PROFESSOR.csv do Saeb 2023, arquivo oficial microdados_saeb_2023.zip.

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano da edição de realização do teste/questionário do SAEB. — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico da região geográfica brasileira. — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE do estado (Unidade da Federação) onde se localiza a escola. — descrição gerada por IA. |
| `ID_MUNICIPIO` | STRING | Código IBGE do município onde a escola está situada. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código do tipo de área de localização da escola (ex: Capital ou Interior). — descrição gerada por IA. |
| `ID_ESCOLA` | STRING | Código INEP de identificação da escola. — descrição gerada por IA. |
| `IN_PUBLICA` | STRING | Indicador de dependência administrativa pública (1 para pública, 0 para privada). — descrição gerada por IA. |
| `ID_LOCALIZACAO` | STRING | Código do tipo de localização da escola (1 para Urbana, 2 para Rural). — descrição gerada por IA. |
| `ID_TURMA` | STRING | Código de identificação da turma no Censo Escolar/SAEB. — descrição gerada por IA. |
| `ID_PROFESSOR` | STRING | Código identificador do professor respondente. — descrição gerada por IA. |
| `ID_SERIE` | STRING | Série ou ano escolar avaliado (ex: 5 para 5º ano, 9 para 9º ano EF, 12 para 3º ano EM). — descrição gerada por IA. |
| `SQ_QUESTIONARIO` | STRING | Sequencial único do instrumento do questionário respondido. — descrição gerada por IA. |
| `IN_PREENCHIMENTO_QUESTIONARIO` | STRING | Indicador do status de preenchimento do questionário (1 = Preenchido, 0 = Não preenchido). — descrição gerada por IA. |
| `IN_PREENCHIMENTO_OUTRA_TURMA` | STRING | Indicador de preenchimento das respostas com base em outra turma vinculada ao professor. — descrição gerada por IA. |
| `TX_Q001` | STRING | Resposta da questão 1 do questionário do professor. — descrição gerada por IA. |
| `TX_Q002` | STRING | Resposta da questão 2 do questionário do professor. — descrição gerada por IA. |
| `TX_Q003` | STRING | Resposta da questão 3 do questionário do professor. — descrição gerada por IA. |
| `TX_Q004` | STRING | Resposta da questão 4 do questionário do professor. — descrição gerada por IA. |
| `TX_Q005` | STRING | Resposta da questão 5 do questionário do professor. — descrição gerada por IA. |
| `TX_Q006` | STRING | Resposta da questão 6 do questionário do professor. — descrição gerada por IA. |
| `TX_Q007` | STRING | Resposta da questão 7 do questionário do professor. — descrição gerada por IA. |
| `TX_Q008` | STRING | Resposta da questão 8 do questionário do professor. — descrição gerada por IA. |
| `TX_Q009` | STRING | Resposta da questão 9 do questionário do professor. — descrição gerada por IA. |
| `TX_Q010` | STRING | Resposta da questão 10 do questionário do professor. — descrição gerada por IA. |
| `TX_Q011` | STRING | Resposta da questão 11 do questionário do professor. — descrição gerada por IA. |
| `TX_Q012` | STRING | Resposta da questão 12 do questionário do professor. — descrição gerada por IA. |
| `TX_Q013` | STRING | Resposta da questão 13 do questionário do professor. — descrição gerada por IA. |
| `TX_Q014` | STRING | Resposta da questão 14 do questionário do professor. — descrição gerada por IA. |
| `TX_Q015` | STRING | Resposta da questão 15 do questionário do professor. — descrição gerada por IA. |
| `TX_Q016` | STRING | Resposta da questão 16 do questionário do professor. — descrição gerada por IA. |
| `TX_Q017` | STRING | Resposta da questão 17 do questionário do professor. — descrição gerada por IA. |
| `TX_Q018` | STRING | Resposta da questão 18 do questionário do professor. — descrição gerada por IA. |
| `TX_Q019` | STRING | Resposta da questão 19 do questionário do professor. — descrição gerada por IA. |
| `TX_Q020` | STRING | Resposta da questão 20 do questionário do professor. — descrição gerada por IA. |
| `TX_Q021` | STRING | Resposta da questão 21 do questionário do professor. — descrição gerada por IA. |
| `TX_Q022` | STRING | Resposta da questão 22 do questionário do professor. — descrição gerada por IA. |
| `TX_Q023` | STRING | Resposta da questão 23 do questionário do professor. — descrição gerada por IA. |
| `TX_Q024` | STRING | Resposta da questão 24 do questionário do professor. — descrição gerada por IA. |
| `TX_Q025` | STRING | Resposta da questão 25 do questionário do professor. — descrição gerada por IA. |
| `TX_Q026` | STRING | Resposta da questão 26 do questionário do professor. — descrição gerada por IA. |
| `TX_Q027` | STRING | Resposta da questão 27 do questionário do professor. — descrição gerada por IA. |
| `TX_Q028` | STRING | Resposta da questão 28 do questionário do professor. — descrição gerada por IA. |
| `TX_Q029` | STRING | Resposta da questão 29 do questionário do professor. — descrição gerada por IA. |
| `TX_Q030` | STRING | Resposta da questão 30 do questionário do professor. — descrição gerada por IA. |
| `TX_Q031` | STRING | Resposta da questão 31 do questionário do professor. — descrição gerada por IA. |
| `TX_Q032` | STRING | Resposta da questão 32 do questionário do professor. — descrição gerada por IA. |
| `TX_Q033` | STRING | Resposta da questão 33 do questionário do professor. — descrição gerada por IA. |
| `TX_Q034` | STRING | Resposta da questão 34 do questionário do professor. — descrição gerada por IA. |
| `TX_Q035` | STRING | Resposta da questão 35 do questionário do professor. — descrição gerada por IA. |
| `TX_Q036` | STRING | Resposta da questão 36 do questionário do professor. — descrição gerada por IA. |
| `TX_Q037` | STRING | Resposta da questão 37 do questionário do professor. — descrição gerada por IA. |
| `TX_Q038` | STRING | Resposta da questão 38 do questionário do professor. — descrição gerada por IA. |
| `TX_Q039` | STRING | Resposta da questão 39 do questionário do professor. — descrição gerada por IA. |
| `TX_Q040` | STRING | Resposta da questão 40 do questionário do professor. — descrição gerada por IA. |
| `TX_Q041` | STRING | Resposta da questão 41 do questionário do professor. — descrição gerada por IA. |
| `TX_Q042` | STRING | Resposta da questão 42 do questionário do professor. — descrição gerada por IA. |
| `TX_Q043` | STRING | Resposta da questão 43 do questionário do professor. — descrição gerada por IA. |
| `TX_Q044` | STRING | Resposta da questão 44 do questionário do professor. — descrição gerada por IA. |
| `TX_Q045` | STRING | Resposta da questão 45 do questionário do professor. — descrição gerada por IA. |
| `TX_Q046` | STRING | Resposta da questão 46 do questionário do professor. — descrição gerada por IA. |
| `TX_Q047` | STRING | Resposta da questão 47 do questionário do professor. — descrição gerada por IA. |
| `TX_Q048` | STRING | Resposta da questão 48 do questionário do professor. — descrição gerada por IA. |
| `TX_Q049` | STRING | Resposta da questão 49 do questionário do professor. — descrição gerada por IA. |
| `TX_Q050` | STRING | Resposta da questão 50 do questionário do professor. — descrição gerada por IA. |
| `TX_Q051` | STRING | Resposta da questão 51 do questionário do professor. — descrição gerada por IA. |
| `TX_Q052` | STRING | Resposta da questão 52 do questionário do professor. — descrição gerada por IA. |
| `TX_Q053` | STRING | Resposta da questão 53 do questionário do professor. — descrição gerada por IA. |
| `TX_Q054` | STRING | Resposta da questão 54 do questionário do professor. — descrição gerada por IA. |
| `TX_Q055` | STRING | Resposta da questão 55 do questionário do professor. — descrição gerada por IA. |
| `TX_Q056` | STRING | Resposta da questão 56 do questionário do professor. — descrição gerada por IA. |
| `TX_Q057` | STRING | Resposta da questão 57 do questionário do professor. — descrição gerada por IA. |
| `TX_Q058` | STRING | Resposta da questão 58 do questionário do professor. — descrição gerada por IA. |
| `TX_Q059` | STRING | Resposta da questão 59 do questionário do professor. — descrição gerada por IA. |
| `TX_Q060` | STRING | Resposta da questão 60 do questionário do professor. — descrição gerada por IA. |
| `TX_Q061` | STRING | Resposta da questão 61 do questionário do professor. — descrição gerada por IA. |
| `TX_Q062` | STRING | Resposta da questão 62 do questionário do professor. — descrição gerada por IA. |
| `TX_Q063` | STRING | Resposta da questão 63 do questionário do professor. — descrição gerada por IA. |
| `TX_Q064` | STRING | Resposta da questão 64 do questionário do professor. — descrição gerada por IA. |
| `TX_Q065` | STRING | Resposta da questão 65 do questionário do professor. — descrição gerada por IA. |
| `TX_Q066` | STRING | Resposta da questão 66 do questionário do professor. — descrição gerada por IA. |
| `TX_Q067` | STRING | Resposta da questão 67 do questionário do professor. — descrição gerada por IA. |
| `TX_Q068` | STRING | Resposta da questão 68 do questionário do professor. — descrição gerada por IA. |
| `TX_Q069` | STRING | Resposta da questão 69 do questionário do professor. — descrição gerada por IA. |
| `TX_Q070` | STRING | Resposta da questão 70 do questionário do professor. — descrição gerada por IA. |
| `TX_Q071` | STRING | Resposta da questão 71 do questionário do professor. — descrição gerada por IA. |
| `TX_Q072` | STRING | Resposta da questão 72 do questionário do professor. — descrição gerada por IA. |
| `TX_Q073` | STRING | Resposta da questão 73 do questionário do professor. — descrição gerada por IA. |
| `TX_Q074` | STRING | Resposta da questão 74 do questionário do professor. — descrição gerada por IA. |
| `TX_Q075` | STRING | Resposta da questão 75 do questionário do professor. — descrição gerada por IA. |
| `TX_Q076` | STRING | Resposta da questão 76 do questionário do professor. — descrição gerada por IA. |
| `TX_Q077` | STRING | Resposta da questão 77 do questionário do professor. — descrição gerada por IA. |
| `TX_Q078` | STRING | Resposta da questão 78 do questionário do professor. — descrição gerada por IA. |
| `TX_Q079` | STRING | Resposta da questão 79 do questionário do professor. — descrição gerada por IA. |
| `TX_Q080` | STRING | Resposta da questão 80 do questionário do professor. — descrição gerada por IA. |
| `TX_Q081` | STRING | Resposta da questão 81 do questionário do professor. — descrição gerada por IA. |
| `TX_Q082` | STRING | Resposta da questão 82 do questionário do professor. — descrição gerada por IA. |
| `TX_Q083` | STRING | Resposta da questão 83 do questionário do professor. — descrição gerada por IA. |
| `TX_Q084` | STRING | Resposta da questão 84 do questionário do professor. — descrição gerada por IA. |
| `TX_Q085` | STRING | Resposta da questão 85 do questionário do professor. — descrição gerada por IA. |
| `TX_Q086` | STRING | Resposta da questão 86 do questionário do professor. — descrição gerada por IA. |
| `TX_Q087` | STRING | Resposta da questão 87 do questionário do professor. — descrição gerada por IA. |
| `TX_Q088` | STRING | Resposta da questão 88 do questionário do professor. — descrição gerada por IA. |
| `TX_Q089` | STRING | Resposta da questão 89 do questionário do professor. — descrição gerada por IA. |
| `TX_Q090` | STRING | Resposta da questão 90 do questionário do professor. — descrição gerada por IA. |
| `TX_Q091` | STRING | Resposta da questão 91 do questionário do professor. — descrição gerada por IA. |
| `TX_Q092` | STRING | Resposta da questão 92 do questionário do professor. — descrição gerada por IA. |
| `TX_Q093` | STRING | Resposta da questão 93 do questionário do professor. — descrição gerada por IA. |
| `TX_Q094` | STRING | Resposta da questão 94 do questionário do professor. — descrição gerada por IA. |
| `TX_Q095` | STRING | Resposta da questão 95 do questionário do professor. — descrição gerada por IA. |
| `TX_Q096` | STRING | Resposta da questão 96 do questionário do professor. — descrição gerada por IA. |
| `TX_Q097` | STRING | Resposta da questão 97 do questionário do professor. — descrição gerada por IA. |
| `TX_Q098` | STRING | Resposta da questão 98 do questionário do professor. — descrição gerada por IA. |
| `TX_Q099` | STRING | Resposta da questão 99 do questionário do professor. — descrição gerada por IA. |
| `TX_Q100` | STRING | Resposta da questão 100 do questionário do professor. — descrição gerada por IA. |
| `TX_Q101` | STRING | Resposta da questão 101 do questionário do professor. — descrição gerada por IA. |
| `TX_Q102` | STRING | Resposta da questão 102 do questionário do professor. — descrição gerada por IA. |
| `TX_Q103` | STRING | Resposta da questão 103 do questionário do professor. — descrição gerada por IA. |
| `TX_Q104` | STRING | Resposta da questão 104 do questionário do professor. — descrição gerada por IA. |
| `TX_Q105` | STRING | Resposta da questão 105 do questionário do professor. — descrição gerada por IA. |
| `TX_Q106` | STRING | Resposta da questão 106 do questionário do professor. — descrição gerada por IA. |
| `TX_Q107` | STRING | Resposta da questão 107 do questionário do professor. — descrição gerada por IA. |
| `TX_Q108` | STRING | Resposta da questão 108 do questionário do professor. — descrição gerada por IA. |
| `TX_Q109` | STRING | Resposta da questão 109 do questionário do professor. — descrição gerada por IA. |
| `TX_Q110` | STRING | Resposta da questão 110 do questionário do professor. — descrição gerada por IA. |
| `TX_Q111` | STRING | Resposta da questão 111 do questionário do professor. — descrição gerada por IA. |
| `TX_Q112` | STRING | Resposta da questão 112 do questionário do professor. — descrição gerada por IA. |
| `TX_Q113` | STRING | Resposta da questão 113 do questionário do professor. — descrição gerada por IA. |
| `TX_Q114` | STRING | Resposta da questão 114 do questionário do professor. — descrição gerada por IA. |
| `TX_Q115` | STRING | Resposta da questão 115 do questionário do professor. — descrição gerada por IA. |
| `TX_Q116` | STRING | Resposta da questão 116 do questionário do professor. — descrição gerada por IA. |
| `TX_Q117` | STRING | Resposta da questão 117 do questionário do professor. — descrição gerada por IA. |
| `TX_Q118` | STRING | Resposta da questão 118 do questionário do professor. — descrição gerada por IA. |
| `TX_Q119` | STRING | Resposta da questão 119 do questionário do professor. — descrição gerada por IA. |
| `TX_Q120` | STRING | Resposta da questão 120 do questionário do professor. — descrição gerada por IA. |
| `TX_Q121` | STRING | Resposta da questão 121 do questionário do professor. — descrição gerada por IA. |
| `TX_Q122` | STRING | Resposta da questão 122 do questionário do professor. — descrição gerada por IA. |
| `TX_Q123` | STRING | Resposta da questão 123 do questionário do professor. — descrição gerada por IA. |
| `TX_Q124` | STRING | Resposta da questão 124 do questionário do professor. — descrição gerada por IA. |
| `TX_Q125` | STRING | Resposta da questão 125 do questionário do professor. — descrição gerada por IA. |
| `TX_Q126` | STRING | Resposta da questão 126 do questionário do professor. — descrição gerada por IA. |
| `TX_Q127` | STRING | Resposta da questão 127 do questionário do professor. — descrição gerada por IA. |
| `TX_Q128` | STRING | Resposta da questão 128 do questionário do professor. — descrição gerada por IA. |
| `TX_Q129` | STRING | Resposta da questão 129 do questionário do professor. — descrição gerada por IA. |
| `TX_Q130` | STRING | Resposta da questão 130 do questionário do professor. — descrição gerada por IA. |
| `TX_Q131` | STRING | Resposta da questão 131 do questionário do professor. — descrição gerada por IA. |
| `TX_Q132` | STRING | Resposta da questão 132 do questionário do professor. — descrição gerada por IA. |
| `TX_Q133` | STRING | Resposta da questão 133 do questionário do professor. — descrição gerada por IA. |
| `TX_Q134` | STRING | Resposta da questão 134 do questionário do professor. — descrição gerada por IA. |
| `TX_Q135` | STRING | Resposta da questão 135 do questionário do professor. — descrição gerada por IA. |
| `TX_Q136` | STRING | Resposta da questão 136 do questionário do professor. — descrição gerada por IA. |
| `TX_Q137` | STRING | Resposta da questão 137 do questionário do professor. — descrição gerada por IA. |
| `TX_Q138` | STRING | Resposta da questão 138 do questionário do professor. — descrição gerada por IA. |
| `TX_Q139` | STRING | Resposta da questão 139 do questionário do professor. — descrição gerada por IA. |
| `TX_Q140` | STRING | Resposta da questão 140 do questionário do professor. — descrição gerada por IA. |
| `TX_Q141` | STRING | Resposta da questão 141 do questionário do professor. — descrição gerada por IA. |
| `TX_Q142` | STRING | Resposta da questão 142 do questionário do professor. — descrição gerada por IA. |
| `TX_Q143` | STRING | Resposta da questão 143 do questionário do professor. — descrição gerada por IA. |
| `TX_Q144` | STRING | Resposta da questão 144 do questionário do professor. — descrição gerada por IA. |
| `TX_Q145` | STRING | Resposta da questão 145 do questionário do professor. — descrição gerada por IA. |
| `TX_Q146` | STRING | Resposta da questão 146 do questionário do professor. — descrição gerada por IA. |
| `TX_Q147` | STRING | Resposta da questão 147 do questionário do professor. — descrição gerada por IA. |
| `TX_Q148` | STRING | Resposta da questão 148 do questionário do professor. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_2023_ts_secretario_municipal

File `raw__inep_saeb_microdados_csv_2023_ts_secretario_municipal.parquet` · 5,568 rows · 182 columns

Raw do microdado CSV TS_SECRETARIO_MUNICIPAL.csv do Saeb 2023, arquivo oficial microdados_saeb_2023.zip.

**Feeds:** `trusted/inep_saeb_secretario`

| Column | Type | Description |
|---|---|---|
| `ID_SAEB` | STRING | Ano de realização da edição do SAEB (ex: '2023'). — descrição gerada por IA. |
| `ID_REGIAO` | STRING | Código numérico de identificação da região geográfica brasileira (1: Norte, 2: Nordeste, 3: Sudeste, 4: Sul, 5: Centro-Oeste). — descrição gerada por IA. |
| `ID_UF` | STRING | Código IBGE de dois dígitos representativo da Unidade da Federação (UF). — descrição gerada por IA. |
| `CO_MUNICIPIO` | STRING | Código IBGE de 7 dígitos identificador do município. — descrição gerada por IA. |
| `ID_AREA` | STRING | Código de localização/área do município (1: Capital, 2: Interior). — descrição gerada por IA. |
| `IN_PREENCHIMENTO` | STRING | Indicador de preenchimento do questionário contextual (1: Preenchido, 0: Não preenchido). — descrição gerada por IA. |
| `TX_Q001` | STRING | Resposta informada para a Questão 1 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q002` | STRING | Resposta informada para a Questão 2 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q003` | STRING | Resposta informada para a Questão 3 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q004` | STRING | Resposta informada para a Questão 4 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q005` | STRING | Resposta informada para a Questão 5 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q006` | STRING | Resposta informada para a Questão 6 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q007` | STRING | Resposta informada para a Questão 7 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q008` | STRING | Resposta informada para a Questão 8 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q009` | STRING | Resposta informada para a Questão 9 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q010` | STRING | Resposta informada para a Questão 10 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q011` | STRING | Resposta informada para a Questão 11 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q012` | STRING | Resposta informada para a Questão 12 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q013` | STRING | Resposta informada para a Questão 13 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q014` | STRING | Resposta informada para a Questão 14 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q015` | STRING | Resposta informada para a Questão 15 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q016` | STRING | Resposta informada para a Questão 16 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q017` | STRING | Resposta informada para a Questão 17 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q018` | STRING | Resposta informada para a Questão 18 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q019` | STRING | Resposta informada para a Questão 19 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q020` | STRING | Resposta informada para a Questão 20 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q021` | STRING | Resposta informada para a Questão 21 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q022` | STRING | Resposta informada para a Questão 22 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q023` | STRING | Resposta informada para a Questão 23 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q024` | STRING | Resposta informada para a Questão 24 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q025` | STRING | Resposta informada para a Questão 25 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q026` | STRING | Resposta informada para a Questão 26 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q027` | STRING | Resposta informada para a Questão 27 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q028` | STRING | Resposta informada para a Questão 28 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q029` | STRING | Resposta informada para a Questão 29 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q030` | STRING | Resposta informada para a Questão 30 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q031` | STRING | Resposta informada para a Questão 31 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q032` | STRING | Resposta informada para a Questão 32 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q033` | STRING | Resposta informada para a Questão 33 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q034` | STRING | Resposta informada para a Questão 34 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q035` | STRING | Resposta informada para a Questão 35 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q036` | STRING | Resposta informada para a Questão 36 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q037` | STRING | Resposta informada para a Questão 37 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q038` | STRING | Resposta informada para a Questão 38 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q039` | STRING | Resposta informada para a Questão 39 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q040` | STRING | Resposta informada para a Questão 40 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q041` | STRING | Resposta informada para a Questão 41 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q042` | STRING | Resposta informada para a Questão 42 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q043` | STRING | Resposta informada para a Questão 43 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q044` | STRING | Resposta informada para a Questão 44 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q045` | STRING | Resposta informada para a Questão 45 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q046` | STRING | Resposta informada para a Questão 46 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q047` | STRING | Resposta informada para a Questão 47 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q048` | STRING | Resposta informada para a Questão 48 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q049` | STRING | Resposta informada para a Questão 49 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q050` | STRING | Resposta informada para a Questão 50 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q051` | STRING | Resposta informada para a Questão 51 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q052` | STRING | Resposta informada para a Questão 52 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q053` | STRING | Resposta informada para a Questão 53 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q054` | STRING | Resposta informada para a Questão 54 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q055` | STRING | Resposta informada para a Questão 55 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q056` | STRING | Resposta informada para a Questão 56 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q057` | STRING | Resposta informada para a Questão 57 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q058` | STRING | Resposta informada para a Questão 58 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q059` | STRING | Resposta informada para a Questão 59 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q060` | STRING | Resposta informada para a Questão 60 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q061` | STRING | Resposta informada para a Questão 61 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q062` | STRING | Resposta informada para a Questão 62 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q063` | STRING | Resposta informada para a Questão 63 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q064` | STRING | Resposta informada para a Questão 64 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q065` | STRING | Resposta informada para a Questão 65 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q066` | STRING | Resposta informada para a Questão 66 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q067` | STRING | Resposta informada para a Questão 67 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q068` | STRING | Resposta informada para a Questão 68 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q069` | STRING | Resposta informada para a Questão 69 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q070` | STRING | Resposta informada para a Questão 70 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q071` | STRING | Resposta informada para a Questão 71 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q072` | STRING | Resposta informada para a Questão 72 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q073` | STRING | Resposta informada para a Questão 73 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q074` | STRING | Resposta informada para a Questão 74 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q075` | STRING | Resposta informada para a Questão 75 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q076` | STRING | Resposta informada para a Questão 76 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q077` | STRING | Resposta informada para a Questão 77 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q078` | STRING | Resposta informada para a Questão 78 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q079` | STRING | Resposta informada para a Questão 79 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q080` | STRING | Resposta informada para a Questão 80 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q081` | STRING | Resposta informada para a Questão 81 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q082` | STRING | Resposta informada para a Questão 82 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q083` | STRING | Resposta informada para a Questão 83 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q084` | STRING | Resposta informada para a Questão 84 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q085` | STRING | Resposta informada para a Questão 85 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q086` | STRING | Resposta informada para a Questão 86 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q087` | STRING | Resposta informada para a Questão 87 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q088` | STRING | Resposta informada para a Questão 88 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q089` | STRING | Resposta informada para a Questão 89 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q090` | STRING | Resposta informada para a Questão 90 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q091` | STRING | Resposta informada para a Questão 91 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q092` | STRING | Resposta informada para a Questão 92 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q093` | STRING | Resposta informada para a Questão 93 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q094` | STRING | Resposta informada para a Questão 94 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q095` | STRING | Resposta informada para a Questão 95 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q096` | STRING | Resposta informada para a Questão 96 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q097` | STRING | Resposta informada para a Questão 97 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q098` | STRING | Resposta informada para a Questão 98 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q099` | STRING | Resposta informada para a Questão 99 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q100` | STRING | Resposta informada para a Questão 100 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q101` | STRING | Resposta informada para a Questão 101 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q102` | STRING | Resposta informada para a Questão 102 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q103` | STRING | Resposta informada para a Questão 103 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q104` | STRING | Resposta informada para a Questão 104 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q105` | STRING | Resposta informada para a Questão 105 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q106` | STRING | Resposta informada para a Questão 106 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q107` | STRING | Resposta informada para a Questão 107 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q108` | STRING | Resposta informada para a Questão 108 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q109` | STRING | Resposta informada para a Questão 109 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q110` | STRING | Resposta informada para a Questão 110 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q111` | STRING | Resposta informada para a Questão 111 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q112` | STRING | Resposta informada para a Questão 112 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q113` | STRING | Resposta informada para a Questão 113 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q114` | STRING | Resposta informada para a Questão 114 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q115` | STRING | Resposta informada para a Questão 115 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q116` | STRING | Resposta informada para a Questão 116 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q117` | STRING | Resposta informada para a Questão 117 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q118` | STRING | Resposta informada para a Questão 118 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q119` | STRING | Resposta informada para a Questão 119 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q120` | STRING | Resposta informada para a Questão 120 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q121` | STRING | Resposta informada para a Questão 121 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q122` | STRING | Resposta informada para a Questão 122 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q123` | STRING | Resposta informada para a Questão 123 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q124` | STRING | Resposta informada para a Questão 124 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q125` | STRING | Resposta informada para a Questão 125 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q126` | STRING | Resposta informada para a Questão 126 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q127` | STRING | Resposta informada para a Questão 127 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q128` | STRING | Resposta informada para a Questão 128 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q129` | STRING | Resposta informada para a Questão 129 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q130` | STRING | Resposta informada para a Questão 130 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q131` | STRING | Resposta informada para a Questão 131 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q132` | STRING | Resposta informada para a Questão 132 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q133` | STRING | Resposta informada para a Questão 133 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q134` | STRING | Resposta informada para a Questão 134 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q135` | STRING | Resposta informada para a Questão 135 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q136` | STRING | Resposta informada para a Questão 136 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q137` | STRING | Resposta informada para a Questão 137 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q138` | STRING | Resposta informada para a Questão 138 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q139` | STRING | Resposta informada para a Questão 139 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q140` | STRING | Resposta informada para a Questão 140 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q141` | STRING | Resposta informada para a Questão 141 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q142` | STRING | Resposta informada para a Questão 142 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q143` | STRING | Resposta informada para a Questão 143 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q144` | STRING | Resposta informada para a Questão 144 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q145` | STRING | Resposta informada para a Questão 145 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q146` | STRING | Resposta informada para a Questão 146 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q147` | STRING | Resposta informada para a Questão 147 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q148` | STRING | Resposta informada para a Questão 148 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q149` | STRING | Resposta informada para a Questão 149 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q150` | STRING | Resposta informada para a Questão 150 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q151` | STRING | Resposta informada para a Questão 151 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q152` | STRING | Resposta informada para a Questão 152 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q153` | STRING | Resposta informada para a Questão 153 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q154` | STRING | Resposta informada para a Questão 154 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q155` | STRING | Resposta informada para a Questão 155 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q156` | STRING | Resposta informada para a Questão 156 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q157` | STRING | Resposta informada para a Questão 157 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q158` | STRING | Resposta informada para a Questão 158 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q159` | STRING | Resposta informada para a Questão 159 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q160` | STRING | Resposta informada para a Questão 160 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q161` | STRING | Resposta informada para a Questão 161 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q162` | STRING | Resposta informada para a Questão 162 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q163` | STRING | Resposta informada para a Questão 163 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q164` | STRING | Resposta informada para a Questão 164 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q165` | STRING | Resposta informada para a Questão 165 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q166` | STRING | Resposta informada para a Questão 166 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q167` | STRING | Resposta informada para a Questão 167 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q168` | STRING | Resposta informada para a Questão 168 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q169` | STRING | Resposta informada para a Questão 169 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q170` | STRING | Resposta informada para a Questão 170 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q171` | STRING | Resposta informada para a Questão 171 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q172` | STRING | Resposta informada para a Questão 172 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q173` | STRING | Resposta informada para a Questão 173 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q174` | STRING | Resposta informada para a Questão 174 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q175` | STRING | Resposta informada para a Questão 175 do questionário contextual do SAEB. — descrição gerada por IA. |
| `TX_Q176` | STRING | Resposta informada para a Questão 176 do questionário contextual do SAEB. — descrição gerada por IA. |

## raw · inep_saeb_microdados_csv_tabelas

File `raw__inep_saeb_microdados_csv_tabelas.parquet` · 64 rows · 13 columns

Catalogo das tabelas raw criadas a partir dos CSVs de microdados do Saeb.

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano da edicao do Saeb. |
| `arquivo_zip` | STRING | Arquivo oficial ZIP de origem. |
| `nome_conteudo` | STRING | Nome do CSV dentro do ZIP. |
| `membro_zip` | STRING | Caminho do membro dentro do ZIP. |
| `familia` | STRING | Familia inferida do microdado: aluno, escola, professor, diretor, item, etc. |
| `serie_arquivo` | STRING | Serie/etapa inferida pelo nome do arquivo, quando aplicavel. |
| `disciplina_arquivo` | STRING | Disciplina inferida pelo nome do arquivo, quando aplicavel. |
| `delimitador` | STRING | Delimitador detectado no CSV original. |
| `qtd_colunas` | INTEGER | Número total de colunas identificadas na tabela carregada. — descrição gerada por IA. |
| `qtd_linhas` | INTEGER | Número total de registros/linhas processados e ingeridos. — descrição gerada por IA. |
| `status_carga` | STRING | Situação do processamento do arquivo no Data Lake (ex: 'loaded', 'failed'). — descrição gerada por IA. |
| `erro_carga` | STRING | Mensagem de erro de carga, quando houver. |
| `dt_ingestao_lake` | TIMESTAMP | Data/hora da carga no BigQuery. |

## raw · inep_saeb_microdados_txt_1997_biologia_03ano_txt

File `raw__inep_saeb_microdados_txt_1997_biologia_03ano_txt.parquet` · 8,005 rows · 1 columns

Raw de linhas TXT do microdado historico BIOLOGIA_03ANO.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_ciencias_04serie_txt

File `raw__inep_saeb_microdados_txt_1997_ciencias_04serie_txt.parquet` · 23,506 rows · 1 columns

Raw de linhas TXT do microdado historico CIENCIAS_04SERIE.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_ciencias_08serie_txt

File `raw__inep_saeb_microdados_txt_1997_ciencias_08serie_txt.parquet` · 18,822 rows · 1 columns

Raw de linhas TXT do microdado historico CIENCIAS_08SERIE.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_diretor_97_txt

File `raw__inep_saeb_microdados_txt_1997_diretor_97_txt.parquet` · 2,351 rows · 1 columns

Raw de linhas TXT do microdado historico DIRETOR_97.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_docente_97_txt

File `raw__inep_saeb_microdados_txt_1997_docente_97_txt.parquet` · 19,339 rows · 1 columns

Raw de linhas TXT do microdado historico DOCENTE_97.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_escola_97_txt

File `raw__inep_saeb_microdados_txt_1997_escola_97_txt.parquet` · 2,351 rows · 1 columns

Raw de linhas TXT do microdado historico ESCOLA_97.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_fisica_03ano_txt

File `raw__inep_saeb_microdados_txt_1997_fisica_03ano_txt.parquet` · 7,988 rows · 1 columns

Raw de linhas TXT do microdado historico FISICA_03ANO.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_matematica_03ano_txt

File `raw__inep_saeb_microdados_txt_1997_matematica_03ano_txt.parquet` · 8,136 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_03ANO.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |

## raw · inep_saeb_microdados_txt_1997_matematica_04serie_txt

File `raw__inep_saeb_microdados_txt_1997_matematica_04serie_txt.parquet` · 23,535 rows · 1 columns

Raw de linhas TXT do microdado historico MATEMATICA_04SERIE.TXT do Saeb 1997.

| Column | Type | Description |
|---|---|---|
| `linha` | STRING | Linha original do arquivo TXT de largura fixa do Saeb. |
