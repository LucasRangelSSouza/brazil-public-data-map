# PNCP public procurement: Raw and Trusted

Dataset: [lucasrangelss/pncp-raw-trusted-part-1](https://www.kaggle.com/datasets/lucasrangelss/pncp-raw-trusted-part-1) · snapshot 2026-09-30 · 40 tables · 213,700,826 rows

**Source:** Portal Nacional de Contratações Públicas (PNCP), [https://pncp.gov.br/api/consulta/v1](https://pncp.gov.br/api/consulta/v1)

Procurement notices (including editais), contracts, price-registration records (atas) and annual procurement plans (PCA) with their items, published through the PNCP consultation API.

**Grain and keys:** One row per natural key, keeping the latest version by `dataAtualizacaoGlobal`: `numero_controle_pncp` for notices and contracts, `numero_controle_pncp_ata` for atas, `id_pca_pncp` for plans. Municipality is reachable through `unidade_codigo_ibge` (IBGE code).

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://lucas.rangeltech.net/datamap/](https://lucas.rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`pncp_atas_atualizacao`](#raw-pncp-atas-atualizacao) | 2,723,277 | 10 | 10 | source |
| raw | [`pncp_contratacoes_arquivos`](#raw-pncp-contratacoes-arquivos) | 4,045,882 | 7 | 7 | source |
| raw | [`pncp_contratacoes_atualizacao`](#raw-pncp-contratacoes-atualizacao) | 7,719,898 | 10 | 10 | source |
| raw | [`pncp_contratacoes_historico`](#raw-pncp-contratacoes-historico) | 68,610,105 | 7 | 7 | source |
| raw | [`pncp_contratacoes_itens`](#raw-pncp-contratacoes-itens) | 25,595,585 | 7 | 7 | source |
| raw | [`pncp_contratacoes_itens_resultados`](#raw-pncp-contratacoes-itens-resultados) | 4,004,953 | 7 | 7 | source |
| raw | [`pncp_contratacoes_proposta`](#raw-pncp-contratacoes-proposta) | 74,088 | 6 | 6 | source |
| raw | [`pncp_contratos_atualizacao`](#raw-pncp-contratos-atualizacao) | 10,275,091 | 10 | 10 | source |
| raw | [`pncp_contratos_termos`](#raw-pncp-contratos-termos) | 382,798 | 7 | 7 | source |
| raw | [`pncp_instrumentos_cobranca`](#raw-pncp-instrumentos-cobranca) | 769,359 | 6 | 6 | source |
| raw | [`pncp_orgaos`](#raw-pncp-orgaos) | 45,594 | 7 | 7 | source |
| raw | [`pncp_orgaos_unidades`](#raw-pncp-orgaos-unidades) | 409,469 | 7 | 7 | source |
| raw | [`pncp_pca_atualizacao`](#raw-pncp-pca-atualizacao) | 147,425 | 10 | 10 | source |
| trusted | [`pncp_atas`](#trusted-pncp-atas) | 1,078,249 | 25 | 0 | `pncp_atas_atualizacao` |
| trusted | [`pncp_contratacoes`](#trusted-pncp-contratacoes) | 3,768,885 | 43 | 0 | `pncp_contratacoes_atualizacao` |
| trusted | [`pncp_contratacoes_arquivos`](#trusted-pncp-contratacoes-arquivos) | 3,289,351 | 9 | 0 | `pncp_contratacoes_arquivos` |
| trusted | [`pncp_contratacoes_historico`](#trusted-pncp-contratacoes-historico) | 51,038,072 | 10 | 0 | `pncp_contratacoes_historico` |
| trusted | [`pncp_contratacoes_itens`](#trusted-pncp-contratacoes-itens) | 20,890,388 | 15 | 0 | `pncp_contratacoes_itens` |
| trusted | [`pncp_contratacoes_itens_resultados`](#trusted-pncp-contratacoes-itens-resultados) | 3,393,191 | 13 | 0 | `pncp_contratacoes_itens_resultados` |
| trusted | [`pncp_contratacoes_proposta`](#trusted-pncp-contratacoes-proposta) | 70 | 19 | 19 | `pncp_contratacoes_proposta` |
| trusted | [`pncp_contratos`](#trusted-pncp-contratos) | 3,435,513 | 50 | 0 | `pncp_contratos_atualizacao` |
| trusted | [`pncp_contratos_termos`](#trusted-pncp-contratos-termos) | 310,593 | 13 | 0 | `pncp_contratos_termos` |
| trusted | [`pncp_dom_amparos_legais`](#trusted-pncp-dom-amparos-legais) | 183 | 12 | 12 | source |
| trusted | [`pncp_dom_catalogos`](#trusted-pncp-dom-catalogos) | 2 | 8 | 8 | source |
| trusted | [`pncp_dom_categoria_item_pca`](#trusted-pncp-dom-categoria-item-pca) | 8 | 7 | 7 | source |
| trusted | [`pncp_dom_criterios_julgamento`](#trusted-pncp-dom-criterios-julgamento) | 9 | 7 | 7 | source |
| trusted | [`pncp_dom_fontes_orcamentarias`](#trusted-pncp-dom-fontes-orcamentarias) | 6 | 7 | 7 | source |
| trusted | [`pncp_dom_modalidades`](#trusted-pncp-dom-modalidades) | 19 | 7 | 7 | source |
| trusted | [`pncp_dom_modos_disputa`](#trusted-pncp-dom-modos-disputa) | 6 | 7 | 7 | source |
| trusted | [`pncp_dom_portes_empresa`](#trusted-pncp-dom-portes-empresa) | 6 | 7 | 7 | source |
| trusted | [`pncp_dom_tipos_contrato`](#trusted-pncp-dom-tipos-contrato) | 12 | 7 | 7 | source |
| trusted | [`pncp_dom_tipos_documento`](#trusted-pncp-dom-tipos-documento) | 20 | 10 | 10 | source |
| trusted | [`pncp_dom_tipos_instrumento_cobranca`](#trusted-pncp-dom-tipos-instrumento-cobranca) | 1 | 7 | 7 | source |
| trusted | [`pncp_dom_tipos_instrumento_convocatorio`](#trusted-pncp-dom-tipos-instrumento-convocatorio) | 5 | 9 | 9 | source |
| trusted | [`pncp_dom_tipos_parte_envolvida`](#trusted-pncp-dom-tipos-parte-envolvida) | 3 | 4 | 4 | source |
| trusted | [`pncp_editais_embeddings`](#trusted-pncp-editais-embeddings) | 1,249,424 | 8 | 8 | source |
| trusted | [`pncp_instrumentos_cobranca`](#trusted-pncp-instrumentos-cobranca) | 262,529 | 9 | 0 | `pncp_instrumentos_cobranca` |
| trusted | [`pncp_orgaos`](#trusted-pncp-orgaos) | 19,126 | 9 | 0 | `pncp_orgaos` |
| trusted | [`pncp_orgaos_unidades`](#trusted-pncp-orgaos-unidades) | 154,097 | 9 | 0 | `pncp_orgaos_unidades` |
| trusted | [`pncp_pca`](#trusted-pncp-pca) | 7,534 | 9 | 0 | `pncp_pca_atualizacao` |

## raw · pncp_atas_atualizacao

File `raw__pncp_atas_atualizacao.parquet` · 2,723,277 rows · 10 columns

Tabela da camada raw (Bronze) do educational data lake, responsável por armazenar payloads JSON brutos e metadados de ingestão particionados por domínio, janela temporal e paginação.

**Feeds:** `trusted/pncp_atas`

| Column | Type | Description |
|---|---|---|
| `chave_natural` | STRING | Identificador único do registro na origem (ex: CNPJ unificado com código de controle), utilizado para garantir a unicidade e rastreabilidade do dado. |
| `data_atualizacao_global` | STRING | Data da última modificação ou atualização do registro no sistema de origem (formato YYYY-MM-DD). |
| `dominio` | STRING | Classificação temática do dado ingerido (ex: 'atas', 'escolas', 'ideb', 'tutoria'), indicando o contexto de negócio. |
| `modalidade` | INTEGER | Identificador da modalidade associada ao registro (ex: tipo de ensino ou licitação), quando aplicável. |
| `janela_inicio` | STRING | Data de início do período de competência ou extração dos dados (formato YYYYMMDD). |
| `janela_fim` | STRING | Data de término do período de competência ou extração dos dados (formato YYYYMMDD). |
| `pagina` | INTEGER | Número da página correspondente na paginação da API de origem durante a coleta do lote. |
| `total_paginas` | INTEGER | Total de páginas disponíveis na consulta à API de origem. |
| `payload_json` | STRING | Estrutura JSON original e completa contendo os dados brutos extraídos da fonte (ex: detalhes de atas, escolas ou notas). |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora exatas da ingestão do registro no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · pncp_contratacoes_arquivos

File `raw__pncp_contratacoes_arquivos.parquet` · 4,045,882 rows · 7 columns

Armazena os registros brutos de arquivos e anexos de compras públicas extraídos da API do Portal Nacional de Contratações Públicas (PNCP) para monitoramento de aquisições na educação pública.

**Feeds:** `trusted/pncp_contratacoes_arquivos`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Código identificador único do processo de compra no PNCP (formato: CNPJ-tipo-número/ano). |
| `data_final` | STRING | Parâmetro sequencial da contratação enviado na requisição da API do PNCP. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora de ingestão do registro no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |
| `payload_json` | STRING | Estrutura JSON bruta com os detalhes e URLs dos arquivos/anexos retornados pela API do PNCP. |
| `numero_pagina` | INTEGER | Número da página consultada na paginação do endpoint da API. |
| `data_inicial` | STRING | CNPJ do órgão público responsável pela contratação, utilizado como parâmetro de consulta. |
| `dominio` | STRING | Identificador do domínio do recurso consultado na API do PNCP (ex: 'arquivos'). |

## raw · pncp_contratacoes_atualizacao

File `raw__pncp_contratacoes_atualizacao.parquet` · 7,719,898 rows · 10 columns

Tabela da camada raw (ingestão) que armazena dados paginados de contratações e aquisições públicas relacionadas aos ecossistemas educacionais of the source lake.

**Feeds:** `trusted/pncp_contratacoes`

| Column | Type | Description |
|---|---|---|
| `chave_natural` | STRING | Identificador único do registro no sistema de origem, composto por CNPJ, código e ano do contrato. |
| `data_atualizacao_global` | STRING | Data e hora da última alteração do registro na API de origem (formato ISO 8601). — descrição gerada por IA. |
| `dominio` | STRING | Classificação do domínio de negócio do dado integrado (ex: 'contratacoes'). |
| `modalidade` | INTEGER | Código identificador da modalidade de licitação ou contratação utilizada. |
| `janela_inicio` | STRING | Data de início do período de extração dos dados (formato AAAAMMDD). |
| `janela_fim` | STRING | Data de término do período de extração dos dados (formato AAAAMMDD). |
| `pagina` | INTEGER | Número da página do lote de dados retornado pela API de origem. |
| `total_paginas` | INTEGER | Número total de páginas retornadas na consulta para a janela temporal informada. |
| `payload_json` | STRING | Dados brutos em formato JSON contendo os detalhes da contratação, como valores e amparo legal. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do carregamento do registro na camada raw do Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · pncp_contratacoes_historico

File `raw__pncp_contratacoes_historico.parquet` · 68,610,105 rows · 7 columns

Tabela de registros e histórico de alterações de contratações públicas obtidas via API do PNCP (Portal Nacional de Contratações Públicas) para auditoria e acompanhamento de contratos educacionais.

**Feeds:** `trusted/pncp_contratacoes_historico`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Número identificador único da contratação no PNCP (formato CNPJ-Tipo-Sequencial/Ano). |
| `data_final` | STRING | Parâmetro do número final ou identificador de término da consulta na API do PNCP. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora em que os dados foram capturados e inseridos no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |
| `payload_json` | STRING | Estrutura JSON bruta com o histórico de alterações, logs de manutenção e detalhes técnicos do contrato. |
| `numero_pagina` | INTEGER | Número da página retornada na paginação da consulta da API. |
| `data_inicial` | STRING | CNPJ do órgão comprador ou parâmetro inicial de busca utilizado na consulta da API. |
| `dominio` | STRING | Classificação do escopo da consulta ou tipo de dado retornado da API (ex: 'historico'). |

## raw · pncp_contratacoes_itens

File `raw__pncp_contratacoes_itens.parquet` · 25,595,585 rows · 7 columns

Tabela de metadados e payloads brutos extraídos do PNCP (Portal Nacional de Contratações Públicas) para auditoria e acompanhamento de itens/insumos adquiridos na rede pública de ensino.

**Feeds:** `trusted/pncp_contratacoes_itens`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Código de identificação único da licitação ou contratação no PNCP (formato CNPJ-tipo-número/ano). |
| `data_final` | INTEGER | Parâmetro final de busca ou valor numérico limite utilizado no filtro da extração via API do PNCP. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do processamento e gravação do registro no Data Lake (formato: YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |
| `payload_json` | STRING | Estrutura JSON bruta com os detalhes do item licitado (ex: número do item, descrição, tipo de material/serviço). |
| `numero_pagina` | INTEGER | Número da página da consulta paginada retornada pela API de origem no momento da extração. |
| `data_inicial` | INTEGER | Parâmetro de filtro inicial ou CNPJ do órgão comprador utilizado na consulta da API de origem. |
| `dominio` | STRING | Domínio ou tipo do recurso extraído do PNCP (ex: 'itens' para especificar produtos/serviços de um processo). |

## raw · pncp_contratacoes_itens_resultados

File `raw__pncp_contratacoes_itens_resultados.parquet` · 4,004,953 rows · 7 columns

Dados brutos de resultados de consultas de compras e contratações públicas extraídos da API do Portal Nacional de Contratações Públicas (PNCP) para monitoramento de contratos educacionais.

**Feeds:** `trusted/pncp_contratacoes_itens_resultados`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Número único de identificação do processo de contratação pública no PNCP (formato CNPJ-tipo-sequencial/ano). |
| `data_final` | STRING | Identificador do item ou parâmetro final de controle da requisição utilizada na API do PNCP. |
| `payload_json` | STRING | Objeto JSON completo retornado pela API do PNCP contendo detalhes do fornecedor, itens e status do contrato. |
| `data_inicial` | STRING | CNPJ do órgão público contratante utilizado como parâmetro de entrada na consulta. |
| `dominio` | STRING | Categoria ou tipo de endpoint consultado na API do PNCP (ex: 'resultados'). |
| `numero_pagina` | INTEGER | Número da página da consulta paginada retornada pela API do PNCP. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora exata em que o registro foi armazenado no data lake (YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · pncp_contratacoes_proposta

File `raw__pncp_contratacoes_proposta.parquet` · 74,088 rows · 6 columns

Tabela de ingestão bruta (landing zone) contendo requisições e respostas em JSON de APIs públicas e editais/propostas governamentais para acompanhamento educacional.

**Feeds:** `trusted/pncp_contratacoes_proposta`

| Column | Type | Description |
|---|---|---|
| `data_final` | INTEGER | Data final utilizada como parâmetro de busca na extração da API (formato YYYYMMDD). |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do processamento e gravação do registro no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |
| `payload_json` | STRING | Conteúdo bruto em formato JSON contendo os dados retornados pela API (ex: órgão, CNPJ, razão social). |
| `numero_pagina` | INTEGER | Número da página do resultado retornado pela paginação da API consultada. |
| `data_inicial` | STRING | Data inicial utilizada como parâmetro de busca na extração da API (formato YYYYMMDD ou vazio). |
| `dominio` | STRING | Identificador do domínio de negócio ou endpoint consultado (ex: 'proposta'). |

## raw · pncp_contratos_atualizacao

File `raw__pncp_contratos_atualizacao.parquet` · 10,275,091 rows · 10 columns

Tabela de transição (landing zone) do educational data lake, responsável por armazenar os payloads brutos de integrações e APIs (como PNCP, the platform vendor e dados escolares) estruturados por domínio e janelas de extração.

**Feeds:** `trusted/pncp_contratos`

| Column | Type | Description |
|---|---|---|
| `chave_natural` | STRING | Identificador único e exclusivo do registro na origem (ex: CNPJ + número do contrato), utilizado para controle de integridade e deduplicação. |
| `data_atualizacao_global` | STRING | Data e hora da última atualização do registro na fonte de origem (formato ISO 8601). — descrição gerada por IA. |
| `dominio` | STRING | Classificação do assunto ou origem do dado integrado (ex: 'contratos', 'escolas', 'tutoria'). |
| `modalidade` | INTEGER | Subtipo ou modalidade específica do domínio (ex: tipo de ensino ou categoria de contratação). |
| `janela_inicio` | STRING | Data de início do período de extração dos dados (formato AAAAMMDD). |
| `janela_fim` | STRING | Data de término do período de extração dos dados (formato AAAAMMDD). |
| `pagina` | INTEGER | Número da página correspondente na paginação da API de origem durante a coleta. |
| `total_paginas` | INTEGER | Total de páginas disponíveis na consulta do lote de extração. — descrição gerada por IA. |
| `payload_json` | STRING | Dados brutos (raw data) em formato JSON contendo todos os campos detalhados retornados pela API de origem. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora exatas do carregamento do registro no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## raw · pncp_contratos_termos

File `raw__pncp_contratos_termos.parquet` · 382,798 rows · 7 columns

Tabela contendo os dados brutos de termos aditivos e contratuais coletados do Portal Nacional de Contratações Públicas (PNCP), focada em contratos públicos de educação.

**Feeds:** `trusted/pncp_contratos_termos`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Código único de identificação do termo/contrato no PNCP (formato CNPJ-Tipo-Número/Ano). |
| `data_final` | STRING | Parâmetro do sequencial final ou limite de consulta utilizado na extração de dados do PNCP. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora da ingestão do registro no Data Lake (AAAA-MM-DD HH:MM:SS). — descrição gerada por IA. |
| `payload_json` | STRING | Estrutura JSON bruta com os detalhes do termo contratual retornado pela API do PNCP. |
| `numero_pagina` | INTEGER | Número da página do resultado retornado na paginação da consulta da API. |
| `data_inicial` | STRING | Parâmetro inicial de consulta (geralmente o CNPJ do órgão contratante) enviado na API do PNCP. |
| `dominio` | STRING | Identificador do tipo de recurso/endpoint consultado na API (ex: 'termos'). |

## raw · pncp_instrumentos_cobranca

File `raw__pncp_instrumentos_cobranca.parquet` · 769,359 rows · 6 columns

Tabela de ingestão bruta (stage/raw) contendo payloads JSON de instrumentos de cobrança vinculados a contratos públicos educacionais (ex: FNDE/PNCP) do programa the source organization.

**Feeds:** `trusted/pncp_instrumentos_cobranca`

| Column | Type | Description |
|---|---|---|
| `data_final` | INTEGER | Data de término do intervalo de consulta utilizado na extração da API (formato YYYYMMDD). |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora em que o registro foi armazenado no Data Lake (formato AAAA-MM-DD HH:MM:SS). — descrição gerada por IA. |
| `payload_json` | STRING | Objeto JSON bruto retornado da API contendo os dados detalhados do instrumento de cobrança (CNPJ, contrato, sequencial, ano). |
| `numero_pagina` | INTEGER | Número da página da requisição paginada retornado pela API de origem. |
| `data_inicial` | INTEGER | Data de início do intervalo de consulta utilizado na extração da API (formato YYYYMMDD). |
| `dominio` | STRING | Nome do domínio ou endpoint da origem dos dados (ex: instrumentos_cobranca). |

## raw · pncp_orgaos

File `raw__pncp_orgaos.parquet` · 45,594 rows · 7 columns

Registros brutos extraídos do PNCP (Portal Nacional de Contratações Públicas) sobre órgãos públicos e entes governamentais relacionados à gestão da educação pública.

**Feeds:** `trusted/pncp_orgaos`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Número de identificação ou CNPJ do órgão consultado no PNCP. |
| `data_final` | STRING | Data final utilizada como filtro na consulta à API do PNCP. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do armazenamento do registro no Data Lake (AAAA-MM-DD HH:MM:SS). — descrição gerada por IA. |
| `payload_json` | STRING | Objeto JSON bruto retornado pela API contendo os detalhes cadastrais do órgão (razão social, natureza jurídica, etc.). |
| `numero_pagina` | INTEGER | Número da página de retorno na paginação da API. |
| `data_inicial` | STRING | Data inicial ou parâmetro de origem utilizado na busca da API. |
| `dominio` | STRING | Nome do domínio/endpoint consultado na API do PNCP (ex: 'orgaos'). |

## raw · pncp_orgaos_unidades

File `raw__pncp_orgaos_unidades.parquet` · 409,469 rows · 7 columns

Tabela de staging/raw para ingestão de dados públicos do PNCP (Portal Nacional de Contratações Públicas), utilizada no acompanhamento de órgãos, contratos e aquisições ligadas à educação pública.

**Feeds:** `trusted/pncp_orgaos_unidades`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Número de identificação do controle no PNCP ou CNPJ do órgão consultado. |
| `data_final` | STRING | Data final do intervalo utilizado como filtro na extração da API do PNCP. |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora em que o dado foi gravado no Data Lake (formato YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |
| `payload_json` | STRING | Conteúdo JSON bruto retornado pela API do PNCP contendo os detalhes das unidades ou contratos. |
| `numero_pagina` | INTEGER | Número da página da resposta paginada da API do PNCP. |
| `data_inicial` | STRING | Data inicial ou parâmetro do filtro de origem utilizado na requisição à API. |
| `dominio` | STRING | Categoria do domínio ou endpoint consultado no PNCP (ex: 'unidades'). |

## raw · pncp_pca_atualizacao

File `raw__pncp_pca_atualizacao.parquet` · 147,425 rows · 10 columns

Tabela de ingestão de dados brutos (raw) do data lake, contendo payloads paginados de APIs externas (como PNCP/PCA) relacionados a compras, insumos e contratos de entidades educacionais.

**Feeds:** `trusted/pncp_pca`, `trusted/pncp_pca_itens`

| Column | Type | Description |
|---|---|---|
| `chave_natural` | STRING | Identificador único de negócio do registro na origem, composto geralmente por CNPJ, código e ano do processo. |
| `data_atualizacao_global` | STRING | Data e hora de atualização da informação na fonte de origem (formato ISO 8601). — descrição gerada por IA. |
| `dominio` | STRING | Agrupador ou contexto de negócio do dado integrado (ex: 'pca' para Plano de Contratações Anuais). |
| `modalidade` | INTEGER | Classificação ou modalidade específica do registro ou processo de origem. |
| `janela_inicio` | STRING | Data de início da janela temporal de extração dos dados (formato YYYYMMDD). |
| `janela_fim` | STRING | Data de término da janela temporal de extração dos dados (formato YYYYMMDD). |
| `pagina` | INTEGER | Número da página correspondente ao lote de dados retornado pela API de origem. |
| `total_paginas` | INTEGER | Total de páginas geradas na extração da API de origem. |
| `payload_json` | STRING | Conteúdo bruto em formato JSON contendo os dados detalhados do registro (itens, valores, descrições). |
| `dt_ingestao_lake` | TIMESTAMP | Data e hora do processamento e gravação do registro no Data Lake (YYYY-MM-DD HH:MM:SS). — descrição gerada por IA. |

## trusted · pncp_atas

File `trusted__pncp_atas.parquet` · 1,078,249 rows · 25 columns

PNCP — Atas de registro de preco. Grao: 1 linha por numero_controle_pncp_ata (versao mais recente). Fonte: raw/pncp_atas_atualizacao.

**Built from:** `raw/pncp_atas_atualizacao`

**Feeds:** `semantic/obt_pncp_atas`

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

## trusted · pncp_contratacoes

File `trusted__pncp_contratacoes.parquet` · 3,768,885 rows · 43 columns

PNCP — Contratacoes/editais (eixo /atualizacao). Grao: 1 linha por numero_controle_pncp (versao mais recente por dataAtualizacaoGlobal). Fonte: raw/pncp_contratacoes_atualizacao.

**Built from:** `raw/pncp_contratacoes_atualizacao`

**Feeds:** `semantic/obt_pncp_contratacoes`

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
| `unidade_codigo_ibge` | INTEGER |  |
| `link_sistema_origem` | STRING |  |
| `link_processo_eletronico` | STRING |  |
| `usuario_nome` | STRING |  |
| `fontes_orcamentarias_json` | STRING |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_contratacoes_arquivos

File `trusted__pncp_contratacoes_arquivos.parquet` · 3,289,351 rows · 9 columns

**Built from:** `raw/pncp_contratacoes_arquivos`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING |  |
| `sequencial_documento` | INTEGER |  |
| `titulo` | STRING |  |
| `uri` | STRING |  |
| `url` | STRING |  |
| `status_ativo` | BOOLEAN |  |
| `tipo_documento_nome` | STRING |  |
| `data_publicacao_pncp` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_contratacoes_historico

File `trusted__pncp_contratacoes_historico.parquet` · 51,038,072 rows · 10 columns

**Built from:** `raw/pncp_contratacoes_historico`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING |  |
| `compra_orgao_cnpj` | STRING |  |
| `compra_ano` | INTEGER |  |
| `log_data_inclusao` | TIMESTAMP |  |
| `tipo_log_manutencao_nome` | STRING |  |
| `categoria_log_manutencao_nome` | STRING |  |
| `usuario_nome` | STRING |  |
| `justificativa` | STRING |  |
| `item_numero` | INTEGER |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_contratacoes_itens

File `trusted__pncp_contratacoes_itens.parquet` · 20,890,388 rows · 15 columns

**Built from:** `raw/pncp_contratacoes_itens`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING |  |
| `numero_item` | INTEGER |  |
| `descricao` | STRING |  |
| `material_ou_servico_nome` | STRING |  |
| `valor_unitario_estimado` | NUMERIC |  |
| `valor_total` | NUMERIC |  |
| `quantidade` | NUMERIC |  |
| `unidade_medida` | STRING |  |
| `item_categoria_nome` | STRING |  |
| `criterio_julgamento_nome` | STRING |  |
| `situacao_compra_item_nome` | STRING |  |
| `tem_resultado` | BOOLEAN |  |
| `data_inclusao` | TIMESTAMP |  |
| `data_atualizacao` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_contratacoes_itens_resultados

File `trusted__pncp_contratacoes_itens_resultados.parquet` · 3,393,191 rows · 13 columns

**Built from:** `raw/pncp_contratacoes_itens_resultados`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING |  |
| `numero_item` | INTEGER |  |
| `sequencial_resultado` | INTEGER |  |
| `ni_fornecedor` | STRING |  |
| `nome_razao_social_fornecedor` | STRING |  |
| `valor_total_homologado` | NUMERIC |  |
| `quantidade_homologada` | NUMERIC |  |
| `valor_unitario_homologado` | NUMERIC |  |
| `situacao_resultado_nome` | STRING |  |
| `ordem_classificacao_srp` | INTEGER |  |
| `data_resultado` | TIMESTAMP |  |
| `data_atualizacao` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_contratacoes_proposta

File `trusted__pncp_contratacoes_proposta.parquet` · 70 rows · 19 columns

PNCP — CONTRATACOES COM PROPOSTA ABERTA (snapshot). Foto do que esta com o prazo de propostas em aberto no momento da coleta — NAO e serie historica: cada carga substitui a foto anterior. Origem: /contratacoes/proposta (API de consulta), segmentada por codigoModalidadeContratacao (1..19). Para historico completo de contratacoes use pncp_contratacoes.

**Built from:** `raw/pncp_contratacoes_proposta`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Chave natural do registro no PNCP, no formato <CNPJ>-<tipo>-<sequencial>/<ano>. Origem: numeroControlePNCP. FK para pncp_contratacoes. |
| `ano_compra` | INTEGER | Ano da compra. Origem: anoCompra. |
| `sequencial_compra` | INTEGER | Sequencial da compra no orgao/ano. Origem: sequencialCompra. |
| `numero_compra` | STRING | Numero da compra no sistema de origem. Origem: numeroCompra. |
| `orgao_cnpj` | STRING | CNPJ do orgao responsavel. FK para pncp_orgaos. Origem: orgaoEntidade.cnpj. |
| `orgao_razao_social` | STRING | Razao social do orgao. Origem: orgaoEntidade.razaoSocial. |
| `unidade_uf_nome` | STRING | UF da unidade administrativa. Origem: unidadeOrgao.ufNome. |
| `unidade_municipio_nome` | STRING | Municipio da unidade administrativa. Origem: unidadeOrgao.municipioNome. |
| `objeto_compra` | STRING | Descricao do objeto da contratacao. Origem: objetoCompra. |
| `modalidade_id` | INTEGER | Codigo da modalidade (1..19). Origem: modalidadeId. |
| `modalidade_nome` | STRING | Nome da modalidade. Origem: modalidadeNome. |
| `valor_total_estimado` | FLOAT | Valor total estimado da contratacao, em reais. Origem: valorTotalEstimado. |
| `data_abertura_proposta` | DATETIME | Data/hora de abertura do prazo de propostas. Origem: dataAberturaProposta. |
| `data_encerramento_proposta` | DATETIME | Data/hora de encerramento do prazo de propostas — e o que define a foto. Origem: dataEncerramentoProposta. |
| `tipo_instrumento_convocatorio_codigo` | INTEGER | Codigo do instrumento convocatorio (1=Edital, 4=Chamamento Publico). Origem: tipoInstrumentoConvocatorioCodigo. |
| `tipo_instrumento_convocatorio_nome` | STRING | Nome do instrumento convocatorio. Origem: tipoInstrumentoConvocatorioNome. |
| `situacao_compra_nome` | STRING | Situacao da compra. Origem: situacaoCompraNome. |
| `data_atualizacao_global` | DATETIME | Marca-d'agua da API. Origem: dataAtualizacaoGlobal. |
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |

## trusted · pncp_contratos

File `trusted__pncp_contratos.parquet` · 3,435,513 rows · 50 columns

PNCP — Contratos/empenhos. Grao: 1 linha por numero_controle_pncp (versao mais recente). Fonte: raw/pncp_contratos_atualizacao.

**Built from:** `raw/pncp_contratos_atualizacao`

**Feeds:** `semantic/obt_pncp_contratos`

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
| `unidade_codigo_ibge` | INTEGER |  |
| `emenda_parlamentar` | STRING |  |
| `identificador_cipi` | STRING |  |
| `url_cipi` | STRING |  |
| `usuario_nome` | STRING |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_contratos_termos

File `trusted__pncp_contratos_termos.parquet` · 310,593 rows · 13 columns

**Built from:** `raw/pncp_contratos_termos`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING |  |
| `numero_termo_contrato` | STRING |  |
| `sequencial_termo_contrato` | INTEGER |  |
| `tipo_termo_contrato_nome` | STRING |  |
| `objeto_termo_contrato` | STRING |  |
| `ni_fornecedor` | STRING |  |
| `nome_razao_social_fornecedor` | STRING |  |
| `valor_global` | NUMERIC |  |
| `data_assinatura` | TIMESTAMP |  |
| `data_vigencia_inicio` | TIMESTAMP |  |
| `data_vigencia_fim` | TIMESTAMP |  |
| `data_atualizacao` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_dom_amparos_legais

File `trusted__pncp_dom_amparos_legais.parquet` · 183 rows · 12 columns

PNCP — DOMINIO: AMPAROS LEGAIS (dispositivos da lei que fundamentam a contratacao). Traduz amparo_legal_codigo em pncp_contratacoes. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `tipoAmparoLegal` | RECORD | Tipo do amparo legal (objeto aninhado com id/nome/descricao). Origem: tipoAmparoLegal. |
| `tipoAmparoLegal.statusAtivo` | BOOLEAN | Indica se o tipo de amparo legal esta ativo. Origem: tipoAmparoLegal.statusAtivo. |
| `tipoAmparoLegal.descricao` | STRING | Descricao do tipo de amparo legal. Origem: tipoAmparoLegal.descricao. |
| `tipoAmparoLegal.nome` | STRING | Nome do tipo de amparo legal. Origem: tipoAmparoLegal.nome. |
| `tipoAmparoLegal.id` | INTEGER | Codigo do tipo de amparo legal. Origem: tipoAmparoLegal.id. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_catalogos

File `trusted__pncp_dom_catalogos.parquet` · 2 rows · 8 columns

PNCP — DOMINIO: CATALOGOS de referencia de itens usados pelo PNCP. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `url` | STRING | URL do catalogo de referencia. Origem: url. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_categoria_item_pca

File `trusted__pncp_dom_categoria_item_pca.parquet` · 8 rows · 7 columns

PNCP — DOMINIO: CATEGORIAS DE ITEM DO PCA (material, servico, obra...). Traduz categoria_item_pca_nome em pncp_pca_itens. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_criterios_julgamento

File `trusted__pncp_dom_criterios_julgamento.parquet` · 9 rows · 7 columns

PNCP — DOMINIO: CRITERIOS DE JULGAMENTO (menor preco, maior desconto, tecnica e preco...). Traduz criterio_julgamento_nome em pncp_contratacoes_itens. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_fontes_orcamentarias

File `trusted__pncp_dom_fontes_orcamentarias.parquet` · 6 rows · 7 columns

PNCP — DOMINIO: FONTES ORCAMENTARIAS. Traduz os codigos em fontes_orcamentarias_json de pncp_contratacoes. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_modalidades

File `trusted__pncp_dom_modalidades.parquet` · 19 rows · 7 columns

PNCP — DOMINIO: MODALIDADES DE CONTRATACAO (pregao, concorrencia, dispensa, inexigibilidade...). Traduz modalidade_id em pncp_contratacoes. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_modos_disputa

File `trusted__pncp_dom_modos_disputa.parquet` · 6 rows · 7 columns

PNCP — DOMINIO: MODOS DE DISPUTA (aberto, fechado, aberto-fechado...). Traduz modo_disputa_id em pncp_contratacoes. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_portes_empresa

File `trusted__pncp_dom_portes_empresa.parquet` · 6 rows · 7 columns

PNCP — DOMINIO: PORTES DE EMPRESA (ME, EPP, demais). Classifica o fornecedor nos resultados dos itens. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_tipos_contrato

File `trusted__pncp_dom_tipos_contrato.parquet` · 12 rows · 7 columns

PNCP — DOMINIO: TIPOS DE CONTRATO (contrato, empenho, credenciamento...). Traduz tipo_contrato_id em pncp_contratos. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_tipos_documento

File `trusted__pncp_dom_tipos_documento.parquet` · 20 rows · 10 columns

PNCP — DOMINIO: TIPOS DE DOCUMENTO (edital, ata, termo de referencia, aviso...). Traduz tipo_documento_nome em pncp_contratacoes_arquivos. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `tipoInformacao` | RECORD | Tipo de informacao a que o documento se refere (objeto aninhado). Origem: tipoInformacao. |
| `tipoInformacao.nome` | STRING | Nome do tipo de informacao do documento. Origem: tipoInformacao.nome. |
| `tipoInformacao.codigo` | INTEGER | Codigo do tipo de informacao do documento. Origem: tipoInformacao.codigo. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_tipos_instrumento_cobranca

File `trusted__pncp_dom_tipos_instrumento_cobranca.parquet` · 1 rows · 7 columns

PNCP — DOMINIO: TIPOS DE INSTRUMENTO DE COBRANCA (nota fiscal eletronica, fatura, recibo...). Traduz tipo_instrumento_cobranca_nome em pncp_instrumentos_cobranca. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_tipos_instrumento_convocatorio

File `trusted__pncp_dom_tipos_instrumento_convocatorio.parquet` · 5 rows · 9 columns

PNCP — DOMINIO: TIPOS DE INSTRUMENTO CONVOCATORIO (1=Edital, 4=Chamamento Publico, 2/3=contratacao direta). Traduz tipo_instrumento_convocatorio_codigo. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `dataAtualizacao` | TIMESTAMP | Data/hora da ultima atualizacao do item de dominio. Origem: dataAtualizacao. |
| `dataInclusao` | TIMESTAMP | Data/hora de inclusao do item de dominio. Origem: dataInclusao. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `obrigatoriedadeDataAberturaPropostaNome` | STRING | Indica se a data de abertura de propostas e obrigatoria para este instrumento. Origem: obrigatoriedadeDataAberturaPropostaNome. |
| `obrigatoriedadeDataEncerramentoPropostaNome` | STRING | Indica se a data de encerramento de propostas e obrigatoria para este instrumento. Origem: obrigatoriedadeDataEncerramentoPropostaNome. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `statusAtivo` | BOOLEAN | Indica se o item de dominio esta ativo. Itens inativos permanecem para leitura de registros historicos. Origem: statusAtivo. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_dom_tipos_parte_envolvida

File `trusted__pncp_dom_tipos_parte_envolvida.parquet` · 3 rows · 4 columns

PNCP — DOMINIO: TIPOS DE PARTE ENVOLVIDA nos registros do PNCP. Tabela de referencia (pequena, muda pouco); mantem os nomes de campo da API (camelCase).

| Column | Type | Description |
|---|---|---|
| `dt_ingestao_lake` | TIMESTAMP | Momento (UTC) em que a linha foi ingerida no lake. Controle interno do pipeline — nao vem da API. Usado como desempate na deduplicacao e como marca-d'agua do delta. |
| `descricao` | STRING | Descricao do item de dominio (texto explicativo). Origem: descricao. |
| `nome` | STRING | Nome do item de dominio (rotulo curto exibido no PNCP). Origem: nome. |
| `id` | INTEGER | Codigo do item de dominio. Chave natural — e o valor referenciado pelas colunas *_id/*_codigo das tabelas transacionais. Origem: id. |

## trusted · pncp_editais_embeddings

File `trusted__pncp_editais_embeddings.parquet` · 1,249,424 rows · 8 columns

Embeddings (busca semantica) dos EDITAIS do PNCP (tipo_instrumento 1/4). Tabela SEPARADA da trusted do PNCP: junte por numero_controle_pncp. Modelo Vertex text-multilingual-embedding-002. Use VECTOR_SEARCH para buscar editais por similaridade de texto.

**Feeds:** `semantic/obt_pncp_editais_semantico`

| Column | Type | Description |
|---|---|---|
| `numero_controle_pncp` | STRING | Chave natural do edital (PNCP). Join com trusted/pncp_contratacoes / semantic/obt_pncp_contratacoes. |
| `ano_compra` | INTEGER | Ano da compra/edital. |
| `texto_base` | STRING | Texto vetorizado (objeto_compra, truncado). |
| `texto_hash` | STRING | Hash do texto_base — re-embute so se o objeto mudar. |
| `modelo` | STRING | Modelo de embedding usado (Vertex AI). |
| `dim` | INTEGER | Dimensao do vetor. |
| `embedding` | FLOAT | Vetor do edital (embedding). Usar em VECTOR_SEARCH / COSINE. |
| `dt_embedding` | TIMESTAMP | Quando foi vetorizado. |

## trusted · pncp_instrumentos_cobranca

File `trusted__pncp_instrumentos_cobranca.parquet` · 262,529 rows · 9 columns

**Built from:** `raw/pncp_instrumentos_cobranca`

| Column | Type | Description |
|---|---|---|
| `cnpj` | STRING |  |
| `ano` | INTEGER |  |
| `sequencial_contrato` | INTEGER |  |
| `sequencial_instrumento_cobranca` | INTEGER |  |
| `tipo_instrumento_cobranca_nome` | STRING |  |
| `numero_instrumento_cobranca` | STRING |  |
| `data_inclusao` | TIMESTAMP |  |
| `data_atualizacao` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_orgaos

File `trusted__pncp_orgaos.parquet` · 19,126 rows · 9 columns

**Built from:** `raw/pncp_orgaos`

| Column | Type | Description |
|---|---|---|
| `cnpj` | STRING |  |
| `razao_social` | STRING |  |
| `nome_fantasia` | STRING |  |
| `poder_id` | STRING |  |
| `esfera_id` | STRING |  |
| `descricao_natureza_juridica` | STRING |  |
| `validado` | BOOLEAN |  |
| `data_atualizacao` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_orgaos_unidades

File `trusted__pncp_orgaos_unidades.parquet` · 154,097 rows · 9 columns

**Built from:** `raw/pncp_orgaos_unidades`

| Column | Type | Description |
|---|---|---|
| `cnpj_orgao` | STRING |  |
| `codigo_unidade` | STRING |  |
| `nome_unidade` | STRING |  |
| `municipio_nome` | STRING |  |
| `municipio_codigo_ibge` | STRING |  |
| `uf_sigla` | STRING |  |
| `status_ativo` | BOOLEAN |  |
| `data_atualizacao` | TIMESTAMP |  |
| `dt_ingestao_lake` | TIMESTAMP |  |

## trusted · pncp_pca

File `trusted__pncp_pca.parquet` · 7,534 rows · 9 columns

PNCP — Plano de Contratacoes Anual (cabecalho). Grao: 1 linha por id_pca_pncp. Itens em pncp_pca_itens. Fonte: raw/pncp_pca_atualizacao.

**Built from:** `raw/pncp_pca_atualizacao`

**Feeds:** `semantic/obt_pncp_pca`

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
