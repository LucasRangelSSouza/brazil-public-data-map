# PNCP public procurement: Analytics

Dataset: [lucasrangelss/pncp-analytics](https://www.kaggle.com/datasets/lucasrangelss/pncp-analytics) · snapshot 2026-09-30 · 6 tables · 10,341,852 rows

**Source:** Portal Nacional de Contratações Públicas (PNCP), [https://pncp.gov.br/api/consulta/v1](https://pncp.gov.br/api/consulta/v1)

Procurement notices (including editais), contracts, price-registration records (atas) and annual procurement plans (PCA) with their items, published through the PNCP consultation API.

**Grain and keys:** One row per natural key, keeping the latest version by `dataAtualizacaoGlobal`: `numero_controle_pncp` for notices and contracts, `numero_controle_pncp_ata` for atas, `id_pca_pncp` for plans. Municipality is reachable through `unidade_codigo_ibge` (IBGE code).

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://lucas.rangeltech.net/datamap/](https://lucas.rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`obt_pncp_atas`](#semantic-obt-pncp-atas) | 1,076,677 | 25 | 0 | `pncp_atas` |
| semantic | [`obt_pncp_contratacoes`](#semantic-obt-pncp-contratacoes) | 3,763,118 | 48 | 0 | `obt_ibge_municipio`, `pncp_contratacoes` |
| semantic | [`obt_pncp_contratos`](#semantic-obt-pncp-contratos) | 3,428,193 | 55 | 0 | `obt_ibge_municipio`, `pncp_contratos` |
| semantic | [`obt_pncp_editais_semantico`](#semantic-obt-pncp-editais-semantico) | 1,248,539 | 29 | 29 | `obt_pncp_contratacoes`, `pncp_editais_embeddings` |
| semantic | [`obt_pncp_pca`](#semantic-obt-pncp-pca) | 7,534 | 9 | 0 | `pncp_pca` |
| semantic | [`obt_pncp_pca_itens`](#semantic-obt-pncp-pca-itens) | 817,791 | 23 | 0 | `pncp_pca_itens` |

## semantic · obt_pncp_atas

File `semantic__obt_pncp_atas.parquet` · 1,076,677 rows · 25 columns

PNCP Atas de registro de preco. Grao: numero_controle_pncp_ata. Sem codigo IBGE na fonte (mantem CNPJ/orgao).

**Built from:** `trusted/pncp_atas`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp_ata` | STRING |  |
| `numero_ata_registro_preco` | STRING |  |
| `ano_ata` | INTEGER |  |
| `numero_controle_pncp_compra` | STRING |  |
| `cancelado` | BOOLEAN |  |
| `data_cancelamento` | DATE |  |
| `data_assinatura` | DATE |  |
| `vigencia_inicio` | DATE |  |
| `vigencia_fim` | DATE |  |
| `data_publicacao_pncp` | DATE |  |
| `data_inclusao` | DATE |  |
| `data_atualizacao` | DATE |  |
| `data_atualizacao_global` | TIMESTAMP |  |
| `objeto_contratacao` | STRING |  |
| `cnpj_orgao` | STRING |  |
| `nome_orgao` | STRING |  |
| `cnpj_orgao_subrogado` | STRING |  |
| `nome_orgao_subrogado` | STRING |  |
| `codigo_unidade_orgao` | STRING |  |
| `nome_unidade_orgao` | STRING |  |
| `codigo_unidade_orgao_subrogado` | STRING |  |
| `nome_unidade_orgao_subrogado` | STRING |  |
| `possibilidade_adesao` | BOOLEAN |  |
| `usuario` | STRING |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## semantic · obt_pncp_contratacoes

File `semantic__obt_pncp_contratacoes.parquet` · 3,763,118 rows · 48 columns

PNCP Contratacoes/editais por ente. Grao: numero_controle_pncp. Enriquecido com geografia (obt_ibge_municipio) via unidade_codigo_ibge -> codigo_municipio.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/pncp_contratacoes`

**Feeds:** `semantic/obt_pncp_editais_semantico`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING |  |
| `ano_compra` | INTEGER |  |
| `sequencial_compra` | INTEGER |  |
| `numero_compra` | STRING |  |
| `processo` | STRING |  |
| `modalidade_id` | INTEGER |  |
| `modalidade_nome` | STRING |  |
| `modo_disputa_id` | INTEGER |  |
| `modo_disputa_nome` | STRING |  |
| `tipo_instrumento_convocatorio_codigo` | INTEGER |  |
| `tipo_instrumento_convocatorio_nome` | STRING |  |
| `situacao_compra_id` | INTEGER |  |
| `situacao_compra_nome` | STRING |  |
| `srp` | BOOLEAN |  |
| `objeto_compra` | STRING |  |
| `informacao_complementar` | STRING |  |
| `justificativa_presencial` | STRING |  |
| `valor_total_estimado` | FLOAT |  |
| `valor_total_homologado` | FLOAT |  |
| `data_inclusao` | TIMESTAMP |  |
| `data_publicacao_pncp` | TIMESTAMP |  |
| `data_atualizacao` | TIMESTAMP |  |
| `data_abertura_proposta` | TIMESTAMP |  |
| `data_encerramento_proposta` | TIMESTAMP |  |
| `data_atualizacao_global` | TIMESTAMP |  |
| `amparo_legal_codigo` | INTEGER |  |
| `amparo_legal_nome` | STRING |  |
| `amparo_legal_descricao` | STRING |  |
| `orgao_cnpj` | STRING |  |
| `orgao_razao_social` | STRING |  |
| `orgao_poder_id` | STRING |  |
| `orgao_esfera_id` | STRING |  |
| `unidade_uf_sigla` | STRING |  |
| `unidade_uf_nome` | STRING |  |
| `unidade_codigo` | STRING |  |
| `unidade_nome` | STRING |  |
| `unidade_municipio_nome` | STRING |  |
| `link_sistema_origem` | STRING |  |
| `link_processo_eletronico` | STRING |  |
| `usuario_nome` | STRING |  |
| `fontes_orcamentarias_json` | STRING |  |
| `codigo_municipio` | INTEGER |  |
| `nome_municipio` | STRING |  |
| `sigla_uf` | STRING |  |
| `nome_uf` | STRING |  |
| `nome_regiao` | STRING |  |
| `codigo_uf` | INTEGER |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## semantic · obt_pncp_contratos

File `semantic__obt_pncp_contratos.parquet` · 3,428,193 rows · 55 columns

PNCP Contratos/empenhos por ente. Grao: numero_controle_pncp. Enriquecido com geografia via codigo IBGE da unidade.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/pncp_contratos`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING |  |
| `numero_controle_pncp_compra` | STRING |  |
| `numero_controle_pncp_ata` | STRING |  |
| `ano_contrato` | INTEGER |  |
| `numero_contrato_empenho` | STRING |  |
| `sequencial_contrato` | INTEGER |  |
| `processo` | STRING |  |
| `tipo_contrato_id` | INTEGER |  |
| `tipo_contrato_nome` | STRING |  |
| `categoria_processo_id` | INTEGER |  |
| `categoria_processo_nome` | STRING |  |
| `data_assinatura` | DATE |  |
| `data_vigencia_inicio` | DATE |  |
| `data_vigencia_fim` | DATE |  |
| `data_publicacao_pncp` | TIMESTAMP |  |
| `data_atualizacao` | TIMESTAMP |  |
| `data_atualizacao_global` | TIMESTAMP |  |
| `ni_fornecedor` | STRING |  |
| `tipo_pessoa` | STRING |  |
| `nome_razao_social_fornecedor` | STRING |  |
| `codigo_pais_fornecedor` | STRING |  |
| `ni_fornecedor_subcontratado` | STRING |  |
| `nome_fornecedor_subcontratado` | STRING |  |
| `tipo_pessoa_subcontratada` | STRING |  |
| `objeto_contrato` | STRING |  |
| `informacao_complementar` | STRING |  |
| `valor_inicial` | FLOAT |  |
| `valor_global` | FLOAT |  |
| `valor_parcela` | FLOAT |  |
| `valor_acumulado` | FLOAT |  |
| `numero_parcelas` | INTEGER |  |
| `receita` | BOOLEAN |  |
| `numero_retificacao` | INTEGER |  |
| `fruto_adesao` | BOOLEAN |  |
| `tem_remanejamento` | BOOLEAN |  |
| `orgao_cnpj` | STRING |  |
| `orgao_razao_social` | STRING |  |
| `orgao_poder_id` | STRING |  |
| `orgao_esfera_id` | STRING |  |
| `unidade_uf_sigla` | STRING |  |
| `unidade_uf_nome` | STRING |  |
| `unidade_codigo` | STRING |  |
| `unidade_nome` | STRING |  |
| `unidade_municipio_nome` | STRING |  |
| `emenda_parlamentar` | STRING |  |
| `identificador_cipi` | STRING |  |
| `url_cipi` | STRING |  |
| `usuario_nome` | STRING |  |
| `codigo_municipio` | INTEGER |  |
| `nome_municipio` | STRING |  |
| `sigla_uf` | STRING |  |
| `nome_uf` | STRING |  |
| `nome_regiao` | STRING |  |
| `codigo_uf` | INTEGER |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## semantic · obt_pncp_editais_semantico

File `semantic__obt_pncp_editais_semantico.parquet` · 1,248,539 rows · 29 columns

PNCP EDITAIS (tipo_instrumento_convocatorio_codigo IN 1,4) vetorizados para BUSCA SEMANTICA. Grao: 1 linha por edital com embedding. Achata obt_pncp_contratacoes (geografia ja enriquecida) + trusted/pncp_editais_embeddings. Traz objeto_normalizado (minusculo sem acento), categoria_area (heuristica de palavra-chave; categoria PRINCIPAL por ordem de prioridade - um edital pode se encaixar em mais de uma area, aqui rotulamos so a primeira correspondencia) e o vetor 768-dim. Fonte do dashboard Metabase de busca semantica. Recarga: CREATE OR REPLACE na DAG ingestion_pncp_delta (6/6h), apos pncp_semantic e pncp_embeddings.

**Built from:** `semantic/obt_pncp_contratacoes`, `trusted/pncp_editais_embeddings`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Chave natural do edital no PNCP (PK). |
| `ano_compra` | INTEGER | Ano da compra validado (BETWEEN 2021 e ano atual+1; senao NULL). |
| `data_publicacao_pncp` | TIMESTAMP | Data de publicacao no PNCP. |
| `data_abertura_proposta` | TIMESTAMP | Abertura do periodo de propostas. |
| `data_encerramento_proposta` | TIMESTAMP | Encerramento do periodo de propostas. |
| `em_aberto` | BOOLEAN | TRUE se data_encerramento_proposta >= agora (ainda recebendo proposta). |
| `sigla_uf` | STRING | UF da unidade compradora. |
| `nome_municipio` | STRING | Municipio da unidade compradora. |
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (FK geografia). |
| `nome_regiao` | STRING | Regiao geografica. |
| `orgao_cnpj` | STRING | CNPJ do orgao comprador. |
| `orgao_razao_social` | STRING | Razao social do orgao comprador. |
| `modalidade_nome` | STRING | Modalidade (pregao, concorrencia, dispensa...). |
| `modo_disputa_nome` | STRING | Modo de disputa (aberto, fechado...). |
| `tipo_instrumento_convocatorio_nome` | STRING | Tipo do instrumento (Edital / Chamamento). |
| `situacao_compra_nome` | STRING | Situacao da compra. |
| `srp` | BOOLEAN | Sistema de Registro de Precos (bool). |
| `objeto_compra` | STRING | Objeto do edital (texto original; foi o texto vetorizado). |
| `objeto_normalizado` | STRING | Objeto em minusculo e sem acento (filtro literal barato). |
| `categoria_area` | STRING | Categoria macro por heuristica de palavra-chave (aproximacao p/ graficos). |
| `valor_total_estimado` | FLOAT | Valor total estimado. |
| `valor_total_homologado` | FLOAT | Valor total homologado (quando houver). |
| `link_sistema_origem` | STRING | URL do portal de origem da disputa (pode ser NULL). |
| `link_pncp` | STRING | URL do edital no portal PNCP (clicavel). |
| `embedding` | FLOAT | Vetor de embedding 768-dim (text-multilingual-embedding-002). |
| `modelo` | STRING | Nome do modelo de embedding. |
| `dim` | INTEGER | Dimensao do vetor (768). |
| `dt_embedding` | TIMESTAMP | Quando o embedding foi gerado. |
| `dt_atualizacao_obt` | TIMESTAMP | Timestamp da rodada que (re)gerou a OBT. |

## semantic · obt_pncp_pca

File `semantic__obt_pncp_pca.parquet` · 7,534 rows · 9 columns

PNCP Plano de Contratacoes Anual (cabecalho). Grao: id_pca_pncp. Sem codigo IBGE na fonte.

**Built from:** `trusted/pncp_pca`

| Column | Type | Description |
|---|---|---|
| `id_pca_pncp` | STRING |  |
| `ano_pca` | INTEGER |  |
| `codigo_unidade` | STRING |  |
| `nome_unidade` | STRING |  |
| `orgao_entidade_cnpj` | STRING |  |
| `orgao_entidade_razao_social` | STRING |  |
| `data_publicacao_pncp` | TIMESTAMP |  |
| `data_atualizacao_global_pca` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## semantic · obt_pncp_pca_itens

File `semantic__obt_pncp_pca_itens.parquet` · 817,791 rows · 23 columns

PNCP itens do Plano de Contratacoes Anual. Grao: id_pca_pncp + numero_item.

**Built from:** `trusted/pncp_pca_itens`

| Column | Type | Description |
|---|---|---|
| `id_pca_pncp` | STRING |  |
| `numero_item` | INTEGER |  |
| `descricao_item` | STRING |  |
| `codigo_item` | STRING |  |
| `categoria_item_pca_nome` | STRING |  |
| `nome_classificacao_catalogo` | STRING |  |
| `classificacao_catalogo_id` | INTEGER |  |
| `classificacao_superior_codigo` | STRING |  |
| `classificacao_superior_nome` | STRING |  |
| `grupo_contratacao_codigo` | STRING |  |
| `grupo_contratacao_nome` | STRING |  |
| `pdm_codigo` | STRING |  |
| `pdm_descricao` | STRING |  |
| `unidade_fornecimento` | STRING |  |
| `unidade_requisitante` | STRING |  |
| `quantidade_estimada` | FLOAT |  |
| `valor_unitario` | FLOAT |  |
| `valor_total` | FLOAT |  |
| `valor_orcamento_exercicio` | FLOAT |  |
| `data_desejada` | DATE |  |
| `data_inclusao` | TIMESTAMP |  |
| `data_atualizacao` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |
