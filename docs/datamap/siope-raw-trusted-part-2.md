# SIOPE education finance: Raw and Trusted

Dataset: [lucasrangelss/siope-raw-trusted-part-2](https://www.kaggle.com/datasets/lucasrangelss/siope-raw-trusted-part-2) · snapshot 2026-10-02 · 13 tables · 530,094,262 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/siope/](https://www.fnde.gov.br/siope/)

Education revenue, expenditure and indicators reported by municipalities and states, from the SIOPE open-data API (Olinda), the FNDE SIOPE exports, and the budget execution report (RREO) PDFs parsed into tables.

**Grain and keys:** Municipality (or state) by year and reporting period. Indicator rows repeat by `num_periodo`, so analyses keep the latest period per municipality and year. Municipality joins to IBGE through `codigo_municipio`.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`api_olinda_siope_despesas_funcao_educacao`](#raw-api-olinda-siope-despesas-funcao-educacao) | 4,982,070 | 26 | 26 | source |
| raw | [`api_olinda_siope_indicadores`](#raw-api-olinda-siope-indicadores) | 21,195,152 | 27 | 27 | source |
| raw | [`api_olinda_siope_informacoes_complementares`](#raw-api-olinda-siope-informacoes-complementares) | 19,789,405 | 24 | 24 | source |
| raw | [`api_olinda_siope_receita`](#raw-api-olinda-siope-receita) | 244,805,525 | 28 | 28 | source |
| raw | [`api_olinda_siope_remuneracao`](#raw-api-olinda-siope-remuneracao) | 68,046,053 | 28 | 28 | source |
| raw | [`api_olinda_siope_responsaveis`](#raw-api-olinda-siope-responsaveis) | 1,732,317 | 49 | 1 | source |
| raw | [`fnde_siope_dados_gerais`](#raw-fnde-siope-dados-gerais) | 166,452 | 53 | 53 | source |
| raw | [`fnde_siope_despesa_total_educacao`](#raw-fnde-siope-despesa-total-educacao) | 139,046,717 | 21 | 21 | source |
| raw | [`fnde_siope_despesas_funcao_educacao`](#raw-fnde-siope-despesas-funcao-educacao) | 1,199,526 | 12 | 12 | source |
| raw | [`fnde_siope_indicadores`](#raw-fnde-siope-indicadores) | 6,441,160 | 14 | 14 | source |
| raw | [`fnde_siope_informacoes_complementares`](#raw-fnde-siope-informacoes-complementares) | 8,378,339 | 9 | 9 | source |
| raw | [`fnde_siope_receita_total`](#raw-fnde-siope-receita-total) | 14,311,287 | 13 | 13 | source |
| raw | [`rreo_siope_data`](#raw-rreo-siope-data) | 259 | 10 | 10 | source |

## raw · api_olinda_siope_despesas_funcao_educacao

File `raw__api_olinda_siope_despesas_funcao_educacao.parquet` · 4,982,070 rows · 26 columns

Tabela de despesas públicas com educação por subfunção, originada do SIOPE (Sistema de Informações sobre Orçamentos Públicos em Educação), detalhando valores empenhados, liquidados e pagos por município e período.

**Feeds:** `trusted/api_olinda_siope_despesas_funcao_educacao`

| Column | Type | Description |
|---|---|---|
| `TIPO` | STRING | Tipo de administração pública declarante (ex: Municipal, Estadual). |
| `NUM_ANO` | STRING | Ano de referência do exercício financeiro (formato YYYY). |
| `NUM_PERI` | STRING | Número do período ou bimestre de referência do relatório SIOPE. |
| `COD_UF` | STRING | Código IBGE de dois dígitos da Unidade da Federação. |
| `SIG_UF` | STRING | Sigla da Unidade da Federação (ex: RO, SP). |
| `COD_MUNI` | STRING | Código IBGE de 6 dígitos identificador do município. |
| `NOM_MUNI` | STRING | Nome oficial do município. |
| `NUM_ORDE` | STRING | Número de ordem ou identificador da linha de despesa no relatório de origem. |
| `DES_SUBF` | STRING | Código identificador da subfunção da despesa orçamentária (ex: 306 para Alimentação, 361 para Ensino Fundamental). |
| `VAL_DESP_EMPE` | STRING | Valor total da despesa empenhada no período, em reais (R$). |
| `VAL_DESP_LIQU` | STRING | Valor total da despesa liquidada no período, em reais (R$). |
| `VAL_DESP_PAGA` | STRING | Valor total da despesa efetivamente paga no período, em reais (R$). |
| `record_index` | INTEGER | Índice sequencial do registro dentro da página extraída da API. |
| `page_number` | INTEGER | Número da página de paginação da API de origem de onde o dado foi extraído. |
| `source_endpoint` | STRING | Nome do endpoint ou serviço de origem dos dados (ex: Despesas_Funcao_Educacao_Siope). |
| `request_url` | STRING | URL completa utilizada para a requisição dos dados na API de origem. |
| `http_status` | INTEGER | Código de status HTTP retornado pela requisição da API (ex: 200). |
| `response_hash` | STRING | Hash MD5/SHA da resposta da API para controle de integridade e duplicidade. |
| `schema_fingerprint` | STRING | Assinatura ou hash que identifica a versão do esquema de dados atual. |
| `record_count` | INTEGER | Contagem total de registros retornados na requisição da API. |
| `ano` | INTEGER | Ano de referência utilizado para fins de partição ou filtro no data lake. |
| `periodo` | INTEGER | Período de referência utilizado para fins de partição ou filtro no data lake. |
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `mes_exercicio` | INTEGER | Mês de exercício financeiro utilizado como parâmetro de extração. |
| `cod_muni_filtro` | STRING | Código do município utilizado como parâmetro de filtro na requisição. |
| `dt_ingestao_lake` | STRING | Data e hora no formato ISO 8601 em que o registro foi gravado no Data Lake. — descrição gerada por IA. |

## raw · api_olinda_siope_indicadores

File `raw__api_olinda_siope_indicadores.parquet` · 21,195,152 rows · 27 columns

Tabela de indicadores financeiros e orçamentários da educação pública municipal e estadual, originados do SIOPE (Sistema de Informações sobre Orçamentos Públicos em Educação), utilizada para monitoramento de despesas com pessoal, FUNDEB e manutenção do ensino.

**Feeds:** `trusted/api_olinda_siope_indicadores`

| Column | Type | Description |
|---|---|---|
| `TIPO` | STRING | Tipo de ente federativo analisado (ex: 'Municipal', 'Estadual'). |
| `NUM_ANO` | STRING | Ano de referência do indicador financeiro (formato YYYY). |
| `NUM_PERI` | STRING | Número do período ou bimestre de referência do indicador. |
| `COD_UF` | STRING | Código IBGE de identificação da Unidade da Federação. |
| `SIG_UF` | STRING | Sigla da Unidade da Federação (ex: 'AC', 'SP'). |
| `COD_MUNI` | STRING | Código IBGE de identificação do município (6 dígitos). |
| `NOM_MUNI` | STRING | Nome oficial do município. |
| `COD_INDI` | STRING | Código identificador único do indicador no sistema de origem. |
| `COD_EXIB` | STRING | Código de exibição ou ordenação estruturada do indicador (ex: '2.11'). |
| `NOM_INDI` | STRING | Descrição textual do indicador educacional ou financeiro. |
| `COD_GRUP` | STRING | Código identificador do grupo de indicadores. |
| `NOM_GRUP_INDI` | STRING | Nome do grupo de indicadores (ex: 'Indicadores de Dispêndio com Pessoal'). |
| `VAL_INDI` | STRING | Valor numérico do indicador (pode representar percentuais, valores monetários ou índices). |
| `record_index` | INTEGER | Índice sequencial do registro dentro do lote de extração. |
| `page_number` | INTEGER | Número da página da API de origem de onde o dado foi extraído. |
| `source_endpoint` | STRING | Nome do endpoint ou serviço de origem dos dados (ex: 'Indicadores_Siope'). |
| `request_url` | STRING | URL completa utilizada na requisição da API de origem. |
| `http_status` | INTEGER | Código de status HTTP retornado na requisição de extração (ex: '200'). |
| `response_hash` | STRING | Hash de validação do conteúdo da resposta para controle de integridade. |
| `schema_fingerprint` | STRING | Assinatura digital do esquema de dados para controle de versionamento. |
| `record_count` | INTEGER | Quantidade total de registros retornados pela requisição. — descrição gerada por IA. |
| `ano` | INTEGER | Ano utilizado como chave de partição ou filtro na ingestão do dado. |
| `periodo` | INTEGER | Período utilizado como chave de partição ou filtro na ingestão do dado. |
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `mes_exercicio` | INTEGER | Mês de exercício financeiro de referência para o registro. |
| `cod_muni_filtro` | STRING | Código do município utilizado como filtro na requisição de extração. |
| `dt_ingestao_lake` | STRING | Data e hora (timestamp ISO 8601) de gravação do registro no Data Lake. — descrição gerada por IA. |

## raw · api_olinda_siope_informacoes_complementares

File `raw__api_olinda_siope_informacoes_complementares.parquet` · 19,789,405 rows · 24 columns

Tabela de informações complementares do SIOPE (Sistema de Informações sobre Orçamentos Públicos em Educação) contendo dados declarados de receitas, despesas e saldos de entes municipais e estaduais, utilizada para análise de financiamento da educação pública.

**Feeds:** `trusted/api_olinda_siope_informacoes_complementares`

| Column | Type | Description |
|---|---|---|
| `TIPO` | STRING | Tipo de ente federativo declarado (ex: 'Municipal' ou 'Estadual'). |
| `NUM_ANO` | STRING | Ano de referência da declaração financeira (formato YYYY). |
| `NUM_PERI` | STRING | Número do período ou bimestre de referência da declaração dentro do ano. |
| `COD_UF` | STRING | Código numérico do IBGE correspondente à Unidade Federativa. |
| `SIG_UF` | STRING | Sigla da Unidade Federativa (ex: 'AC', 'SP'). |
| `COD_MUNI` | STRING | Código numérico do IBGE correspondente ao município (6 dígitos). |
| `NOM_MUNI` | STRING | Nome oficial do município declarante. |
| `COD_EXIB` | STRING | Código identificador de exibição do item orçamentário no sistema SIOPE. |
| `NOM_ITEM` | STRING | Nome ou descrição da rubrica/item financeiro declarado (ex: pagamentos do Fundeb, royalties). |
| `VAL_DECL` | STRING | Valor monetário declarado para o item específico (em formato decimal). |
| `record_index` | INTEGER | Índice sequencial do registro dentro do lote ou página extraída. |
| `page_number` | INTEGER | Número da página da API de origem de onde o dado foi extraído. |
| `source_endpoint` | STRING | Nome do endpoint ou serviço de origem dos dados da extração (ex: 'Informacoes_Complementares_Siope'). |
| `request_url` | STRING | URL completa utilizada na requisição para coleta do dado. |
| `http_status` | INTEGER | Código de status HTTP retornado pela API de origem durante a coleta (ex: '200'). |
| `response_hash` | STRING | Hash de controle gerado a partir da resposta da API para verificar integridade e duplicidade. |
| `schema_fingerprint` | STRING | Assinatura digital do esquema de dados para controle de versionamento da estrutura da tabela. |
| `record_count` | INTEGER | Contagem total de registros retornados na requisição de origem. |
| `ano` | INTEGER | Ano de referência normalizado para fins de particionamento e filtro no data lake. |
| `periodo` | INTEGER | Período/bimestre normalizado para fins de particionamento e filtro no data lake. |
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `mes_exercicio` | INTEGER | Mês de exercício de referência do dado, quando aplicável. |
| `cod_muni_filtro` | STRING | Código do município utilizado como parâmetro de filtro na requisição de origem. |
| `dt_ingestao_lake` | STRING | Data e hora exatas da inserção do registro no Data Lake (formato ISO 8601). — descrição gerada por IA. |

## raw · api_olinda_siope_receita

File `raw__api_olinda_siope_receita.parquet` · 244,805,525 rows · 28 columns

Tabela contendo dados de receitas declaradas no SIOPE (Sistema de Informações sobre Orçamentos Públicos em Educação) por municípios, utilizada para monitoramento de recursos e investimentos em educação pública.

**Feeds:** `trusted/api_olinda_siope_receita`

| Column | Type | Description |
|---|---|---|
| `TIPO` | STRING | Tipo de administração ou ente federativo (ex: 'Municipal'). |
| `NUM_ANO` | STRING | Ano de referência do dado financeiro declarado. |
| `NUM_PERI` | STRING | Número do período de referência (ex: bimestre ou semestre). |
| `COD_UF` | STRING | Código IBGE de 2 dígitos identificador da Unidade Federativa. |
| `SIG_UF` | STRING | Sigla da Unidade Federativa (ex: 'PA'). |
| `COD_MUNI` | STRING | Código IBGE de 6 dígitos identificador do município. |
| `NOM_MUNI` | STRING | Nome do município correspondente. |
| `COD_EXIB_FORMATADO` | STRING | Código formatado de exibição da classificação da receita (ex: '4,17,21,35,01,00'). |
| `NOM_ITEM` | STRING | Nome da rubrica, receita ou transferência declarada (ex: 'Transferências do Salário Educação'). |
| `IDN_CLAS` | STRING | Identificador da classificação do dado financeiro (ex: 'PA' para Previsão Atualizada). |
| `NOM_COLU` | STRING | Nome da coluna de exibição do dado financeiro (ex: 'Previsão Atualizada'). |
| `NUM_NIVE` | STRING | Nível hierárquico do item na estrutura de classificação do relatório. |
| `NUM_ORDE` | STRING | Número de ordem para ordenação do item no relatório. |
| `VAL_DECL` | STRING | Valor financeiro declarado para o item em reais. |
| `record_index` | INTEGER | Índice sequencial único do registro dentro da carga de dados. |
| `page_number` | INTEGER | Número da página da API de origem de onde o registro foi extraído. |
| `source_endpoint` | STRING | Nome do endpoint ou tabela de origem na API do SIOPE (ex: 'Receita_Siope'). |
| `request_url` | STRING | URL da requisição feita à API de origem para obtenção do dado. |
| `http_status` | INTEGER | Código de status HTTP retornado pela API de origem na extração. |
| `response_hash` | STRING | Hash de controle de integridade do payload de resposta da API. |
| `schema_fingerprint` | STRING | Assinatura digital do esquema de dados para controle de versionamento. |
| `record_count` | INTEGER | Quantidade de registros retornados na página da requisição HTTP. — descrição gerada por IA. |
| `ano` | INTEGER | Ano de referência utilizado como partição ou filtro na extração. |
| `periodo` | INTEGER | Período de referência utilizado como parâmetro na extração dos dados. |
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `mes_exercicio` | INTEGER | Mês de exercício de referência do dado financeiro. |
| `cod_muni_filtro` | STRING | Código do município utilizado como parâmetro de filtro na requisição de origem. |
| `dt_ingestao_lake` | STRING | Data e hora ISO-8601 da ingestão do registro no Data Lake. — descrição gerada por IA. |

## raw · api_olinda_siope_remuneracao

File `raw__api_olinda_siope_remuneracao.parquet` · 68,046,053 rows · 28 columns

Tabela com dados de remuneração de profissionais da educação básica pública, extraídos do SIOPE (Sistema de Informações sobre Orçamentos Públicos em Educação), detalhando salários, carga horária e fontes de recursos (FUNDEB).

| Column | Type | Description |
|---|---|---|
| `TIPO` | STRING | Tipo de dependência administrativa da rede de ensino (ex: Municipal). |
| `AN_DECLARACAO` | STRING | Ano de referência da declaração ao SIOPE (formato YYYY). |
| `NU_PERIODO` | STRING | Número do período de referência declarado. |
| `ME_EXERCICIO` | STRING | Mês de exercício da atividade profissional (1 a 12). |
| `COD_UF` | STRING | Código IBGE de 2 dígitos da Unidade da Federação. |
| `SIG_UF` | STRING | Sigla da Unidade da Federação (ex: MA, SP). |
| `COD_MUNI` | STRING | Código IBGE de 6 dígitos do município. |
| `NOM_MUNI` | STRING | Nome do município correspondente. |
| `NO_PROFISSIONAL` | STRING | Nome completo do profissional da educação. |
| `CO_ESCOLA` | STRING | Código identificador único da escola no INEP. |
| `NO_RAZAO_SOCIAL` | STRING | Razão social ou nome da escola/entidade de atuação. |
| `NO_CATEGORIA_PROFISSIONAL` | STRING | Nome detalhado da categoria profissional ou cargo exercido. |
| `DS_SITUACAO_PROFISSIONAL` | STRING | Descrição da situação funcional ou vínculo empregatício do profissional. |
| `TP_CATEGORIA` | STRING | Tipo geral da categoria do profissional (ex: Profissionais do magistério). |
| `NU_CARGA_HORARIA` | STRING | Carga horária contratual do profissional. |
| `VL_SALARIO` | STRING | Valor do salário bruto pago ao profissional. |
| `VL_MINIMO_FUNDEB` | STRING | Valor mínimo pago ao profissional com recursos do FUNDEB. |
| `VL_MAXIMO_FUNDEB` | STRING | Valor máximo pago ao profissional com recursos do FUNDEB. |
| `VL_OUTROS` | STRING | Outros valores remuneratórios pagos que não provêm do FUNDEB. |
| `record_index` | INTEGER | Índice sequencial do registro dentro do lote importado. |
| `page_number` | INTEGER | Número da página de paginação da API de origem. |
| `source_endpoint` | STRING | Nome do endpoint ou serviço de origem dos dados (ex: Remuneracao_Siope). |
| `response_hash` | STRING | Hash de controle de integridade da resposta da API. |
| `ano` | INTEGER | Ano de referência utilizado para particionamento ou filtro no data lake. |
| `periodo` | INTEGER | Período de referência utilizado como filtro ou partição. |
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `mes_exercicio` | INTEGER | Mês de exercício utilizado como filtro ou partição. |
| `dt_ingestao_lake` | STRING | Data e hora em que o registro foi ingerido no Data Lake (formato ISO 8601). — descrição gerada por IA. |

## raw · api_olinda_siope_responsaveis

File `raw__api_olinda_siope_responsaveis.parquet` · 1,732,317 rows · 49 columns

**Feeds:** `trusted/api_olinda_siope_responsaveis`

| Column | Type | Description |
|---|---|---|
| `TIPO` | STRING |  |
| `NUM_ANO` | STRING |  |
| `NUM_PERI` | STRING |  |
| `COD_UF` | STRING |  |
| `SIG_UF` | STRING |  |
| `COD_MUNI` | STRING |  |
| `NOM_MUNI` | STRING |  |
| `NUM_POPU` | STRING |  |
| `NUM_FPM` | STRING |  |
| `NUM_ITR` | STRING |  |
| `NUM_LC` | STRING |  |
| `NUM_FUNDEF` | STRING |  |
| `NUM_CP_FUNDEF` | STRING |  |
| `NUM_ICMS` | STRING |  |
| `NUM_CIDE` | STRING |  |
| `NUM_IPI_EXPO` | STRING |  |
| `NUM_IPVA_FUNDEB` | STRING |  |
| `NUM_ITCMD_FUNDEB` | STRING |  |
| `NUM_FPE` | STRING |  |
| `VAL_PIB` | STRING |  |
| `VAL_PIB_PERCAPTO` | STRING |  |
| `NUM_RECI` | STRING |  |
| `DAT_DECL` | STRING |  |
| `NOM_RESP` | STRING |  |
| `DES_EMAI` | STRING |  |
| `NUM_TELE` | STRING |  |
| `NUM_CNPJ` | STRING |  |
| `TIP_RESP` | STRING |  |
| `DES_ENDR` | STRING |  |
| `END_NUMR` | STRING |  |
| `END_COMP` | STRING |  |
| `DES_BAIR` | STRING |  |
| `NUM_CEP` | STRING |  |
| `CO_MUNICIPIO_RESID` | STRING |  |
| `CO_UF_RESID` | STRING |  |
| `record_index` | INTEGER |  |
| `page_number` | INTEGER |  |
| `source_endpoint` | STRING |  |
| `request_url` | STRING |  |
| `http_status` | INTEGER |  |
| `response_hash` | STRING |  |
| `schema_fingerprint` | STRING |  |
| `record_count` | INTEGER |  |
| `ano` | INTEGER |  |
| `periodo` | INTEGER |  |
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `mes_exercicio` | INTEGER |  |
| `cod_muni_filtro` | STRING |  |
| `dt_ingestao_lake` | STRING |  |

## raw · fnde_siope_dados_gerais

File `raw__fnde_siope_dados_gerais.parquet` · 166,452 rows · 53 columns

SIOPE - Dados gerais do ente: receita, despesa total, indicadores fiscais. Grao: ente x ano x periodo. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE) -- ver dados.gov.br/dados/conjuntos-dados/sistema-de-informacoes-sobre-orcamentos-publicos-em-educacao-siope. Prefixo fnde_ do pipeline (fnde_siope_raw/trusted/semantic) identifica essa origem (NAO e PDF/scraping). Havera futuramente uma 2a origem distinta, SIOPE RREO (dados extraidos de PDFs de Relatorios Resumidos de Execucao Orcamentaria enviados pelas prefeituras), pipeline/tabelas proprias ainda nao implementados.

**Feeds:** `trusted/fnde_siope_dados_gerais`

| Column | Type | Description |
|---|---|---|
| `tipo` | STRING | Tipo de ente federativo declarante (ex: Estadual, Municipal). |
| `num_ano` | STRING | Ano de referência da declaração financeira (formato YYYY). |
| `num_peri` | STRING | Período ou bimestre de referência do relatório orçamentário. |
| `cod_uf` | STRING | Código IBGE identificador da Unidade da Federação. |
| `sig_uf` | STRING | Sigla da Unidade da Federação. |
| `cod_muni` | STRING | Código IBGE identificador do município. |
| `nom_muni` | STRING | Nome do município declarante. |
| `num_popu` | STRING | População estimada do município ou estado. |
| `num_fpm` | STRING | Valor recebido do Fundo de Participação dos Municípios (FPM). |
| `num_itr` | STRING | Valor arrecadado do Imposto Territorial Rural (ITR). |
| `num_lc` | STRING | Data de referência ou número de controle da Lei Complementar. |
| `num_fundef` | STRING | Valor de recursos recebidos do antigo FUNDEF. |
| `num_cp_fundef` | STRING | Valor da complementação da União ao FUNDEF. |
| `num_icms` | STRING | Valor arrecadado ou recebido referente ao ICMS. |
| `num_cide` | STRING | Valor recebido da Contribuição de Intervenção no Domínio Econômico (CIDE). |
| `num_ipi_expo` | STRING | Valor recebido de IPI proporcional às exportações. |
| `num_ipva_fundeb` | STRING | Valor de IPVA destinado à composição do FUNDEB. |
| `num_itcmd_fundeb` | STRING | Valor de ITCMD destinado à composição do FUNDEB. |
| `num_fpe` | STRING | Valor recebido do Fundo de Participação dos Estados (FPE). |
| `val_pib` | STRING | Valor do Produto Interno Bruto (PIB) do ente federativo. |
| `val_pib_percapto` | STRING | Valor do PIB per capita do ente federativo. |
| `num_reci` | STRING | Número do recibo de entrega da declaração. |
| `dat_decl` | STRING | Data de transmissão ou assinatura da declaração financeira. |
| `val_rece_prev_atua` | STRING | Valor da receita prevista atualizada para o exercício. |
| `val_rece_real` | STRING | Valor da receita efetivamente realizada. |
| `val_rece_orca` | STRING | Valor da receita inicialmente orçada. |
| `val_desp_dota_atua` | STRING | Valor total da dotação atualizada para despesas gerais. |
| `val_desp_empe` | STRING | Valor total das despesas gerais empenhadas. |
| `val_desp_liqu` | STRING | Valor total das despesas gerais liquidadas. |
| `val_desp_paga` | STRING | Valor total das despesas gerais pagas. |
| `val_desp_orca` | STRING | Valor total das despesas gerais orçadas. |
| `idn_assu_resp_mtdo_apur` | STRING | Indicador de assunção de responsabilidade pelo método de apuração adotado. |
| `idn_meto_limi_cons` | STRING | Indicador de metodologia utilizada para cálculo do limite constitucional. |
| `idn_decl_reti` | STRING | Indicador se a declaração é retificadora. |
| `idn_tipo_decl` | STRING | Identificador do tipo de declaração enviada. |
| `des_just_prob_bala` | STRING | Descrição de justificativa para eventuais inconsistências ou problemas no balanço. |
| `idn_meto_siope_igua_tc` | STRING | Indicador se a metodologia do SIOPE é idêntica à do Tribunal de Contas local. |
| `idn_poss_cert_tc` | STRING | Indicador de posse de certidão de regularidade emitida pelo Tribunal de Contas. |
| `idn_poss_deci_judi` | STRING | Indicador de existência de decisão judicial ativa sobre a prestação de contas. |
| `des_dife_meto_calc` | STRING | Descrição das diferenças encontradas nas metodologias de cálculo de limites. |
| `num_soli` | STRING | Número de protocolo da solicitação ou processo administrativo. |
| `ds_just_retificacao` | STRING | Descrição da justificativa para a retificação da declaração. |
| `cod_digit` | STRING | Código de controle de digitação do documento. |
| `cod_verific` | STRING | Código de verificação de autenticidade da declaração. |
| `val_transmissao` | STRING | Valor ou status associado à transmissão dos dados. |
| `vl_desp_dota_atua_edu` | STRING | Valor da dotação atualizada destinada especificamente à educação. |
| `vl_desp_empe_edu` | STRING | Valor das despesas empenhadas especificamente em educação. |
| `vl_desp_liqu_edu` | STRING | Valor das despesas liquidadas especificamente em educação. |
| `vl_desp_paga_edu` | STRING | Valor das despesas pagas especificamente em educação. |
| `vl_desp_orca_edu` | STRING | Valor das despesas orçadas especificamente para a educação. |
| `ds_nota_rodape_rreo` | STRING | Texto de nota de rodapé do Relatório Resumido da Execução Orçamentária (RREO). |
| `ds_nota_rodape_fundeb` | STRING | Texto de nota de rodapé específico sobre os recursos do FUNDEB. |
| `dt_ingestao_lake` | STRING | Data e hora do registro da ingestão dos dados no Data Lake (ISO 8601). — descrição gerada por IA. |

## raw · fnde_siope_despesa_total_educacao

File `raw__fnde_siope_despesa_total_educacao.parquet` · 139,046,717 rows · 21 columns

SIOPE - Despesa total em educacao por ente. Grao: ente x ano x periodo. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE) -- ver dados.gov.br/dados/conjuntos-dados/sistema-de-informacoes-sobre-orcamentos-publicos-em-educacao-siope. Prefixo fnde_ do pipeline (fnde_siope_raw/trusted/semantic) identifica essa origem (NAO e PDF/scraping). Havera futuramente uma 2a origem distinta, SIOPE RREO (dados extraidos de PDFs de Relatorios Resumidos de Execucao Orcamentaria enviados pelas prefeituras), pipeline/tabelas proprias ainda nao implementados.

**Feeds:** `trusted/fnde_siope_despesa_total_educacao`

| Column | Type | Description |
|---|---|---|
| `tipo` | STRING | Tipo de administração pública responsável pela despesa (ex: Municipal, Estadual). |
| `num_ano` | STRING | Ano de referência do exercício financeiro (formato AAAA). |
| `num_peri` | STRING | Número do período ou bimestre de referência dentro do ano fiscal. |
| `cod_uf` | STRING | Código IBGE de dois dígitos que identifica a Unidade da Federação. |
| `sig_uf` | STRING | Sigla de duas letras da Unidade da Federação (UF). |
| `cod_muni` | STRING | Código IBGE identificador do município (com sufixo decimal). |
| `nom_muni` | STRING | Nome oficial do município. |
| `nom_past` | STRING | Nome da pasta, área temática ou subfunção de aplicação do recurso (ex: Merenda Escolar). |
| `idn_exib_codi` | STRING | Indicador de exibição do código da despesa (S para Sim, N para Não). |
| `cod_past` | STRING | Código identificador da pasta ou área de aplicação orçamentária. |
| `cod_subf` | STRING | Código da subfunção orçamentária da educação (ex: 361 para Ensino Fundamental). |
| `tip_pasta` | STRING | Tipo de classificação da pasta de recursos (ex: VINCULADAS). |
| `cod_exib` | STRING | Código de classificação da natureza da despesa orçamentária. |
| `cod_exib_formatado` | STRING | Código de classificação da despesa em formato padronizado para exibição. |
| `cod_fonte` | STRING | Código identificador da fonte de recursos financeiros utilizada. |
| `nom_item` | STRING | Nome do item ou elemento de despesa orçamentária (ex: Gêneros de Alimentação). |
| `idn_clas` | STRING | Sigla identificadora do tipo de classificação do valor (ex: DA para Dotação Atualizada, DL para Despesa Liquidada). |
| `nom_colu` | STRING | Nome descritivo da coluna de estágio da despesa (ex: Dotação Atualizada, Desp. Empenhadas). |
| `num_nive` | STRING | Nível hierárquico do item de despesa na estrutura orçamentária (0 para consolidado, níveis maiores para detalhamentos). |
| `num_orde` | STRING | Número de ordenação sequencial para exibição dos itens em relatórios. |
| `val_decl` | STRING | Valor financeiro declarado em reais (BRL) para a respectiva despesa. |

## raw · fnde_siope_despesas_funcao_educacao

File `raw__fnde_siope_despesas_funcao_educacao.parquet` · 1,199,526 rows · 12 columns

SIOPE - Despesas por subfuncao de educacao (EF, EI, EM, EJA, Especial). Grao: ente x ano x periodo x subfuncao. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE) -- ver dados.gov.br/dados/conjuntos-dados/sistema-de-informacoes-sobre-orcamentos-publicos-em-educacao-siope. Prefixo fnde_ do pipeline (fnde_siope_raw/trusted/semantic) identifica essa origem (NAO e PDF/scraping). Havera futuramente uma 2a origem distinta, SIOPE RREO (dados extraidos de PDFs de Relatorios Resumidos de Execucao Orcamentaria enviados pelas prefeituras), pipeline/tabelas proprias ainda nao implementados.

**Feeds:** `trusted/fnde_siope_despesas_funcao_educacao`

| Column | Type | Description |
|---|---|---|
| `tipo` | STRING | Tipo de dependência administrativa responsável pela despesa (ex: Estadual, Municipal). |
| `num_ano` | STRING | Ano de referência do exercício financeiro (formato AAAA). |
| `num_peri` | STRING | Período de apuração dos dados financeiros (ex: bimestre). |
| `cod_uf` | STRING | Código IBGE da Unidade da Federação. |
| `sig_uf` | STRING | Sigla da Unidade da Federação (ex: DF). |
| `cod_muni` | STRING | Código identificador do município ou do registro na base de origem. |
| `nom_muni` | STRING | Código e nome da subfunção orçamentária da educação (ex: Ensino Fundamental), apesar do nome da coluna indicar município. |
| `num_orde` | STRING | Valor de dotação inicial ou limite orçamentário autorizado para a despesa. |
| `des_subf` | STRING | Valor de dotação atualizada ou limite de despesa para a subfunção específica. |
| `val_desp_empe` | STRING | Valor total da despesa empenhada (reservada para pagamento) no período, em reais. |
| `val_desp_liqu` | STRING | Valor total da despesa liquidada (comprovada a entrega do bem/serviço) no período, em reais. |
| `val_desp_paga` | STRING | Valor total da despesa efetivamente paga no período, em reais. |

## raw · fnde_siope_indicadores

File `raw__fnde_siope_indicadores.parquet` · 6,441,160 rows · 14 columns

SIOPE - Indicadores de cumprimento do MDE e FUNDEB. Grao: ente x ano x periodo x grupo de indicador. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE) -- ver dados.gov.br/dados/conjuntos-dados/sistema-de-informacoes-sobre-orcamentos-publicos-em-educacao-siope. Prefixo fnde_ do pipeline (fnde_siope_raw/trusted/semantic) identifica essa origem (NAO e PDF/scraping). Havera futuramente uma 2a origem distinta, SIOPE RREO (dados extraidos de PDFs de Relatorios Resumidos de Execucao Orcamentaria enviados pelas prefeituras), pipeline/tabelas proprias ainda nao implementados.

**Feeds:** `trusted/fnde_siope_indicadores`

| Column | Type | Description |
|---|---|---|
| `tipo` | STRING | Tipo de abrangência geográfica ou administrativa do registro (ex: Municipal, Estadual). |
| `num_ano` | STRING | Ano de referência da apuração do indicador (formato YYYY). |
| `num_peri` | STRING | Período ou ciclo de apuração do indicador dentro do ano (ex: quadrimestre, semestre). |
| `cod_uf` | STRING | Código IBGE identificador do estado (UF). |
| `sig_uf` | STRING | Sigla da Unidade Federativa (UF) com duas letras. |
| `cod_muni` | STRING | Código IBGE identificador do município. |
| `nom_muni` | STRING | Nome oficial do município correspondente. |
| `cod_indi` | STRING | Código identificador único do indicador. |
| `cod_exib` | STRING | Código de ordenação ou exibição do indicador em relatórios e painéis (ex: 1.1). |
| `nom_indi` | STRING | Nome descritivo do indicador (ex: percentual de aplicação de receitas em MDE). |
| `cod_grup` | STRING | Código identificador do grupo de indicadores. |
| `nom_grup_indi` | STRING | Nome do grupo temático ao qual o indicador pertence (ex: Indicadores de Dispêndio com Pessoal). |
| `val_indi` | STRING | Valor numérico calculado para o indicador no período e localidade especificados. |
| `dt_atualizacao` | STRING | Data e hora da última atualização do registro no data lake (timestamp). — descrição gerada por IA. |

## raw · fnde_siope_informacoes_complementares

File `raw__fnde_siope_informacoes_complementares.parquet` · 8,378,339 rows · 9 columns

SIOPE - Informacoes complementares declaradas pelo ente. Grao: ente x ano x periodo. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE) -- ver dados.gov.br/dados/conjuntos-dados/sistema-de-informacoes-sobre-orcamentos-publicos-em-educacao-siope. Prefixo fnde_ do pipeline (fnde_siope_raw/trusted/semantic) identifica essa origem (NAO e PDF/scraping). Havera futuramente uma 2a origem distinta, SIOPE RREO (dados extraidos de PDFs de Relatorios Resumidos de Execucao Orcamentaria enviados pelas prefeituras), pipeline/tabelas proprias ainda nao implementados.

**Feeds:** `trusted/fnde_siope_informacoes_complementares`

| Column | Type | Description |
|---|---|---|
| `num_ano` | STRING | Ano de referência da declaração financeira (formato YYYY). |
| `num_peri` | STRING | Número do período de referência do relatório (ex: bimestre ou semestre). |
| `cod_uf` | STRING | Código numérico do IBGE correspondente ao Estado (UF). |
| `sig_uf` | STRING | Sigla da Unidade da Federação (UF). |
| `cod_muni` | STRING | Código de identificação do município. |
| `nom_muni` | STRING | Nome do município (pode conter a descrição da despesa declarada devido à estrutura de origem). |
| `cod_exib` | STRING | Código identificador da rubrica, conta ou item de exibição no relatório financeiro. |
| `nom_item` | STRING | Nome ou descrição detalhada do item ou despesa declarada. |
| `val_decl` | STRING | Valor monetário declarado para a respectiva rubrica ou despesa. |

## raw · fnde_siope_receita_total

File `raw__fnde_siope_receita_total.parquet` · 14,311,287 rows · 13 columns

SIOPE - Receita total do ente. Grao: ente x ano x periodo. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE) -- ver dados.gov.br/dados/conjuntos-dados/sistema-de-informacoes-sobre-orcamentos-publicos-em-educacao-siope. Prefixo fnde_ do pipeline (fnde_siope_raw/trusted/semantic) identifica essa origem (NAO e PDF/scraping). Havera futuramente uma 2a origem distinta, SIOPE RREO (dados extraidos de PDFs de Relatorios Resumidos de Execucao Orcamentaria enviados pelas prefeituras), pipeline/tabelas proprias ainda nao implementados.

**Feeds:** `trusted/fnde_siope_receita_total`

| Column | Type | Description |
|---|---|---|
| `an_exercicio` | STRING | Ano de referência do exercício financeiro (formato YYYY). |
| `tp_periodo` | STRING | Tipo de período do balanço financeiro (ex: ANUAL). |
| `nu_periodo` | STRING | Número do período correspondente ao tipo de período informado. |
| `co_uf` | STRING | Código IBGE de duas posições da Unidade da Federação. |
| `no_uf` | STRING | Nome por extenso da Unidade da Federação. |
| `co_municipio` | STRING | Código IBGE de seis dígitos identificador do município. |
| `no_municipio` | STRING | Nome do município correspondente. |
| `no_esfera_adm` | STRING | Esfera administrativa responsável pela gestão do recurso (ex: MUNICIPAL). |
| `co_conta_contabil` | STRING | Código identificador da conta contábil da receita. |
| `no_conta_contabil` | STRING | Descrição da conta contábil ou origem da receita. |
| `vl_receita_previsao_atualizada` | STRING | Valor atualizado da previsão de arrecadação da receita em reais. |
| `vl_receita_realizadas` | STRING | Valor efetivamente arrecadado (realizado) da receita em reais. |
| `vl_receita_orcada` | STRING | Valor inicialmente estimado (orçado) para a receita em reais. |

## raw · rreo_siope_data

File `raw__rreo_siope_data.parquet` · 259 rows · 10 columns

Tabela que armazena dados extraídos dos Relatórios Resumidos da Execução Orçamentária (RREO) do SIOPE, detalhando receitas e despesas com educação pública por estado ou município.

| Column | Type | Description |
|---|---|---|
| `arquivo` | STRING | Nome do arquivo PDF original do relatório RREO obtido do SIOPE. |
| `tipo_entidade` | STRING | Tipo de ente federativo analisado, indicando se é estadual ('uf') ou municipal. |
| `codigo_ibge` | INTEGER | Código IBGE de 7 dígitos do município (preenchido apenas para entidades municipais). |
| `co_uf` | INTEGER | Código IBGE de 2 dígitos correspondente à Unidade da Federação. |
| `sg_uf` | STRING | Sigla da Unidade da Federação (ex: RO, AC, AM). |
| `ano` | INTEGER | Ano de referência do relatório orçamentário (formato YYYY). |
| `bimestre` | INTEGER | Bimestre de referência do relatório (valores de 1 a 6). |
| `dados_json` | STRING | Dados estruturados em formato JSON contendo metadados e tabelas financeiras extraídas do PDF (ex: receitas de impostos e FUNDEB). |
| `data_extracao` | TIMESTAMP | Data e hora de extração e processamento do relatório (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |
| `ftp_size` | INTEGER | Tamanho do arquivo PDF original em bytes obtido do servidor FTP de origem. |
