# SIOPE education finance: Raw and Trusted

Dataset: [lucasrangelss/siope-raw-trusted-part-3](https://www.kaggle.com/datasets/lucasrangelss/siope-raw-trusted-part-3) · snapshot 2026-10-02 · 8 tables · 338,460,104 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/siope/](https://www.fnde.gov.br/siope/)

Education revenue, expenditure and indicators reported by municipalities and states, from the SIOPE open-data API (Olinda), the FNDE SIOPE exports, and the budget execution report (RREO) PDFs parsed into tables.

**Grain and keys:** Municipality (or state) by year and reporting period. Indicator rows repeat by `num_periodo`, so analyses keep the latest period per municipality and year. Municipality joins to IBGE through `codigo_municipio`.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`rreo_siope_municipio`](#raw-rreo-siope-municipio) | 354,781 | 9 | 9 | source |
| raw | [`rreo_siope_uf`](#raw-rreo-siope-uf) | 1,687 | 10 | 10 | source |
| raw | [`siope_data`](#raw-siope-data) | 190,229 | 6 | 6 | source |
| trusted | [`api_olinda_siope_dados_gerais`](#trusted-api-olinda-siope-dados-gerais) | 384,692 | 63 | 63 | `api_olinda_siope_dados_gerais` |
| trusted | [`api_olinda_siope_despesas`](#trusted-api-olinda-siope-despesas) | 305,518,954 | 32 | 32 | `api_olinda_siope_despesas` |
| trusted | [`api_olinda_siope_despesas_funcao_educacao`](#trusted-api-olinda-siope-despesas-funcao-educacao) | 3,060,708 | 23 | 23 | `api_olinda_siope_despesas_funcao_educacao` |
| trusted | [`api_olinda_siope_indicadores`](#trusted-api-olinda-siope-indicadores) | 15,058,952 | 24 | 24 | `api_olinda_siope_indicadores` |
| trusted | [`api_olinda_siope_informacoes_complementares`](#trusted-api-olinda-siope-informacoes-complementares) | 13,890,101 | 21 | 21 | `api_olinda_siope_informacoes_complementares` |

## raw · rreo_siope_municipio

File `raw__rreo_siope_municipio.parquet` · 354,781 rows · 9 columns

Tabela contendo dados extraídos e estruturados dos Relatórios Resumidos da Execução Orçamentária (RREO) do SIOPE, utilizados para monitorar receitas e despesas públicas em educação de municípios e estados.

**Feeds:** `trusted/rreo_siope_municipio`

| Column | Type | Description |
|---|---|---|
| `arquivo` | STRING | Nome do arquivo PDF original do RREO obtido do SIOPE. |
| `tipo_entidade` | STRING | Tipo de ente federativo analisado (ex: 'municipio'). |
| `codigo_ibge` | INTEGER | Código identificador do município ou estado segundo o IBGE. |
| `ano` | INTEGER | Ano de referência do relatório orçamentário (formato YYYY). |
| `bimestre` | INTEGER | Bimestre de referência do relatório (valores de 1 a 6). |
| `dados_json` | STRING | Dados estruturados extraídos do PDF em formato JSON, contendo metadados do parser e tabelas detalhadas de receitas de impostos e despesas de educação. |
| `ftp_mod_date` | STRING | Data e hora de modificação do arquivo na fonte de origem/FTP (formato ISO 8601). — descrição gerada por IA. |
| `ftp_size` | INTEGER | Tamanho do arquivo PDF original no servidor FTP de origem, representado em bytes. |
| `data_extracao` | TIMESTAMP | Data e hora em que o relatório foi capturado e processado para o Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · rreo_siope_uf

File `raw__rreo_siope_uf.parquet` · 1,687 rows · 10 columns

Tabela que armazena dados extraídos dos relatórios RREO (Relatório Resumido da Execução Orçamentária) do SIOPE, contendo metadados dos PDFs originais e os dados financeiros estruturados em JSON para análise de investimentos em educação.

**Feeds:** `trusted/rreo_siope_uf`

| Column | Type | Description |
|---|---|---|
| `arquivo` | STRING | Nome do arquivo PDF original do RREO obtido do SIOPE. |
| `tipo_entidade` | STRING | Tipo de ente federativo analisado, como 'uf' (estadual) ou 'municipio'. |
| `co_uf` | INTEGER | Código IBGE de dois dígitos correspondente à Unidade da Federação. |
| `sg_uf` | STRING | Sigla da Unidade da Federação (ex: SP, RJ). |
| `ano` | INTEGER | Ano de referência do relatório orçamentário (formato YYYY). |
| `bimestre` | INTEGER | Bimestre de referência do relatório (valores de 1 a 6). |
| `dados_json` | STRING | Dados financeiros e orçamentários estruturados em formato JSON, contendo tabelas de receitas e despesas extraídas do PDF. |
| `ftp_mod_date` | STRING | Data e hora da última modificação do arquivo no servidor FTP do SIOPE/FNDE (formato ISO 8601). — descrição gerada por IA. |
| `ftp_size` | INTEGER | Tamanho do arquivo PDF original no servidor FTP, medido em bytes. |
| `data_extracao` | TIMESTAMP | Data e hora do processamento e ingestão do arquivo no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · siope_data

File `raw__siope_data.parquet` · 190,229 rows · 6 columns

Tabela contendo dados extraídos dos relatórios RREO (Relatório Resumido da Execução Orçamentária) obtidos via SIOPE, detalhando receitas e despesas com educação pública por município.

| Column | Type | Description |
|---|---|---|
| `arquivo` | STRING | Nome do arquivo PDF original do RREO do qual os dados foram extraídos. |
| `codigo_ibge` | INTEGER | Código identificador de 6 dígitos do IBGE para o município correspondente. |
| `ano` | INTEGER | Ano de referência do relatório orçamentário (formato YYYY). |
| `bimestre` | INTEGER | Bimestre de referência do relatório (valores de 1 a 6). |
| `dados_json` | STRING | Dados estruturados em formato JSON contendo os metadados e as tabelas de receitas e despesas de educação extraídas do PDF. |
| `data_extracao` | TIMESTAMP | Data e hora em que o processamento e extração do arquivo ocorreram (YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · api_olinda_siope_dados_gerais

File `trusted__api_olinda_siope_dados_gerais.parquet` · 384,692 rows · 63 columns

SIOPE Olinda — Dados Gerais (manifesto da declaração). Grão: 1 linha por ente/ano/bimestre. Totais macro de receita/despesa + despesa em educação (VL_*_EDU) + auditoria (recibo, data, retificação, notas). Origem: API OData pública FNDE (DADOS_ABERTOS_SIOPE). Complementa fnde_siope_* (Antonieta) e rreo_siope_*.

**Built from:** `raw/api_olinda_siope_dados_gerais`

| Column | Type | Description |
|---|---|---|
| `ente` | INTEGER | Chave de ente = COD_MUNI (municipal) ou COD_UF (estadual). Derivada. |
| `TIPO` | STRING | Esfera do ente declarante: Municipal ou Estadual. |
| `NUM_ANO` | INTEGER | Ano de referência da declaração SIOPE. |
| `NUM_PERI` | INTEGER | Bimestre da declaração (1 a 6). |
| `COD_UF` | INTEGER | Código IBGE da UF (2 dígitos). |
| `SIG_UF` | STRING | Sigla da UF. |
| `COD_MUNI` | INTEGER | Código IBGE do município (6 dígitos, sem dígito verificador). NULL em linhas de esfera Estadual. |
| `NOM_MUNI` | STRING | Nome do município. |
| `NUM_POPU` | INTEGER | População do município (habitantes). |
| `NUM_FPM` | NUMERIC | Receita do FPM — Fundo de Participação dos Municípios (R$). |
| `NUM_ITR` | NUMERIC | Receita do ITR (R$). |
| `NUM_LC` | NUMERIC | Receita de transferências da Lei Kandir / LC 87/96 (R$). |
| `NUM_FUNDEF` | NUMERIC | Receita FUNDEF/FUNDEB (R$). |
| `NUM_CP_FUNDEF` | NUMERIC | Complementação da União ao FUNDEF/FUNDEB (R$). |
| `NUM_ICMS` | NUMERIC | Receita do ICMS (R$). |
| `NUM_CIDE` | NUMERIC | Receita da CIDE (R$). |
| `NUM_IPI_EXPO` | NUMERIC | Receita do IPI-Exportação (R$). |
| `NUM_IPVA_FUNDEB` | NUMERIC | Parcela do IPVA destinada ao FUNDEB (R$). |
| `NUM_ITCMD_FUNDEB` | NUMERIC | Parcela do ITCMD ao FUNDEB (R$). |
| `NUM_FPE` | NUMERIC | Receita do FPE — Fundo de Participação dos Estados (R$). |
| `VAL_PIB` | NUMERIC | PIB do município (R$). |
| `VAL_PIB_PERCAPTO` | NUMERIC | PIB per capita do município (R$). |
| `NUM_RECI` | INTEGER | Número do recibo de transmissão da declaração. |
| `DAT_DECL` | DATE | Data da declaração/transmissão ao SIOPE. |
| `VAL_RECE_PREV_ATUA` | NUMERIC | Receita: previsão atualizada (R$). |
| `VAL_RECE_REAL` | NUMERIC | Receita realizada até o bimestre (R$). |
| `VAL_RECE_ORCA` | NUMERIC | Receita orçada (R$). |
| `VAL_DESP_DOTA_ATUA` | NUMERIC | Despesa: dotação atualizada (R$). |
| `VAL_DESP_EMPE` | NUMERIC | Despesa empenhada (R$). |
| `VAL_DESP_LIQU` | NUMERIC | Despesa liquidada (R$). |
| `VAL_DESP_PAGA` | NUMERIC | Despesa paga (R$). |
| `VAL_DESP_ORCA` | NUMERIC | Despesa orçada (R$). |
| `IDN_ASSU_RESP_MTDO_APUR` | STRING | Indicador: responsável assume método de apuração. |
| `IDN_METO_LIMI_CONS` | STRING | Indicador de método de limite constitucional. |
| `IDN_DECL_RETI` | STRING | Indicador de declaração retificadora (S/N). |
| `IDN_TIPO_DECL` | STRING | Tipo da declaração (código). |
| `DES_JUST_PROB_BALA` | STRING | Justificativa de problema de balanço. |
| `IDN_METO_SIOPE_IGUA_TC` | STRING | Indicador: método SIOPE igual ao Tribunal de Contas (S/N). |
| `IDN_POSS_CERT_TC` | STRING | Indicador: possui certidão do TC (S/N). |
| `IDN_POSS_DECI_JUDI` | STRING | Indicador: possui decisão judicial (S/N). |
| `DES_DIFE_METO_CALC` | STRING | Descrição de diferença de método de cálculo. |
| `NUM_SOLI` | INTEGER | Número da solicitação. |
| `DS_JUST_RETIFICACAO` | STRING | Justificativa da retificação. |
| `COD_DIGIT` | STRING | Dígito de controle do recibo. |
| `COD_VERIFIC` | STRING | Código verificador do recibo de transmissão. |
| `VAL_TRANSMISSAO` | STRING | Flag de transmissão (S/N). |
| `VL_DESP_DOTA_ATUA_EDU` | NUMERIC | Despesa em educação: dotação atualizada (R$). |
| `VL_DESP_EMPE_EDU` | NUMERIC | Despesa em educação empenhada (R$). |
| `VL_DESP_LIQU_EDU` | NUMERIC | Despesa em educação liquidada (R$). |
| `VL_DESP_PAGA_EDU` | NUMERIC | Despesa em educação paga (R$). |
| `VL_DESP_ORCA_EDU` | NUMERIC | Despesa em educação orçada (R$). |
| `DS_NOTA_RODAPE_RREO` | STRING | Nota de rodapé do RREO. |
| `DS_NOTA_RODAPE_FUNDEB` | STRING | Nota de rodapé do FUNDEB. |
| `record_index` | INTEGER | Posição 0-based do registro no payload da API (preserva ordem — crítico p/ info_complementares). |
| `page_number` | INTEGER | Página da paginação de origem. |
| `source_endpoint` | STRING | FunctionImport OData de origem. |
| `response_hash` | STRING | Hash MD5 da 1ª página (dedup de payload). |
| `schema_fingerprint` | STRING | Hash dos campos do payload (detecta drift de layout). |
| `ano` | INTEGER | Ano do recorte da chamada. |
| `periodo` | INTEGER | Período/bimestre do recorte. |
| `uf` | STRING | UF do recorte. |
| `mes_exercicio` | INTEGER | Mês de exercício do recorte (só remuneração). |
| `dt_ingestao_lake` | STRING | Timestamp de ingestão no lake (UTC). |

## trusted · api_olinda_siope_despesas

File `trusted__api_olinda_siope_despesas.parquet` · 305,518,954 rows · 32 columns

SIOPE Olinda — Despesa declarada por pasta/rubrica. Grão: ente/ano/bimestre/pasta/rubrica/classe(DA/DE/DL/DP)/fonte. Valores em R$. Origem: API OData FNDE.

**Built from:** `raw/api_olinda_siope_despesas`

| Column | Type | Description |
|---|---|---|
| `ente` | INTEGER | Chave de ente = COD_MUNI (municipal) ou COD_UF (estadual). Derivada. |
| `TIPO` | STRING | Esfera do ente declarante: Municipal ou Estadual. |
| `NUM_ANO` | INTEGER | Ano de referência da declaração SIOPE. |
| `NUM_PERI` | INTEGER | Bimestre da declaração (1 a 6). |
| `COD_UF` | INTEGER | Código IBGE da UF (2 dígitos). |
| `SIG_UF` | STRING | Sigla da UF. |
| `COD_MUNI` | INTEGER | Código IBGE do município (6 dígitos, sem dígito verificador). NULL em linhas de esfera Estadual. |
| `NOM_MUNI` | STRING | Nome do município. |
| `NOM_PAST` | STRING | Nome da pasta/bloco de despesa. |
| `IDN_EXIB_CODI` | STRING | Indicador de exibição do código (S/N). |
| `COD_PAST` | INTEGER | Código da pasta/bloco de despesa. |
| `COD_SUBF` | INTEGER | Código da subfunção orçamentária. |
| `TIP_PASTA` | STRING | Tipo da pasta (ex.: VINCULADAS). |
| `COD_EXIB` | STRING | Código de exibição da rubrica/item. |
| `COD_EXIB_FORMATADO` | STRING | Código de exibição hierárquico formatado da rubrica (árvore contábil). |
| `COD_FONTE` | STRING | Código da fonte de recurso. |
| `NOM_ITEM` | STRING | Nome do item/rubrica contábil. |
| `IDN_CLAS` | STRING | Classe da coluna: receita PA/RR/DF/IO (Previsão Atualizada, Receita Realizada, Deduções Fundeb, Intraorçamentária); despesa DA/DE/DL/DP (Dotação/Empenhada/Liquidada/Paga). |
| `NOM_COLU` | STRING | Nome descritivo da coluna/classe. |
| `NUM_NIVE` | INTEGER | Nível hierárquico da rubrica na árvore. |
| `NUM_ORDE` | INTEGER | Ordem de exibição da rubrica. |
| `VAL_DECL` | NUMERIC | Valor declarado da rubrica (R$). |
| `record_index` | INTEGER | Posição 0-based do registro no payload da API (preserva ordem — crítico p/ info_complementares). |
| `page_number` | INTEGER | Página da paginação de origem. |
| `source_endpoint` | STRING | FunctionImport OData de origem. |
| `response_hash` | STRING | Hash MD5 da 1ª página (dedup de payload). |
| `schema_fingerprint` | STRING | Hash dos campos do payload (detecta drift de layout). |
| `ano` | INTEGER | Ano do recorte da chamada. |
| `periodo` | INTEGER | Período/bimestre do recorte. |
| `uf` | STRING | UF do recorte. |
| `mes_exercicio` | INTEGER | Mês de exercício do recorte (só remuneração). |
| `dt_ingestao_lake` | STRING | Timestamp de ingestão no lake (UTC). |

## trusted · api_olinda_siope_despesas_funcao_educacao

File `trusted__api_olinda_siope_despesas_funcao_educacao.parquet` · 3,060,708 rows · 23 columns

SIOPE Olinda — Despesa da função Educação por subfunção. Grão: ente/ano/bimestre/subfunção. Empenhada/liquidada/paga (R$). Origem: API OData FNDE.

**Built from:** `raw/api_olinda_siope_despesas_funcao_educacao`

| Column | Type | Description |
|---|---|---|
| `ente` | INTEGER | Chave de ente = COD_MUNI (municipal) ou COD_UF (estadual). Derivada. |
| `TIPO` | STRING | Esfera do ente declarante: Municipal ou Estadual. |
| `NUM_ANO` | INTEGER | Ano de referência da declaração SIOPE. |
| `NUM_PERI` | INTEGER | Bimestre da declaração (1 a 6). |
| `COD_UF` | INTEGER | Código IBGE da UF (2 dígitos). |
| `SIG_UF` | STRING | Sigla da UF. |
| `COD_MUNI` | INTEGER | Código IBGE do município (6 dígitos, sem dígito verificador). NULL em linhas de esfera Estadual. |
| `NOM_MUNI` | STRING | Nome do município. |
| `NUM_ORDE` | INTEGER | Ordem de exibição da rubrica. |
| `DES_SUBF` | STRING | Subfunção da despesa por função educação. |
| `VAL_DESP_EMPE` | NUMERIC | Despesa empenhada (R$). |
| `VAL_DESP_LIQU` | NUMERIC | Despesa liquidada (R$). |
| `VAL_DESP_PAGA` | NUMERIC | Despesa paga (R$). |
| `record_index` | INTEGER | Posição 0-based do registro no payload da API (preserva ordem — crítico p/ info_complementares). |
| `page_number` | INTEGER | Página da paginação de origem. |
| `source_endpoint` | STRING | FunctionImport OData de origem. |
| `response_hash` | STRING | Hash MD5 da 1ª página (dedup de payload). |
| `schema_fingerprint` | STRING | Hash dos campos do payload (detecta drift de layout). |
| `ano` | INTEGER | Ano do recorte da chamada. |
| `periodo` | INTEGER | Período/bimestre do recorte. |
| `uf` | STRING | UF do recorte. |
| `mes_exercicio` | INTEGER | Mês de exercício do recorte (só remuneração). |
| `dt_ingestao_lake` | STRING | Timestamp de ingestão no lake (UTC). |

## trusted · api_olinda_siope_indicadores

File `trusted__api_olinda_siope_indicadores.parquet` · 15,058,952 rows · 24 columns

SIOPE Olinda — Indicadores calculados pelo FNDE (% aplicação MDE/Fundeb, investimento por aluno, etc.). Grão: ente/ano/bimestre/indicador. Origem: API OData FNDE.

**Built from:** `raw/api_olinda_siope_indicadores`

**Feeds:** `semantic/obt_api_olinda_siope_indicadores_municipio_ano`, `semantic/obt_api_olinda_siope_indicadores_municipio_bimestre`, `semantic/obt_api_olinda_siope_indicadores_uf_ano`, `semantic/obt_api_olinda_siope_indicadores_uf_bimestre`

| Column | Type | Description |
|---|---|---|
| `ente` | INTEGER | Chave de ente = COD_MUNI (municipal) ou COD_UF (estadual). Derivada. |
| `TIPO` | STRING | Esfera do ente declarante: Municipal ou Estadual. |
| `NUM_ANO` | INTEGER | Ano de referência da declaração SIOPE. |
| `NUM_PERI` | INTEGER | Bimestre da declaração (1 a 6). |
| `COD_UF` | INTEGER | Código IBGE da UF (2 dígitos). |
| `SIG_UF` | STRING | Sigla da UF. |
| `COD_MUNI` | INTEGER | Código IBGE do município (6 dígitos, sem dígito verificador). NULL em linhas de esfera Estadual. |
| `NOM_MUNI` | STRING | Nome do município. |
| `COD_INDI` | INTEGER | Código do indicador FNDE. |
| `COD_EXIB` | STRING | Código de exibição da rubrica/item. |
| `NOM_INDI` | STRING | Nome do indicador calculado pelo FNDE. |
| `COD_GRUP` | INTEGER | Código do grupo de indicadores. |
| `NOM_GRUP_INDI` | STRING | Nome do grupo de indicadores. |
| `VAL_INDI` | NUMERIC | Valor do indicador (percentual ou R$ conforme o indicador). |
| `record_index` | INTEGER | Posição 0-based do registro no payload da API (preserva ordem — crítico p/ info_complementares). |
| `page_number` | INTEGER | Página da paginação de origem. |
| `source_endpoint` | STRING | FunctionImport OData de origem. |
| `response_hash` | STRING | Hash MD5 da 1ª página (dedup de payload). |
| `schema_fingerprint` | STRING | Hash dos campos do payload (detecta drift de layout). |
| `ano` | INTEGER | Ano do recorte da chamada. |
| `periodo` | INTEGER | Período/bimestre do recorte. |
| `uf` | STRING | UF do recorte. |
| `mes_exercicio` | INTEGER | Mês de exercício do recorte (só remuneração). |
| `dt_ingestao_lake` | STRING | Timestamp de ingestão no lake (UTC). |

## trusted · api_olinda_siope_informacoes_complementares

File `trusted__api_olinda_siope_informacoes_complementares.parquet` · 13,890,101 rows · 21 columns

SIOPE Olinda — Informações Complementares (saldos, superávit, restos a pagar, rendimentos). Grão: ente/ano/bimestre/código+posição. ATENÇÃO: COD_EXIB duplicado = previsão+realizado, distinguível só por record_index (ordem do payload). Origem: API OData FNDE.

**Built from:** `raw/api_olinda_siope_informacoes_complementares`

| Column | Type | Description |
|---|---|---|
| `ente` | INTEGER | Chave de ente = COD_MUNI (municipal) ou COD_UF (estadual). Derivada. |
| `TIPO` | STRING | Esfera do ente declarante: Municipal ou Estadual. |
| `NUM_ANO` | INTEGER | Ano de referência da declaração SIOPE. |
| `NUM_PERI` | INTEGER | Bimestre da declaração (1 a 6). |
| `COD_UF` | INTEGER | Código IBGE da UF (2 dígitos). |
| `SIG_UF` | STRING | Sigla da UF. |
| `COD_MUNI` | INTEGER | Código IBGE do município (6 dígitos, sem dígito verificador). NULL em linhas de esfera Estadual. |
| `NOM_MUNI` | STRING | Nome do município. |
| `COD_EXIB` | STRING | Código de exibição da rubrica/item. |
| `NOM_ITEM` | STRING | Nome do item/rubrica contábil. |
| `VAL_DECL` | NUMERIC | Valor declarado da rubrica (R$). |
| `record_index` | INTEGER | Posição 0-based do registro no payload da API (preserva ordem — crítico p/ info_complementares). |
| `page_number` | INTEGER | Página da paginação de origem. |
| `source_endpoint` | STRING | FunctionImport OData de origem. |
| `response_hash` | STRING | Hash MD5 da 1ª página (dedup de payload). |
| `schema_fingerprint` | STRING | Hash dos campos do payload (detecta drift de layout). |
| `ano` | INTEGER | Ano do recorte da chamada. |
| `periodo` | INTEGER | Período/bimestre do recorte. |
| `uf` | STRING | UF do recorte. |
| `mes_exercicio` | INTEGER | Mês de exercício do recorte (só remuneração). |
| `dt_ingestao_lake` | STRING | Timestamp de ingestão no lake (UTC). |
