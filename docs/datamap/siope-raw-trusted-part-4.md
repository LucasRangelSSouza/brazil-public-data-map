# SIOPE education finance: Raw and Trusted

Dataset: [lucasrangelss/siope-raw-trusted-part-4](https://www.kaggle.com/datasets/lucasrangelss/siope-raw-trusted-part-4) · snapshot 2026-10-02 · 10 tables · 448,707,902 rows

**Source:** Fundo Nacional de Desenvolvimento da Educação (FNDE), [https://www.fnde.gov.br/siope/](https://www.fnde.gov.br/siope/)

Education revenue, expenditure and indicators reported by municipalities and states, from the SIOPE open-data API (Olinda), the FNDE SIOPE exports, and the budget execution report (RREO) PDFs parsed into tables.

**Grain and keys:** Municipality (or state) by year and reporting period. Indicator rows repeat by `num_periodo`, so analyses keep the latest period per municipality and year. Municipality joins to IBGE through `codigo_municipio`.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://lucas.rangeltech.net/datamap/](https://lucas.rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| trusted | [`api_olinda_siope_receita`](#trusted-api-olinda-siope-receita) | 122,659,262 | 25 | 25 | `api_olinda_siope_receita` |
| trusted | [`api_olinda_siope_responsaveis`](#trusted-api-olinda-siope-responsaveis) | 1,495,180 | 46 | 46 | `api_olinda_siope_responsaveis` |
| trusted | [`fnde_siope_dados_gerais`](#trusted-fnde-siope-dados-gerais) | 166,452 | 53 | 53 | `fnde_siope_dados_gerais` |
| trusted | [`fnde_siope_despesa_total_educacao`](#trusted-fnde-siope-despesa-total-educacao) | 139,046,717 | 22 | 22 | `fnde_siope_despesa_total_educacao` |
| trusted | [`fnde_siope_despesas_funcao_educacao`](#trusted-fnde-siope-despesas-funcao-educacao) | 1,199,526 | 13 | 13 | `fnde_siope_despesas_funcao_educacao` |
| trusted | [`fnde_siope_indicadores`](#trusted-fnde-siope-indicadores) | 6,441,160 | 15 | 15 | `fnde_siope_indicadores` |
| trusted | [`fnde_siope_informacoes_complementares`](#trusted-fnde-siope-informacoes-complementares) | 8,378,339 | 11 | 11 | `fnde_siope_informacoes_complementares` |
| trusted | [`fnde_siope_receita_total`](#trusted-fnde-siope-receita-total) | 14,311,287 | 14 | 14 | `fnde_siope_receita_total` |
| trusted | [`rreo_siope_municipio`](#trusted-rreo-siope-municipio) | 154,283,183 | 15 | 15 | `rreo_siope_municipio` |
| trusted | [`rreo_siope_uf`](#trusted-rreo-siope-uf) | 726,796 | 16 | 16 | `rreo_siope_uf` |

## trusted · api_olinda_siope_receita

File `trusted__api_olinda_siope_receita.parquet` · 122,659,262 rows · 25 columns

SIOPE Olinda — Receita declarada por rubrica. Grão: ente/ano/bimestre/rubrica(COD_EXIB_FORMATADO)/classe(IDN_CLAS: PA/RR/DF/IO). Valores em R$. Árvore contábil em COD_EXIB_FORMATADO+NUM_NIVE. Origem: API OData FNDE.

**Built from:** `raw/api_olinda_siope_receita`

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
| `COD_EXIB_FORMATADO` | STRING | Código de exibição hierárquico formatado da rubrica (árvore contábil). |
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

## trusted · api_olinda_siope_responsaveis

File `trusted__api_olinda_siope_responsaveis.parquet` · 1,495,180 rows · 46 columns

SIOPE Olinda — Responsáveis pela declaração. Grão: ente/ano/bimestre/tipo de responsável. CONTÉM PII (nome, e-mail, telefone, endereço). Origem: API OData FNDE (consulta por município — UF retorna 500).

**Built from:** `raw/api_olinda_siope_responsaveis`

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
| `NOM_RESP` | STRING | Nome do responsável pela declaração (PII). |
| `DES_EMAI` | STRING | E-mail do responsável (PII). |
| `NUM_TELE` | STRING | Telefone do responsável (PII). |
| `NUM_CNPJ` | STRING | CNPJ do ente. |
| `TIP_RESP` | STRING | Tipo de responsável (P=Prefeito, S=Secretário Educação, F=Financeiro, C=Contábil — mapeamento empírico, validar). |
| `DES_ENDR` | STRING | Endereço do responsável (PII). |
| `END_NUMR` | STRING | Número do endereço (PII). |
| `END_COMP` | STRING | Complemento do endereço (PII). |
| `DES_BAIR` | STRING | Bairro (PII). |
| `NUM_CEP` | STRING | CEP (PII). |
| `CO_MUNICIPIO_RESID` | INTEGER | Código IBGE do município de residência. |
| `CO_UF_RESID` | INTEGER | Código da UF de residência. |
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

## trusted · fnde_siope_dados_gerais

File `trusted__fnde_siope_dados_gerais.parquet` · 166,452 rows · 53 columns

SIOPE FNDE Dados Gerais tipado. Grao: (tipo/esfera, num_ano, num_peri, cod_muni). Totais de receita/despesa/despesa-educacao + FPM/ICMS/FUNDEB/PIB/populacao + campos declaratorios. Origem: raw/fnde_siope_dados_gerais (reprocessado com parse por ancora).

**Built from:** `raw/fnde_siope_dados_gerais`

**Feeds:** `semantic/obt_fnde_siope_dados_gerais_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `tipo` | STRING | Tipo/esfera do ente (Municipal/Estadual). |
| `num_ano` | INTEGER | Ano de referencia. |
| `num_peri` | INTEGER | Periodo/bimestre da declaracao. |
| `cod_uf` | INTEGER | Codigo da UF. |
| `sig_uf` | STRING | Sigla da UF. |
| `cod_muni` | INTEGER | Codigo do municipio. |
| `nom_muni` | STRING | Nome do municipio. |
| `num_popu` | INTEGER | Populacao do municipio. |
| `num_fpm` | FLOAT | Receita do FPM - Fundo de Participacao dos Municipios (R$). |
| `num_itr` | FLOAT | Receita do ITR (R$). |
| `num_lc` | FLOAT | Receita de Lei Complementar (LC 87/96 - Lei Kandir) (R$). |
| `num_fundef` | FLOAT | Receita do FUNDEF/FUNDEB (R$). |
| `num_cp_fundef` | FLOAT | Complementacao do FUNDEF/FUNDEB (R$). |
| `num_icms` | FLOAT | Receita do ICMS (R$). |
| `num_cide` | FLOAT | Receita da CIDE (R$). |
| `num_ipi_expo` | FLOAT | Receita do IPI-Exportacao (R$). |
| `num_ipva_fundeb` | FLOAT | Parcela do IPVA destinada ao FUNDEB (R$). |
| `num_itcmd_fundeb` | FLOAT | Parcela do ITCMD destinada ao FUNDEB (R$). |
| `num_fpe` | FLOAT | Receita do FPE - Fundo de Participacao dos Estados (R$). |
| `val_pib` | FLOAT | PIB do municipio (R$). |
| `val_pib_percapto` | FLOAT | PIB per capita do municipio (R$). |
| `num_reci` | INTEGER | Numero do recibo da declaracao. |
| `dat_decl` | TIMESTAMP | Data da declaracao. |
| `val_rece_prev_atua` | FLOAT | Receita prevista atualizada (R$). |
| `val_rece_real` | FLOAT | Receita realizada (R$). |
| `val_rece_orca` | FLOAT | Receita orcada (R$). |
| `val_desp_dota_atua` | FLOAT | Despesa - dotacao atualizada (R$). |
| `val_desp_empe` | FLOAT | Despesa empenhada (R$). |
| `val_desp_liqu` | FLOAT | Despesa liquidada (R$). |
| `val_desp_paga` | FLOAT | Despesa paga (R$). |
| `val_desp_orca` | FLOAT | Despesa orcada (R$). |
| `idn_assu_resp_mtdo_apur` | STRING | Indicador (flag). |
| `idn_meto_limi_cons` | STRING | Indicador (flag). |
| `idn_decl_reti` | STRING | Indicador (flag). |
| `idn_tipo_decl` | STRING | Indicador (flag). |
| `des_just_prob_bala` | STRING | Descricao. |
| `idn_meto_siope_igua_tc` | STRING | Indicador (flag). |
| `idn_poss_cert_tc` | STRING | Indicador (flag). |
| `idn_poss_deci_judi` | STRING | Indicador (flag). |
| `des_dife_meto_calc` | STRING | Descricao. |
| `num_soli` | INTEGER | Valor (R$). |
| `ds_just_retificacao` | STRING | Descricao. |
| `cod_digit` | STRING | Codigo. |
| `cod_verific` | STRING | Codigo. |
| `val_transmissao` | FLOAT | Valor de controle da transmissao. |
| `vl_desp_dota_atua_edu` | FLOAT | Despesa com educacao - dotacao atualizada (R$). |
| `vl_desp_empe_edu` | FLOAT | Despesa com educacao empenhada (R$). |
| `vl_desp_liqu_edu` | FLOAT | Despesa com educacao liquidada (R$). |
| `vl_desp_paga_edu` | FLOAT | Despesa com educacao paga (R$). |
| `vl_desp_orca_edu` | FLOAT | Despesa com educacao orcada (R$). |
| `ds_nota_rodape_rreo` | STRING | Descricao. |
| `ds_nota_rodape_fundeb` | STRING | Descricao. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · fnde_siope_despesa_total_educacao

File `trusted__fnde_siope_despesa_total_educacao.parquet` · 139,046,717 rows · 22 columns

SIOPE - Detalhamento despesa com educacao por pasta e subfuncao orcamentaria. Grao: ente x ano x periodo x item. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE). Prefixo fnde do pipeline identifica essa origem (NAO e PDF). Havera futuramente 2a origem distinta SIOPE RREO (PDFs de RREO das prefeituras), ainda nao implementada.

**Built from:** `raw/fnde_siope_despesa_total_educacao`

**Feeds:** `semantic/obt_fnde_siope_despesa_educacao_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `tipo` | STRING | Tipo/esfera do ente (Municipal/Estadual). |
| `num_ano` | INTEGER | Ano de referencia. |
| `num_peri` | INTEGER | Periodo/bimestre da declaracao. |
| `cod_uf` | INTEGER | Codigo da UF. |
| `sig_uf` | STRING | Sigla da UF. |
| `cod_muni` | INTEGER | Codigo do municipio. |
| `nom_muni` | STRING | Nome do municipio. |
| `nom_past` | STRING | Nome. |
| `idn_exib_codi` | STRING | Indicador (flag). |
| `cod_past` | STRING | Codigo. |
| `cod_subf` | STRING | Codigo. |
| `tip_pasta` | STRING | Tipo. |
| `cod_exib` | STRING | Codigo. |
| `cod_exib_formatado` | STRING | Codigo. |
| `cod_fonte` | STRING | Codigo. |
| `nom_item` | STRING | Nome. |
| `idn_clas` | STRING | Indicador (flag). |
| `nom_colu` | STRING | Nome. |
| `num_nive` | INTEGER | Valor (R$). |
| `num_orde` | INTEGER | Número de ordem para ordenação do item no relatório financeiro. — descrição gerada por IA. |
| `val_decl` | FLOAT | Valor (R$). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · fnde_siope_despesas_funcao_educacao

File `trusted__fnde_siope_despesas_funcao_educacao.parquet` · 1,199,526 rows · 13 columns

SIOPE - Despesa com funcao Educacao por subfuncao. Grao: ente x ano x periodo x subfuncao. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE). Prefixo fnde do pipeline identifica essa origem (NAO e PDF). Havera futuramente 2a origem distinta SIOPE RREO (PDFs de RREO das prefeituras), ainda nao implementada.

**Built from:** `raw/fnde_siope_despesas_funcao_educacao`

**Feeds:** `semantic/obt_fnde_siope_despesa_funcao_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `tipo` | STRING | Tipo/esfera do ente (Municipal/Estadual). |
| `num_ano` | INTEGER | Ano de referencia. |
| `num_peri` | INTEGER | Periodo/bimestre da declaracao. |
| `cod_uf` | INTEGER | Codigo da UF. |
| `sig_uf` | STRING | Sigla da UF. |
| `cod_muni` | INTEGER | Codigo do municipio. |
| `nom_muni` | STRING | Nome do municipio. |
| `num_orde` | INTEGER | Número de ordem de classificação da despesa/subfunção. — descrição gerada por IA. |
| `des_subf` | STRING | Descricao da subfuncao de despesa. |
| `val_desp_empe` | FLOAT | Despesa empenhada (R$). |
| `val_desp_liqu` | FLOAT | Despesa liquidada (R$). |
| `val_desp_paga` | FLOAT | Despesa paga (R$). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · fnde_siope_indicadores

File `trusted__fnde_siope_indicadores.parquet` · 6,441,160 rows · 15 columns

SIOPE - Indicadores legais e educacionais (% MDE, FUNDEB, remuneracao docente). Grao: ente x ano x periodo x indicador. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE). Prefixo fnde do pipeline identifica essa origem (NAO e PDF). Havera futuramente 2a origem distinta SIOPE RREO (PDFs de RREO das prefeituras), ainda nao implementada.

**Built from:** `raw/fnde_siope_indicadores`

**Feeds:** `semantic/obt_fnde_siope_indicador_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `tipo` | STRING | Tipo/esfera do ente (Municipal/Estadual). |
| `num_ano` | INTEGER | Ano de referencia. |
| `num_peri` | INTEGER | Periodo/bimestre da declaracao. |
| `cod_uf` | INTEGER | Codigo da UF. |
| `sig_uf` | STRING | Sigla da UF. |
| `cod_muni` | INTEGER | Codigo do municipio. |
| `nom_muni` | STRING | Nome do municipio. |
| `cod_indi` | STRING | Codigo do indicador. |
| `cod_exib` | STRING | Codigo. |
| `nom_indi` | STRING | Nome do indicador. |
| `cod_grup` | STRING | Codigo do grupo de indicadores. |
| `nom_grup_indi` | STRING | Nome do grupo de indicadores. |
| `val_indi` | FLOAT | Valor apurado do indicador. |
| `dt_atualizacao` | DATE | Data de atualizacao do registro na fonte. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · fnde_siope_informacoes_complementares

File `trusted__fnde_siope_informacoes_complementares.parquet` · 8,378,339 rows · 11 columns

SIOPE - Informacoes complementares de preenchimento. Grao: ente x ano x periodo x item. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE). Prefixo fnde do pipeline identifica essa origem (NAO e PDF). Havera futuramente 2a origem distinta SIOPE RREO (PDFs de RREO das prefeituras), ainda nao implementada.

**Built from:** `raw/fnde_siope_informacoes_complementares`

**Feeds:** `semantic/obt_fnde_siope_info_complementar_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `num_ano` | INTEGER | Ano de referencia. |
| `num_peri` | INTEGER | Periodo/bimestre da declaracao. |
| `cod_uf` | INTEGER | Codigo da UF. |
| `sig_uf` | STRING | Sigla da UF. |
| `cod_muni` | INTEGER | Codigo do municipio. |
| `nom_muni` | STRING | Nome do municipio. |
| `cod_exib` | STRING | Codigo. |
| `nom_item` | STRING | Nome. |
| `val_decl_str` | STRING | Valor (R$). |
| `val_decl_num` | FLOAT | Valor (R$). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · fnde_siope_receita_total

File `trusted__fnde_siope_receita_total.parquet` · 14,311,287 rows · 14 columns

SIOPE - Receita total por conta contabil. Historico desde 2005. Grao: ente x ano x periodo x conta. Origem: extracao de arquivos brutos (CSV) publicados como dados abertos pelo FNDE na Plataforma Antonieta de Barros, espelhados em dados.gov.br (conjunto SIOPE). Prefixo fnde do pipeline identifica essa origem (NAO e PDF). Havera futuramente 2a origem distinta SIOPE RREO (PDFs de RREO das prefeituras), ainda nao implementada.

**Built from:** `raw/fnde_siope_receita_total`

**Feeds:** `semantic/obt_fnde_siope_receita_municipio_ano`

| Column | Type | Description |
|---|---|---|
| `an_exercicio` | INTEGER | Ano do exercicio. |
| `tp_periodo` | STRING | Tipo de periodo. |
| `nu_periodo` | INTEGER | Periodo de referencia. |
| `co_uf` | INTEGER | Codigo IBGE da UF. |
| `no_uf` | STRING | Nome da UF. |
| `co_municipio` | INTEGER | Codigo IBGE do municipio. |
| `no_municipio` | STRING | Nome do municipio. |
| `no_esfera_adm` | STRING | Esfera administrativa. |
| `co_conta_contabil` | STRING | Codigo da conta contabil. |
| `no_conta_contabil` | STRING | Nome da conta contabil. |
| `vl_receita_previsao_atualizada` | FLOAT | Receita - previsao atualizada (R$). |
| `vl_receita_realizadas` | FLOAT | Receita realizada (R$). |
| `vl_receita_orcada` | FLOAT | Receita orcada (R$). |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake. |

## trusted · rreo_siope_municipio

File `trusted__rreo_siope_municipio.parquet` · 154,283,183 rows · 15 columns

RREO SIOPE Municipio formato LONG/tidy. Grao: 1 linha por (ente, ano, bimestre, codigo, posicao). Arvore hierarquica achatada (todas granularidades). coluna=header (NULL=posicional); juntar com rreo_siope_coluna por (tipo_ente, secao, posicao). Robusto a mudanca de estrutura. Origem: raw/rreo_siope_municipio.

**Built from:** `raw/rreo_siope_municipio`

**Feeds:** `semantic/obt_rreo_siope_municipio_ano`, `semantic/obt_rreo_siope_municipio_bimestre`

| Column | Type | Description |
|---|---|---|
| `codigo_ibge` | INTEGER | Codigo IBGE do municipio (7 digitos). FK -> semantic/obt_ibge_municipio. |
| `ano` | INTEGER | Ano de exercicio do RREO. |
| `bimestre` | INTEGER | Bimestre do RREO (1 a 6). A semantica usa o ultimo bimestre disponivel (acumulado do ano). |
| `secao` | INTEGER | Secao raiz do RREO (inteiro 1..~52) que agrupa o assunto: receitas, deducoes, FUNDEB, despesas MDE, restos a pagar, disponibilidade financeira. |
| `codigo` | STRING | Codigo hierarquico da rubrica no RREO (ex.: 1, 1.1, 1.1.1). |
| `nivel` | INTEGER | Nivel de profundidade da rubrica na arvore (1=secao raiz, 2=subitem, ...). |
| `descricao` | STRING | Descrição da conta, imposto ou receita fiscal declarada. — descrição gerada por IA. |
| `coluna` | STRING | Rotulo original da coluna de valor no PDF, quando capturado. |
| `posicao` | INTEGER | Posicao ordinal da coluna de valor na tabela do RREO. |
| `nome_metrica` | STRING | Metrica do valor: Previsao/Dotacao, Realizada/Empenhada/Liquidada/Paga, Restos a Pagar ou % aplicado (resolvida pelo header ou pelo perfil da secao). |
| `valor` | FLOAT | Valor numerico da celula (rubrica x metrica), em R$ ou % conforme a metrica. |
| `arquivo` | STRING | Nome do arquivo PDF de origem no FTP do FNDE. |
| `ftp_mod_date` | STRING | Data de modificacao do PDF no FTP (YYYYMMDDHHMMSS) — usada no delta. |
| `data_extracao` | TIMESTAMP | Timestamp UTC da extracao/parse do PDF. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake (trusted). |

## trusted · rreo_siope_uf

File `trusted__rreo_siope_uf.parquet` · 726,796 rows · 16 columns

RREO SIOPE UF/Estado formato LONG/tidy. Grao: 1 linha por (ente, ano, bimestre, codigo, posicao). Arvore hierarquica achatada (todas granularidades). coluna=header (NULL=posicional); juntar com rreo_siope_coluna por (tipo_ente, secao, posicao). Robusto a mudanca de estrutura. Origem: raw/rreo_siope_uf.

**Built from:** `raw/rreo_siope_uf`

**Feeds:** `semantic/obt_rreo_siope_uf_ano`, `semantic/obt_rreo_siope_uf_bimestre`

| Column | Type | Description |
|---|---|---|
| `co_uf` | INTEGER | Codigo IBGE da UF (2 digitos). |
| `sg_uf` | STRING | Sigla da UF. |
| `ano` | INTEGER | Ano de exercicio do RREO. |
| `bimestre` | INTEGER | Bimestre do RREO (1 a 6). A semantica usa o ultimo bimestre disponivel (acumulado do ano). |
| `secao` | INTEGER | Secao raiz do RREO (inteiro 1..~52) que agrupa o assunto: receitas, deducoes, FUNDEB, despesas MDE, restos a pagar, disponibilidade financeira. |
| `codigo` | STRING | Codigo hierarquico da rubrica no RREO (ex.: 1, 1.1, 1.1.1). |
| `nivel` | INTEGER | Nivel de profundidade da rubrica na arvore (1=secao raiz, 2=subitem, ...). |
| `descricao` | STRING | Descrição da conta orçamentária (ex: Receita de Impostos). — descrição gerada por IA. |
| `coluna` | STRING | Rotulo original da coluna de valor no PDF, quando capturado. |
| `posicao` | INTEGER | Posicao ordinal da coluna de valor na tabela do RREO. |
| `nome_metrica` | STRING | Metrica do valor: Previsao/Dotacao, Realizada/Empenhada/Liquidada/Paga, Restos a Pagar ou % aplicado (resolvida pelo header ou pelo perfil da secao). |
| `valor` | FLOAT | Valor numerico da celula (rubrica x metrica), em R$ ou % conforme a metrica. |
| `arquivo` | STRING | Nome do arquivo PDF de origem no FTP do FNDE. |
| `ftp_mod_date` | STRING | Data de modificacao do PDF no FTP (YYYYMMDDHHMMSS) — usada no delta. |
| `data_extracao` | TIMESTAMP | Timestamp UTC da extracao/parse do PDF. |
| `dt_ingestao_lake` | TIMESTAMP | Timestamp UTC da carga no lake (trusted). |
