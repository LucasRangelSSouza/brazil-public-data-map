# IDEB (INEP): Analytics

Dataset: [lucasrangelss/ideb-analytics](https://www.kaggle.com/datasets/lucasrangelss/ideb-analytics) · snapshot 2026-09-30 · 4 tables · 981,919 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/ideb](https://www.gov.br/inep/pt-br/areas-de-atuacao/avaliacao-e-exames-educacionais/ideb)

Observed IDEB against targets by school, municipality, state, region and Brazil, every two years. IDEB is the SAEB proficiency score times the flow indicator.

**Grain and keys:** School, municipality, state, region or Brazil by edition.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| semantic | [`obt_inep_ideb_brasil_ano`](#semantic-obt-inep-ideb-brasil-ano) | 55 | 21 | 21 | `inep_ideb_brasil` |
| semantic | [`obt_inep_ideb_escola_ano`](#semantic-obt-inep-ideb-escola-ano) | 798,779 | 24 | 24 | `obt_ibge_municipio`, `inep_ideb_escola` |
| semantic | [`obt_inep_ideb_municipio_ano`](#semantic-obt-inep-ideb-municipio-ano) | 181,677 | 31 | 31 | `obt_ibge_municipio`, `inep_ideb_municipio` |
| semantic | [`obt_inep_ideb_regiao_ano`](#semantic-obt-inep-ideb-regiao-ano) | 1,408 | 29 | 29 | `obt_ibge_uf`, `inep_ideb_regioes_ufs` |

## semantic · obt_inep_ideb_brasil_ano

File `semantic__obt_inep_ideb_brasil_ano.parquet` · 55 rows · 21 columns

IDEB do Brasil por ano e rede, com AI, AF e EM pivotados em colunas. Grao: 1 linha por (ano, rede). Origem: trusted_zone.inep_ideb_brasil.

**Built from:** `trusted/inep_ideb_brasil`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano de referencia do IDEB (bienal: 2005, 2007, ..., 2023). |
| `rede` | STRING | Dependencia administrativa: Total, Publica, Federal, Estadual, Municipal, Privada. |
| `ideb_ai_observado` | FLOAT | IDEB observado nos Anos Iniciais do EF (1-5 ano) no Brasil. |
| `ideb_ai_meta` | FLOAT | Meta projetada do IDEB nos Anos Iniciais do EF. |
| `ideb_ai_mat` | FLOAT | Nota SAEB media em Matematica nos Anos Iniciais do EF. |
| `ideb_ai_lp` | FLOAT | Nota SAEB media em Lingua Portuguesa nos Anos Iniciais do EF. |
| `ideb_ai_nota_media` | FLOAT | Nota SAEB media padronizada (LP + Mat) nos Anos Iniciais do EF. |
| `ideb_ai_indicador_rendimento` | FLOAT | Indicador de rendimento (P) dos Anos Iniciais do EF: fluxo escolar 0-1 usado no calculo do IDEB (IDEB = nota media padronizada x P). |
| `ideb_af_observado` | FLOAT | IDEB observado nos Anos Finais do EF (6-9 ano) no Brasil. |
| `ideb_af_meta` | FLOAT | Meta projetada do IDEB nos Anos Finais do EF. |
| `ideb_af_mat` | FLOAT | Nota SAEB media em Matematica nos Anos Finais do EF. |
| `ideb_af_lp` | FLOAT | Nota SAEB media em Lingua Portuguesa nos Anos Finais do EF. |
| `ideb_af_nota_media` | FLOAT | Nota SAEB media padronizada nos Anos Finais do EF. |
| `ideb_af_indicador_rendimento` | FLOAT | Indicador de rendimento (P) dos Anos Finais do EF: fluxo escolar 0-1 usado no calculo do IDEB (IDEB = nota media padronizada x P). |
| `ideb_em_observado` | FLOAT | IDEB observado no Ensino Medio no Brasil. |
| `ideb_em_meta` | FLOAT | Meta projetada do IDEB no Ensino Medio. |
| `ideb_em_mat` | FLOAT | Nota SAEB media em Matematica no Ensino Medio. |
| `ideb_em_lp` | FLOAT | Nota SAEB media em Lingua Portuguesa no Ensino Medio. |
| `ideb_em_nota_media` | FLOAT | Nota SAEB media padronizada no Ensino Medio. |
| `ideb_em_indicador_rendimento` | FLOAT | Indicador de rendimento (P) do Ensino Medio: fluxo escolar 0-1 usado no calculo do IDEB (IDEB = nota media padronizada x P). |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de quando este registro foi gerado na camada semantica. |

## semantic · obt_inep_ideb_escola_ano

File `semantic__obt_inep_ideb_escola_ano.parquet` · 798,779 rows · 24 columns

IDEB por escola, nivel educacional e ano. Grao: 1 linha por (id_escola, nivel, ano, rede). EF: 2005-2023 bienal. EM: 2017-2023. FK: codigo_municipio para obt_ibge_municipio. Origem: trusted_zone.inep_ideb_escola. INEP.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/inep_ideb_escola`

| Column | Type | Description |
|---|---|---|
| `nivel` | STRING | Nivel: anos_iniciais (EF 1-5), anos_finais (EF 6-9), ensino_medio. |
| `ano` | INTEGER | Ano de referencia do IDEB (bienal). |
| `codigo_uf` | INTEGER | Codigo IBGE numerico da UF (2 digitos). |
| `nome_uf` | STRING | Nome da UF. |
| `sigla_uf` | STRING | Sigla da UF (2 letras). |
| `codigo_regiao` | INTEGER | Codigo IBGE da regiao geografica. |
| `nome_regiao` | STRING | Nome da regiao geografica. |
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (INT64). FK para obt_ibge_municipio. |
| `nome_municipio` | STRING | Nome do municipio. |
| `codigo_escola` | INTEGER | Codigo INEP da escola (INT64). |
| `nome_escola` | STRING | Nome da escola. |
| `uf` | STRING | Alias historico de sigla_uf, mantido para compatibilidade com dashboards existentes. |
| `regiao` | STRING | Alias historico de nome_regiao, mantido para compatibilidade com dashboards existentes. |
| `municipio` | STRING | Alias historico de nome_municipio, mantido para compatibilidade com dashboards existentes. |
| `id_escola` | INTEGER | Alias historico de codigo_escola, mantido para compatibilidade com dashboards existentes. |
| `escola` | STRING | Alias historico de nome_escola, mantido para compatibilidade com dashboards existentes. |
| `rede` | STRING | Rede: Total, Publica, Federal, Estadual, Municipal, Privada. |
| `ideb_observado` | FLOAT | Nota IDEB observada (0-10). |
| `ideb_meta` | FLOAT | Meta projetada do IDEB. |
| `nota_saeb_lp` | FLOAT | Nota SAEB Lingua Portuguesa (componente IDEB). |
| `nota_saeb_mat` | FLOAT | Nota SAEB Matematica (componente IDEB). |
| `nota_saeb_total` | FLOAT | Nota SAEB media combinada (componente IDEB). |
| `indicador_rendimento` | FLOAT | Indicador de rendimento (P): fluxo escolar 0-1, componente do IDEB (IDEB = nota_saeb_total x P). |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |

## semantic · obt_inep_ideb_municipio_ano

File `semantic__obt_inep_ideb_municipio_ano.parquet` · 181,677 rows · 31 columns

IDEB por municipio, rede e ano, com AI, AF e EM pivotados em colunas. Grao: 1 linha por (codigo_municipio, ano, rede). Redes no nivel municipal: Publica, Municipal, Estadual e Federal (o INEP nao publica Privada/Total por municipio). Mantem formato wide historico da OBT. FK: codigo_municipio para obt_ibge_municipio. Origem: trusted_zone.inep_ideb_municipio. INEP.

**Built from:** `semantic/obt_ibge_municipio`, `trusted/inep_ideb_municipio`

| Column | Type | Description |
|---|---|---|
| `codigo_municipio` | INTEGER | Codigo IBGE do municipio (INT64). FK para obt_ibge_municipio. Chave primaria composta com ano. |
| `nome_municipio` | STRING | Nome do municipio. |
| `codigo_uf` | INTEGER | Codigo IBGE numerico da UF (2 digitos). |
| `nome_uf` | STRING | Nome da UF. |
| `sigla_uf` | STRING | Sigla da UF (2 letras). |
| `codigo_regiao` | INTEGER | Codigo IBGE da regiao geografica. |
| `nome_regiao` | STRING | Nome da regiao geografica. |
| `uf` | STRING | Alias historico de sigla_uf, mantido para compatibilidade com dashboards existentes. |
| `regiao` | STRING | Alias historico de nome_regiao, mantido para compatibilidade com dashboards existentes. |
| `municipio` | STRING | Alias historico de nome_municipio, mantido para compatibilidade com dashboards existentes. |
| `ano` | INTEGER | Ano de referencia do IDEB (bienal). Chave primaria composta com codigo_municipio. |
| `rede` | STRING | Dependencia administrativa (rede) da agregacao municipal: Publica (rede publica consolidada), Municipal, Estadual ou Federal. Faz parte do grao — sempre filtre a rede desejada para nao somar redes sobrepostas (Publica ja contem Municipal+Estadual+Federal). |
| `ideb_ai_observado` | FLOAT | IDEB observado anos iniciais EF (rede Total). NULL em anos sem avaliacao. |
| `ideb_ai_meta` | FLOAT | Meta projetada IDEB anos iniciais EF. |
| `ideb_ai_mat` | FLOAT | Nota SAEB Matematica anos iniciais EF. |
| `ideb_ai_lp` | FLOAT | Nota SAEB Lingua Portuguesa anos iniciais EF. |
| `ideb_ai_nota_media` | FLOAT | Nota SAEB media padronizada - Anos Iniciais. |
| `ideb_ai_indicador_rendimento` | FLOAT | Indicador de rendimento (P) - Anos Iniciais: fluxo escolar 0-1 usado no calculo do IDEB (IDEB = nota media padronizada x P). |
| `ideb_af_observado` | FLOAT | IDEB observado anos finais EF (rede Total). NULL em anos sem avaliacao. |
| `ideb_af_meta` | FLOAT | Meta projetada IDEB anos finais EF. |
| `ideb_af_mat` | FLOAT | Nota SAEB Matematica anos finais EF. |
| `ideb_af_lp` | FLOAT | Nota SAEB Lingua Portuguesa anos finais EF. |
| `ideb_af_nota_media` | FLOAT | Nota SAEB media padronizada - Anos Finais. |
| `ideb_af_indicador_rendimento` | FLOAT | Indicador de rendimento (P) - Anos Finais: fluxo escolar 0-1 usado no calculo do IDEB (IDEB = nota media padronizada x P). |
| `ideb_em_observado` | FLOAT | IDEB observado Ensino Medio (rede Total). Disponivel a partir de 2017. |
| `ideb_em_meta` | FLOAT | Meta projetada IDEB Ensino Medio. |
| `ideb_em_mat` | FLOAT | Nota SAEB Matematica Ensino Medio. |
| `ideb_em_lp` | FLOAT | Nota SAEB Lingua Portuguesa Ensino Medio. |
| `ideb_em_nota_media` | FLOAT | Nota SAEB media padronizada - Ensino Medio. |
| `ideb_em_indicador_rendimento` | FLOAT | Indicador de rendimento (P) - Ensino Medio: fluxo escolar 0-1 usado no calculo do IDEB (IDEB = nota media padronizada x P). |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de geracao na camada semantica. |

## semantic · obt_inep_ideb_regiao_ano

File `semantic__obt_inep_ideb_regiao_ano.parquet` · 1,408 rows · 29 columns

IDEB por regiao geografica e Unidade da Federacao, ano e rede, com AI, AF e EM pivotados em colunas. Grao: 1 linha por (tipo_unidade, codigo_regiao/codigo_uf, ano, rede). Origem: trusted_zone.inep_ideb_regioes_ufs.

**Built from:** `semantic/obt_ibge_uf`, `trusted/inep_ideb_regioes_ufs`

| Column | Type | Description |
|---|---|---|
| `tipo_unidade` | STRING | Tipo: 'regiao' (5 regioes) ou 'uf' (27 UFs). |
| `codigo_uf` | INTEGER | Codigo IBGE numerico da UF (2 digitos). NULL para linhas de regiao. |
| `nome_uf` | STRING | Nome da UF. NULL para linhas de regiao. |
| `sigla_uf` | STRING | Sigla da UF (2 letras). NULL para linhas de regiao. |
| `codigo_regiao` | INTEGER | Codigo IBGE da regiao geografica. |
| `nome_regiao` | STRING | Nome da regiao geografica. |
| `unidade_geografica` | STRING | Alias historico: unidade geografica original do INEP (regiao ou UF). |
| `sg_uf` | STRING | Alias historico da sigla da UF. NULL para linhas de regiao. |
| `ano` | INTEGER | Ano de referencia do IDEB (bienal: 2005, 2007, ..., 2023). |
| `rede` | STRING | Dependencia administrativa: Total, Publica, Federal, Estadual, Municipal, Privada. |
| `ideb_ai_observado` | FLOAT | IDEB observado nos Anos Iniciais do EF (1-5 ano) na unidade geografica. |
| `ideb_ai_meta` | FLOAT | Meta projetada do IDEB nos Anos Iniciais do EF. NULL em 2005 e 2023. |
| `ideb_ai_mat` | FLOAT | Nota SAEB media em Matematica nos Anos Iniciais do EF. |
| `ideb_ai_lp` | FLOAT | Nota SAEB media em Lingua Portuguesa nos Anos Iniciais do EF. |
| `ideb_ai_nota_media` | FLOAT | Nota SAEB media padronizada (LP + Mat) nos Anos Iniciais do EF. |
| `ideb_ai_indicador_rendimento` | FLOAT | Indicador de rendimento (P) - Anos Iniciais: fluxo escolar 0-1 usado no calculo do IDEB (IDEB = nota media padronizada x P). |
| `ideb_af_observado` | FLOAT | IDEB observado nos Anos Finais do EF (6-9 ano) na unidade geografica. |
| `ideb_af_meta` | FLOAT | Meta projetada do IDEB nos Anos Finais do EF. NULL em 2005 e 2023. |
| `ideb_af_mat` | FLOAT | Nota SAEB media em Matematica nos Anos Finais do EF. |
| `ideb_af_lp` | FLOAT | Nota SAEB media em Lingua Portuguesa nos Anos Finais do EF. |
| `ideb_af_nota_media` | FLOAT | Nota SAEB media padronizada nos Anos Finais do EF. |
| `ideb_af_indicador_rendimento` | FLOAT | Indicador de rendimento (P) - Anos Finais: fluxo escolar 0-1 usado no calculo do IDEB (IDEB = nota media padronizada x P). |
| `ideb_em_observado` | FLOAT | IDEB observado no Ensino Medio na unidade geografica. |
| `ideb_em_meta` | FLOAT | Meta projetada do IDEB no Ensino Medio. NULL em 2005 e 2023. |
| `ideb_em_mat` | FLOAT | Nota SAEB media em Matematica no Ensino Medio. |
| `ideb_em_lp` | FLOAT | Nota SAEB media em Lingua Portuguesa no Ensino Medio. |
| `ideb_em_nota_media` | FLOAT | Nota SAEB media padronizada no Ensino Medio. |
| `ideb_em_indicador_rendimento` | FLOAT | Indicador de rendimento (P) - Ensino Medio: fluxo escolar 0-1 usado no calculo do IDEB (IDEB = nota media padronizada x P). |
| `data_carga_semantica` | TIMESTAMP | Timestamp UTC de quando este registro foi gerado na camada semantica. |
