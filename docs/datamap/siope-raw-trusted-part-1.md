# SIOPE education finance: Raw and Trusted

Dataset: [lucasrangelss/siope-raw-trusted-part-1](https://www.kaggle.com/datasets/lucasrangelss/siope-raw-trusted-part-1) · snapshot 2026-10-01 · 2 tables · 721,981,186 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/siope/](https://www.fnde.gov.br/siope/)

Education revenue, expenditure and indicators reported by municipalities and states, from the SIOPE open-data API (Olinda), the FNDE SIOPE exports, and the budget execution report (RREO) PDFs parsed into tables.

**Grain and keys:** Municipality (or state) by year and reporting period. Indicator rows repeat by `num_periodo`, so analyses keep the latest period per municipality and year. Municipality joins to IBGE through `codigo_municipio`.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://lucas.rangeltech.net/datamap/](https://lucas.rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`api_olinda_siope_dados_gerais`](#raw-api-olinda-siope-dados-gerais) | 742,142 | 66 | 66 | source |
| raw | [`api_olinda_siope_despesas`](#raw-api-olinda-siope-despesas) | 721,239,044 | 35 | 35 | source |

## raw · api_olinda_siope_dados_gerais

File `raw__api_olinda_siope_dados_gerais.parquet` · 742,142 rows · 66 columns

Dados Gerais do SIOPE (Sistema de Informações sobre Orçamentos Públicos em Educação), contendo informações detalhadas de receitas, despesas gerais e de educação, transferências constitucionais e metadados de declaração de estados e municípios.

**Feeds:** `trusted/api_olinda_siope_dados_gerais`

| Column | Type | Description |
|---|---|---|
| `TIPO` | STRING | Tipo de ente federativo declarante (ex: Municipal, Estadual). |
| `NUM_ANO` | STRING | Ano de referência dos dados financeiros declarados. |
| `NUM_PERI` | STRING | Período de referência da declaração (ex: bimestre ou semestre). |
| `COD_UF` | STRING | Código IBGE da Unidade da Federação. |
| `SIG_UF` | STRING | Sigla da Unidade da Federação. |
| `COD_MUNI` | STRING | Código IBGE do município (6 dígitos). |
| `NOM_MUNI` | STRING | Nome oficial do município. |
| `NUM_POPU` | STRING | População estimada ou oficial do município. |
| `NUM_FPM` | STRING | Valor recebido do Fundo de Participação dos Municípios (FPM) no período. |
| `NUM_ITR` | STRING | Valor arrecadado do Imposto Territorial Rural (ITR). |
| `NUM_LC` | STRING | Valor recebido por transferências de Leis Complementares (ex: Lei Kandir). |
| `NUM_FUNDEF` | STRING | Valor de recursos recebidos ou retidos do antigo FUNDEF. |
| `NUM_CP_FUNDEF` | STRING | Valor da complementação da União ao FUNDEF. |
| `NUM_ICMS` | STRING | Valor arrecadado ou recebido de ICMS. |
| `NUM_CIDE` | STRING | Valor recebido da Contribuição de Intervenção no Domínio Econômico (CIDE). |
| `NUM_IPI_EXPO` | STRING | Valor recebido de IPI proporcional às exportações. |
| `NUM_IPVA_FUNDEB` | STRING | Valor de IPVA destinado à composição do FUNDEB. |
| `NUM_ITCMD_FUNDEB` | STRING | Valor de ITCMD destinado à composição do FUNDEB. |
| `NUM_FPE` | STRING | Valor recebido do Fundo de Participação dos Estados (FPE). |
| `VAL_PIB` | STRING | Valor do Produto Interno Bruto (PIB) do município. |
| `VAL_PIB_PERCAPTO` | STRING | Valor do PIB per capita do município. |
| `NUM_RECI` | STRING | Número do recibo de entrega da declaração ao SIOPE. |
| `DAT_DECL` | STRING | Data de transmissão da declaração ao SIOPE (formato AAAA-MM-DD). |
| `VAL_RECE_PREV_ATUA` | STRING | Valor total da receita prevista atualizada do ente. |
| `VAL_RECE_REAL` | STRING | Valor total da receita realizada (arrecadada) no período. |
| `VAL_RECE_ORCA` | STRING | Valor total da receita estimada na Lei Orçamentária Anual (LOA). |
| `VAL_DESP_DOTA_ATUA` | STRING | Valor total da despesa com dotação atualizada. |
| `VAL_DESP_EMPE` | STRING | Valor total de despesas empenhadas pelo ente. |
| `VAL_DESP_LIQU` | STRING | Valor total de despesas liquidadas pelo ente. |
| `VAL_DESP_PAGA` | STRING | Valor total de despesas efetivamente pagas. |
| `VAL_DESP_ORCA` | STRING | Valor total da despesa fixada na Lei Orçamentária Anual (LOA). |
| `IDN_ASSU_RESP_MTDO_APUR` | STRING | Indicador de assunção de responsabilidade pelo método de apuração adotado. |
| `IDN_METO_LIMI_CONS` | STRING | Indicador da metodologia utilizada para cálculo do limite constitucional. |
| `IDN_DECL_RETI` | STRING | Indicador se a declaração atual é retificadora. |
| `IDN_TIPO_DECL` | STRING | Código identificador do tipo de declaração enviada. |
| `DES_JUST_PROB_BALA` | STRING | Descrição ou justificativa de inconsistências encontradas no balanço. |
| `IDN_METO_SIOPE_IGUA_TC` | STRING | Indicador se a metodologia do SIOPE é idêntica à do Tribunal de Contas local. |
| `IDN_POSS_CERT_TC` | STRING | Indicador de posse de certidão de regularidade emitida pelo Tribunal de Contas. |
| `IDN_POSS_DECI_JUDI` | STRING | Indicador de existência de decisão judicial liminar ativa. |
| `DES_DIFE_METO_CALC` | STRING | Descrição detalhada das diferenças de metodologia de cálculo aplicadas. |
| `NUM_SOLI` | STRING | Número de solicitação de suporte ou alteração cadastral. |
| `DS_JUST_RETIFICACAO` | STRING | Texto descritivo com a justificativa para a retificação da declaração. |
| `COD_DIGIT` | STRING | Código de controle de digitação do sistema. |
| `COD_VERIFIC` | STRING | Código verificador de autenticidade do documento transmitido. |
| `VAL_TRANSMISSAO` | STRING | Valor ou código de validação associado à transmissão dos dados. |
| `VL_DESP_DOTA_ATUA_EDU` | STRING | Valor da dotação atualizada destinada especificamente à Educação. |
| `VL_DESP_EMPE_EDU` | STRING | Valor das despesas empenhadas especificamente em Educação. |
| `VL_DESP_LIQU_EDU` | STRING | Valor das despesas liquidadas especificamente em Educação. |
| `VL_DESP_PAGA_EDU` | STRING | Valor das despesas pagas especificamente em Educação. |
| `VL_DESP_ORCA_EDU` | STRING | Valor orçado inicialmente na LOA para a área de Educação. |
| `DS_NOTA_RODAPE_RREO` | STRING | Texto de nota de rodapé do Relatório Resumido da Execução Orçamentária (RREO). |
| `DS_NOTA_RODAPE_FUNDEB` | STRING | Texto de nota de rodapé referente aos demonstrativos do FUNDEB. |
| `record_index` | INTEGER | Índice sequencial do registro dentro do lote de extração. |
| `page_number` | INTEGER | Número da página da API de origem de onde o dado foi extraído. |
| `source_endpoint` | STRING | Nome do endpoint da API de origem (ex: Dados_Gerais_Siope). |
| `request_url` | STRING | URL completa utilizada na requisição de extração. |
| `http_status` | INTEGER | Código de status HTTP retornado pela API de origem (ex: 200). |
| `response_hash` | STRING | Hash de controle de integridade do conteúdo da resposta da API. |
| `schema_fingerprint` | STRING | Identificador único da versão do esquema de dados. |
| `record_count` | INTEGER | Quantidade total de registros presentes no lote retornado. — descrição gerada por IA. |
| `ano` | INTEGER | Ano de referência utilizado como partição/filtro no data lake. |
| `periodo` | INTEGER | Período de referência utilizado como partição/filtro no data lake. |
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `mes_exercicio` | INTEGER | Mês de exercício de referência para filtros adicionais. |
| `cod_muni_filtro` | STRING | Código do município utilizado como parâmetro de filtro na extração. |
| `dt_ingestao_lake` | STRING | Data e hora no formato ISO 8601 em que o registro foi armazenado no Data Lake. — descrição gerada por IA. |

## raw · api_olinda_siope_despesas

File `raw__api_olinda_siope_despesas.parquet` · 721,239,044 rows · 35 columns

Dados de despesas declaradas no SIOPE (Sistema de Informações sobre Orçamentos Públicos em Educação) por municípios, detalhando dotações, liquidações e pagamentos na educação básica.

**Feeds:** `trusted/api_olinda_siope_despesas`

| Column | Type | Description |
|---|---|---|
| `TIPO` | STRING | Tipo de administração pública declarante (ex: Municipal). |
| `NUM_ANO` | STRING | Ano de referência do exercício financeiro declarado. |
| `NUM_PERI` | STRING | Número do período (geralmente bimestre) de referência do dado. |
| `COD_UF` | STRING | Código numérico do estado (UF) segundo o IBGE. |
| `SIG_UF` | STRING | Sigla da Unidade da Federação (estado). |
| `COD_MUNI` | STRING | Código IBGE de 6 dígitos identificador do município. |
| `NOM_MUNI` | STRING | Nome do município declarante. |
| `NOM_PAST` | STRING | Nome da pasta ou nível de ensino associado à despesa (ex: Ensino Fundamental). |
| `IDN_EXIB_CODI` | STRING | Indicador de exibição de código no relatório do SIOPE. |
| `COD_PAST` | STRING | Código identificador da pasta ou subcategoria de ensino no SIOPE. |
| `COD_SUBF` | STRING | Código da subfunção orçamentária associada à despesa. |
| `TIP_PASTA` | STRING | Tipo de classificação da pasta de despesa (ex: VINCULADAS). |
| `COD_EXIB` | STRING | Código identificador do item de despesa ou elemento orçamentário sem formatação. |
| `COD_EXIB_FORMATADO` | STRING | Código do item de despesa formatado com separadores (ex: 3,33,90,30,39,00). |
| `COD_FONTE` | STRING | Código da fonte de recursos utilizada para o financiamento da despesa. |
| `NOM_ITEM` | STRING | Descrição do item de despesa ou elemento orçamentário (ex: Material de Consumo). |
| `IDN_CLAS` | STRING | Sigla identificadora do tipo de classificação do valor (ex: DL para Despesas Liquidadas, DP para Pagas, DA para Dotação Atualizada). |
| `NOM_COLU` | STRING | Nome da coluna de classificação do valor no relatório (ex: Desp. Liquidadas, Dotação Atualizada). |
| `NUM_NIVE` | STRING | Nível hierárquico do item na estrutura do plano de contas orçamentário. |
| `NUM_ORDE` | STRING | Número de ordenação do item no relatório do SIOPE. |
| `VAL_DECL` | STRING | Valor monetário declarado para o item de despesa (em Reais). |
| `record_index` | INTEGER | Índice sequencial do registro dentro do lote de ingestão. |
| `page_number` | INTEGER | Número da página da API de origem de onde o registro foi extraído. |
| `source_endpoint` | STRING | Nome do endpoint ou tabela de origem na API do SIOPE. |
| `request_url` | STRING | URL da requisição de API utilizada para obter o dado. |
| `http_status` | INTEGER | Código de status HTTP retornado pela API de origem durante a extração. |
| `response_hash` | STRING | Hash da resposta da API para controle de integridade e duplicidade. |
| `schema_fingerprint` | STRING | Identificador único da versão do esquema de dados (schema) no momento da ingestão. |
| `record_count` | INTEGER | Quantidade total de registros retornados na página da requisição. — descrição gerada por IA. |
| `ano` | INTEGER | Ano de referência utilizado para partição ou filtro de extração. |
| `periodo` | INTEGER | Período de referência (bimestre/semestre) utilizado como filtro na extração. |
| `uf` | STRING | Sigla da unidade da federação onde se encontra o estabelecimento. |
| `mes_exercicio` | INTEGER | Mês de referência do exercício financeiro, quando aplicável. |
| `cod_muni_filtro` | STRING | Código do município utilizado como parâmetro de filtro na requisição da API. |
| `dt_ingestao_lake` | STRING | Data e hora no formato ISO 8601 da ingestão do registro no Data Lake. — descrição gerada por IA. |
