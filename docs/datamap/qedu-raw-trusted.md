# QEdu early childhood: Raw and Trusted

Dataset: [lucasrangelss/qedu-raw-trusted](https://www.kaggle.com/datasets/lucasrangelss/qedu-raw-trusted) · snapshot 2026-09-30 · 5 tables · 33,296 rows

**Source:** QEdu, [https://qedu.org.br/](https://qedu.org.br/)

Early childhood education attendance, teachers, infrastructure and policies per municipality, collected from the QEdu site.

**Grain and keys:** Municipality. Two endpoints (basic infrastructure and teachers) return no data at the source for early childhood, which is not a parsing error.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`wscrap_qedu_educacao_infantil_raw`](#raw-wscrap-qedu-educacao-infantil-raw) | 5,570 | 8 | 8 | source |
| trusted | [`wscrap_qedu_educacao_infantil_atendimento`](#trusted-wscrap-qedu-educacao-infantil-atendimento) | 11,016 | 9 | 9 | `wscrap_qedu_educacao_infantil_raw` |
| trusted | [`wscrap_qedu_educacao_infantil_docentes`](#trusted-wscrap-qedu-educacao-infantil-docentes) | 5,570 | 18 | 18 | `wscrap_qedu_educacao_infantil_raw` |
| trusted | [`wscrap_qedu_educacao_infantil_infraestrutura`](#trusted-wscrap-qedu-educacao-infantil-infraestrutura) | 5,570 | 24 | 24 | `wscrap_qedu_educacao_infantil_raw` |
| trusted | [`wscrap_qedu_educacao_infantil_politicas`](#trusted-wscrap-qedu-educacao-infantil-politicas) | 5,570 | 19 | 19 | `wscrap_qedu_educacao_infantil_raw` |

## raw · wscrap_qedu_educacao_infantil_raw

File `raw__wscrap_qedu_educacao_infantil_raw.parquet` · 5,570 rows · 8 columns

Dados brutos extraidos da API publica do QEdu para Educacao Infantil. Grao: 1 linha por municipio. Campo json_bruto contem JSON completo de 8 endpoints: atendimento (evolucao historica de matriculas), infraestrutura basica e pedagogica, adequacao de infraestrutura, formacao de professores, necessidade de formacao, politicas municipais resumidas e politicas completas. Fonte: qedu.org.br/api/v1/educacao-infantil.

**Feeds:** `trusted/wscrap_qedu_educacao_infantil_atendimento`, `trusted/wscrap_qedu_educacao_infantil_docentes`, `trusted/wscrap_qedu_educacao_infantil_infraestrutura`, `trusted/wscrap_qedu_educacao_infantil_politicas`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | STRING | Código IBGE do município (7 dígitos). Chave primária. |
| `municipio` | STRING | Nome do município conforme a base do Censo Escolar INEP. |
| `uf` | STRING | Sigla da UF (ex: SP, MG, BA). |
| `json_bruto` | STRING | JSON completo com as respostas de todos os endpoints da API QEdu para Educação Infantil deste município. Estrutura: {endpoints: {evolucao, infraestrutura, infraestrutura_basica, adequacao_infra, professores, necessidade_formacao, politicas, politicas_completas}}. |
| `dt_extracao` | TIMESTAMP | Timestamp UTC de quando a extração foi realizada pelo scraper. |
| `status` | STRING | Resultado da extração: 'success' ou 'error'. |
| `erro_msg` | STRING | Mensagem de erro se status=error; NULL se success. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC de ingestao no data lake. |

## trusted · wscrap_qedu_educacao_infantil_atendimento

File `trusted__wscrap_qedu_educacao_infantil_atendimento.parquet` · 11,016 rows · 9 columns

Percentual de criancas matriculadas na Educacao Infantil por municipio e ano, separado por faixa etaria (creche 0-3 anos e pre-escola 4-5 anos). Grao: 1 linha por (municipio, faixa_etaria, ano). Fonte: API QEdu /atendimento/evolucao.

**Built from:** `raw/wscrap_qedu_educacao_infantil_raw`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | STRING | Codigo IBGE do municipio (7 digitos). FK -> semantic_zone.obt_ibge_municipio. |
| `municipio` | STRING | Nome do municipio. |
| `uf` | STRING | Sigla da UF. |
| `faixa_etaria` | STRING | Faixa etaria da educacao infantil: creche (0 a 3 anos) ou pre-escola (4 a 5 anos). |
| `ano` | INTEGER | Ano de referencia do indicador de atendimento. |
| `perc_matriculadas` | FLOAT | Percentual de criancas da faixa etaria matriculadas na educacao infantil no municipio (%). |
| `observacao` | INTEGER | Observacao/nota do QEdu sobre o indicador, quando houver. |
| `dt_extracao` | TIMESTAMP | Timestamp UTC da extracao da API QEdu. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake (trusted). |

## trusted · wscrap_qedu_educacao_infantil_docentes

File `trusted__wscrap_qedu_educacao_infantil_docentes.parquet` · 5,570 rows · 18 columns

Perfil de formacao e vinculo dos professores de Educacao Infantil por municipio, mais percentual de diretores que relatam necessidade de formacao por area. Grao: 1 linha por municipio. Fonte: API QEdu /professores e /necessidade-formacao.

**Built from:** `raw/wscrap_qedu_educacao_infantil_raw`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | STRING | Codigo IBGE do municipio (7 digitos). FK -> semantic_zone.obt_ibge_municipio. |
| `municipio` | STRING | Nome do municipio. |
| `uf` | STRING | Sigla da UF. |
| `perc_docentes_licenciatura` | FLOAT | Percentual de docentes da educacao infantil com licenciatura (%). |
| `perc_docentes_concursados` | FLOAT | Percentual de docentes concursados (efetivos) (%). |
| `perc_docentes_custeio_publico` | FLOAT | Percentual de docentes custeados pelo poder publico (%). |
| `perc_docentes_assistentes` | FLOAT | Percentual de auxiliares/assistentes de docencia (%). |
| `perc_nec_educacao_especial` | FLOAT | Percentual de diretores que relatam necessidade de formacao docente em educacao especial (%). |
| `perc_nec_ludico` | FLOAT | Percentual que relata necessidade de formacao em atividades ludicas (%). |
| `perc_nec_tecnologia` | FLOAT | Percentual que relata necessidade de formacao em tecnologia educacional (%). |
| `perc_nec_planejamento` | FLOAT | Percentual que relata necessidade de formacao em planejamento pedagogico (%). |
| `perc_nec_gestao_conflitos` | FLOAT | Percentual que relata necessidade de formacao em gestao de conflitos/problemas (%). |
| `perc_nec_avaliacao` | FLOAT | Percentual que relata necessidade de formacao em avaliacao da aprendizagem (%). |
| `perc_nec_cultura_local` | FLOAT | Percentual que relata necessidade de formacao em cultura local (%). |
| `perc_nec_conflitos_familia` | FLOAT | Percentual que relata necessidade de formacao para lidar com conflitos/relacao com familias (%). |
| `perc_nec_projeto_pedagogico` | FLOAT | Percentual que relata necessidade de formacao em projeto pedagogico (%). |
| `dt_extracao` | TIMESTAMP | Timestamp UTC da extracao da API QEdu. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake (trusted). |

## trusted · wscrap_qedu_educacao_infantil_infraestrutura

File `trusted__wscrap_qedu_educacao_infantil_infraestrutura.parquet` · 5,570 rows · 24 columns

Percentual de unidades de Educacao Infantil (rede publica) com cada item de infraestrutura, por municipio. Cobre infraestrutura basica (energia, agua, banheiro, internet, biblioteca, cozinha, predio proprio) e pedagogica especifica da etapa (banheiro infantil, parque, area verde, materiais artisticos, material pedagogico infantil). Grao: 1 linha por municipio. Fonte: API QEdu /infraestrutura (dependencia_id=5, rede publica agregada: Federal+Estadual+Municipal).

**Built from:** `raw/wscrap_qedu_educacao_infantil_raw`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | STRING | Codigo IBGE do municipio (7 digitos). FK -> semantic_zone.obt_ibge_municipio. |
| `municipio` | STRING | Nome do municipio. |
| `uf` | STRING | Sigla da UF. |
| `perc_energia_rede_publica` | FLOAT | Percentual de unidades de educacao infantil com energia da rede publica (%). |
| `perc_agua_rede_publica` | FLOAT | Percentual de unidades com agua da rede publica (%). |
| `perc_banheiro` | FLOAT | Percentual de unidades com banheiro (%). |
| `perc_esgoto_rede_publica` | FLOAT | Percentual de unidades com esgoto ligado a rede publica (%). |
| `perc_coleta_lixo` | FLOAT | Percentual de unidades com coleta de lixo (%). |
| `perc_internet` | FLOAT | Percentual de unidades com acesso a internet (%). |
| `perc_acessibilidade` | FLOAT | Percentual de unidades com recursos de acessibilidade (%). |
| `perc_biblioteca_sala_leitura` | FLOAT | Percentual de unidades com biblioteca ou sala de leitura (%). |
| `perc_alimentacao_oferecida` | FLOAT | Percentual de unidades que oferecem alimentacao (%). |
| `perc_cozinha` | FLOAT | Percentual de unidades com cozinha (%). |
| `perc_predio_proprio` | FLOAT | Percentual de unidades que funcionam em predio proprio/escolar (%). |
| `perc_banheiro_infantil` | FLOAT | Percentual de unidades com banheiro adequado a educacao infantil (%). |
| `perc_parque_infantil` | FLOAT | Percentual de unidades com parque infantil (%). |
| `perc_area_verde` | FLOAT | Percentual de unidades com area verde (%). |
| `perc_materiais_artisticos` | FLOAT | Percentual de unidades com materiais artisticos (%). |
| `perc_jogos_brinquedos` | FLOAT | Percentual de unidades com jogos e brinquedos pedagogicos (%). |
| `perc_material_pedagogico_infantil` | FLOAT | Percentual de unidades com material pedagogico especifico para a educacao infantil (%). |
| `perc_infra_basica_completa` | FLOAT | Percentual de unidades com infraestrutura basica completa (%). |
| `perc_infra_pedagogica_completa` | FLOAT | Percentual de unidades com TODOS os itens de infraestrutura pedagogica (especifica da etapa) completos (%). Fonte: campo infraestrutura.pedagogica da API QEdu. |
| `dt_extracao` | TIMESTAMP | Timestamp UTC da extracao da API QEdu. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake (trusted). |

## trusted · wscrap_qedu_educacao_infantil_politicas

File `trusted__wscrap_qedu_educacao_infantil_politicas.parquet` · 5,570 rows · 19 columns

Politicas municipais de Educacao Infantil declaradas pelas Secretarias de Educacao no Questionario do Saeb. Grao: 1 linha por municipio. 100=Sim, 0=Nao, NULL=sem resposta. Fonte: API QEdu /politicas e /politicas-completas.

**Built from:** `raw/wscrap_qedu_educacao_infantil_raw`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | STRING | Codigo IBGE do municipio (7 digitos). FK -> semantic_zone.obt_ibge_municipio. |
| `municipio` | STRING | Nome do municipio. |
| `uf` | STRING | Sigla da UF. |
| `tem_formacao_professores` | INTEGER | Municipio declara politica de formacao de professores da educacao infantil (100=Sim, 0=Nao, NULL=sem resposta). |
| `tem_curriculo_especifico` | INTEGER | Declara curriculo especifico para a educacao infantil (100/0/NULL). |
| `tem_plano_carreira` | INTEGER | Declara plano de carreira para profissionais da educacao infantil (100/0/NULL). |
| `tem_politica_demanda_vagas` | INTEGER | Declara politica de gestao da demanda por vagas (100/0/NULL). |
| `tem_politica_supervisao` | INTEGER | Declara supervisao/coordenacao pedagogica (100/0/NULL). |
| `tem_politica_formacao_docente` | INTEGER | Declara formacao continuada docente (100/0/NULL). |
| `tem_politica_busca_ativa` | INTEGER | Declara busca ativa de criancas fora da pre-escola (100/0/NULL). |
| `tem_politica_intersetorial` | INTEGER | Declara atuacao intersetorial (saude/assistencia social) (100/0/NULL). |
| `tem_metas_pme` | INTEGER | Declara metas de educacao infantil no Plano Municipal de Educacao (100/0/NULL). |
| `tem_curriculo_municipal` | INTEGER | Declara curriculo municipal (100/0/NULL). |
| `tem_plano_carreira_docente` | INTEGER | Declara plano de carreira docente (100/0/NULL). |
| `tem_politica_transporte` | INTEGER | Declara politica de transporte escolar (100/0/NULL). |
| `tem_parceria_privada_creche` | INTEGER | Declara parceria com instituicoes privadas para creche (100/0/NULL). |
| `tem_parceria_privada_pre_escola` | INTEGER | Declara parceria com instituicoes privadas para pre-escola (100/0/NULL). |
| `dt_extracao` | TIMESTAMP | Timestamp UTC da extracao da API QEdu. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake (trusted). |
