# School Census (INEP): Raw and Trusted

Dataset: [lucasrangelss/censo-escolar-raw-trusted-part-3](https://www.kaggle.com/datasets/lucasrangelss/censo-escolar-raw-trusted-part-3) · snapshot 2026-10-01 · 30 tables · 55,639,423 rows

**Source:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP), [https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar)

Yearly School Census microdata at school level: schools, classes, teachers, enrolments and infrastructure, with the historical series recovered from 1995. Student-level and teacher-level microdata are not released.

**Grain and keys:** School by year for the school tables; the semantic tables aggregate to school-year and municipality-year. The 2025 edition changed the enrolment file from student level to school-level aggregates.

**Layers.** `raw` is the source snapshot as delivered. `trusted` is typed, deduplicated and named consistently. `semantic` joins and reshapes trusted tables for analysis. Every table is a Parquet file named `<layer>__<table>.parquet` at the root of the dataset.

The full interactive map (lineage, joins, search) is at [https://rangeltech.net/datamap/](https://rangeltech.net/datamap/). Column descriptions come from the source lake's catalogue and are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns | Described | Upstream |
|---|---|---:|---:|---:|---|
| raw | [`inep_censo_escolar_curso_tecnico`](#raw-inep-censo-escolar-curso-tecnico) | 32,136 | 25 | 25 | source |
| raw | [`inep_censo_escolar_dados_desp`](#raw-inep-censo-escolar-dados-desp) | 49,642 | 29 | 29 | source |
| raw | [`inep_censo_escolar_dadoscurso`](#raw-inep-censo-escolar-dadoscurso) | 25,572 | 33 | 33 | source |
| raw | [`inep_censo_escolar_educprof`](#raw-inep-censo-escolar-educprof) | 323,177 | 184 | 184 | source |
| raw | [`inep_censo_escolar_em11`](#raw-inep-censo-escolar-em11) | 19,617 | 21 | 21 | source |
| raw | [`inep_censo_escolar_em12`](#raw-inep-censo-escolar-em12) | 58,310 | 18 | 18 | source |
| raw | [`inep_censo_escolar_em22`](#raw-inep-censo-escolar-em22) | 1,201 | 22 | 22 | source |
| raw | [`inep_censo_escolar_em8`](#raw-inep-censo-escolar-em8) | 24,893 | 24 | 24 | source |
| raw | [`inep_censo_escolar_es6`](#raw-inep-censo-escolar-es6) | 406 | 20 | 20 | source |
| raw | [`inep_censo_escolar_escola`](#raw-inep-censo-escolar-escola) | 214,192 | 307 | 307 | source |
| raw | [`inep_censo_escolar_gestor_escolar`](#raw-inep-censo-escolar-gestor-escolar) | 180,540 | 70 | 70 | source |
| raw | [`inep_censo_escolar_indicesc`](#raw-inep-censo-escolar-indicesc) | 877,062 | 199 | 199 | source |
| raw | [`inep_censo_escolar_indicreg`](#raw-inep-censo-escolar-indicreg) | 270,956 | 195 | 195 | source |
| raw | [`inep_censo_escolar_matricula`](#raw-inep-censo-escolar-matricula) | 178,766 | 242 | 242 | source |
| raw | [`inep_censo_escolar_medprof`](#raw-inep-censo-escolar-medprof) | 102,591 | 43 | 43 | source |
| raw | [`inep_censo_escolar_microdados_ed_basica`](#raw-inep-censo-escolar-microdados-ed-basica) | 4,058,464 | 479 | 479 | source |
| raw | [`inep_censo_escolar_suplemento_cursos_tecnicos`](#raw-inep-censo-escolar-suplemento-cursos-tecnicos) | 50,740 | 34 | 34 | source |
| raw | [`inep_censo_escolar_turma`](#raw-inep-censo-escolar-turma) | 178,772 | 195 | 195 | source |
| trusted | [`inep_censo_escolar_colunas_fonte`](#trusted-inep-censo-escolar-colunas-fonte) | 29,684 | 8 | 8 | source |
| trusted | [`inep_censo_escolar_cursos_tecnicos`](#trusted-inep-censo-escolar-cursos-tecnicos) | 82,876 | 39 | 39 | source |
| trusted | [`inep_censo_escolar_dicionario_campos`](#trusted-inep-censo-escolar-dicionario-campos) | 28,786 | 11 | 11 | source |
| trusted | [`inep_censo_escolar_docentes`](#trusted-inep-censo-escolar-docentes) | 4,237,236 | 160 | 160 | source |
| trusted | [`inep_censo_escolar_educacao_profissional`](#trusted-inep-censo-escolar-educacao-profissional) | 4,911,299 | 295 | 295 | source |
| trusted | [`inep_censo_escolar_escolas`](#trusted-inep-censo-escolar-escolas) | 7,376,443 | 102 | 102 | `inep_censo_escolar_escola` |
| trusted | [`inep_censo_escolar_etapas_ensino`](#trusted-inep-censo-escolar-etapas-ensino) | 4,808,966 | 713 | 713 | source |
| trusted | [`inep_censo_escolar_gestores`](#trusted-inep-censo-escolar-gestores) | 4,239,004 | 69 | 69 | source |
| trusted | [`inep_censo_escolar_infraestrutura`](#trusted-inep-censo-escolar-infraestrutura) | 7,376,443 | 134 | 134 | `inep_censo_escolar_escola` |
| trusted | [`inep_censo_escolar_localizacao`](#trusted-inep-censo-escolar-localizacao) | 7,427,183 | 39 | 39 | source |
| trusted | [`inep_censo_escolar_matriculas`](#trusted-inep-censo-escolar-matriculas) | 4,237,230 | 247 | 247 | `inep_censo_escolar_matricula` |
| trusted | [`inep_censo_escolar_turmas`](#trusted-inep-censo-escolar-turmas) | 4,237,236 | 194 | 194 | `inep_censo_escolar_turma` |

## raw · inep_censo_escolar_curso_tecnico

File `raw__inep_censo_escolar_curso_tecnico.parquet` · 32,136 rows · 25 columns

Raw Censo Escolar INEP. Familia de CSV: curso_tecnico. Anos cobertos: 2025-2025 (1 ano(s)): 2025. Arquivos de origem: Tabela_Curso_Tecnico_2025.csv. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano de realização do Censo Escolar (formato YYYY). — descrição gerada por IA. |
| `CO_ENTIDADE` | STRING | Código INEP identificador único da escola/entidade de ensino. — descrição gerada por IA. |
| `NO_AREA_CURSO_PROFISSIONAL` | STRING | Nome do eixo tecnológico ou área profissional do curso técnico. — descrição gerada por IA. |
| `ID_AREA_CURSO_PROFISSIONAL` | STRING | Código identificador da área profissional do curso. — descrição gerada por IA. |
| `NO_CURSO_EDUC_PROFISSIONAL` | STRING | Nome oficial do curso técnico de educação profissional. — descrição gerada por IA. |
| `CO_CURSO_EDUC_PROFISSIONAL` | STRING | Código de identificação do curso técnico no sistema INEP/MEC. — descrição gerada por IA. |
| `QT_CURSO_TEC` | STRING | Quantidade total de turmas/ofertas do curso técnico na instituição. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC` | STRING | Quantidade total de alunos matriculados no curso técnico. — descrição gerada por IA. |
| `QT_CURSO_TEC_IFTP` | STRING | Quantidade de cursos técnicos via Itinerário de Formação Técnica e Profissional (Novo Ensino Médio). — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_IFTP` | STRING | Quantidade de matrículas em cursos técnicos via Itinerário de Formação Técnica e Profissional. — descrição gerada por IA. |
| `QT_CURSO_TEC_NM` | STRING | Quantidade de cursos técnicos oferecidos na modalidade integrada ao Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_NM` | STRING | Quantidade de matrículas no curso técnico integrado ao Ensino Médio. — descrição gerada por IA. |
| `QT_CURSO_TEC_CONC` | STRING | Quantidade de cursos técnicos oferecidos na modalidade concomitante ao Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_CONC` | STRING | Quantidade de matrículas no curso técnico concomitante ao Ensino Médio. — descrição gerada por IA. |
| `QT_CURSO_TEC_SUBS` | STRING | Quantidade de cursos técnicos oferecidos na modalidade subsequente (pós-médio). — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_SUBS` | STRING | Quantidade de matrículas no curso técnico subsequente. — descrição gerada por IA. |
| `QT_CURSO_TEC_IFTP_CT` | STRING | Quantidade de cursos técnicos concomitantes no Itinerário de Formação Técnica e Profissional. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_IFTP_CT` | STRING | Quantidade de matrículas concomitantes no Itinerário de Formação Técnica e Profissional. — descrição gerada por IA. |
| `QT_CURSO_TEC_EJA` | STRING | Quantidade de cursos técnicos integrados à Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_EJA` | STRING | Quantidade de matrículas no curso técnico integrado à EJA. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_dados_desp

File `raw__inep_censo_escolar_dados_desp.parquet` · 49,642 rows · 29 columns

Raw Censo Escolar INEP. Familia de CSV: dados_desp. Anos cobertos: 1995-1995 (1 ano(s)): 1995. Arquivos de origem: DADOS_DESP_1995.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `MASCARA` | STRING | Código identificador ou máscara da escola no Censo Escolar de 1995. — descrição gerada por IA. |
| `NU_ANO` | STRING | Ano letivo de referência dos dados (ex: 1995). — descrição gerada por IA. |
| `CO_IBGE` | STRING | Código IBGE de identificação do município. — descrição gerada por IA. |
| `UF` | STRING | Nome do Estado (Unidade da Federação) da escola. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla do Estado (UF) onde a escola se localiza. — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do município onde a escola se localiza. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa da escola (ex: Estadual, Municipal, Privada). — descrição gerada por IA. |
| `LOC` | STRING | Localização do estabelecimento de ensino (Urbana ou Rural). — descrição gerada por IA. |
| `CODFUNC` | STRING | Situação de funcionamento da escola (ex: Ativo). — descrição gerada por IA. |
| `NIVELPRE` | STRING | Indicador ou número de alunos/turmas praticantes na Pré-Escola. — descrição gerada por IA. |
| `NIV_1GRAU` | STRING | Indicador ou número de alunos/turmas praticantes no 1º Grau (atual Ensino Fundamental). — descrição gerada por IA. |
| `NIV_2GRAU` | STRING | Indicador ou número de alunos/turmas praticantes no 2º Grau (atual Ensino Médio). — descrição gerada por IA. |
| `ENSSUPLET` | STRING | Indicador ou número de alunos/turmas praticantes no Ensino Supletivo (EJA). — descrição gerada por IA. |
| `CO_MODALIDADE` | STRING | Código numérico de identificação da modalidade esportiva. — descrição gerada por IA. |
| `DS_MODALID` | STRING | Nome/descrição da modalidade esportiva (ex: ATLETISMO, FUTEBOL). — descrição gerada por IA. |
| `VDE101` | STRING | Variável quantitativa do Censo sobre participantes/turmas da modalidade (Série/Série 1). — descrição gerada por IA. |
| `VDE102` | STRING | Variável quantitativa do Censo sobre participantes/turmas da modalidade (Série/Série 2). — descrição gerada por IA. |
| `VDE103` | STRING | Variável quantitativa do Censo sobre participantes/turmas da modalidade (Série/Série 3). — descrição gerada por IA. |
| `VDE104` | STRING | Variável quantitativa do Censo sobre participantes/turmas da modalidade (Série/Série 4). — descrição gerada por IA. |
| `VDE105` | STRING | Variável quantitativa do Censo sobre participantes/turmas da modalidade (Série/Série 5). — descrição gerada por IA. |
| `VDE106` | STRING | Variável quantitativa do Censo sobre participantes/turmas da modalidade (Série/Série 6). — descrição gerada por IA. |
| `VDE107` | STRING | Variável quantitativa do Censo sobre participantes/turmas da modalidade (Série/Série 7). — descrição gerada por IA. |
| `VDE108` | STRING | Variável quantitativa do Censo sobre participantes/turmas da modalidade (Série/Série 8). — descrição gerada por IA. |
| `VDE109` | STRING | Variável quantitativa do Censo sobre participantes/turmas da modalidade (não-seriado/outros). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_dadoscurso

File `raw__inep_censo_escolar_dadoscurso.parquet` · 25,572 rows · 33 columns

Raw Censo Escolar INEP. Familia de CSV: dadoscurso. Anos cobertos: 1995-1995 (1 ano(s)): 1995. Arquivos de origem: DADOSCURSO_1995.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `MASCARA` | STRING | Código alfanumérico de identificação da escola utilizado no Censo Escolar de 1995. — descrição gerada por IA. |
| `CO_IBGE` | STRING | Código IBGE de identificação do município/localidade da escola. — descrição gerada por IA. |
| `UF` | STRING | Nome da Unidade da Federação (Estado) onde a escola está localizada. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla de duas letras da Unidade da Federação (ex: PE, RN). — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do município de localização da escola. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa da escola (ex: Estadual, Municipal, Privada). — descrição gerada por IA. |
| `LOC` | STRING | Localização do estabelecimento de ensino (Urbana ou Rural). — descrição gerada por IA. |
| `CODFUNC` | STRING | Situação de funcionamento da escola (ex: Ativo). — descrição gerada por IA. |
| `NIVELPRE` | STRING | Indicador de atendimento na etapa de Pré-escola / Educação Infantil. — descrição gerada por IA. |
| `NIV_1GRAU` | STRING | Indicador de atendimento na etapa de Ensino de 1º Grau (Ensino Fundamental). — descrição gerada por IA. |
| `NIV_2GRAU` | STRING | Indicador de atendimento na etapa de Ensino de 2º Grau (Ensino Médio). — descrição gerada por IA. |
| `ENSSUPLET` | STRING | Indicador de atendimento em modalidade de Ensino Supletivo (EJA). — descrição gerada por IA. |
| `NU_ANO` | STRING | Ano de referência dos dados do Censo (ex: 1995). — descrição gerada por IA. |
| `CO_CURSO` | STRING | Código numérico do curso ou habilitação profissional ofertada. — descrição gerada por IA. |
| `DS_CURSO` | STRING | Descrição do curso ou habilitação técnica (ex: HABILIT AGROPEC, OUTRAS). — descrição gerada por IA. |
| `VEM3001` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3001). — descrição gerada por IA. |
| `VEM3002` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3002). — descrição gerada por IA. |
| `VEM3003` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3003). — descrição gerada por IA. |
| `VEM3004` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3004). — descrição gerada por IA. |
| `VEM3005` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3005). — descrição gerada por IA. |
| `VEM3006` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3006). — descrição gerada por IA. |
| `VEM3007` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3007). — descrição gerada por IA. |
| `VEM3008` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3008). — descrição gerada por IA. |
| `VEM3009` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3009). — descrição gerada por IA. |
| `VEM3010` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3010). — descrição gerada por IA. |
| `VEM3011` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3011). — descrição gerada por IA. |
| `VEM3012` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3012). — descrição gerada por IA. |
| `VEM3013` | STRING | Variável quantitativa do Censo 1995 relativa a matrículas/turmas do curso (campo 3013). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_educprof

File `raw__inep_censo_escolar_educprof.parquet` · 323,177 rows · 184 columns

Raw Censo Escolar INEP. Familia de CSV: educprof. Anos cobertos: 1998-2006 (8 ano(s)): 1998, 1999, 2001, 2002, 2003, 2004, 2005, 2006. Arquivos de origem: EDUCPROF_1998.CSV, EDUCPROF_1999.CSV, EDUCPROF_2001.CSV, EDUCPROF_2002.CSV, EDUCPROF_2003.CSV, EDUCPROF_2004.CSV, EDUCPROF_2005.CSV, EDUCPROF_2006.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `MASCARA` | STRING | Código identificador mascarado da escola no Censo Escolar. — descrição gerada por IA. |
| `ANO` | STRING | Ano letivo de referência das informações registradas no censo. — descrição gerada por IA. |
| `CODMUNIC` | STRING | Código IBGE/INEP do município onde a escola está localizada. — descrição gerada por IA. |
| `UF` | STRING | Nome da Unidade Federativa (Estado) da escola. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla de dois caracteres da Unidade Federativa (ex: RO, SP). — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do município onde se localiza a instituição de ensino. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa da escola (ex: Federal, Estadual, Municipal, Privada). — descrição gerada por IA. |
| `LOC` | STRING | Localização da escola (Urbana ou Rural). — descrição gerada por IA. |
| `CODFUNC` | STRING | Situação de funcionamento da escola ou do curso (ex: Ativo). — descrição gerada por IA. |
| `CODCURSO` | STRING | Código do curso técnico ou profissionalizante. — descrição gerada por IA. |
| `NOMECUR` | STRING | Nome do curso técnico ou profissional ofertado. — descrição gerada por IA. |
| `EM1513` | STRING | Contagem de matrículas em etapa/série específica do ensino médio técnico (código Censo 1513). — descrição gerada por IA. |
| `EM1514` | STRING | Contagem de matrículas em etapa/série específica do ensino médio técnico (código Censo 1514). — descrição gerada por IA. |
| `EM1515` | STRING | Contagem de matrículas em etapa/série específica do ensino médio técnico (código Censo 1515). — descrição gerada por IA. |
| `EM1214` | STRING | Contagem de matrículas no ensino médio/técnico para o código de etapa 1214. — descrição gerada por IA. |
| `EM1215` | STRING | Contagem de matrículas no ensino médio/técnico para o código de etapa 1215. — descrição gerada por IA. |
| `EM1216` | STRING | Contagem de matrículas no ensino médio/técnico para o código de etapa 1216. — descrição gerada por IA. |
| `EM1217` | STRING | Contagem de matrículas no ensino médio/técnico para o código de etapa 1217. — descrição gerada por IA. |
| `EM1218` | STRING | Contagem de matrículas no ensino médio/técnico para o código de etapa 1218. — descrição gerada por IA. |
| `EM1219` | STRING | Contagem de matrículas no ensino médio/técnico para o código de etapa 1219. — descrição gerada por IA. |
| `NOME_CUR` | STRING | Nome alternativo ou complementar do curso técnico. — descrição gerada por IA. |
| `GRD_COD` | STRING | Código da grade curricular ou programa educacional do curso. — descrição gerada por IA. |
| `AREA_COD` | STRING | Código da área profissional do curso técnico. — descrição gerada por IA. |
| `SUBAREAC` | STRING | Código da subárea de conhecimento ou habilitação profissional. — descrição gerada por IA. |
| `VEP111` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP111). — descrição gerada por IA. |
| `VEP112` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP112). — descrição gerada por IA. |
| `VEP113` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP113). — descrição gerada por IA. |
| `VPE114` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VPE114). — descrição gerada por IA. |
| `VEP115` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP115). — descrição gerada por IA. |
| `VEP116` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP116). — descrição gerada por IA. |
| `VEP117` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP117). — descrição gerada por IA. |
| `VEP121` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP121). — descrição gerada por IA. |
| `VEP122` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP122). — descrição gerada por IA. |
| `VEP123` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP123). — descrição gerada por IA. |
| `VEP124` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP124). — descrição gerada por IA. |
| `VEP125` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP125). — descrição gerada por IA. |
| `VEP126` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP126). — descrição gerada por IA. |
| `VEP127` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP127). — descrição gerada por IA. |
| `VEP118` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP118). — descrição gerada por IA. |
| `VEP119` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP119). — descrição gerada por IA. |
| `VEP128` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP128). — descrição gerada por IA. |
| `VEP129` | STRING | Indicador estatístico de vagas/matrículas de Educação Profissional (categoria VEP129). — descrição gerada por IA. |
| `DEP131` | STRING | Indicador de desligamento ou aproveitamento em curso profissional (código DEP131). — descrição gerada por IA. |
| `DEP132` | STRING | Indicador de desligamento ou aproveitamento em curso profissional (código DEP132). — descrição gerada por IA. |
| `DEP133` | STRING | Indicador de desligamento ou aproveitamento em curso profissional (código DEP133). — descrição gerada por IA. |
| `DEP134` | STRING | Indicador de desligamento ou aproveitamento em curso profissional (código DEP134). — descrição gerada por IA. |
| `DEP135` | STRING | Indicador de desligamento ou aproveitamento em curso profissional (código DEP135). — descrição gerada por IA. |
| `DEP136` | STRING | Indicador de desligamento ou aproveitamento em curso profissional (código DEP136). — descrição gerada por IA. |
| `DEP137` | STRING | Indicador de desligamento ou aproveitamento em curso profissional (código DEP137). — descrição gerada por IA. |
| `NEP141` | STRING | Número de novos alunos ou ingressantes na Educação Profissional (código NEP141). — descrição gerada por IA. |
| `NEP142` | STRING | Número de novos alunos ou ingressantes na Educação Profissional (código NEP142). — descrição gerada por IA. |
| `NEP143` | STRING | Número de novos alunos ou ingressantes na Educação Profissional (código NEP143). — descrição gerada por IA. |
| `NEP144` | STRING | Número de novos alunos ou ingressantes na Educação Profissional (código NEP144). — descrição gerada por IA. |
| `NEP145` | STRING | Número de novos alunos ou ingressantes na Educação Profissional (código NEP145). — descrição gerada por IA. |
| `NEP146` | STRING | Número de novos alunos ou ingressantes na Educação Profissional (código NEP146). — descrição gerada por IA. |
| `NEP147` | STRING | Número de novos alunos ou ingressantes na Educação Profissional (código NEP147). — descrição gerada por IA. |
| `DEP138` | STRING | Indicador de desligamento ou aproveitamento em curso profissional (código DEP138). — descrição gerada por IA. |
| `DEP139` | STRING | Indicador de desligamento ou aproveitamento em curso profissional (código DEP139). — descrição gerada por IA. |
| `NEP148` | STRING | Número de novos alunos ou ingressantes na Educação Profissional (código NEP148). — descrição gerada por IA. |
| `NEP149` | STRING | Número de novos alunos ou ingressantes na Educação Profissional (código NEP149). — descrição gerada por IA. |
| `EP111` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP111). — descrição gerada por IA. |
| `EP112` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP112). — descrição gerada por IA. |
| `EP113` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP113). — descrição gerada por IA. |
| `EP114` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP114). — descrição gerada por IA. |
| `EP115` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP115). — descrição gerada por IA. |
| `EP116` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP116). — descrição gerada por IA. |
| `EP117` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP117). — descrição gerada por IA. |
| `EP121` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP121). — descrição gerada por IA. |
| `EP122` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP122). — descrição gerada por IA. |
| `EP123` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP123). — descrição gerada por IA. |
| `EP124` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP124). — descrição gerada por IA. |
| `EP125` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP125). — descrição gerada por IA. |
| `EP126` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP126). — descrição gerada por IA. |
| `EP127` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP127). — descrição gerada por IA. |
| `EP118` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP118). — descrição gerada por IA. |
| `EP119` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP119). — descrição gerada por IA. |
| `EP128` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP128). — descrição gerada por IA. |
| `EP129` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP129). — descrição gerada por IA. |
| `EP131` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP131). — descrição gerada por IA. |
| `EP132` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP132). — descrição gerada por IA. |
| `EP133` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP133). — descrição gerada por IA. |
| `EP134` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP134). — descrição gerada por IA. |
| `EP135` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP135). — descrição gerada por IA. |
| `EP136` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP136). — descrição gerada por IA. |
| `EP137` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP137). — descrição gerada por IA. |
| `EP141` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP141). — descrição gerada por IA. |
| `EP142` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP142). — descrição gerada por IA. |
| `EP143` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP143). — descrição gerada por IA. |
| `EP144` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP144). — descrição gerada por IA. |
| `EP145` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP145). — descrição gerada por IA. |
| `EP146` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP146). — descrição gerada por IA. |
| `EP147` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP147). — descrição gerada por IA. |
| `EP138` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP138). — descrição gerada por IA. |
| `EP139` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP139). — descrição gerada por IA. |
| `EP148` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP148). — descrição gerada por IA. |
| `EP149` | STRING | Matrículas na Educação Profissional por recorte/etapa (código EP149). — descrição gerada por IA. |
| `COD_CUR` | STRING | Código do curso técnico (variação de nomenclatura do Censo). — descrição gerada por IA. |
| `CARG_HOR` | STRING | Carga horária total do curso em horas. — descrição gerada por IA. |
| `SUB` | STRING | Subárea ou módulo funcional do curso profissional. — descrição gerada por IA. |
| `ART` | STRING | Tipo de articulação do curso profissionalizante (ex: Integrado, Concomitante, Subsequente). — descrição gerada por IA. |
| `EP211` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP211). — descrição gerada por IA. |
| `EP212` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP212). — descrição gerada por IA. |
| `EP213` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP213). — descrição gerada por IA. |
| `EP214` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP214). — descrição gerada por IA. |
| `EP215` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP215). — descrição gerada por IA. |
| `EP216` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP216). — descrição gerada por IA. |
| `EP217` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP217). — descrição gerada por IA. |
| `EP221` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP221). — descrição gerada por IA. |
| `EP222` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP222). — descrição gerada por IA. |
| `EP223` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP223). — descrição gerada por IA. |
| `EP224` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP224). — descrição gerada por IA. |
| `EP225` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP225). — descrição gerada por IA. |
| `EP226` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP226). — descrição gerada por IA. |
| `EP227` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP227). — descrição gerada por IA. |
| `EP218` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP218). — descrição gerada por IA. |
| `EP219` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP219). — descrição gerada por IA. |
| `EP228` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP228). — descrição gerada por IA. |
| `EP229` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP229). — descrição gerada por IA. |
| `EP23A` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP23A). — descrição gerada por IA. |
| `EP233` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP233). — descrição gerada por IA. |
| `EP234` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP234). — descrição gerada por IA. |
| `EP235` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP235). — descrição gerada por IA. |
| `EP236` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP236). — descrição gerada por IA. |
| `EP237` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP237). — descrição gerada por IA. |
| `EP24A` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP24A). — descrição gerada por IA. |
| `EP243` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP243). — descrição gerada por IA. |
| `EP244` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP244). — descrição gerada por IA. |
| `EP245` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP245). — descrição gerada por IA. |
| `EP246` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP246). — descrição gerada por IA. |
| `EP247` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP247). — descrição gerada por IA. |
| `EP238` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP238). — descrição gerada por IA. |
| `EP239` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP239). — descrição gerada por IA. |
| `EP248` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP248). — descrição gerada por IA. |
| `EP249` | STRING | Matrículas/Turmas em Educação Profissional (grupo EP249). — descrição gerada por IA. |
| `HOR_DIA` | STRING | Carga horária ou quantidade de turmas no turno diurno. — descrição gerada por IA. |
| `HOR_NOIT` | STRING | Carga horária ou quantidade de turmas no turno noturno. — descrição gerada por IA. |
| `MOD_EDPR` | STRING | Modalidade da Educação Profissional ministrada. — descrição gerada por IA. |
| `EP311` | STRING | Indicador complementar Censo de Educação Profissional (código EP311). — descrição gerada por IA. |
| `EP312` | STRING | Indicador complementar Censo de Educação Profissional (código EP312). — descrição gerada por IA. |
| `EP313` | STRING | Indicador complementar Censo de Educação Profissional (código EP313). — descrição gerada por IA. |
| `EP314` | STRING | Indicador complementar Censo de Educação Profissional (código EP314). — descrição gerada por IA. |
| `EP315` | STRING | Indicador complementar Censo de Educação Profissional (código EP315). — descrição gerada por IA. |
| `EP316` | STRING | Indicador complementar Censo de Educação Profissional (código EP316). — descrição gerada por IA. |
| `EP317` | STRING | Indicador complementar Censo de Educação Profissional (código EP317). — descrição gerada por IA. |
| `EP321` | STRING | Indicador complementar Censo de Educação Profissional (código EP321). — descrição gerada por IA. |
| `EP322` | STRING | Indicador complementar Censo de Educação Profissional (código EP322). — descrição gerada por IA. |
| `EP323` | STRING | Indicador complementar Censo de Educação Profissional (código EP323). — descrição gerada por IA. |
| `EP324` | STRING | Indicador complementar Censo de Educação Profissional (código EP324). — descrição gerada por IA. |
| `EP325` | STRING | Indicador complementar Censo de Educação Profissional (código EP325). — descrição gerada por IA. |
| `EP326` | STRING | Indicador complementar Censo de Educação Profissional (código EP326). — descrição gerada por IA. |
| `EP327` | STRING | Indicador complementar Censo de Educação Profissional (código EP327). — descrição gerada por IA. |
| `EP351` | STRING | Indicador complementar Censo de Educação Profissional (código EP351). — descrição gerada por IA. |
| `EP361` | STRING | Indicador complementar Censo de Educação Profissional (código EP361). — descrição gerada por IA. |
| `EP371` | STRING | Indicador complementar Censo de Educação Profissional (código EP371). — descrição gerada por IA. |
| `EP381` | STRING | Indicador complementar Censo de Educação Profissional (código EP381). — descrição gerada por IA. |
| `EP391` | STRING | Indicador complementar Censo de Educação Profissional (código EP391). — descrição gerada por IA. |
| `EP3A1` | STRING | Indicador complementar Censo de Educação Profissional (código EP3A1). — descrição gerada por IA. |
| `EP352` | STRING | Indicador complementar Censo de Educação Profissional (código EP352). — descrição gerada por IA. |
| `EP362` | STRING | Indicador complementar Censo de Educação Profissional (código EP362). — descrição gerada por IA. |
| `EP372` | STRING | Indicador complementar Censo de Educação Profissional (código EP372). — descrição gerada por IA. |
| `EP382` | STRING | Indicador complementar Censo de Educação Profissional (código EP382). — descrição gerada por IA. |
| `EP392` | STRING | Indicador complementar Censo de Educação Profissional (código EP392). — descrição gerada por IA. |
| `EP3A2` | STRING | Indicador complementar Censo de Educação Profissional (código EP3A2). — descrição gerada por IA. |
| `EP33A` | STRING | Indicador complementar Censo de Educação Profissional (código EP33A). — descrição gerada por IA. |
| `EP333` | STRING | Indicador complementar Censo de Educação Profissional (código EP333). — descrição gerada por IA. |
| `EP334` | STRING | Indicador complementar Censo de Educação Profissional (código EP334). — descrição gerada por IA. |
| `EP335` | STRING | Indicador complementar Censo de Educação Profissional (código EP335). — descrição gerada por IA. |
| `EP336` | STRING | Indicador complementar Censo de Educação Profissional (código EP336). — descrição gerada por IA. |
| `EP337` | STRING | Indicador complementar Censo de Educação Profissional (código EP337). — descrição gerada por IA. |
| `EP338` | STRING | Indicador complementar Censo de Educação Profissional (código EP338). — descrição gerada por IA. |
| `EP339` | STRING | Indicador complementar Censo de Educação Profissional (código EP339). — descrição gerada por IA. |
| `EP34A` | STRING | Indicador complementar Censo de Educação Profissional (código EP34A). — descrição gerada por IA. |
| `EP343` | STRING | Indicador complementar Censo de Educação Profissional (código EP343). — descrição gerada por IA. |
| `EP344` | STRING | Indicador complementar Censo de Educação Profissional (código EP344). — descrição gerada por IA. |
| `EP345` | STRING | Indicador complementar Censo de Educação Profissional (código EP345). — descrição gerada por IA. |
| `EP346` | STRING | Indicador complementar Censo de Educação Profissional (código EP346). — descrição gerada por IA. |
| `EP347` | STRING | Indicador complementar Censo de Educação Profissional (código EP347). — descrição gerada por IA. |
| `EP348` | STRING | Indicador complementar Censo de Educação Profissional (código EP348). — descrição gerada por IA. |
| `EP349` | STRING | Indicador complementar Censo de Educação Profissional (código EP349). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_em11

File `raw__inep_censo_escolar_em11.parquet` · 19,617 rows · 21 columns

Raw Censo Escolar INEP. Familia de CSV: em11. Anos cobertos: 1996-1996 (1 ano(s)): 1996. Arquivos de origem: EM11_1996.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `MASCARA` | STRING | Identificador único ou mascarado da escola no Censo Escolar. — descrição gerada por IA. |
| `ANO` | STRING | Ano letivo de referência dos dados. — descrição gerada por IA. |
| `CODMUNIC` | STRING | Código IBGE/INEP do município de localização da escola. — descrição gerada por IA. |
| `UF` | STRING | Nome completo da Unidade da Federação. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla de duas letras do estado (ex: RO, SP). — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do município onde a escola está localizada. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa da escola (ex: Estadual, Municipal, Privada). — descrição gerada por IA. |
| `LOC` | STRING | Localização do estabelecimento de ensino (ex: Urbana, Rural). — descrição gerada por IA. |
| `CODFUNC` | STRING | Situação de funcionamento do estabelecimento (ex: Ativo). — descrição gerada por IA. |
| `CODCURSO` | STRING | Código de identificação do curso técnico ou profissionalizante. — descrição gerada por IA. |
| `NOMECUR` | STRING | Nome do curso oferecido pela escola (ex: Administração, Magistério, Técnico em Contabilidade). — descrição gerada por IA. |
| `EM1111` | STRING | Métrica de alunos/turmas na 1ª série do curso ofertado. — descrição gerada por IA. |
| `EM1112` | STRING | Métrica de alunos/turmas na 2ª série do curso ofertado. — descrição gerada por IA. |
| `EM1113` | STRING | Métrica de alunos/turmas na 3ª série do curso ofertado. — descrição gerada por IA. |
| `EM1114` | STRING | Métrica de alunos/turmas na 4ª série do curso ofertado. — descrição gerada por IA. |
| `EM1115` | STRING | Métrica de alunos/turmas em séries complementares ou total do curso. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_em12

File `raw__inep_censo_escolar_em12.parquet` · 58,310 rows · 18 columns

Raw Censo Escolar INEP. Familia de CSV: em12. Anos cobertos: 1997-1998 (2 ano(s)): 1997, 1998. Arquivos de origem: EM12_1997.CSV, EM12_1998.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `MASCARA` | STRING | Código identificador (máscara) do estabelecimento de ensino no Censo Escolar de 1998. — descrição gerada por IA. |
| `ANO` | STRING | Ano de referência do Censo Escolar (ex: '1998'). — descrição gerada por IA. |
| `CODMUNIC` | STRING | Código de identificação do município da escola (padrão IBGE/INEP). — descrição gerada por IA. |
| `UF` | STRING | Nome da Unidade Federativa onde se localiza a escola. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla da Unidade Federativa (ex: 'RO'). — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do município de localização da escola. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa da escola (ex: 'Estadual', 'Municipal', 'Privada'). — descrição gerada por IA. |
| `LOC` | STRING | Zona de localização da escola ('Urbana' ou 'Rural'). — descrição gerada por IA. |
| `CODFUNC` | STRING | Situação de funcionamento do estabelecimento de ensino (ex: 'Ativo'). — descrição gerada por IA. |
| `CODCURSO` | STRING | Código numérico do curso ou habilitação profissional de Ensino Médio. — descrição gerada por IA. |
| `NOMECUR` | STRING | Nome do curso técnico, magistério ou habilitação profissional ofertada. — descrição gerada por IA. |
| `EM1213` | STRING | Quantidade de matrículas registradas na variável EM1213 da tabela de Ensino Médio do INEP. — descrição gerada por IA. |
| `EM1214` | STRING | Quantidade de matrículas registradas na variável EM1214 da tabela de Ensino Médio do INEP. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_em22

File `raw__inep_censo_escolar_em22.parquet` · 1,201 rows · 22 columns

Raw Censo Escolar INEP. Familia de CSV: em22. Anos cobertos: 2005-2006 (2 ano(s)): 2005, 2006. Arquivos de origem: EM22_2005.CSV, EM22_2006.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `CODESC` | STRING | Código INEP de 8 dígitos que identifica a escola. — descrição gerada por IA. |
| `ANO` | STRING | Ano de referência dos dados do Censo Escolar (ex: '2005'). — descrição gerada por IA. |
| `COD_EM22` | STRING | Código da modalidade, tipo de curso ou habilitação do Ensino Médio na tabela EM22 do Censo 2005. — descrição gerada por IA. |
| `VEM2211` | STRING | Número de matrículas na 1ª série do Ensino Médio (1º turno/diurno). — descrição gerada por IA. |
| `VEM2212` | STRING | Número de matrículas na 2ª série do Ensino Médio (1º turno/diurno). — descrição gerada por IA. |
| `VEM2213` | STRING | Número de matrículas na 3ª série do Ensino Médio (1º turno/diurno). — descrição gerada por IA. |
| `VEM2214` | STRING | Número de matrículas na 4ª série ou módulo equivalente do Ensino Médio (1º turno/diurno). — descrição gerada por IA. |
| `VEM2215` | STRING | Número de matrículas em turmas não seriadas ou de dependência do Ensino Médio (1º turno/diurno). — descrição gerada por IA. |
| `VEM2216` | STRING | Quantidade total de turmas de Ensino Médio associadas ao curso (1º turno/diurno). — descrição gerada por IA. |
| `VEM2217` | STRING | Carga horária total ou cômputo anual de horas do curso (1º turno/diurno). — descrição gerada por IA. |
| `VEM2221` | STRING | Número de matrículas na 1ª série do Ensino Médio (2º turno/noturno). — descrição gerada por IA. |
| `VEM2222` | STRING | Número de matrículas na 2ª série do Ensino Médio (2º turno/noturno). — descrição gerada por IA. |
| `VEM2223` | STRING | Número de matrículas na 3ª série do Ensino Médio (2º turno/noturno). — descrição gerada por IA. |
| `VEM2224` | STRING | Número de matrículas na 4ª série ou módulo equivalente do Ensino Médio (2º turno/noturno). — descrição gerada por IA. |
| `VEM2225` | STRING | Número de matrículas em turmas não seriadas ou dependência (2º turno/noturno). — descrição gerada por IA. |
| `VEM2226` | STRING | Quantidade total de turmas de Ensino Médio associadas ao curso (2º turno/noturno). — descrição gerada por IA. |
| `VEM2227` | STRING | Carga horária total ou cômputo anual de horas do curso (2º turno/noturno). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_em8

File `raw__inep_censo_escolar_em8.parquet` · 24,893 rows · 24 columns

Raw Censo Escolar INEP. Familia de CSV: em8. Anos cobertos: 1996-1996 (1 ano(s)): 1996. Arquivos de origem: EM8_1996.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `MASCARA` | STRING | Código mascarado de identificação da escola no Censo Escolar de 1996. — descrição gerada por IA. |
| `ANO` | STRING | Ano de referência dos dados do Censo Escolar (ex: '1996'). — descrição gerada por IA. |
| `CODMUNIC` | STRING | Código de identificação do município da escola. — descrição gerada por IA. |
| `UF` | STRING | Nome completo do estado (Unidade Federativa) da escola. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla de dois caracteres do estado da escola (ex: 'RO', 'AC'). — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do município onde a escola está localizada. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa da escola (ex: 'Estadual', 'Federal', 'Municipal'). — descrição gerada por IA. |
| `LOC` | STRING | Localização da zona da escola ('Urbana' ou 'Rural'). — descrição gerada por IA. |
| `CODFUNC` | STRING | Situação de funcionamento da escola (ex: 'Ativo'). — descrição gerada por IA. |
| `CODCURSO` | STRING | Código identificador do curso ou habilitação profissional de Ensino Médio. — descrição gerada por IA. |
| `NOMECUR` | STRING | Nome do curso de Ensino Médio ou habilitação técnica oferecida. — descrição gerada por IA. |
| `EM811` | STRING | Métrica do Censo EM8: Carga horária teórica/mínima prevista do curso em horas. — descrição gerada por IA. |
| `EM812` | STRING | Métrica do Censo EM8: Carga horária prática ou complementar do curso em horas. — descrição gerada por IA. |
| `EM813` | STRING | Métrica do Censo EM8: Carga horária de estágio do curso em horas. — descrição gerada por IA. |
| `EM814` | STRING | Métrica do Censo EM8: Número de alunos matriculados na 1ª série/etapa do curso. — descrição gerada por IA. |
| `EM815` | STRING | Métrica do Censo EM8: Número de alunos matriculados na 2ª série/etapa do curso. — descrição gerada por IA. |
| `EM816` | STRING | Métrica do Censo EM8: Número de alunos matriculados na 3ª série/etapa do curso. — descrição gerada por IA. |
| `EM817` | STRING | Métrica do Censo EM8: Número de alunos matriculados na 4ª série/etapa do curso. — descrição gerada por IA. |
| `EM818` | STRING | Métrica do Censo EM8: Número de alunos matriculados em etapas não seriadas ou concluintes. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_es6

File `raw__inep_censo_escolar_es6.parquet` · 406 rows · 20 columns

Raw Censo Escolar INEP. Familia de CSV: es6. Anos cobertos: 1996-1996 (1 ano(s)): 1996. Arquivos de origem: ES6_1996.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `MASCARA` | STRING | Identificador mascarado único da escola no Censo Escolar de 1996. — descrição gerada por IA. |
| `ANO` | STRING | Ano de referência dos dados coletados pelo Censo Escolar (ex: '1996'). — descrição gerada por IA. |
| `CODMUNIC` | STRING | Código numérico de identificação do município no IBGE/INEP. — descrição gerada por IA. |
| `UF` | STRING | Nome da Unidade Federativa onde a escola está localizada. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla da Unidade Federativa (ex: 'RO'). — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do município onde a escola está localizada. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa da escola (ex: 'Estadual', 'Municipal', 'Privada'). — descrição gerada por IA. |
| `LOC` | STRING | Localização da zona da escola ('Urbana' ou 'Rural'). — descrição gerada por IA. |
| `CODFUNC` | STRING | Situação de funcionamento da unidade escolar (ex: 'Ativo'). — descrição gerada por IA. |
| `CODCURSO` | STRING | Código de identificação do curso técnico ou profissionalizante. — descrição gerada por IA. |
| `NOMECUR` | STRING | Nome descritivo do curso técnico/profissionalizante ofertado (ex: 'Tecnico em Eletromecanica'). — descrição gerada por IA. |
| `ES611` | STRING | Métrica de contagem do formulário ES6 referente ao curso (geralmente quantidade de alunos/matrículas). — descrição gerada por IA. |
| `ES612` | STRING | Métrica de contagem complementar do formulário ES6 para o curso (ex: concluintes ou turmas). — descrição gerada por IA. |
| `ES613` | STRING | Métrica suplementar do formulário ES6 (pode conter valores nulos). — descrição gerada por IA. |
| `ES614` | STRING | Métrica suplementar do formulário ES6 (pode conter valores nulos). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_escola

File `raw__inep_censo_escolar_escola.parquet` · 214,192 rows · 307 columns

Raw Censo Escolar INEP. Familia de CSV: escola. Anos cobertos: 2025-2025 (1 ano(s)): 2025. Arquivos de origem: Tabela_Escola_2025.csv. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

**Feeds:** `trusted/inep_censo_escolar_escolas`, `trusted/inep_censo_escolar_infraestrutura`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano letivo de referência da coleta do Censo Escolar (AAAA). — descrição gerada por IA. |
| `NO_REGIAO` | STRING | Nome da região geográfica onde a escola está localizada. — descrição gerada por IA. |
| `CO_REGIAO` | STRING | Código IBGE da região geográfica da escola. — descrição gerada por IA. |
| `NO_UF` | STRING | Nome da Unidade Federativa da escola. — descrição gerada por IA. |
| `SG_UF` | STRING | Sigla da Unidade Federativa (UF) da escola. — descrição gerada por IA. |
| `CO_UF` | STRING | Código IBGE da Unidade Federativa. — descrição gerada por IA. |
| `NO_MUNICIPIO` | STRING | Nome do município onde a escola está localizada. — descrição gerada por IA. |
| `CO_MUNICIPIO` | STRING | Código IBGE de 7 dígitos do município. — descrição gerada por IA. |
| `NO_REGIAO_GEOG_INTERM` | STRING | Nome da região geográfica intermediária (IBGE). — descrição gerada por IA. |
| `CO_REGIAO_GEOG_INTERM` | STRING | Código da região geográfica intermediária (IBGE). — descrição gerada por IA. |
| `NO_REGIAO_GEOG_IMED` | STRING | Nome da região geográfica imediata (IBGE). — descrição gerada por IA. |
| `CO_REGIAO_GEOG_IMED` | STRING | Código da região geográfica imediata (IBGE). — descrição gerada por IA. |
| `NO_MESORREGIAO` | STRING | Nome da mesorregião estatística (IBGE). — descrição gerada por IA. |
| `CO_MESORREGIAO` | STRING | Código da mesorregião estatística (IBGE). — descrição gerada por IA. |
| `NO_MICRORREGIAO` | STRING | Nome da microrregião estatística (IBGE). — descrição gerada por IA. |
| `CO_MICRORREGIAO` | STRING | Código da microrregião estatística (IBGE). — descrição gerada por IA. |
| `NO_DISTRITO` | STRING | Nome do distrito municipal da escola. — descrição gerada por IA. |
| `CO_DISTRITO` | STRING | Código IBGE do distrito municipal. — descrição gerada por IA. |
| `NO_REGIAO_ADMINISTRATIVA` | STRING | Nome da região administrativa (ex: Distrito Federal). — descrição gerada por IA. |
| `CO_REGIAO_ADMINISTRATIVA` | STRING | Código da região administrativa. — descrição gerada por IA. |
| `NO_ENTIDADE` | STRING | Nome oficial da escola ou entidade escolar. — descrição gerada por IA. |
| `CO_ENTIDADE` | STRING | Código INEP (ID único) da escola. — descrição gerada por IA. |
| `TP_DEPENDENCIA` | STRING | Tipo de dependência administrativa (1: Federal, 2: Estadual, 3: Municipal, 4: Privada). — descrição gerada por IA. |
| `TP_CATEGORIA_ESCOLA_PRIVADA` | STRING | Categoria da escola privada (1: Particular, 2: Comunitária, 3: Confessional, 4: Filantrópica). — descrição gerada por IA. |
| `TP_LOCALIZACAO` | STRING | Localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `TP_LOCALIZACAO_DIFERENCIADA` | STRING | Área de localização diferenciada (ex: assentamento, terra indígena, quilombola). — descrição gerada por IA. |
| `DS_ENDERECO` | STRING | Logradouro e endereço da escola. — descrição gerada por IA. |
| `NU_ENDERECO` | STRING | Número do endereço da escola. — descrição gerada por IA. |
| `DS_COMPLEMENTO` | STRING | Complemento do endereço da escola. — descrição gerada por IA. |
| `NO_BAIRRO` | STRING | Bairro de localização da escola. — descrição gerada por IA. |
| `CO_CEP` | STRING | Código de Endereçamento Postal (CEP) da escola. — descrição gerada por IA. |
| `NU_DDD` | STRING | Número de DDD do telefone institucional. — descrição gerada por IA. |
| `NU_TELEFONE` | STRING | Número do telefone institucional da escola. — descrição gerada por IA. |
| `LATITUDE` | STRING | Coordenada geográfica de latitude da escola. — descrição gerada por IA. |
| `LONGITUDE` | STRING | Coordenada geográfica de longitude da escola. — descrição gerada por IA. |
| `TP_SITUACAO_FUNCIONAMENTO` | STRING | Situação de funcionamento da escola (1: Em atividade, 2: Paralisada, 3: Extinta). — descrição gerada por IA. |
| `CO_ORGAO_REGIONAL` | STRING | Código do órgão regional/SRE de ensino. — descrição gerada por IA. |
| `DT_ANO_LETIVO_INICIO` | STRING | Data de início do ano letivo (AAAA-MM-DD). — descrição gerada por IA. |
| `DT_ANO_LETIVO_TERMINO` | STRING | Data de término do ano letivo (AAAA-MM-DD). — descrição gerada por IA. |
| `IN_VINCULO_SECRETARIA_EDUCACAO` | STRING | Indica vínculo direto com a Secretaria de Educação (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_VINCULO_SEGURANCA_PUBLICA` | STRING | Indica vínculo com órgão de Segurança Pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_VINCULO_SECRETARIA_SAUDE` | STRING | Indica vínculo com a Secretaria de Saúde (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_VINCULO_OUTRO_ORGAO` | STRING | Indica vínculo com outro órgão público (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PODER_PUBLICO_PARCERIA` | STRING | Indica se a escola privada tem parceria/convênio com o poder público (1: Sim, 0: Não). — descrição gerada por IA. |
| `TP_PODER_PUBLICO_PARCERIA` | STRING | Tipo da parceria com o poder público (1: Municipal, 2: Estadual, 3: Ambas). — descrição gerada por IA. |
| `IN_FORMA_CONT_TERMO_COLABORA` | STRING | Parceria firmada via Termo de Colaboração (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_TERMO_FOMENTO` | STRING | Parceria firmada via Termo de Fomento (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ACORDO_COOP` | STRING | Parceria firmada via Acordo de Cooperação (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_PRESTACAO_SERV` | STRING | Parceria firmada via Contrato de Prestação de Serviços (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_COOP_TEC_FIN` | STRING | Parceria firmada via Cooperação Técnica e Financeira (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_CONSORCIO_PUB` | STRING | Parceria firmada via Consórcio Público (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_TERMO_COLAB` | STRING | Parceria municipal via Termo de Colaboração (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_TERMO_FOMENTO` | STRING | Parceria municipal via Termo de Fomento (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_ACORDO_COOP` | STRING | Parceria municipal via Acordo de Cooperação (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_PREST_SERV` | STRING | Parceria municipal via Prestação de Serviços (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_COOP_TEC_FIN` | STRING | Parceria municipal via Cooperação Técnica e Financeira (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_CONSORCIO_PUB` | STRING | Parceria municipal via Consórcio Público (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_TERMO_COLAB` | STRING | Parceria estadual via Termo de Colaboração (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_TERMO_FOMENTO` | STRING | Parceria estadual via Termo de Fomento (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_ACORDO_COOP` | STRING | Parceria estadual via Acordo de Cooperação (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_PREST_SERV` | STRING | Parceria estadual via Prestação de Serviços (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_COOP_TEC_FIN` | STRING | Parceria estadual via Cooperação Técnica e Financeira (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_CONSORCIO_PUB` | STRING | Parceria estadual via Consórcio Público (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_EMP` | STRING | Mantenedora privada é empresa/grupo de pessoas físicas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_ONG` | STRING | Mantenedora privada é associação/ONG (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_OSCIP` | STRING | Mantenedora privada é OSCIP (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIV_ONG_OSCIP` | STRING | Mantenedora privada é ONG ou OSCIP (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_SIND` | STRING | Mantenedora privada é sindicato ou associação de classe (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_SIST_S` | STRING | Mantenedora privada pertence ao Sistema S (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_S_FINS` | STRING | Mantenedora privada é instituição sem fins lucrativos (1: Sim, 0: Não). — descrição gerada por IA. |
| `NU_CNPJ_ESCOLA_PRIVADA` | STRING | CNPJ da escola privada. — descrição gerada por IA. |
| `NU_CNPJ_MANTENEDORA` | STRING | CNPJ da instituição mantenedora da escola. — descrição gerada por IA. |
| `TP_REGULAMENTACAO` | STRING | Situação da regulamentação no Conselho de Educação (1: Sim, 2: Não, 3: Em tramitação). — descrição gerada por IA. |
| `TP_RESPONSAVEL_REGULAMENTACAO` | STRING | Esfera responsável pela regulamentação (1: Federal, 2: Estadual, 3: Municipal). — descrição gerada por IA. |
| `CO_ESCOLA_SEDE_VINCULADA` | STRING | Código INEP da escola sede no caso de unidade vinculada. — descrição gerada por IA. |
| `CO_IES_OFERTANTE` | STRING | Código da Instituição de Ensino Superior ofertante. — descrição gerada por IA. |
| `IN_LOCAL_FUNC_PREDIO_ESCOLAR` | STRING | Funciona em prédio escolar específico (1: Sim, 0: Não). — descrição gerada por IA. |
| `TP_OCUPACAO_PREDIO_ESCOLAR` | STRING | Tipo de ocupação do prédio (1: Próprio, 2: Alugado, 3: Cedido). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SOCIOEDUCATIVO` | STRING | Funciona em unidade socioeducativa (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_UNID_PRISIONAL` | STRING | Funciona em unidade prisional (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_PRISIONAL_SOCIO` | STRING | Funciona em unidade prisional ou socioeducativa (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_GALPAO` | STRING | Funciona em galpão/rancho/paiol (1: Sim, 0: Não). — descrição gerada por IA. |
| `TP_OCUPACAO_GALPAO` | STRING | Tipo de ocupação do galpão (1: Próprio, 2: Alugado, 3: Cedido). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SALAS_OUTRA_ESC` | STRING | Funciona em salas cedidas de outra escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_OUTROS` | STRING | Funciona em outros locais não especificados (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PREDIO_COMPARTILHADO` | STRING | Indica se compartilha o mesmo prédio com outra escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AGUA_POTAVEL` | STRING | Possui água potável para consumo humano (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AGUA_REDE_PUBLICA` | STRING | Abastecimento de água via rede pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AGUA_POCO_ARTESIANO` | STRING | Abastecimento de água via poço artesiano (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AGUA_CACIMBA` | STRING | Abastecimento de água via cacimba/poço/cisterna (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AGUA_FONTE_RIO` | STRING | Abastecimento de água via fonte, rio ou igarapé (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AGUA_INEXISTENTE` | STRING | Não possui abastecimento de água (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AGUA_CARRO_PIPA` | STRING | Abastecimento de água via carro-pipa (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ENERGIA_REDE_PUBLICA` | STRING | Energia elétrica fornecida por rede pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ENERGIA_GERADOR_FOSSIL` | STRING | Energia elétrica gerada por combustível fósseis (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ENERGIA_RENOVAVEL` | STRING | Energia elétrica gerada por fonte renovável/solar/eólica (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ENERGIA_INEXISTENTE` | STRING | Não possui energia elétrica (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESGOTO_REDE_PUBLICA` | STRING | Esgotamento sanitário via rede pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESGOTO_FOSSA_SEPTICA` | STRING | Esgotamento sanitário via fossa séptica (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESGOTO_FOSSA_COMUM` | STRING | Esgotamento sanitário via fossa comum/rudimentar (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESGOTO_FOSSA` | STRING | Possui fossa sanitária (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESGOTO_INEXISTENTE` | STRING | Não possui esgotamento sanitário (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LIXO_SERVICO_COLETA` | STRING | Lixo com destinação via coleta periódica (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LIXO_QUEIMA` | STRING | Lixo queimado nas dependências da escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LIXO_ENTERRA` | STRING | Lixo enterrado nas dependências da escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LIXO_DESTINO_FINAL_PUBLICO` | STRING | Lixo descartado em lixão/área pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LIXO_DESCARTA_OUTRA_AREA` | STRING | Lixo descartado em outra área fora da escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_SEPARACAO` | STRING | Realiza separação/coleta seletiva do lixo (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_REUTILIZA` | STRING | Realiza reutilização de materiais descartados (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_RECICLAGEM` | STRING | Realiza reciclagem do lixo (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_INEXISTENTE` | STRING | Não realiza tratamento do lixo (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ALMOXARIFADO` | STRING | Possui almoxarifado (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AREA_VERDE` | STRING | Possui área verde (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AREA_PLANTIO` | STRING | Possui horta escolar ou área para plantio (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_AUDITORIO` | STRING | Possui auditório (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_BANHEIRO` | STRING | Possui banheiro na escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_BANHEIRO_EI` | STRING | Possui banheiro adequado à Educação Infantil (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_BANHEIRO_PNE` | STRING | Possui banheiro adaptado a alunos com deficiência (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_BANHEIRO_FUNCIONARIOS` | STRING | Possui banheiro exclusivo para funcionários (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_BANHEIRO_CHUVEIRO` | STRING | Possui chuveiros no banheiro (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA` | STRING | Possui biblioteca (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA_SALA_LEITURA` | STRING | Possui biblioteca ou sala de leitura (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COZINHA` | STRING | Possui cozinha (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_DESPENSA` | STRING | Possui despensa para alimentos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_DORMITORIO_ALUNO` | STRING | Possui dormitório para alunos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_DORMITORIO_PROFESSOR` | STRING | Possui dormitório para professores (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LABORATORIO_CIENCIAS` | STRING | Possui laboratório de ciências (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LABORATORIO_INFORMATICA` | STRING | Possui laboratório de informática (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_LABORATORIO_EDUC_PROF` | STRING | Possui laboratório específico de educação profissional (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PATIO_COBERTO` | STRING | Possui pátio coberto (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PATIO_DESCOBERTO` | STRING | Possui pátio descoberto (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PARQUE_INFANTIL` | STRING | Possui parque infantil/playground (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PISCINA` | STRING | Possui piscina (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES` | STRING | Possui quadra de esportes (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES_COBERTA` | STRING | Possui quadra de esportes coberta (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES_DESCOBERTA` | STRING | Possui quadra de esportes descoberta (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_REFEITORIO` | STRING | Possui refeitório (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_ATELIE_ARTES` | STRING | Possui ateliê/sala de artes (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_MUSICA_CORAL` | STRING | Possui sala de música/coral (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_ESTUDIO_DANCA` | STRING | Possui estúdio de dança (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_MULTIUSO` | STRING | Possui sala de uso múltiplo (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_ESTUDIO_GRAVACAO` | STRING | Possui estúdio de gravação (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_OFICINAS_EDUC_PROF` | STRING | Possui sala/oficina de ensino profissionalizante (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_DIRETORIA` | STRING | Possui sala de diretoria (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_LEITURA` | STRING | Possui sala de leitura (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_PROFESSOR` | STRING | Possui sala de professores (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_REPOUSO_ALUNO` | STRING | Possui sala de repouso para alunos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SECRETARIA` | STRING | Possui sala de secretaria (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_SALA_ATENDIMENTO_ESPECIAL` | STRING | Possui sala de Atendimento Educacional Especializado - AEE (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_TERREIRAO` | STRING | Possui terreirão/espaço aberto tradicional (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_VIVEIRO` | STRING | Possui viveiro escolar (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_DEPENDENCIAS_OUTRAS` | STRING | Possui outras dependências não listadas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_CORRIMAO` | STRING | Acessibilidade: possui corrimão e guarda-corpos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_ELEVADOR` | STRING | Acessibilidade: possui elevador adaptado (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_PISOS_TATEIS` | STRING | Acessibilidade: possui pisos táteis (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_VAO_LIVRE` | STRING | Acessibilidade: possui portas com vão livre acessível (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_RAMPAS` | STRING | Acessibilidade: possui rampas de acesso (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINAL_SONORO` | STRING | Acessibilidade: possui sinalização sonora (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINAL_TATIL` | STRING | Acessibilidade: possui sinalização tátil em Braille (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINAL_VISUAL` | STRING | Acessibilidade: possui sinalização visual acessível (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_INEXISTENTE` | STRING | Indica ausência de recursos de acessibilidade (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINALIZACAO` | STRING | Possui sinalização tátil, sonora ou visual acessível (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_SALAS_UTILIZADAS_DENTRO` | STRING | Quantidade de salas de aula utilizadas dentro do prédio. — descrição gerada por IA. |
| `QT_SALAS_UTILIZADAS_FORA` | STRING | Quantidade de salas de aula utilizadas fora do prédio. — descrição gerada por IA. |
| `QT_SALAS_UTILIZADAS` | STRING | Quantidade total de salas de aula utilizadas na escola. — descrição gerada por IA. |
| `QT_SALAS_UTILIZA_CLIMATIZADAS` | STRING | Quantidade de salas de aula climatizadas (com ar-condicionado). — descrição gerada por IA. |
| `QT_SALAS_UTILIZADAS_ACESSIVEIS` | STRING | Quantidade de salas de aula acessíveis a PCD. — descrição gerada por IA. |
| `QT_SALAS_LEITURA` | STRING | Quantidade de salas de leitura disponíveis na escola. — descrição gerada por IA. |
| `IN_EQUIP_PARABOLICA` | STRING | Possui antena parabólica (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMPUTADOR` | STRING | Possui computadores na escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EQUIP_COPIADORA` | STRING | Possui máquina copiadora (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EQUIP_IMPRESSORA` | STRING | Possui impressora (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EQUIP_IMPRESSORA_MULT` | STRING | Possui impressora multifuncional (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EQUIP_SCANNER` | STRING | Possui scanner de documentos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EQUIP_NENHUM` | STRING | Não possui equipamentos tecnológicos listados (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EQUIP_DVD` | STRING | Possui aparelho de DVD/Blu-Ray (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_EQUIP_DVD` | STRING | Quantidade de aparelhos de DVD/Blu-Ray. — descrição gerada por IA. |
| `IN_EQUIP_SOM` | STRING | Possui equipamento de som (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_EQUIP_SOM` | STRING | Quantidade de equipamentos de som. — descrição gerada por IA. |
| `IN_EQUIP_TV` | STRING | Possui aparelhos de televisão (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_EQUIP_TV` | STRING | Quantidade de aparelhos de TV. — descrição gerada por IA. |
| `IN_EQUIP_LOUSA_DIGITAL` | STRING | Possui lousa digital/interativa (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_EQUIP_LOUSA_DIGITAL` | STRING | Quantidade de lousas digitais. — descrição gerada por IA. |
| `IN_EQUIP_MULTIMIDIA` | STRING | Possui projetor multimídia / Data Show (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_EQUIP_MULTIMIDIA` | STRING | Quantidade de projetores multimídia. — descrição gerada por IA. |
| `IN_DESKTOP_ALUNO` | STRING | Possui computadores de mesa para uso dos alunos (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_DESKTOP_ALUNO` | STRING | Quantidade de computadores de mesa para alunos. — descrição gerada por IA. |
| `IN_COMP_PORTATIL_ALUNO` | STRING | Possui notebooks/laptops para uso dos alunos (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_COMP_PORTATIL_ALUNO` | STRING | Quantidade de notebooks/laptops para uso dos alunos. — descrição gerada por IA. |
| `IN_TABLET_ALUNO` | STRING | Possui tablets para uso dos alunos (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_TABLET_ALUNO` | STRING | Quantidade de tablets para uso dos alunos. — descrição gerada por IA. |
| `IN_INTERNET` | STRING | Possui acesso à internet (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_INTERNET_ALUNOS` | STRING | Internet com acesso liberado para alunos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_INTERNET_ADMINISTRATIVO` | STRING | Internet disponível para uso administrativo (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_INTERNET_APRENDIZAGEM` | STRING | Internet utilizada para apoio ao processo de aprendizagem (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_INTERNET_COMUNIDADE` | STRING | Internet aberta para a comunidade externa (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACESSO_INTERNET_COMPUTADOR` | STRING | Acesso à internet via computadores da escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ACES_INTERNET_DISP_PESSOAIS` | STRING | Acesso à internet via dispositivos pessoais dos usuários (1: Sim, 0: Não). — descrição gerada por IA. |
| `TP_REDE_LOCAL` | STRING | Tipo de rede local instalada (0: Não há, 1: Cabo, 2: Wireless, 3: Cabo e Wireless). — descrição gerada por IA. |
| `IN_BANDA_LARGA` | STRING | Possui conexão à internet em banda larga (1: Sim, 0: Não). — descrição gerada por IA. |
| `QT_PROF_ADMINISTRATIVOS` | STRING | Quantidade de funcionários na gestão administrativa. — descrição gerada por IA. |
| `QT_PROF_SERVICOS_GERAIS` | STRING | Quantidade de funcionários de serviços gerais e limpeza. — descrição gerada por IA. |
| `QT_PROF_BIBLIOTECARIO` | STRING | Quantidade de bibliotecários ou auxiliares de biblioteca. — descrição gerada por IA. |
| `QT_PROF_SAUDE` | STRING | Quantidade de profissionais da saúde. — descrição gerada por IA. |
| `QT_PROF_COORDENADOR` | STRING | Quantidade de coordenadores pedagógicos. — descrição gerada por IA. |
| `QT_PROF_FONAUDIOLOGO` | STRING | Quantidade de fonoaudiólogos. — descrição gerada por IA. |
| `QT_PROF_NUTRICIONISTA` | STRING | Quantidade de nutricionistas. — descrição gerada por IA. |
| `QT_PROF_PSICOLOGO` | STRING | Quantidade de psicólogos na escola. — descrição gerada por IA. |
| `QT_PROF_ALIMENTACAO` | STRING | Quantidade de merendeiras e pessoal de preparação de alimentos. — descrição gerada por IA. |
| `QT_PROF_PEDAGOGIA` | STRING | Quantidade de pedagogos/orientadores educacionais. — descrição gerada por IA. |
| `QT_PROF_SECRETARIO` | STRING | Quantidade de secretários escolares. — descrição gerada por IA. |
| `QT_PROF_SEGURANCA` | STRING | Quantidade de vigilantes/porteiros/seguranças. — descrição gerada por IA. |
| `QT_PROF_MONITORES` | STRING | Quantidade de monitores de sala ou auxiliares. — descrição gerada por IA. |
| `QT_PROF_GESTAO` | STRING | Quantidade de gestores/diretores escolares. — descrição gerada por IA. |
| `QT_PROF_ASSIST_SOCIAL` | STRING | Quantidade de assistentes sociais. — descrição gerada por IA. |
| `QT_PROF_TRAD_LIBRAS` | STRING | Quantidade de tradutores e intérpretes de LIBRAS. — descrição gerada por IA. |
| `QT_PROF_AGRICOLA` | STRING | Quantidade de monitores ou técnicos agrícolas. — descrição gerada por IA. |
| `QT_PROF_REVISOR_BRAILLE` | STRING | Quantidade de revisores/transcritores de Braille. — descrição gerada por IA. |
| `IN_ALIMENTACAO` | STRING | Oferece alimentação/merenda escolar aos estudantes (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_MULTIMIDIA` | STRING | Oferece material pedagógico multimídia (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_INFANTIL` | STRING | Oferece material específico para educação infantil (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_CIENTIFICO` | STRING | Oferece kits/materiais científicos pedagógicos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_DIFUSAO` | STRING | Oferece materiais para difusão cultural/educacional (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_MUSICAL` | STRING | Oferece instrumentos e materiais de educação musical (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_JOGOS` | STRING | Oferece jogos educativos e jogos de tabuleiro (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_ARTISTICAS` | STRING | Oferece materiais para atividades artísticas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_PROFISSIONAL` | STRING | Oferece materiais de suporte à formação profissional (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_DESPORTIVA` | STRING | Oferece materiais e equipamentos esportivos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_INDIGENA` | STRING | Oferece material pedagógico específico para educação indígena (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_ETNICO` | STRING | Oferece material pedagógico para relações étnico-raciais (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_CAMPO` | STRING | Oferece material pedagógico para educação do campo (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_BIL_SURDOS` | STRING | Oferece material pedagógico para educação bilíngue de surdos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_AGRICOLA` | STRING | Oferece material pedagógico agrícola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_QUILOMBOLA` | STRING | Oferece material pedagógico para educação quilombola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_EDU_ESP` | STRING | Oferece material pedagógico para educação especial (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_NENHUM` | STRING | Não possui materiais pedagógicos específicos cadastrados (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EDUCACAO_INDIGENA` | STRING | Oferece modalidade de educação escolar indígena (1: Sim, 0: Não). — descrição gerada por IA. |
| `TP_INDIGENA_LINGUA` | STRING | Língua em que as aulas são ministradas na ed. indígena (1: Indígena, 2: Português, 3: Ambas). — descrição gerada por IA. |
| `CO_LINGUA_INDIGENA_1` | STRING | Código da primeira língua indígena utilizada. — descrição gerada por IA. |
| `CO_LINGUA_INDIGENA_2` | STRING | Código da segunda língua indígena utilizada. — descrição gerada por IA. |
| `CO_LINGUA_INDIGENA_3` | STRING | Código da terceira língua indígena utilizada. — descrição gerada por IA. |
| `IN_EXAME_SELECAO` | STRING | Aplica exame de seleção/vestibulinho para ingresso de alunos (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_RESERVA_PPI` | STRING | Possui reserva de vagas para Pretos, Pardos ou Indígenas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_RESERVA_RENDA` | STRING | Possui reserva de vagas por perfil socioeconômico/renda (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_RESERVA_PUBLICA` | STRING | Possui reserva de vagas para oriundos da rede pública (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_RESERVA_PCD` | STRING | Possui reserva de vagas para pessoas com deficiência (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_RESERVA_OUTROS` | STRING | Possui outras modalidades de reserva de vagas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_RESERVA_NENHUMA` | STRING | Não aplica sistema de reserva de vagas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_REDES_SOCIAIS` | STRING | Mantém redes sociais ativas para comunicação da escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESPACO_ATIVIDADE` | STRING | Oferece espaço comunitário para atividades educativas (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESPACO_EQUIPAMENTO` | STRING | Compartilha espaço/equipamentos com a comunidade externa (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ORGAO_ASS_PAIS` | STRING | Possui Associação de Pais formalizada (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ORGAO_ASS_PAIS_MESTRES` | STRING | Possui Associação de Pais e Mestres - APM (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ORGAO_CONSELHO_ESCOLAR` | STRING | Possui Conselho Escolar constituído (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ORGAO_GREMIO_ESTUDANTIL` | STRING | Possui Grêmio Estudantil ativo (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ORGAO_OUTROS` | STRING | Possui outros órgãos colegiados da escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ORGAO_NENHUM` | STRING | Não possui órgãos colegiados constituídos (1: Sim, 0: Não). — descrição gerada por IA. |
| `TP_PROPOSTA_PEDAGOGICA` | STRING | Tipo de proposta pedagógica/projeto político-pedagógico da escola. — descrição gerada por IA. |
| `IN_EDUC_AMBIENTAL` | STRING | Desenvolve ações relativas à educação ambiental (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_CONTEUDO` | STRING | Educação ambiental tratada como conteúdo disciplinar (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_CURRICULAR` | STRING | Educação ambiental tratada como disciplina curricular (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_EIXO` | STRING | Educação ambiental tratada como eixo transversal (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_EVENTOS` | STRING | Educação ambiental trabalhada por meio de eventos/feiras (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_PROJETOS` | STRING | Educação ambiental trabalhada em projetos interdisciplinares (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_NENHUMA` | STRING | Não realiza ações ou projetos de educação ambiental (1: Sim, 0: Não). — descrição gerada por IA. |
| `TP_AEE` | STRING | Indica tipo de Atendimento Educacional Especializado oferecido. — descrição gerada por IA. |
| `TP_ATIVIDADE_COMPLEMENTAR` | STRING | Tipo de atividade complementar desenvolvida pela escola. — descrição gerada por IA. |
| `TP_ITINERARIO_FORMATIVO` | STRING | Tipo de itinerário formativo ofertado no Ensino Médio. — descrição gerada por IA. |
| `IN_ITINERARIO_APROFUNDAMENTO` | STRING | Oferta itinerário formativo de aprofundamento de aprendizagem (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ITINERARIO_TECN_PROF` | STRING | Oferta itinerário formativo de formação técnica e profissional (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESCOLARIZACAO` | STRING | Oferece turmas de escolarização regular (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MEDIACAO_PRESENCIAL` | STRING | Mediação pedagógica na modalidade presencial (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MEDIACAO_SEMIPRESENCIAL` | STRING | Mediação pedagógica na modalidade semipresencial (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_MEDIACAO_EAD` | STRING | Mediação pedagógica na modalidade Educação a Distância (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESPECIAL_EXCLUSIVA` | STRING | Oferece turmas exclusivas de Educação Especial (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_REGULAR` | STRING | Oferece ensino de Educação Básica Regular (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_EJA` | STRING | Oferece modalidade Educação de Jovens e Adultos - EJA (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_PROFISSIONALIZANTE` | STRING | Oferece Educação Profissionalizante (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_CRECHE` | STRING | Oferece turmas comuns de creche na Educação Infantil (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_PRE` | STRING | Oferece turmas comuns de pré-escola na Educação Infantil (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_FUND_AI` | STRING | Oferece turmas comuns do Ensino Fundamental Anos Iniciais (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_FUND_AF` | STRING | Oferece turmas comuns do Ensino Fundamental Anos Finais (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_MEDIO_MEDIO` | STRING | Oferece turmas comuns do Ensino Médio Propedêutico (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_MEDIO_INTEGRADO` | STRING | Oferece turmas comuns do Ensino Médio Integrado (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_MEDIO_FIC` | STRING | Oferece turmas comuns de Ensino Médio com Formação Inicial e Continuada (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_MEDIO_NORMAL` | STRING | Oferece turmas comuns de Ensino Médio na modalidade Normal/Magistério (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_CRECHE` | STRING | Oferece turmas exclusivas de Educação Especial na creche (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_PRE` | STRING | Oferece turmas exclusivas de Educação Especial na pré-escola (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_FUND_AI` | STRING | Oferece turmas exclusivas de Ed. Especial no EF Anos Iniciais (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_FUND_AF` | STRING | Oferece turmas exclusivas de Ed. Especial no EF Anos Finais (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_MEDIO_MEDIO` | STRING | Oferece turmas exclusivas de Ed. Especial no Ensino Médio Propedêutico (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_MEDIO_INTEGR` | STRING | Oferece turmas exclusivas de Ed. Especial no Ensino Médio Integrado (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_MEDIO_FIC` | STRING | Oferece turmas exclusivas de Ed. Especial no Ensino Médio FIC (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_MEDIO_NORMAL` | STRING | Oferece turmas exclusivas de Ed. Especial no Ensino Médio Normal (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_EJA_FUND` | STRING | Oferece turmas comuns de EJA para Ensino Fundamental (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_EJA_MEDIO` | STRING | Oferece turmas comuns de EJA para Ensino Médio (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_EJA_PROF` | STRING | Oferece turmas comuns de EJA integrada à Educação Profissional (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_EJA_FUND` | STRING | Oferece turmas exclusivas de Educação Especial na EJA Fundamental (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_EJA_MEDIO` | STRING | Oferece turmas exclusivas de Educação Especial na EJA Médio (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_EJA_PROF` | STRING | Oferece turmas exclusivas de Ed. Especial na EJA Profissionalizante (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_COMUM_PROF` | STRING | Oferece Cursos Téc./Profissionalizantes na modalidade comum (1: Sim, 0: Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_PROF` | STRING | Oferece Cursos Téc./Profissionalizantes exclusivos para Educação Especial (1: Sim, 0: Não). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_gestor_escolar

File `raw__inep_censo_escolar_gestor_escolar.parquet` · 180,540 rows · 70 columns

Raw Censo Escolar INEP. Familia de CSV: gestor_escolar. Anos cobertos: 2025-2025 (1 ano(s)): 2025. Arquivos de origem: Tabela_Gestor_Escolar_2025.csv. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano de realização do Censo Escolar (formato YYYY). — descrição gerada por IA. |
| `CO_ENTIDADE` | STRING | Código INEP de 8 dígitos de identificação única da escola. — descrição gerada por IA. |
| `QT_GEST_BAS` | STRING | Quantidade total de gestores atuantes na Educação Básica da escola. — descrição gerada por IA. |
| `QT_GEST_BAS_FEM` | STRING | Quantidade de gestores do sexo feminino. — descrição gerada por IA. |
| `QT_GEST_BAS_MASC` | STRING | Quantidade de gestores do sexo masculino. — descrição gerada por IA. |
| `QT_GEST_BAS_ND` | STRING | Quantidade de gestores com sexo não declarado. — descrição gerada por IA. |
| `QT_GEST_BAS_BRANCA` | STRING | Quantidade de gestores autodeclarados de raça/cor branca. — descrição gerada por IA. |
| `QT_GEST_BAS_PRETA` | STRING | Quantidade de gestores autodeclarados de raça/cor preta. — descrição gerada por IA. |
| `QT_GEST_BAS_PARDA` | STRING | Quantidade de gestores autodeclarados de raça/cor parda. — descrição gerada por IA. |
| `QT_GEST_BAS_AMARELA` | STRING | Quantidade de gestores autodeclarados de raça/cor amarela. — descrição gerada por IA. |
| `QT_GEST_BAS_INDIGENA` | STRING | Quantidade de gestores autodeclarados de raça/cor indígena. — descrição gerada por IA. |
| `QT_GEST_BAS_NACIO_BRASILEIRA` | STRING | Quantidade de gestores de nacionalidade brasileira. — descrição gerada por IA. |
| `QT_GEST_BAS_NACIO_ESTRANG` | STRING | Quantidade de gestores de nacionalidade estrangeira. — descrição gerada por IA. |
| `QT_GEST_BAS_0_24` | STRING | Quantidade de gestores com idade de até 24 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_25_29` | STRING | Quantidade de gestores na faixa etária de 25 a 29 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_30_39` | STRING | Quantidade de gestores na faixa etária de 30 a 39 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_40_49` | STRING | Quantidade de gestores na faixa etária de 40 a 49 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_50_54` | STRING | Quantidade de gestores na faixa etária de 50 a 54 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_55_59` | STRING | Quantidade de gestores na faixa etária de 55 a 59 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_60_MAIS` | STRING | Quantidade de gestores com 60 anos de idade ou mais. — descrição gerada por IA. |
| `QT_GEST_BAS_PCD` | STRING | Quantidade de gestores com deficiência (Pessoa com Deficiência). — descrição gerada por IA. |
| `QT_GEST_BAS_ZR_URB` | STRING | Quantidade de gestores que residem em zona urbana. — descrição gerada por IA. |
| `QT_GEST_BAS_ZR_RUR` | STRING | Quantidade de gestores que residem em zona rural. — descrição gerada por IA. |
| `QT_GEST_BAS_ZR_NA` | STRING | Quantidade de gestores com zona de residência não declarada ou não aplicável. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_EF` | STRING | Quantidade de gestores com nível de escolaridade até o Ensino Fundamental. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_EM` | STRING | Quantidade de gestores com nível de escolaridade até o Ensino Médio. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_GRAD` | STRING | Quantidade de gestores com Ensino Superior concluído. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_GRAD_LICEN` | STRING | Quantidade de gestores graduados com Licenciatura. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_GRAD_SLICEN` | STRING | Quantidade de gestores graduados sem Licenciatura (Bacharelado/Tecnólogo). — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_POS_ESPEC` | STRING | Quantidade de gestores com pós-graduação lato sensu (Especialização). — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_POS_MESTRA` | STRING | Quantidade de gestores com mestrado concluído. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_POS_DOUTO` | STRING | Quantidade de gestores com doutorado concluído. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_POS_NENHUM` | STRING | Quantidade de gestores graduados sem pós-graduação. — descrição gerada por IA. |
| `QT_GEST_BAS_VINCULO_CONCUR` | STRING | Quantidade de gestores com vínculo de servidor público concursado/efetivo. — descrição gerada por IA. |
| `QT_GEST_BAS_VINCULO_CONTRA` | STRING | Quantidade de gestores com contrato temporário. — descrição gerada por IA. |
| `QT_GEST_BAS_VINCULO_TERCEIR` | STRING | Quantidade de gestores terceirizados. — descrição gerada por IA. |
| `QT_GEST_BAS_VINCULO_CLT` | STRING | Quantidade de gestores contratados via CLT. — descrição gerada por IA. |
| `QT_GEST_BAS_DIRETOR` | STRING | Quantidade de gestores no cargo específico de Diretor da escola. — descrição gerada por IA. |
| `QT_GEST_BAS_OUTRO` | STRING | Quantidade de gestores em outras funções de gestão (ex: vice-diretor, coordenador). — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_PROP` | STRING | Quantidade de gestores que acessaram o cargo por serem proprietários/sócios. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_INDIC` | STRING | Quantidade de gestores que acessaram o cargo por indicação. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_SEL` | STRING | Quantidade de gestores selecionados por processo seletivo simplificado. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_CONC` | STRING | Quantidade de gestores selecionados por concurso público específico. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_ELEIC` | STRING | Quantidade de gestores eleitos diretamente pela comunidade escolar. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_P_SEL` | STRING | Quantidade de gestores selecionados por processo seletivo combinado com eleição. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_OUTRO` | STRING | Quantidade de gestores com outras formas de acesso ao cargo. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_CRE` | STRING | Quantidade de gestores com curso de formação continuada em Creche. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_PRE_ESCOLA` | STRING | Quantidade de gestores com curso de formação continuada em Pré-Escola. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ANOS_INICIAIS` | STRING | Quantidade de gestores com formação continuada nos Anos Iniciais do EF. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ANOS_FINAIS` | STRING | Quantidade de gestores com formação continuada nos Anos Finais do EF. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ENS_MEDIO` | STRING | Quantidade de gestores com formação continuada em Ensino Médio. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_EJA` | STRING | Quantidade de gestores com formação continuada em Educação de Jovens e Adultos. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ED_ESPECIAL` | STRING | Quantidade de gestores com formação continuada em Educação Especial. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_BIL_SURDOS` | STRING | Quantidade de gestores com formação continuada em Educação Bilíngue de Surdos. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ED_INDIGENA` | STRING | Quantidade de gestores com formação continuada em Educação Indígena. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_CAMPO` | STRING | Quantidade de gestores com formação continuada em Educação do Campo. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_AMBIENTAL` | STRING | Quantidade de gestores com formação continuada em Educação Ambiental. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_DIR_HUMANOS` | STRING | Quantidade de gestores com formação continuada em Direitos Humanos. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_DIV_SEXUAL` | STRING | Quantidade de gestores com formação em Diversidade Sexual/Gênero. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_DIR_ADOLESC` | STRING | Quantidade de gestores com formação em Direitos da Criança e do Adolescente. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_AFRO` | STRING | Quantidade de gestores com formação em História/Cultura Afro-Brasileira e Indígena. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_GESTAO` | STRING | Quantidade de gestores com formação continuada em Gestão Escolar. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_EDUC_TIC` | STRING | Quantidade de gestores com formação em Tecnologias da Informação e Comunicação (TIC). — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_OUTROS` | STRING | Quantidade de gestores com cursos de formação continuada em outras áreas específicas. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_NENHUM` | STRING | Quantidade de gestores sem formação continuada registrada. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_indicesc

File `raw__inep_censo_escolar_indicesc.parquet` · 877,062 rows · 199 columns

Raw Censo Escolar INEP. Familia de CSV: indicesc. Anos cobertos: 2000-2003 (4 ano(s)): 2000, 2001, 2002, 2003. Arquivos de origem: INDICESC_2000.CSV, INDICESC_2001.CSV, INDICESC_2002.CSV, INDICESC_2003.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `MASCARA` | STRING | Código alfanumérico que mascara/identifica a escola no Censo Escolar (INEP). — descrição gerada por IA. |
| `ANO` | STRING | Ano letivo de referência dos dados do Censo Escolar (formato AAAA). — descrição gerada por IA. |
| `CODMUNIC` | STRING | Código IBGE de 6 ou 7 dígitos do município onde se localiza a escola. — descrição gerada por IA. |
| `UF` | STRING | Nome completo da Unidade da Federação onde a escola está situada. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla da Unidade da Federação (ex: RO, SP, RJ). — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do município de localização da escola. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa da escola (ex: Federal, Estadual, Municipal, Particular). — descrição gerada por IA. |
| `LOC` | STRING | Localização do estabelecimento de ensino (ex: Urbana, Rural). — descrição gerada por IA. |
| `CODFUNC` | STRING | Situação de funcionamento do estabelecimento escolar (ex: Ativo, Paralisada, Extinta). — descrição gerada por IA. |
| `IEI00001` | STRING | Indicador 00001 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00002` | STRING | Indicador 00002 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00003` | STRING | Indicador 00003 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00004` | STRING | Indicador 00004 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00005` | STRING | Indicador 00005 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00006` | STRING | Indicador 00006 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00007` | STRING | Indicador 00007 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00008` | STRING | Indicador 00008 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00009` | STRING | Indicador 00009 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00010` | STRING | Indicador 00010 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00011` | STRING | Indicador 00011 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEI00012` | STRING | Indicador 00012 da Educação Infantil (INEP/Censo Escolar). — descrição gerada por IA. |
| `ICA00001` | STRING | Indicador 00001 de Creche/Atendimento Complementar (INEP/Censo Escolar). — descrição gerada por IA. |
| `ICA00002` | STRING | Indicador 00002 de Creche/Atendimento Complementar (INEP/Censo Escolar). — descrição gerada por IA. |
| `ICA00003` | STRING | Indicador 00003 de Creche/Atendimento Complementar (INEP/Censo Escolar). — descrição gerada por IA. |
| `ICA00004` | STRING | Indicador 00004 de Creche/Atendimento Complementar (INEP/Censo Escolar). — descrição gerada por IA. |
| `ICA00005` | STRING | Indicador 00005 de Creche/Atendimento Complementar (INEP/Censo Escolar). — descrição gerada por IA. |
| `ICA00006` | STRING | Indicador 00006 de Creche/Atendimento Complementar (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00001` | STRING | Indicador 00001 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00002` | STRING | Indicador 00002 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00003` | STRING | Indicador 00003 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00004` | STRING | Indicador 00004 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00005` | STRING | Indicador 00005 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00006` | STRING | Indicador 00006 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00007` | STRING | Indicador 00007 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00008` | STRING | Indicador 00008 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00009` | STRING | Indicador 00009 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00010` | STRING | Indicador 00010 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00011` | STRING | Indicador 00011 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00012` | STRING | Indicador 00012 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00013` | STRING | Indicador 00013 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00014` | STRING | Indicador 00014 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00015` | STRING | Indicador 00015 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00016` | STRING | Indicador 00016 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00017` | STRING | Indicador 00017 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00018` | STRING | Indicador 00018 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00019` | STRING | Indicador 00019 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00020` | STRING | Indicador 00020 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00021` | STRING | Indicador 00021 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00022` | STRING | Indicador 00022 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00023` | STRING | Indicador 00023 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00024` | STRING | Indicador 00024 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00025` | STRING | Indicador 00025 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00026` | STRING | Indicador 00026 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00027` | STRING | Indicador 00027 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00028` | STRING | Indicador 00028 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00029` | STRING | Indicador 00029 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00030` | STRING | Indicador 00030 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00031` | STRING | Indicador 00031 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00032` | STRING | Indicador 00032 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00033` | STRING | Indicador 00033 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00034` | STRING | Indicador 00034 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00035` | STRING | Indicador 00035 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00036` | STRING | Indicador 00036 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00037` | STRING | Indicador 00037 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00038` | STRING | Indicador 00038 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00039` | STRING | Indicador 00039 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00040` | STRING | Indicador 00040 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00041` | STRING | Indicador 00041 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00042` | STRING | Indicador 00042 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00043` | STRING | Indicador 00043 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00044` | STRING | Indicador 00044 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00045` | STRING | Indicador 00045 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00046` | STRING | Indicador 00046 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00047` | STRING | Indicador 00047 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00048` | STRING | Indicador 00048 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00049` | STRING | Indicador 00049 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00050` | STRING | Indicador 00050 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00051` | STRING | Indicador 00051 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00052` | STRING | Indicador 00052 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00053` | STRING | Indicador 00053 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00054` | STRING | Indicador 00054 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00055` | STRING | Indicador 00055 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00056` | STRING | Indicador 00056 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00057` | STRING | Indicador 00057 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00058` | STRING | Indicador 00058 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00059` | STRING | Indicador 00059 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00060` | STRING | Indicador 00060 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00061` | STRING | Indicador 00061 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00062` | STRING | Indicador 00062 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00063` | STRING | Indicador 00063 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00064` | STRING | Indicador 00064 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00065` | STRING | Indicador 00065 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00066` | STRING | Indicador 00066 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00067` | STRING | Indicador 00067 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00068` | STRING | Indicador 00068 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00069` | STRING | Indicador 00069 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00070` | STRING | Indicador 00070 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00071` | STRING | Indicador 00071 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00072` | STRING | Indicador 00072 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00073` | STRING | Indicador 00073 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00074` | STRING | Indicador 00074 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00075` | STRING | Indicador 00075 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00076` | STRING | Indicador 00076 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00077` | STRING | Indicador 00077 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00078` | STRING | Indicador 00078 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00079` | STRING | Indicador 00079 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00080` | STRING | Indicador 00080 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00081` | STRING | Indicador 00081 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00082` | STRING | Indicador 00082 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00083` | STRING | Indicador 00083 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00084` | STRING | Indicador 00084 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00085` | STRING | Indicador 00085 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00086` | STRING | Indicador 00086 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00087` | STRING | Indicador 00087 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00088` | STRING | Indicador 00088 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00089` | STRING | Indicador 00089 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00090` | STRING | Indicador 00090 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00091` | STRING | Indicador 00091 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00092` | STRING | Indicador 00092 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00093` | STRING | Indicador 00093 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00094` | STRING | Indicador 00094 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00095` | STRING | Indicador 00095 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00096` | STRING | Indicador 00096 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00097` | STRING | Indicador 00097 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00098` | STRING | Indicador 00098 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00099` | STRING | Indicador 00099 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00100` | STRING | Indicador 00100 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00101` | STRING | Indicador 00101 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00102` | STRING | Indicador 00102 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00103` | STRING | Indicador 00103 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00104` | STRING | Indicador 00104 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00105` | STRING | Indicador 00105 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00106` | STRING | Indicador 00106 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00107` | STRING | Indicador 00107 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00108` | STRING | Indicador 00108 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEF00109` | STRING | Indicador 00109 do Ensino Fundamental (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00001` | STRING | Indicador 00001 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00002` | STRING | Indicador 00002 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00003` | STRING | Indicador 00003 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00004` | STRING | Indicador 00004 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00005` | STRING | Indicador 00005 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00006` | STRING | Indicador 00006 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00007` | STRING | Indicador 00007 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00008` | STRING | Indicador 00008 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00009` | STRING | Indicador 00009 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00010` | STRING | Indicador 00010 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00011` | STRING | Indicador 00011 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00012` | STRING | Indicador 00012 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00013` | STRING | Indicador 00013 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00014` | STRING | Indicador 00014 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00015` | STRING | Indicador 00015 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00016` | STRING | Indicador 00016 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00017` | STRING | Indicador 00017 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00018` | STRING | Indicador 00018 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00019` | STRING | Indicador 00019 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00020` | STRING | Indicador 00020 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00021` | STRING | Indicador 00021 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00022` | STRING | Indicador 00022 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00023` | STRING | Indicador 00023 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00024` | STRING | Indicador 00024 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00025` | STRING | Indicador 00025 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00026` | STRING | Indicador 00026 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00027` | STRING | Indicador 00027 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00028` | STRING | Indicador 00028 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00029` | STRING | Indicador 00029 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00030` | STRING | Indicador 00030 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00031` | STRING | Indicador 00031 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00032` | STRING | Indicador 00032 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00033` | STRING | Indicador 00033 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00034` | STRING | Indicador 00034 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00035` | STRING | Indicador 00035 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00037` | STRING | Indicador 00037 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00038` | STRING | Indicador 00038 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00039` | STRING | Indicador 00039 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00040` | STRING | Indicador 00040 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00041` | STRING | Indicador 00041 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00042` | STRING | Indicador 00042 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00043` | STRING | Indicador 00043 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00044` | STRING | Indicador 00044 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00045` | STRING | Indicador 00045 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00046` | STRING | Indicador 00046 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00047` | STRING | Indicador 00047 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00048` | STRING | Indicador 00048 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00049` | STRING | Indicador 00049 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00050` | STRING | Indicador 00050 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00051` | STRING | Indicador 00051 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00052` | STRING | Indicador 00052 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00053` | STRING | Indicador 00053 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00054` | STRING | Indicador 00054 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00055` | STRING | Indicador 00055 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00056` | STRING | Indicador 00056 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00057` | STRING | Indicador 00057 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00058` | STRING | Indicador 00058 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `IEM00059` | STRING | Indicador 00059 do Ensino Médio (INEP/Censo Escolar). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_indicreg

File `raw__inep_censo_escolar_indicreg.parquet` · 270,956 rows · 195 columns

Raw Censo Escolar INEP. Familia de CSV: indicreg. Anos cobertos: 2000-2003 (4 ano(s)): 2000, 2001, 2002, 2003. Arquivos de origem: INDICREG_2000.CSV, INDICREG_2001.CSV, INDICREG_2002.CSV, INDICREG_2003.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `ANO` | STRING | Ano de referência dos indicadores educacionais. — descrição gerada por IA. |
| `CODUNGE` | STRING | Código da Unidade Geográfica ou do município segundo a classificação do INEP/IBGE. — descrição gerada por IA. |
| `NOME` | STRING | Nome da Unidade Geográfica ou do município correspondente. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa das instituições agregadas (ex: Total, Estadual, Municipal, Privada). — descrição gerada por IA. |
| `LOC` | STRING | Localização do endereço/zona das escolas agregadas (ex: Urbana, Rural). — descrição gerada por IA. |
| `IEI00001` | STRING | Indicador estatístico de Educação Infantil - código 01 do Censo Escolar. — descrição gerada por IA. |
| `IEI00002` | STRING | Indicador estatístico de Educação Infantil - código 02 do Censo Escolar. — descrição gerada por IA. |
| `IEI00003` | STRING | Indicador estatístico de Educação Infantil - código 03 do Censo Escolar. — descrição gerada por IA. |
| `IEI00004` | STRING | Indicador estatístico de Educação Infantil - código 04 do Censo Escolar. — descrição gerada por IA. |
| `IEI00005` | STRING | Indicador estatístico de Educação Infantil - código 05 do Censo Escolar. — descrição gerada por IA. |
| `IEI00006` | STRING | Indicador estatístico de Educação Infantil - código 06 do Censo Escolar. — descrição gerada por IA. |
| `IEI00007` | STRING | Indicador estatístico de Educação Infantil - código 07 do Censo Escolar. — descrição gerada por IA. |
| `IEI00008` | STRING | Indicador estatístico de Educação Infantil - código 08 do Censo Escolar. — descrição gerada por IA. |
| `IEI00009` | STRING | Indicador estatístico de Educação Infantil - código 09 do Censo Escolar. — descrição gerada por IA. |
| `IEI00010` | STRING | Indicador estatístico de Educação Infantil - código 10 do Censo Escolar. — descrição gerada por IA. |
| `IEI00011` | STRING | Indicador estatístico de Educação Infantil - código 11 do Censo Escolar. — descrição gerada por IA. |
| `IEI00012` | STRING | Indicador estatístico de Educação Infantil - código 12 do Censo Escolar. — descrição gerada por IA. |
| `ICA00001` | STRING | Indicador estatístico de Atendimento em Creche/Infantil - código 01. — descrição gerada por IA. |
| `ICA00002` | STRING | Indicador estatístico de Atendimento em Creche/Infantil - código 02. — descrição gerada por IA. |
| `ICA00003` | STRING | Indicador estatístico de Atendimento em Creche/Infantil - código 03. — descrição gerada por IA. |
| `ICA00004` | STRING | Indicador estatístico de Atendimento em Creche/Infantil - código 04. — descrição gerada por IA. |
| `ICA00005` | STRING | Indicador estatístico de Atendimento em Creche/Infantil - código 05. — descrição gerada por IA. |
| `ICA00006` | STRING | Indicador estatístico de Atendimento em Creche/Infantil - código 06. — descrição gerada por IA. |
| `IEF00001` | STRING | Indicador estatístico do Ensino Fundamental - código 01 (ex: taxa de aprovação/média). — descrição gerada por IA. |
| `IEF00002` | STRING | Indicador estatístico do Ensino Fundamental - código 02. — descrição gerada por IA. |
| `IEF00003` | STRING | Indicador estatístico do Ensino Fundamental - código 03. — descrição gerada por IA. |
| `IEF00004` | STRING | Indicador estatístico do Ensino Fundamental - código 04. — descrição gerada por IA. |
| `IEF00005` | STRING | Indicador estatístico do Ensino Fundamental - código 05. — descrição gerada por IA. |
| `IEF00006` | STRING | Indicador estatístico do Ensino Fundamental - código 06. — descrição gerada por IA. |
| `IEF00007` | STRING | Indicador estatístico do Ensino Fundamental - código 07. — descrição gerada por IA. |
| `IEF00008` | STRING | Indicador estatístico do Ensino Fundamental - código 08. — descrição gerada por IA. |
| `IEF00009` | STRING | Indicador estatístico do Ensino Fundamental - código 09. — descrição gerada por IA. |
| `IEF00010` | STRING | Indicador estatístico do Ensino Fundamental - código 10. — descrição gerada por IA. |
| `IEF00011` | STRING | Indicador estatístico do Ensino Fundamental - código 11. — descrição gerada por IA. |
| `IEF00012` | STRING | Indicador estatístico do Ensino Fundamental - código 12. — descrição gerada por IA. |
| `IEF00013` | STRING | Indicador estatístico do Ensino Fundamental - código 13. — descrição gerada por IA. |
| `IEF00014` | STRING | Indicador estatístico do Ensino Fundamental - código 14. — descrição gerada por IA. |
| `IEF00015` | STRING | Indicador estatístico do Ensino Fundamental - código 15. — descrição gerada por IA. |
| `IEF00016` | STRING | Indicador estatístico do Ensino Fundamental - código 16. — descrição gerada por IA. |
| `IEF00017` | STRING | Indicador estatístico do Ensino Fundamental - código 17. — descrição gerada por IA. |
| `IEF00018` | STRING | Indicador estatístico do Ensino Fundamental - código 18. — descrição gerada por IA. |
| `IEF00019` | STRING | Indicador estatístico do Ensino Fundamental - código 19. — descrição gerada por IA. |
| `IEF00020` | STRING | Indicador estatístico do Ensino Fundamental - código 20. — descrição gerada por IA. |
| `IEF00021` | STRING | Indicador estatístico do Ensino Fundamental - código 21. — descrição gerada por IA. |
| `IEF00022` | STRING | Indicador estatístico do Ensino Fundamental - código 22. — descrição gerada por IA. |
| `IEF00023` | STRING | Indicador estatístico do Ensino Fundamental - código 23. — descrição gerada por IA. |
| `IEF00024` | STRING | Indicador estatístico do Ensino Fundamental - código 24. — descrição gerada por IA. |
| `IEF00025` | STRING | Indicador estatístico do Ensino Fundamental - código 25. — descrição gerada por IA. |
| `IEF00026` | STRING | Indicador estatístico do Ensino Fundamental - código 26. — descrição gerada por IA. |
| `IEF00027` | STRING | Indicador estatístico do Ensino Fundamental - código 27. — descrição gerada por IA. |
| `IEF00028` | STRING | Indicador estatístico do Ensino Fundamental - código 28. — descrição gerada por IA. |
| `IEF00029` | STRING | Indicador estatístico do Ensino Fundamental - código 29. — descrição gerada por IA. |
| `IEF00030` | STRING | Indicador estatístico do Ensino Fundamental - código 30. — descrição gerada por IA. |
| `IEF00031` | STRING | Indicador estatístico do Ensino Fundamental - código 31. — descrição gerada por IA. |
| `IEF00032` | STRING | Indicador estatístico do Ensino Fundamental - código 32. — descrição gerada por IA. |
| `IEF00033` | STRING | Indicador estatístico do Ensino Fundamental - código 33. — descrição gerada por IA. |
| `IEF00034` | STRING | Indicador estatístico do Ensino Fundamental - código 34. — descrição gerada por IA. |
| `IEF00035` | STRING | Indicador estatístico do Ensino Fundamental - código 35. — descrição gerada por IA. |
| `IEF00036` | STRING | Indicador estatístico do Ensino Fundamental - código 36. — descrição gerada por IA. |
| `IEF00037` | STRING | Indicador estatístico do Ensino Fundamental - código 37. — descrição gerada por IA. |
| `IEF00038` | STRING | Indicador estatístico do Ensino Fundamental - código 38. — descrição gerada por IA. |
| `IEF00039` | STRING | Indicador estatístico do Ensino Fundamental - código 39. — descrição gerada por IA. |
| `IEF00040` | STRING | Indicador estatístico do Ensino Fundamental - código 40. — descrição gerada por IA. |
| `IEF00041` | STRING | Indicador estatístico do Ensino Fundamental - código 41. — descrição gerada por IA. |
| `IEF00042` | STRING | Indicador estatístico do Ensino Fundamental - código 42. — descrição gerada por IA. |
| `IEF00043` | STRING | Indicador estatístico do Ensino Fundamental - código 43. — descrição gerada por IA. |
| `IEF00044` | STRING | Indicador estatístico do Ensino Fundamental - código 44. — descrição gerada por IA. |
| `IEF00045` | STRING | Indicador estatístico do Ensino Fundamental - código 45. — descrição gerada por IA. |
| `IEF00046` | STRING | Indicador estatístico do Ensino Fundamental - código 46. — descrição gerada por IA. |
| `IEF00047` | STRING | Indicador estatístico do Ensino Fundamental - código 47. — descrição gerada por IA. |
| `IEF00048` | STRING | Indicador estatístico do Ensino Fundamental - código 48. — descrição gerada por IA. |
| `IEF00049` | STRING | Indicador estatístico do Ensino Fundamental - código 49. — descrição gerada por IA. |
| `IEF00050` | STRING | Indicador estatístico do Ensino Fundamental - código 50. — descrição gerada por IA. |
| `IEF00051` | STRING | Indicador estatístico do Ensino Fundamental - código 51. — descrição gerada por IA. |
| `IEF00052` | STRING | Indicador estatístico do Ensino Fundamental - código 52. — descrição gerada por IA. |
| `IEF00053` | STRING | Indicador estatístico do Ensino Fundamental - código 53. — descrição gerada por IA. |
| `IEF00054` | STRING | Indicador estatístico do Ensino Fundamental - código 54. — descrição gerada por IA. |
| `IEF00055` | STRING | Indicador estatístico do Ensino Fundamental - código 55. — descrição gerada por IA. |
| `IEF00056` | STRING | Indicador estatístico do Ensino Fundamental - código 56. — descrição gerada por IA. |
| `IEF00057` | STRING | Indicador estatístico do Ensino Fundamental - código 57. — descrição gerada por IA. |
| `IEF00058` | STRING | Indicador estatístico do Ensino Fundamental - código 58. — descrição gerada por IA. |
| `IEF00059` | STRING | Indicador estatístico do Ensino Fundamental - código 59. — descrição gerada por IA. |
| `IEF00060` | STRING | Indicador estatístico do Ensino Fundamental - código 60. — descrição gerada por IA. |
| `IEF00061` | STRING | Indicador estatístico do Ensino Fundamental - código 61. — descrição gerada por IA. |
| `IEF00062` | STRING | Indicador estatístico do Ensino Fundamental - código 62. — descrição gerada por IA. |
| `IEF00063` | STRING | Indicador estatístico do Ensino Fundamental - código 63. — descrição gerada por IA. |
| `IEF00064` | STRING | Indicador estatístico do Ensino Fundamental - código 64. — descrição gerada por IA. |
| `IEF00065` | STRING | Indicador estatístico do Ensino Fundamental - código 65. — descrição gerada por IA. |
| `IEF00066` | STRING | Indicador estatístico do Ensino Fundamental - código 66. — descrição gerada por IA. |
| `IEF00067` | STRING | Indicador estatístico do Ensino Fundamental - código 67. — descrição gerada por IA. |
| `IEF00068` | STRING | Indicador estatístico do Ensino Fundamental - código 68. — descrição gerada por IA. |
| `IEF00069` | STRING | Indicador estatístico do Ensino Fundamental - código 69. — descrição gerada por IA. |
| `IEF00070` | STRING | Indicador estatístico do Ensino Fundamental - código 70. — descrição gerada por IA. |
| `IEF00071` | STRING | Indicador estatístico do Ensino Fundamental - código 71. — descrição gerada por IA. |
| `IEF00072` | STRING | Indicador estatístico do Ensino Fundamental - código 72. — descrição gerada por IA. |
| `IEF00073` | STRING | Indicador estatístico do Ensino Fundamental - código 73. — descrição gerada por IA. |
| `IEF00074` | STRING | Indicador estatístico do Ensino Fundamental - código 74. — descrição gerada por IA. |
| `IEF00075` | STRING | Indicador estatístico do Ensino Fundamental - código 75. — descrição gerada por IA. |
| `IEF00076` | STRING | Indicador estatístico do Ensino Fundamental - código 76. — descrição gerada por IA. |
| `IEF00077` | STRING | Indicador estatístico do Ensino Fundamental - código 77. — descrição gerada por IA. |
| `IEF00078` | STRING | Indicador estatístico do Ensino Fundamental - código 78. — descrição gerada por IA. |
| `IEF00079` | STRING | Indicador estatístico do Ensino Fundamental - código 79. — descrição gerada por IA. |
| `IEF00080` | STRING | Indicador estatístico do Ensino Fundamental - código 80. — descrição gerada por IA. |
| `IEF00081` | STRING | Indicador estatístico do Ensino Fundamental - código 81. — descrição gerada por IA. |
| `IEF00082` | STRING | Indicador estatístico do Ensino Fundamental - código 82. — descrição gerada por IA. |
| `IEF00083` | STRING | Indicador estatístico do Ensino Fundamental - código 83. — descrição gerada por IA. |
| `IEF00084` | STRING | Indicador estatístico do Ensino Fundamental - código 84. — descrição gerada por IA. |
| `IEF00085` | STRING | Indicador estatístico do Ensino Fundamental - código 85. — descrição gerada por IA. |
| `IEF00086` | STRING | Indicador estatístico do Ensino Fundamental - código 86. — descrição gerada por IA. |
| `IEF00087` | STRING | Indicador estatístico do Ensino Fundamental - código 87. — descrição gerada por IA. |
| `IEF00088` | STRING | Indicador estatístico do Ensino Fundamental - código 88. — descrição gerada por IA. |
| `IEF00089` | STRING | Indicador estatístico do Ensino Fundamental - código 89. — descrição gerada por IA. |
| `IEF00090` | STRING | Indicador estatístico do Ensino Fundamental - código 90. — descrição gerada por IA. |
| `IEF00091` | STRING | Indicador estatístico do Ensino Fundamental - código 91. — descrição gerada por IA. |
| `IEF00092` | STRING | Indicador estatístico do Ensino Fundamental - código 92. — descrição gerada por IA. |
| `IEF00093` | STRING | Indicador estatístico do Ensino Fundamental - código 93. — descrição gerada por IA. |
| `IEF00094` | STRING | Indicador estatístico do Ensino Fundamental - código 94. — descrição gerada por IA. |
| `IEF00095` | STRING | Indicador estatístico do Ensino Fundamental - código 95. — descrição gerada por IA. |
| `IEF00096` | STRING | Indicador estatístico do Ensino Fundamental - código 96. — descrição gerada por IA. |
| `IEF00097` | STRING | Indicador estatístico do Ensino Fundamental - código 97. — descrição gerada por IA. |
| `IEF00098` | STRING | Indicador estatístico do Ensino Fundamental - código 98. — descrição gerada por IA. |
| `IEF00099` | STRING | Indicador estatístico do Ensino Fundamental - código 99. — descrição gerada por IA. |
| `IEF00100` | STRING | Indicador estatístico do Ensino Fundamental - código 100. — descrição gerada por IA. |
| `IEF00101` | STRING | Indicador estatístico do Ensino Fundamental - código 101. — descrição gerada por IA. |
| `IEF00102` | STRING | Indicador estatístico do Ensino Fundamental - código 102. — descrição gerada por IA. |
| `IEF00103` | STRING | Indicador estatístico do Ensino Fundamental - código 103. — descrição gerada por IA. |
| `IEF00104` | STRING | Indicador estatístico do Ensino Fundamental - código 104. — descrição gerada por IA. |
| `IEF00105` | STRING | Indicador estatístico do Ensino Fundamental - código 105. — descrição gerada por IA. |
| `IEF00106` | STRING | Indicador estatístico do Ensino Fundamental - código 106. — descrição gerada por IA. |
| `IEF00107` | STRING | Indicador estatístico do Ensino Fundamental - código 107. — descrição gerada por IA. |
| `IEF00108` | STRING | Indicador estatístico do Ensino Fundamental - código 108. — descrição gerada por IA. |
| `IEF00109` | STRING | Indicador estatístico do Ensino Fundamental - código 109. — descrição gerada por IA. |
| `IEM00001` | STRING | Indicador estatístico do Ensino Médio - código 01. — descrição gerada por IA. |
| `IEM00002` | STRING | Indicador estatístico do Ensino Médio - código 02. — descrição gerada por IA. |
| `IEM00003` | STRING | Indicador estatístico do Ensino Médio - código 03. — descrição gerada por IA. |
| `IEM00004` | STRING | Indicador estatístico do Ensino Médio - código 04. — descrição gerada por IA. |
| `IEM00005` | STRING | Indicador estatístico do Ensino Médio - código 05. — descrição gerada por IA. |
| `IEM00006` | STRING | Indicador estatístico do Ensino Médio - código 06. — descrição gerada por IA. |
| `IEM00007` | STRING | Indicador estatístico do Ensino Médio - código 07. — descrição gerada por IA. |
| `IEM00008` | STRING | Indicador estatístico do Ensino Médio - código 08. — descrição gerada por IA. |
| `IEM00009` | STRING | Indicador estatístico do Ensino Médio - código 09. — descrição gerada por IA. |
| `IEM00010` | STRING | Indicador estatístico do Ensino Médio - código 10. — descrição gerada por IA. |
| `IEM00011` | STRING | Indicador estatístico do Ensino Médio - código 11. — descrição gerada por IA. |
| `IEM00012` | STRING | Indicador estatístico do Ensino Médio - código 12. — descrição gerada por IA. |
| `IEM00013` | STRING | Indicador estatístico do Ensino Médio - código 13. — descrição gerada por IA. |
| `IEM00014` | STRING | Indicador estatístico do Ensino Médio - código 14. — descrição gerada por IA. |
| `IEM00015` | STRING | Indicador estatístico do Ensino Médio - código 15. — descrição gerada por IA. |
| `IEM00016` | STRING | Indicador estatístico do Ensino Médio - código 16. — descrição gerada por IA. |
| `IEM00017` | STRING | Indicador estatístico do Ensino Médio - código 17. — descrição gerada por IA. |
| `IEM00018` | STRING | Indicador estatístico do Ensino Médio - código 18. — descrição gerada por IA. |
| `IEM00019` | STRING | Indicador estatístico do Ensino Médio - código 19. — descrição gerada por IA. |
| `IEM00020` | STRING | Indicador estatístico do Ensino Médio - código 20. — descrição gerada por IA. |
| `IEM00021` | STRING | Indicador estatístico do Ensino Médio - código 21. — descrição gerada por IA. |
| `IEM00022` | STRING | Indicador estatístico do Ensino Médio - código 22. — descrição gerada por IA. |
| `IEM00023` | STRING | Indicador estatístico do Ensino Médio - código 23. — descrição gerada por IA. |
| `IEM00024` | STRING | Indicador estatístico do Ensino Médio - código 24. — descrição gerada por IA. |
| `IEM00025` | STRING | Indicador estatístico do Ensino Médio - código 25. — descrição gerada por IA. |
| `IEM00026` | STRING | Indicador estatístico do Ensino Médio - código 26. — descrição gerada por IA. |
| `IEM00027` | STRING | Indicador estatístico do Ensino Médio - código 27. — descrição gerada por IA. |
| `IEM00028` | STRING | Indicador estatístico do Ensino Médio - código 28. — descrição gerada por IA. |
| `IEM00029` | STRING | Indicador estatístico do Ensino Médio - código 29. — descrição gerada por IA. |
| `IEM00030` | STRING | Indicador estatístico do Ensino Médio - código 30. — descrição gerada por IA. |
| `IEM00031` | STRING | Indicador estatístico do Ensino Médio - código 31. — descrição gerada por IA. |
| `IEM00032` | STRING | Indicador estatístico do Ensino Médio - código 32. — descrição gerada por IA. |
| `IEM00033` | STRING | Indicador estatístico do Ensino Médio - código 33. — descrição gerada por IA. |
| `IEM00034` | STRING | Indicador estatístico do Ensino Médio - código 34. — descrição gerada por IA. |
| `IEM00035` | STRING | Indicador estatístico do Ensino Médio - código 35. — descrição gerada por IA. |
| `IEM00037` | STRING | Indicador estatístico do Ensino Médio - código 37. — descrição gerada por IA. |
| `IEM00038` | STRING | Indicador estatístico do Ensino Médio - código 38. — descrição gerada por IA. |
| `IEM00039` | STRING | Indicador estatístico do Ensino Médio - código 39. — descrição gerada por IA. |
| `IEM00040` | STRING | Indicador estatístico do Ensino Médio - código 40. — descrição gerada por IA. |
| `IEM00041` | STRING | Indicador estatístico do Ensino Médio - código 41. — descrição gerada por IA. |
| `IEM00042` | STRING | Indicador estatístico do Ensino Médio - código 42. — descrição gerada por IA. |
| `IEM00043` | STRING | Indicador estatístico do Ensino Médio - código 43. — descrição gerada por IA. |
| `IEM00044` | STRING | Indicador estatístico do Ensino Médio - código 44. — descrição gerada por IA. |
| `IEM00045` | STRING | Indicador estatístico do Ensino Médio - código 45. — descrição gerada por IA. |
| `IEM00046` | STRING | Indicador estatístico do Ensino Médio - código 46. — descrição gerada por IA. |
| `IEM00047` | STRING | Indicador estatístico do Ensino Médio - código 47. — descrição gerada por IA. |
| `IEM00048` | STRING | Indicador estatístico do Ensino Médio - código 48. — descrição gerada por IA. |
| `IEM00049` | STRING | Indicador estatístico do Ensino Médio - código 49. — descrição gerada por IA. |
| `IEM00050` | STRING | Indicador estatístico do Ensino Médio - código 50. — descrição gerada por IA. |
| `IEM00051` | STRING | Indicador estatístico do Ensino Médio - código 51. — descrição gerada por IA. |
| `IEM00052` | STRING | Indicador estatístico do Ensino Médio - código 52. — descrição gerada por IA. |
| `IEM00053` | STRING | Indicador estatístico do Ensino Médio - código 53. — descrição gerada por IA. |
| `IEM00054` | STRING | Indicador estatístico do Ensino Médio - código 54. — descrição gerada por IA. |
| `IEM00055` | STRING | Indicador estatístico do Ensino Médio - código 55. — descrição gerada por IA. |
| `IEM00056` | STRING | Indicador estatístico do Ensino Médio - código 56. — descrição gerada por IA. |
| `IEM00057` | STRING | Indicador estatístico do Ensino Médio - código 57. — descrição gerada por IA. |
| `IEM00058` | STRING | Indicador estatístico do Ensino Médio - código 58. — descrição gerada por IA. |
| `IEM00059` | STRING | Indicador estatístico do Ensino Médio - código 59. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_matricula

File `raw__inep_censo_escolar_matricula.parquet` · 178,766 rows · 242 columns

Raw Censo Escolar INEP. Familia de CSV: matricula. Anos cobertos: 2025-2025 (1 ano(s)): 2025. Arquivos de origem: Tabela_Matricula_2025.csv. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

**Feeds:** `trusted/inep_censo_escolar_matriculas`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano de realização do Censo Escolar (YYYY). — descrição gerada por IA. |
| `CO_ENTIDADE` | STRING | Código INEP de identificação única da escola (entidade). — descrição gerada por IA. |
| `QT_MAT_BAS` | STRING | Quantidade total de matrículas na educação básica. — descrição gerada por IA. |
| `QT_MAT_INF` | STRING | Quantidade total de matrículas na educação infantil. — descrição gerada por IA. |
| `QT_MAT_INF_CRE` | STRING | Quantidade de matrículas na educação infantil - creche. — descrição gerada por IA. |
| `QT_MAT_INF_PRE` | STRING | Quantidade de matrículas na educação infantil - pré-escola. — descrição gerada por IA. |
| `QT_MAT_FUND` | STRING | Quantidade total de matrículas no ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI` | STRING | Quantidade de matrículas nos anos iniciais do ensino fundamental (1º ao 5º ano). — descrição gerada por IA. |
| `QT_MAT_FUND_AI_1` | STRING | Quantidade de matrículas no 1º ano do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_2` | STRING | Quantidade de matrículas no 2º ano do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_3` | STRING | Quantidade de matrículas no 3º ano do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_4` | STRING | Quantidade de matrículas no 4º ano do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_5` | STRING | Quantidade de matrículas no 5º ano do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF` | STRING | Quantidade de matrículas nos anos finais do ensino fundamental (6º ao 9º ano). — descrição gerada por IA. |
| `QT_MAT_FUND_AF_6` | STRING | Quantidade de matrículas no 6º ano do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_7` | STRING | Quantidade de matrículas no 7º ano do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_8` | STRING | Quantidade de matrículas no 8º ano do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_9` | STRING | Quantidade de matrículas no 9º ano do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_MED` | STRING | Quantidade total de matrículas no ensino médio. — descrição gerada por IA. |
| `QT_MAT_MED_PROP` | STRING | Quantidade de matrículas no ensino médio propedêutico (regular). — descrição gerada por IA. |
| `QT_MAT_MED_PROP_1` | STRING | Quantidade de matrículas na 1ª série do ensino médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_2` | STRING | Quantidade de matrículas na 2ª série do ensino médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_3` | STRING | Quantidade de matrículas na 3ª série do ensino médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_4` | STRING | Quantidade de matrículas na 4ª série do ensino médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_NS` | STRING | Quantidade de matrículas no ensino médio propedêutico não seriado. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT` | STRING | Quantidade de matrículas no ensino médio integrado à educação profissional técnica. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_1` | STRING | Quantidade de matrículas na 1ª série do ensino médio integrado técnico. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_2` | STRING | Quantidade de matrículas na 2ª série do ensino médio integrado técnico. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_3` | STRING | Quantidade de matrículas na 3ª série do ensino médio integrado técnico. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_4` | STRING | Quantidade de matrículas na 4ª série do ensino médio integrado técnico. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_NS` | STRING | Quantidade de matrículas no ensino médio integrado técnico não seriado. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP` | STRING | Quantidade de matrículas no ensino médio integrado com qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_1` | STRING | Quantidade de matrículas na 1ª série do ensino médio integrado com qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_2` | STRING | Quantidade de matrículas na 2ª série do ensino médio integrado com qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_3` | STRING | Quantidade de matrículas na 3ª série do ensino médio integrado com qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_4` | STRING | Quantidade de matrículas na 4ª série do ensino médio integrado com qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_NS` | STRING | Quantidade de matrículas no ensino médio integrado com qualificação profissional não seriado. — descrição gerada por IA. |
| `QT_MAT_MED_NM` | STRING | Quantidade de matrículas na modalidade Normal/Magistério do ensino médio. — descrição gerada por IA. |
| `QT_MAT_MED_NM_1` | STRING | Quantidade de matrículas na 1ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_2` | STRING | Quantidade de matrículas na 2ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_3` | STRING | Quantidade de matrículas na 3ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_4` | STRING | Quantidade de matrículas na 4ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_IFA` | STRING | Quantidade total de matrículas em itinerários formativos do ensino médio. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING` | STRING | Matrículas no itinerário formativo de Linguagens e suas Tecnologias. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING_MT` | STRING | Matrículas em Linguagens associadas à formação técnica. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING_OTME` | STRING | Matrículas em Linguagens associadas a outro itinerário formativo. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING_OE` | STRING | Matrículas em itinerário específico de Linguagens. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE` | STRING | Matrículas no itinerário formativo de Matemática e suas Tecnologias. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE_MT` | STRING | Matrículas em Matemática associadas à formação técnica. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE_OTME` | STRING | Matrículas em Matemática associadas a outro itinerário. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE_OE` | STRING | Matrículas em itinerário específico de Matemática. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC` | STRING | Matrículas no itinerário formativo de Ciências da Natureza. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC_MT` | STRING | Matrículas em Ciências da Natureza associadas à formação técnica. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC_OTME` | STRING | Matrículas em Ciências da Natureza associadas a outro itinerário. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC_OE` | STRING | Matrículas em itinerário específico de Ciências da Natureza. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA` | STRING | Matrículas no itinerário formativo de Ciências Humanas e Sociais Aplicadas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA_MT` | STRING | Matrículas em Ciências Humanas associadas à formação técnica. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA_OTME` | STRING | Matrículas em Ciências Humanas associadas a outro itinerário. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA_OE` | STRING | Matrículas em itinerário específico de Ciências Humanas. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT` | STRING | Matrículas em ensino médio articulado com curso técnico. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT_MT` | STRING | Matrículas articuladas com curso técnico concomitante. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT_OTME` | STRING | Matrículas articuladas com curso técnico associado a outro itinerário. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT_OE` | STRING | Matrículas articuladas com curso técnico em itinerário exclusivo. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP` | STRING | Matrículas articuladas de qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP_MT` | STRING | Matrículas articuladas de qualificação profissional concomitante. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP_OTME` | STRING | Matrículas articuladas de qualificação profissional associadas a outro itinerário. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP_OE` | STRING | Matrículas articuladas de qualificação profissional exclusivas. — descrição gerada por IA. |
| `QT_MAT_PROF` | STRING | Total de matrículas em Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC` | STRING | Matrículas na Educação Profissional Técnica de Nível Médio. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_CONC` | STRING | Matrículas no ensino técnico em modalidade concomitante. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_SUBS` | STRING | Matrículas no ensino técnico em modalidade subsequente. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_IFTP_CT` | STRING | Matrículas no ensino técnico integrado. — descrição gerada por IA. |
| `QT_MAT_PROF_NAO_TEC` | STRING | Matrículas em cursos de formação inicial/qualificação profissional não técnica. — descrição gerada por IA. |
| `QT_MAT_PROF_IFTP_QP` | STRING | Matrículas em qualificação profissional no ensino médio integrado. — descrição gerada por IA. |
| `QT_MAT_PROF_FIC_CONC` | STRING | Matrículas em Formação Inicial e Continuada (FIC) concomitantes. — descrição gerada por IA. |
| `QT_MAT_EJA` | STRING | Total de matrículas na Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |
| `QT_MAT_EJA_FUND` | STRING | Matrículas na EJA do ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_NPROF` | STRING | Matrículas na EJA fundamental não profissionalizante. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AI` | STRING | Matrículas na EJA do ensino fundamental - anos iniciais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AF` | STRING | Matrículas na EJA do ensino fundamental - anos finais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_FIC` | STRING | Matrículas na EJA do ensino fundamental integrada à formação inicial/continuada (FIC). — descrição gerada por IA. |
| `QT_MAT_EJA_MED` | STRING | Matrículas na EJA do ensino médio. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_NPROF` | STRING | Matrículas na EJA do ensino médio não profissionalizante. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_FIC` | STRING | Matrículas na EJA do ensino médio integrada à FIC. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_TEC` | STRING | Matrículas na EJA do ensino médio integrada ao ensino técnico. — descrição gerada por IA. |
| `QT_MAT_ESP` | STRING | Total de matrículas na Educação Especial. — descrição gerada por IA. |
| `QT_MAT_ESP_INF` | STRING | Matrículas na Educação Especial - educação infantil. — descrição gerada por IA. |
| `QT_MAT_ESP_INF_CRE` | STRING | Matrículas na Educação Especial - creche. — descrição gerada por IA. |
| `QT_MAT_ESP_INF_PRE` | STRING | Matrículas na Educação Especial - pré-escola. — descrição gerada por IA. |
| `QT_MAT_ESP_FUND` | STRING | Matrículas na Educação Especial - ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_FUND_AI` | STRING | Matrículas na Educação Especial - fundamental anos iniciais. — descrição gerada por IA. |
| `QT_MAT_ESP_FUND_AF` | STRING | Matrículas na Educação Especial - fundamental anos finais. — descrição gerada por IA. |
| `QT_MAT_ESP_MED` | STRING | Matrículas na Educação Especial - ensino médio. — descrição gerada por IA. |
| `QT_MAT_ESP_PROF` | STRING | Matrículas na Educação Especial - educação profissional. — descrição gerada por IA. |
| `QT_MAT_ESP_PROF_TEC` | STRING | Matrículas na Educação Especial - profissional técnica. — descrição gerada por IA. |
| `QT_MAT_ESP_EJA` | STRING | Matrículas na Educação Especial - EJA. — descrição gerada por IA. |
| `QT_MAT_ESP_EJA_FUND` | STRING | Matrículas na Educação Especial - EJA ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_EJA_MED` | STRING | Matrículas na Educação Especial - EJA ensino médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CC` | STRING | Matrículas na Educação Especial em classes comuns/inclusivas. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INF` | STRING | Matrículas em classes comuns de Educação Especial - infantil. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INF_CRE` | STRING | Matrículas em classes comuns de Educação Especial - creche. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INF_PRE` | STRING | Matrículas em classes comuns de Educação Especial - pré-escola. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_FUND` | STRING | Matrículas em classes comuns de Educação Especial - fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_FUND_AI` | STRING | Matrículas em classes comuns de Educação Especial - fundamental anos iniciais. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_FUND_AF` | STRING | Matrículas em classes comuns de Educação Especial - fundamental anos finais. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_MED` | STRING | Matrículas em classes comuns de Educação Especial - ensino médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_PROF` | STRING | Matrículas em classes comuns de Educação Especial - educação profissional. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_PROF_TEC` | STRING | Matrículas em classes comuns de Educação Especial - profissional técnica. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EJA` | STRING | Matrículas em classes comuns de Educação Especial - EJA. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EJA_FUND` | STRING | Matrículas em classes comuns de Educação Especial - EJA fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EJA_MED` | STRING | Matrículas em classes comuns de Educação Especial - EJA médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CE` | STRING | Matrículas na Educação Especial em classes exclusivas ou escolas especiais. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INF` | STRING | Matrículas em classes exclusivas de Educação Especial - infantil. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INF_CRE` | STRING | Matrículas em classes exclusivas de Educação Especial - creche. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INF_PRE` | STRING | Matrículas em classes exclusivas de Educação Especial - pré-escola. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_FUND` | STRING | Matrículas em classes exclusivas de Educação Especial - fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_FUND_AI` | STRING | Matrículas em classes exclusivas de Educação Especial - fundamental anos iniciais. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_FUND_AF` | STRING | Matrículas em classes exclusivas de Educação Especial - fundamental anos finais. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_MED` | STRING | Matrículas em classes exclusivas de Educação Especial - ensino médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_PROF` | STRING | Matrículas em classes exclusivas de Educação Especial - educação profissional. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_PROF_TEC` | STRING | Matrículas em classes exclusivas de Educação Especial - profissional técnica. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EJA` | STRING | Matrículas em classes exclusivas de Educação Especial - EJA. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EJA_FUND` | STRING | Matrículas em classes exclusivas de Educação Especial - EJA fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EJA_MED` | STRING | Matrículas em classes exclusivas de Educação Especial - EJA médio. — descrição gerada por IA. |
| `QT_MAT_BAS_FEM` | STRING | Matrículas de alunos do sexo feminino na educação básica. — descrição gerada por IA. |
| `QT_MAT_BAS_MASC` | STRING | Matrículas de alunos do sexo masculino na educação básica. — descrição gerada por IA. |
| `QT_MAT_BAS_ND` | STRING | Matrículas na educação básica com sexo não declarado. — descrição gerada por IA. |
| `QT_MAT_BAS_BRANCA` | STRING | Matrículas de alunos autodeclarados brancos na educação básica. — descrição gerada por IA. |
| `QT_MAT_BAS_PRETA` | STRING | Matrículas de alunos autodeclarados pretos na educação básica. — descrição gerada por IA. |
| `QT_MAT_BAS_PARDA` | STRING | Matrículas de alunos autodeclarados pardos na educação básica. — descrição gerada por IA. |
| `QT_MAT_BAS_AMARELA` | STRING | Matrículas de alunos autodeclarados amarelos na educação básica. — descrição gerada por IA. |
| `QT_MAT_BAS_INDIGENA` | STRING | Matrículas de alunos autodeclarados indígenas na educação básica. — descrição gerada por IA. |
| `QT_MAT_BAS_0_3` | STRING | Matrículas na educação básica com idade de 0 a 3 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_4_5` | STRING | Matrículas na educação básica com idade de 4 a 5 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_6_10` | STRING | Matrículas na educação básica com idade de 6 a 10 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_11_14` | STRING | Matrículas na educação básica com idade de 11 a 14 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_15_17` | STRING | Matrículas na educação básica com idade de 15 a 17 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_18_MAIS` | STRING | Matrículas na educação básica com 18 anos ou mais. — descrição gerada por IA. |
| `QT_MAT_BAS_0_3_REF_31_03` | STRING | Matrículas na educação básica de 0 a 3 anos em 31/03 do ano censo. — descrição gerada por IA. |
| `QT_MAT_BAS_4_5_REF_31_03` | STRING | Matrículas na educação básica de 4 a 5 anos em 31/03 do ano censo. — descrição gerada por IA. |
| `QT_MAT_BAS_6_10_REF_31_03` | STRING | Matrículas na educação básica de 6 a 10 anos em 31/03 do ano censo. — descrição gerada por IA. |
| `QT_MAT_BAS_11_14_REF_31_03` | STRING | Matrículas na educação básica de 11 a 14 anos em 31/03 do ano censo. — descrição gerada por IA. |
| `QT_MAT_BAS_15_17_REF_31_03` | STRING | Matrículas na educação básica de 15 a 17 anos em 31/03 do ano censo. — descrição gerada por IA. |
| `QT_MAT_BAS_18_MAIS_REF_31_03` | STRING | Matrículas na educação básica com 18 anos ou mais em 31/03 do ano censo. — descrição gerada por IA. |
| `QT_MAT_BAS_D` | STRING | Matrículas na educação básica em turno diurno. — descrição gerada por IA. |
| `QT_MAT_BAS_DM` | STRING | Matrículas na educação básica no turno da manhã. — descrição gerada por IA. |
| `QT_MAT_BAS_DV` | STRING | Matrículas na educação básica no turno da tarde. — descrição gerada por IA. |
| `QT_MAT_BAS_N` | STRING | Matrículas na educação básica no turno da noite. — descrição gerada por IA. |
| `QT_MAT_BAS_EAD` | STRING | Matrículas na educação básica na modalidade a distância (EAD). — descrição gerada por IA. |
| `QT_MAT_INF_CRE_D` | STRING | Matrículas em creche - turno diurno. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_DM` | STRING | Matrículas em creche - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_DV` | STRING | Matrículas em creche - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_N` | STRING | Matrículas em creche - turno da noite. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_D` | STRING | Matrículas na pré-escola - turno diurno. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_DM` | STRING | Matrículas na pré-escola - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_DV` | STRING | Matrículas na pré-escola - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_N` | STRING | Matrículas na pré-escola - turno da noite. — descrição gerada por IA. |
| `QT_MAT_FUND_D` | STRING | Matrículas no ensino fundamental - turno diurno. — descrição gerada por IA. |
| `QT_MAT_FUND_DM` | STRING | Matrículas no ensino fundamental - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_FUND_DV` | STRING | Matrículas no ensino fundamental - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_FUND_N` | STRING | Matrículas no ensino fundamental - turno da noite. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_D` | STRING | Matrículas no fundamental anos iniciais - turno diurno. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_DM` | STRING | Matrículas no fundamental anos iniciais - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_DV` | STRING | Matrículas no fundamental anos iniciais - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_N` | STRING | Matrículas no fundamental anos iniciais - turno da noite. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_D` | STRING | Matrículas no fundamental anos finais - turno diurno. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_DM` | STRING | Matrículas no fundamental anos finais - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_DV` | STRING | Matrículas no fundamental anos finais - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_N` | STRING | Matrículas no fundamental anos finais - turno da noite. — descrição gerada por IA. |
| `QT_MAT_MED_D` | STRING | Matrículas no ensino médio - turno diurno. — descrição gerada por IA. |
| `QT_MAT_MED_DM` | STRING | Matrículas no ensino médio - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_MED_DV` | STRING | Matrículas no ensino médio - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_MED_N` | STRING | Matrículas no ensino médio - turno da noite. — descrição gerada por IA. |
| `QT_MAT_MED_EAD` | STRING | Matrículas no ensino médio na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_PROF_D` | STRING | Matrículas na educação profissional - turno diurno. — descrição gerada por IA. |
| `QT_MAT_PROF_DM` | STRING | Matrículas na educação profissional - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_PROF_DV` | STRING | Matrículas na educação profissional - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_PROF_N` | STRING | Matrículas na educação profissional - turno da noite. — descrição gerada por IA. |
| `QT_MAT_PROF_EAD` | STRING | Matrículas na educação profissional - modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_D` | STRING | Matrículas na educação profissional técnica - turno diurno. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_DM` | STRING | Matrículas na educação profissional técnica - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_DV` | STRING | Matrículas na educação profissional técnica - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_N` | STRING | Matrículas na educação profissional técnica - turno da noite. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_EAD` | STRING | Matrículas na educação profissional técnica - modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_EJA_D` | STRING | Matrículas na EJA - turno diurno. — descrição gerada por IA. |
| `QT_MAT_EJA_DM` | STRING | Matrículas na EJA - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_EJA_DV` | STRING | Matrículas na EJA - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_EJA_N` | STRING | Matrículas na EJA - turno da noite. — descrição gerada por IA. |
| `QT_MAT_EJA_EAD` | STRING | Matrículas na EJA - modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_D` | STRING | Matrículas na EJA ensino fundamental - turno diurno. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_DM` | STRING | Matrículas na EJA ensino fundamental - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_DV` | STRING | Matrículas na EJA ensino fundamental - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_N` | STRING | Matrículas na EJA ensino fundamental - turno da noite. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_EAD` | STRING | Matrículas na EJA ensino fundamental - modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_D` | STRING | Matrículas na EJA ensino médio - turno diurno. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_DM` | STRING | Matrículas na EJA ensino médio - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_DV` | STRING | Matrículas na EJA ensino médio - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_N` | STRING | Matrículas na EJA ensino médio - turno da noite. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_EAD` | STRING | Matrículas na EJA ensino médio - modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_ESP_D` | STRING | Matrículas na Educação Especial - turno diurno. — descrição gerada por IA. |
| `QT_MAT_ESP_DM` | STRING | Matrículas na Educação Especial - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_ESP_DV` | STRING | Matrículas na Educação Especial - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_ESP_N` | STRING | Matrículas na Educação Especial - turno da noite. — descrição gerada por IA. |
| `QT_MAT_ESP_EAD` | STRING | Matrículas na Educação Especial - modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_D` | STRING | Matrículas na Educação Especial em classes comuns - turno diurno. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_DM` | STRING | Matrículas na Educação Especial em classes comuns - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_DV` | STRING | Matrículas na Educação Especial em classes comuns - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_N` | STRING | Matrículas na Educação Especial em classes comuns - turno da noite. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EAD` | STRING | Matrículas na Educação Especial em classes comuns - EAD. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_D` | STRING | Matrículas na Educação Especial em classes exclusivas - turno diurno. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_DM` | STRING | Matrículas na Educação Especial em classes exclusivas - turno da manhã. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_DV` | STRING | Matrículas na Educação Especial em classes exclusivas - turno da tarde. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_N` | STRING | Matrículas na Educação Especial em classes exclusivas - turno da noite. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EAD` | STRING | Matrículas na Educação Especial em classes exclusivas - EAD. — descrição gerada por IA. |
| `QT_MAT_BAS_INT` | STRING | Matrículas em tempo integral na educação básica. — descrição gerada por IA. |
| `QT_MAT_INF_INT` | STRING | Matrículas em tempo integral na educação infantil. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_INT` | STRING | Matrículas em tempo integral na creche. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_INT` | STRING | Matrículas em tempo integral na pré-escola. — descrição gerada por IA. |
| `QT_MAT_FUND_INT` | STRING | Matrículas em tempo integral no ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_INT` | STRING | Matrículas em tempo integral no fundamental anos iniciais. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_INT` | STRING | Matrículas em tempo integral no fundamental anos finais. — descrição gerada por IA. |
| `QT_MAT_MED_INT` | STRING | Matrículas em tempo integral no ensino médio. — descrição gerada por IA. |
| `QT_MAT_PROF_INT` | STRING | Matrículas em tempo integral na educação profissional. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_INT` | STRING | Matrículas em tempo integral na educação profissional técnica. — descrição gerada por IA. |
| `QT_MAT_EJA_INT` | STRING | Matrículas em tempo integral na EJA. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_INT` | STRING | Matrículas em tempo integral na EJA ensino fundamental. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_INT` | STRING | Matrículas em tempo integral na EJA ensino médio. — descrição gerada por IA. |
| `QT_MAT_ESP_INT` | STRING | Matrículas em tempo integral na Educação Especial. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INT` | STRING | Matrículas em tempo integral na Educação Especial em classes comuns. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INT` | STRING | Matrículas em tempo integral na Educação Especial em classes exclusivas. — descrição gerada por IA. |
| `QT_MAT_BAS_LIBRAS` | STRING | Quantidade de matrículas na educação básica que utilizam Libras. — descrição gerada por IA. |
| `QT_MAT_ZR_URB` | STRING | Quantidade de alunos matriculados residentes em zona urbana. — descrição gerada por IA. |
| `QT_MAT_ZR_RUR` | STRING | Quantidade de alunos matriculados residentes em zona rural. — descrição gerada por IA. |
| `QT_MAT_ZR_NA` | STRING | Matrículas de alunos cuja zona de residência não se aplica ou não foi declarada. — descrição gerada por IA. |
| `QT_TRANSP_PUBLICO` | STRING | Total de matrículas com uso de transporte escolar público. — descrição gerada por IA. |
| `QT_TRANSP_RESP_EST` | STRING | Matrículas com transporte público sob responsabilidade do Estado. — descrição gerada por IA. |
| `QT_TRANSP_RESP_MUN` | STRING | Matrículas com transporte público sob responsabilidade do Município. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_medprof

File `raw__inep_censo_escolar_medprof.parquet` · 102,591 rows · 43 columns

Raw Censo Escolar INEP. Familia de CSV: medprof. Anos cobertos: 2000-2003 (4 ano(s)): 2000, 2001, 2002, 2003. Arquivos de origem: MEDPROF_2000.CSV, MEDPROF_2001.CSV, MEDPROF_2002.CSV, MEDPROF_2003.CSV. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `MASCARA` | STRING | Identificador mascarado/código da escola no microdado do Censo Escolar. — descrição gerada por IA. |
| `ANO` | STRING | Ano de referência do Censo Escolar (ex: 2000). — descrição gerada por IA. |
| `CODMUNIC` | STRING | Código IBGE/INEP do município da escola. — descrição gerada por IA. |
| `UF` | STRING | Nome completo da Unidade Federativa da escola. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla da Unidade Federativa (ex: BA, GO, MA). — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do município onde a escola está localizada. — descrição gerada por IA. |
| `DEP` | STRING | Dependência administrativa da escola (Federal, Estadual, Municipal ou Particular). — descrição gerada por IA. |
| `LOC` | STRING | Localização da zona da escola (Urbana ou Rural). — descrição gerada por IA. |
| `CODFUNC` | STRING | Situação de funcionamento da escola (ex: Ativo). — descrição gerada por IA. |
| `HABILCOD` | STRING | Código numérico da habilitação profissional/curso técnico. — descrição gerada por IA. |
| `HABILNOM` | STRING | Nome do curso técnico ou habilitação profissional ofertada (ex: Técnico em Agricultura). — descrição gerada por IA. |
| `VEM1215` | STRING | Quantidade de matrículas/vagas no Ensino Médio Profissionalizante no turno vespertino/noturno (código 1215). — descrição gerada por IA. |
| `VEM1216` | STRING | Quantidade de matrículas/vagas no Ensino Médio Profissionalizante no turno vespertino/noturno (código 1216). — descrição gerada por IA. |
| `VEM1217` | STRING | Quantidade de matrículas/vagas no Ensino Médio Profissionalizante no turno vespertino/noturno (código 1217). — descrição gerada por IA. |
| `VEM1218` | STRING | Quantidade de matrículas/vagas no Ensino Médio Profissionalizante no turno vespertino/noturno (código 1218). — descrição gerada por IA. |
| `VEM1219` | STRING | Quantidade de matrículas/vagas no Ensino Médio Profissionalizante no turno vespertino/noturno (código 1219). — descrição gerada por IA. |
| `VEM1214` | STRING | Quantidade de matrículas/vagas no Ensino Médio Profissionalizante no turno vespertino/noturno (código 1214). — descrição gerada por IA. |
| `DEM1214` | STRING | Demanda ou contagem de alunos para a modalidade/turma 1214. — descrição gerada por IA. |
| `VEM2015` | STRING | Quantidade de vagas/matrículas para o código de modalidade 2015. — descrição gerada por IA. |
| `VEM2016` | STRING | Quantidade de vagas/matrículas para o código de modalidade 2016. — descrição gerada por IA. |
| `VEM2017` | STRING | Quantidade de vagas/matrículas para o código de modalidade 2017. — descrição gerada por IA. |
| `VEM2018` | STRING | Quantidade de vagas/matrículas para o código de modalidade 2018. — descrição gerada por IA. |
| `VEM2019` | STRING | Quantidade de vagas/matrículas para o código de modalidade 2019. — descrição gerada por IA. |
| `NEM2014` | STRING | Número de turmas ou alunos no Ensino Médio Técnico para o código 2014. — descrição gerada por IA. |
| `CODIGO` | STRING | Código identificador adicional da instituição ou habilitação. — descrição gerada por IA. |
| `NOME` | STRING | Nome da escola ou instituição de ensino profissionalizante. — descrição gerada por IA. |
| `EM1215` | STRING | Contagem de matrículas no Ensino Médio (modalidade 1215). — descrição gerada por IA. |
| `EM1216` | STRING | Contagem de matrículas no Ensino Médio (modalidade 1216). — descrição gerada por IA. |
| `EM1217` | STRING | Contagem de matrículas no Ensino Médio (modalidade 1217). — descrição gerada por IA. |
| `EM1218` | STRING | Contagem de matrículas no Ensino Médio (modalidade 1218). — descrição gerada por IA. |
| `EM1219` | STRING | Contagem de matrículas no Ensino Médio (modalidade 1219). — descrição gerada por IA. |
| `EM1214` | STRING | Contagem de matrículas no Ensino Médio (modalidade 1214). — descrição gerada por IA. |
| `EM2015` | STRING | Contagem de matrículas no Ensino Médio (modalidade 2015). — descrição gerada por IA. |
| `EM2016` | STRING | Contagem de matrículas no Ensino Médio (modalidade 2016). — descrição gerada por IA. |
| `EM2017` | STRING | Contagem de matrículas no Ensino Médio (modalidade 2017). — descrição gerada por IA. |
| `EM2018` | STRING | Contagem de matrículas no Ensino Médio (modalidade 2018). — descrição gerada por IA. |
| `EM2019` | STRING | Contagem de matrículas no Ensino Médio (modalidade 2019). — descrição gerada por IA. |
| `EM2014` | STRING | Contagem de matrículas no Ensino Médio (modalidade 2014). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_microdados_ed_basica

File `raw__inep_censo_escolar_microdados_ed_basica.parquet` · 4,058,464 rows · 479 columns

Raw Censo Escolar INEP. Familia de CSV: microdados_ed_basica. Anos cobertos: 2007-2024 (18 ano(s)): 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024. Arquivos de origem: microdados_ed_basica_2007.csv, microdados_ed_basica_2008.csv, microdados_ed_basica_2009.csv, microdados_ed_basica_2010.csv, microdados_ed_basica_2011.csv, microdados_ed_basica_2012.csv, microdados_ed_basica_2013.csv, microdados_ed_basica_2014.csv, microdados_ed_basica_2015.csv, microdados_ed_basica_2016.csv, microdados_ed_basica_2017.csv, microdados_ed_basica_2018.csv, microdados_ed_basica_2019.csv, microdados_ed_basica_2020.CSV, microdados_ed_basica_2021.csv, microdados_ed_basica_2022.csv, microdados_ed_basica_2023.csv, microdados_ed_basica_2024.csv. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano de referência do Censo Escolar (AAAA). — descrição gerada por IA. |
| `NO_REGIAO` | STRING | Nome da região geográfica da escola. — descrição gerada por IA. |
| `CO_REGIAO` | STRING | Código IBGE da região geográfica. — descrição gerada por IA. |
| `NO_UF` | STRING | Nome da Unidade da Federação. — descrição gerada por IA. |
| `SG_UF` | STRING | Sigla da Unidade da Federação. — descrição gerada por IA. |
| `CO_UF` | STRING | Código IBGE da Unidade da Federação. — descrição gerada por IA. |
| `NO_MUNICIPIO` | STRING | Nome do município da escola. — descrição gerada por IA. |
| `CO_MUNICIPIO` | STRING | Código IBGE do município. — descrição gerada por IA. |
| `NO_MESORREGIAO` | STRING | Nome da mesorregião geográfica. — descrição gerada por IA. |
| `CO_MESORREGIAO` | STRING | Código IBGE da mesorregião. — descrição gerada por IA. |
| `NO_MICRORREGIAO` | STRING | Nome da microrregião geográfica. — descrição gerada por IA. |
| `CO_MICRORREGIAO` | STRING | Código IBGE da microrregião. — descrição gerada por IA. |
| `CO_DISTRITO` | STRING | Código IBGE do distrito. — descrição gerada por IA. |
| `CO_ENTIDADE` | STRING | Código INEP único da escola. — descrição gerada por IA. |
| `NO_ENTIDADE` | STRING | Nome oficial da escola. — descrição gerada por IA. |
| `TP_DEPENDENCIA` | STRING | Dependência administrativa (1:Federal, 2:Estadual, 3:Municipal, 4:Privada). — descrição gerada por IA. |
| `TP_CATEGORIA_ESCOLA_PRIVADA` | STRING | Categoria da escola privada (Particular, Comunitária, Confessional, Filantrópica). — descrição gerada por IA. |
| `TP_LOCALIZACAO` | STRING | Localização da escola (1:Urbana, 2:Rural). — descrição gerada por IA. |
| `TP_LOCALIZACAO_DIFERENCIADA` | STRING | Indicador de localização em área diferenciada (Assentamento, Terra Indígena, Quilombola, etc.). — descrição gerada por IA. |
| `DS_ENDERECO` | STRING | Logradouro e endereço da escola. — descrição gerada por IA. |
| `NU_ENDERECO` | STRING | Número do endereço da escola. — descrição gerada por IA. |
| `DS_COMPLEMENTO` | STRING | Complemento do endereço. — descrição gerada por IA. |
| `NO_BAIRRO` | STRING | Bairro onde a escola está localizada. — descrição gerada por IA. |
| `CO_CEP` | STRING | CEP do endereço da escola. — descrição gerada por IA. |
| `NU_DDD` | STRING | DDD do telefone da escola. — descrição gerada por IA. |
| `NU_TELEFONE` | STRING | Número de telefone da escola. — descrição gerada por IA. |
| `TP_SITUACAO_FUNCIONAMENTO` | STRING | Situação de funcionamento (1:Em atividade, 2:Paralisada, 3:Extinta). — descrição gerada por IA. |
| `CO_ORGAO_REGIONAL` | STRING | Código do órgão regional de ensino associado. — descrição gerada por IA. |
| `DT_ANO_LETIVO_INICIO` | STRING | Data de início do ano letivo. — descrição gerada por IA. |
| `DT_ANO_LETIVO_TERMINO` | STRING | Data de término do ano letivo. — descrição gerada por IA. |
| `IN_VINCULO_SECRETARIA_EDUCACAO` | STRING | Indica vínculo com a Secretaria de Educação (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_VINCULO_SEGURANCA_PUBLICA` | STRING | Indica vínculo com órgão de Segurança Pública (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_VINCULO_SECRETARIA_SAUDE` | STRING | Indica vínculo com a Secretaria de Saúde (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_VINCULO_OUTRO_ORGAO` | STRING | Indica vínculo com outro órgão público (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_CONVENIADA_PP` | STRING | Indica se a escola privada tem convênio com o poder público (1:Sim, 0:Não). — descrição gerada por IA. |
| `TP_CONVENIO_PODER_PUBLICO` | STRING | Tipo de conveniamento com o poder público. — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_EMP` | STRING | Indica mantenedora empresa/grupo empresarial (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_ONG` | STRING | Indica mantenedora associação/ONG (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_OSCIP` | STRING | Indica mantenedora OSCIP (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIV_ONG_OSCIP` | STRING | Indica mantenedora ONG/OSCIP. — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_SIND` | STRING | Indica mantenedora sindicato (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_SIST_S` | STRING | Indica mantenedora Sistema S (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_S_FINS` | STRING | Indica mantenedora sem fins lucrativos (1:Sim, 0:Não). — descrição gerada por IA. |
| `NU_CNPJ_ESCOLA_PRIVADA` | STRING | CNPJ da escola privada. — descrição gerada por IA. |
| `NU_CNPJ_MANTENEDORA` | STRING | CNPJ da mantenedora da escola. — descrição gerada por IA. |
| `TP_REGULAMENTACAO` | STRING | Situação de regulamentação no Conselho de Educação (1:Sim, 2:Não, 3:Em tramitação). — descrição gerada por IA. |
| `TP_RESPONSAVEL_REGULAMENTACAO` | STRING | Órgão responsável pela regulamentação. — descrição gerada por IA. |
| `CO_ESCOLA_SEDE_VINCULADA` | STRING | Código INEP da escola sede em caso de extensão. — descrição gerada por IA. |
| `CO_IES_OFERTANTE` | STRING | Código da Instituição de Ensino Superior ofertante. — descrição gerada por IA. |
| `IN_LOCAL_FUNC_PREDIO_ESCOLAR` | STRING | Indica funcionamento em prédio escolar próprio/alugado (1:Sim, 0:Não). — descrição gerada por IA. |
| `TP_OCUPACAO_PREDIO_ESCOLAR` | STRING | Tipo de ocupação do prédio (Próprio, Alugado, Cedido). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SALAS_EMPRESA` | STRING | Indica funcionamento em salas de empresa (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SOCIOEDUCATIVO` | STRING | Indica funcionamento em unidade socioeducativa (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_UNID_PRISIONAL` | STRING | Indica funcionamento em unidade prisional (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_PRISIONAL_SOCIO` | STRING | Indica funcionamento em unidade prisional/socioeducativa (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_TEMPLO_IGREJA` | STRING | Indica funcionamento em templo/igreja (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_CASA_PROFESSOR` | STRING | Indica funcionamento na casa do professor (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_GALPAO` | STRING | Indica funcionamento em galpão (1:Sim, 0:Não). — descrição gerada por IA. |
| `TP_OCUPACAO_GALPAO` | STRING | Tipo de ocupação do galpão. — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SALAS_OUTRA_ESC` | STRING | Indica funcionamento em salas de outra escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_OUTROS` | STRING | Indica funcionamento em outros locais (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PREDIO_COMPARTILHADO` | STRING | Indica compartilhamento de prédio com outra escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AGUA_FILTRADA` | STRING | Indica fornecimento de água filtrada (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AGUA_POTAVEL` | STRING | Indica fornecimento de água potável (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AGUA_REDE_PUBLICA` | STRING | Indica abastecimento via rede pública de água (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AGUA_POCO_ARTESIANO` | STRING | Indica abastecimento via poço artesiano (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AGUA_CACIMBA` | STRING | Indica abastecimento via cacimba/poço/cisterna (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AGUA_FONTE_RIO` | STRING | Indica abastecimento via fonte/rio/igarapé (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AGUA_INEXISTENTE` | STRING | Indica inexistência de abastecimento de água (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ENERGIA_REDE_PUBLICA` | STRING | Indica energia da rede pública (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ENERGIA_GERADOR` | STRING | Indica uso de gerador elétrico (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ENERGIA_GERADOR_FOSSIL` | STRING | Indica uso de gerador a combustível fóssil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ENERGIA_OUTROS` | STRING | Indica outras fontes de energia (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ENERGIA_RENOVAVEL` | STRING | Indica fonte de energia renovável/solar/eólica (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ENERGIA_INEXISTENTE` | STRING | Indica inexistência de energia elétrica (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESGOTO_REDE_PUBLICA` | STRING | Indica esgotamento por rede pública (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESGOTO_FOSSA_SEPTICA` | STRING | Indica esgotamento por fossa séptica (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESGOTO_FOSSA_COMUM` | STRING | Indica esgotamento por fossa comum/rudimentar (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESGOTO_FOSSA` | STRING | Indica presença de fossa sanitária (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESGOTO_INEXISTENTE` | STRING | Indica inexistência de esgotamento sanitário (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LIXO_SERVICO_COLETA` | STRING | Indica destinação do lixo por serviço de coleta (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LIXO_QUEIMA` | STRING | Indica queima do lixo na escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LIXO_ENTERRA` | STRING | Indica descarte de lixo enterrado (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LIXO_DESTINO_FINAL_PUBLICO` | STRING | Indica descarte em destino público apropriado (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LIXO_DESCARTA_OUTRA_AREA` | STRING | Indica descarte em outra área fora da escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LIXO_JOGA_OUTRA_AREA` | STRING | Indica descarte inadequado em outra área (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LIXO_OUTROS` | STRING | Indica outros destinos de lixo (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LIXO_RECICLA` | STRING | Indica presença de coleta/destinação para reciclagem (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_SEPARACAO` | STRING | Indica separação de resíduos sólidos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_REUTILIZA` | STRING | Indica reutilização de materiais/lixo (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_RECICLAGEM` | STRING | Indica processo de reciclagem de lixo (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_INEXISTENTE` | STRING | Indica ausência de tratamento do lixo (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ALMOXARIFADO` | STRING | Indica existência de almoxarifado (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AREA_VERDE` | STRING | Indica presença de área verde (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AUDITORIO` | STRING | Indica presença de auditório (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BANHEIRO_FORA_PREDIO` | STRING | Indica banheiro fora do prédio escolar (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BANHEIRO_DENTRO_PREDIO` | STRING | Indica banheiro dentro do prédio escolar (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BANHEIRO` | STRING | Indica presença de banheiro na escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BANHEIRO_EI` | STRING | Indica banheiro adequado para Educação Infantil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BANHEIRO_PNE` | STRING | Indica banheiro adaptado para pessoas com deficiência/mobilidade reduzida (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BANHEIRO_FUNCIONARIOS` | STRING | Indica banheiro exclusivo para funcionários (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BANHEIRO_CHUVEIRO` | STRING | Indica banheiro com chuveiro (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BERCARIO` | STRING | Indica presença de berçário (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA` | STRING | Indica presença de biblioteca (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA_SALA_LEITURA` | STRING | Indica presença de biblioteca ou sala de leitura (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_COZINHA` | STRING | Indica presença de cozinha (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_DESPENSA` | STRING | Indica presença de despensa (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_DORMITORIO_ALUNO` | STRING | Indica presença de dormitório de alunos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_DORMITORIO_PROFESSOR` | STRING | Indica presença de dormitório de professores (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LABORATORIO_CIENCIAS` | STRING | Indica presença de laboratório de ciências (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LABORATORIO_INFORMATICA` | STRING | Indica presença de laboratório de informática (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PATIO_COBERTO` | STRING | Indica presença de pátio coberto (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PATIO_DESCOBERTO` | STRING | Indica presença de pátio descoberto (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PARQUE_INFANTIL` | STRING | Indica presença de parque infantil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PISCINA` | STRING | Indica presença de piscina (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES` | STRING | Indica presença de quadra de esportes (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES_COBERTA` | STRING | Indica presença de quadra de esportes coberta (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES_DESCOBERTA` | STRING | Indica presença de quadra de esportes descoberta (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_REFEITORIO` | STRING | Indica presença de refeitório (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_ATELIE_ARTES` | STRING | Indica presença de ateliê de artes (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_MUSICA_CORAL` | STRING | Indica presença de sala de música/coral (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_ESTUDIO_DANCA` | STRING | Indica presença de estúdio de dança (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_MULTIUSO` | STRING | Indica presença de sala multiuso (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_DIRETORIA` | STRING | Indica presença de sala de diretoria (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_LEITURA` | STRING | Indica presença de sala de leitura (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_PROFESSOR` | STRING | Indica presença de sala dos professores (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_REPOUSO_ALUNO` | STRING | Indica presença de sala de repouso para alunos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SECRETARIA` | STRING | Indica presença de secretaria (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_ATENDIMENTO_ESPECIAL` | STRING | Indica presença de sala de Atendimento Educacional Especializado - AEE (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_TERREIRAO` | STRING | Indica presença de terreirão/espaço ao ar livre para práticas culturais (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_VIVEIRO` | STRING | Indica presença de viveiro/criação de animais (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_DEPENDENCIAS_PNE` | STRING | Indica existência de instalações/dependências acessíveis a PcD (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LAVANDERIA` | STRING | Indica presença de lavanderia (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_DEPENDENCIAS_OUTRAS` | STRING | Indica presença de outras dependências (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_CORRIMAO` | STRING | Indica acessibilidade com corrimão/guardacorpo (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_ELEVADOR` | STRING | Indica acessibilidade com elevador (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_PISOS_TATEIS` | STRING | Indica acessibilidade com piso tátil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_VAO_LIVRE` | STRING | Indica acessibilidade por portas com vão livre adequado (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_RAMPAS` | STRING | Indica acessibilidade com rampas (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINAL_SONORO` | STRING | Indica acessibilidade com sinalização sonora (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINAL_TATIL` | STRING | Indica acessibilidade com sinalização tátil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINAL_VISUAL` | STRING | Indica acessibilidade com sinalização visual (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_INEXISTENTE` | STRING | Indica ausência de recursos de acessibilidade (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_SALAS_EXISTENTES` | STRING | Quantidade total de salas de aula existentes na escola. — descrição gerada por IA. |
| `QT_SALAS_UTILIZADAS_DENTRO` | STRING | Quantidade de salas de aula utilizadas dentro do prédio escolar. — descrição gerada por IA. |
| `QT_SALAS_UTILIZADAS_FORA` | STRING | Quantidade de salas de aula utilizadas fora do prédio escolar. — descrição gerada por IA. |
| `QT_SALAS_UTILIZADAS` | STRING | Quantidade total de salas de aula utilizadas. — descrição gerada por IA. |
| `QT_SALAS_UTILIZA_CLIMATIZADAS` | STRING | Quantidade de salas de aula climatizadas (ar-condicionado/ventilador). — descrição gerada por IA. |
| `QT_SALAS_UTILIZADAS_ACESSIVEIS` | STRING | Quantidade de salas de aula acessíveis a pessoas com deficiência. — descrição gerada por IA. |
| `IN_EQUIP_PARABOLICA` | STRING | Indica presença de antena parabólica (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_COMPUTADOR` | STRING | Indica presença de computadores na escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EQUIP_COPIADORA` | STRING | Indica presença de máquina copiadora (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EQUIP_IMPRESSORA` | STRING | Indica presença de impressora (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EQUIP_IMPRESSORA_MULT` | STRING | Indica presença de impressora multifuncional (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EQUIP_SCANNER` | STRING | Indica presença de scanner (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EQUIP_NENHUM` | STRING | Indica ausência de equipamentos listados (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EQUIP_DVD` | STRING | Indica presença de aparelho de DVD (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_EQUIP_DVD` | STRING | Quantidade de aparelhos de DVD. — descrição gerada por IA. |
| `IN_EQUIP_SOM` | STRING | Indica presença de aparelho de som (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_EQUIP_SOM` | STRING | Quantidade de aparelhos de som. — descrição gerada por IA. |
| `IN_EQUIP_TV` | STRING | Indica presença de aparelho de televisão (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_EQUIP_TV` | STRING | Quantidade de aparelhos de televisão. — descrição gerada por IA. |
| `IN_EQUIP_LOUSA_DIGITAL` | STRING | Indica presença de lousa digital (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_EQUIP_LOUSA_DIGITAL` | STRING | Quantidade de lousas digitais. — descrição gerada por IA. |
| `IN_EQUIP_MULTIMIDIA` | STRING | Indica presença de projetor/multimídia (datashow) (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_EQUIP_MULTIMIDIA` | STRING | Quantidade de aparelhos multimídia/projetores. — descrição gerada por IA. |
| `IN_EQUIP_VIDEOCASSETE` | STRING | Indica presença de videocassete (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EQUIP_RETROPROJETOR` | STRING | Indica presença de retroprojetor (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EQUIP_FAX` | STRING | Indica presença de fax (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EQUIP_FOTO` | STRING | Indica presença de câmera fotográfica/filmadora (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_EQUIP_VIDEOCASSETE` | STRING | Quantidade de aparelhos de videocassete. — descrição gerada por IA. |
| `QT_EQUIP_PARABOLICA` | STRING | Quantidade de antenas parabólicas. — descrição gerada por IA. |
| `QT_EQUIP_COPIADORA` | STRING | Quantidade de copiadoras. — descrição gerada por IA. |
| `QT_EQUIP_RETROPROJETOR` | STRING | Quantidade de retroprojetores. — descrição gerada por IA. |
| `QT_EQUIP_IMPRESSORA` | STRING | Quantidade de impressoras simples. — descrição gerada por IA. |
| `QT_EQUIP_IMPRESSORA_MULT` | STRING | Quantidade de impressoras multifuncionais. — descrição gerada por IA. |
| `QT_EQUIP_FAX` | STRING | Quantidade de aparelhos de fax. — descrição gerada por IA. |
| `QT_EQUIP_FOTO` | STRING | Quantidade de câmeras fotográficas/filmadoras. — descrição gerada por IA. |
| `QT_COMP_ALUNO` | STRING | Quantidade total de computadores de uso dos alunos. — descrição gerada por IA. |
| `IN_DESKTOP_ALUNO` | STRING | Indica uso de computadores desktop por alunos (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_DESKTOP_ALUNO` | STRING | Quantidade de computadores desktop para alunos. — descrição gerada por IA. |
| `IN_COMP_PORTATIL_ALUNO` | STRING | Indica uso de notebooks/laptops por alunos (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_COMP_PORTATIL_ALUNO` | STRING | Quantidade de notebooks/laptops para alunos. — descrição gerada por IA. |
| `IN_TABLET_ALUNO` | STRING | Indica uso de tablets por alunos (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_TABLET_ALUNO` | STRING | Quantidade de tablets para alunos. — descrição gerada por IA. |
| `QT_COMPUTADOR` | STRING | Quantidade total de computadores na escola. — descrição gerada por IA. |
| `QT_COMP_ADMINISTRATIVO` | STRING | Quantidade de computadores para uso administrativo. — descrição gerada por IA. |
| `IN_INTERNET` | STRING | Indica se a escola possui acesso à internet (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_INTERNET_ALUNOS` | STRING | Indica acesso à internet para alunos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_INTERNET_ADMINISTRATIVO` | STRING | Indica acesso à internet para uso administrativo (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_INTERNET_APRENDIZAGEM` | STRING | Indica acesso à internet para atividades de aprendizagem (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_INTERNET_COMUNIDADE` | STRING | Indica acesso à internet aberto para a comunidade (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSO_INTERNET_COMPUTADOR` | STRING | Indica acesso à internet por computadores (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACES_INTERNET_DISP_PESSOAIS` | STRING | Indica acesso à internet por dispositivos pessoais (1:Sim, 0:Não). — descrição gerada por IA. |
| `TP_REDE_LOCAL` | STRING | Tipo de rede local de computadores (1:A cabo, 2:Wireless, 3:Ambos, 0:Não há). — descrição gerada por IA. |
| `IN_BANDA_LARGA` | STRING | Indica conexão de internet banda larga (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_FUNCIONARIOS` | STRING | Quantidade total de funcionários na escola. — descrição gerada por IA. |
| `IN_PROF_ADMINISTRATIVOS` | STRING | Indica presença de profissionais administrativos (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_ADMINISTRATIVOS` | STRING | Quantidade de profissionais de apoio administrativo. — descrição gerada por IA. |
| `IN_PROF_SERVICOS_GERAIS` | STRING | Indica presença de profissionais de serviços gerais (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_SERVICOS_GERAIS` | STRING | Quantidade de profissionais de serviços gerais (limpeza, manutenção, etc.). — descrição gerada por IA. |
| `IN_PROF_BIBLIOTECARIO` | STRING | Indica presença de bibliotecário ou auxiliar de biblioteca (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_BIBLIOTECARIO` | STRING | Quantidade de bibliotecários/auxiliares. — descrição gerada por IA. |
| `IN_PROF_SAUDE` | STRING | Indica presença de profissionais da saúde (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_SAUDE` | STRING | Quantidade de profissionais da saúde (enfermeiros, médicos, etc.). — descrição gerada por IA. |
| `IN_PROF_COORDENADOR` | STRING | Indica presença de coordenador pedagógico/orientador educacional (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_COORDENADOR` | STRING | Quantidade de coordenadores pedagógicos. — descrição gerada por IA. |
| `IN_PROF_FONAUDIOLOGO` | STRING | Indica presença de fonoaudiólogo (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_FONAUDIOLOGO` | STRING | Quantidade de fonoaudiólogos. — descrição gerada por IA. |
| `IN_PROF_NUTRICIONISTA` | STRING | Indica presença de nutricionista (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_NUTRICIONISTA` | STRING | Quantidade de nutricionistas. — descrição gerada por IA. |
| `IN_PROF_PSICOLOGO` | STRING | Indica presença de psicólogo escolar (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_PSICOLOGO` | STRING | Quantidade de psicólogos. — descrição gerada por IA. |
| `IN_PROF_ALIMENTACAO` | STRING | Indica presença de cozinheiros/merendeiros (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_ALIMENTACAO` | STRING | Quantidade de profissionais de preparação de alimentos. — descrição gerada por IA. |
| `IN_PROF_PEDAGOGIA` | STRING | Indica presença de pedagogos/especialistas em pedagogia (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_PEDAGOGIA` | STRING | Quantidade de pedagogos/especialistas. — descrição gerada por IA. |
| `IN_PROF_SECRETARIO` | STRING | Indica presença de secretário escolar (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_SECRETARIO` | STRING | Quantidade de secretários escolares. — descrição gerada por IA. |
| `IN_PROF_SEGURANCA` | STRING | Indica presença de porteiros/seguranças/vigias (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_SEGURANCA` | STRING | Quantidade de profissionais de segurança/portaria. — descrição gerada por IA. |
| `IN_PROF_MONITORES` | STRING | Indica presença de monitores/cuidadores de alunos (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_MONITORES` | STRING | Quantidade de monitores/cuidadores. — descrição gerada por IA. |
| `IN_PROF_GESTAO` | STRING | Indica presença de diretores/gestores escolares (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_GESTAO` | STRING | Quantidade de diretores e vice-diretores. — descrição gerada por IA. |
| `IN_PROF_ASSIST_SOCIAL` | STRING | Indica presença de assistente social (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_ASSIST_SOCIAL` | STRING | Quantidade de assistentes sociais. — descrição gerada por IA. |
| `IN_ALIMENTACAO` | STRING | Indica fornecimento de alimentação escolar (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SERIE_ANO` | STRING | Indica organização escolar por séries/anos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PERIODOS_SEMESTRAIS` | STRING | Indica organização escolar por períodos semestrais (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FUNDAMENTAL_CICLOS` | STRING | Indica organização do ensino fundamental por ciclos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_GRUPOS_NAO_SERIADOS` | STRING | Indica organização em grupos não seriados (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MODULOS` | STRING | Indica organização em módulos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMACAO_ALTERNANCIA` | STRING | Indica organização em pedagogia da alternância (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_MULTIMIDIA` | STRING | Indica uso de materiais pedagógicos multimídia (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_INFANTIL` | STRING | Indica uso de materiais para Educação Infantil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_CIENTIFICO` | STRING | Indica uso de materiais pedagógicos para experimentos científicos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_DIFUSAO` | STRING | Indica uso de material de difusão cultural (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_MUSICAL` | STRING | Indica uso de instrumentos/materiais musicais pedagógicos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_JOGOS` | STRING | Indica uso de jogos pedagógicos (incluindo jogos de raciocínio da the source organization) (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_ARTISTICAS` | STRING | Indica uso de materiais pedagógicos para artes visuais/plásticas (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_DESPORTIVA` | STRING | Indica uso de materiais pedagógicos esportivos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_INDIGENA` | STRING | Indica uso de materiais pedagógicos específicos para educação indígena (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_ETNICO` | STRING | Indica uso de materiais pedagógicos para relações étnico-raciais (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_CAMPO` | STRING | Indica uso de materiais específicos para educação do campo (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_NENHUM` | STRING | Indica ausência de materiais pedagógicos específicos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_ESP_QUILOMBOLA` | STRING | Indica uso de material específico para educação quilombola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_ESP_INDIGENA` | STRING | Indica uso de material específico para educação indígena (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_ESP_NAO_UTILIZA` | STRING | Indica não utilização de materiais didáticos específicos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EDUCACAO_INDIGENA` | STRING | Indica oferta de Educação Escolar Indígena (1:Sim, 0:Não). — descrição gerada por IA. |
| `TP_INDIGENA_LINGUA` | STRING | Língua em que o ensino é ministrado na escola indígena (1:Língua Indígena, 2:Língua Portuguesa). — descrição gerada por IA. |
| `CO_LINGUA_INDIGENA_1` | STRING | Código da primeira língua indígena utilizada. — descrição gerada por IA. |
| `CO_LINGUA_INDIGENA_2` | STRING | Código da segunda língua indígena utilizada. — descrição gerada por IA. |
| `CO_LINGUA_INDIGENA_3` | STRING | Código da terceira língua indígena utilizada. — descrição gerada por IA. |
| `IN_BRASIL_ALFABETIZADO` | STRING | Indica adesão/oferta do programa Brasil Alfabetizado (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FINAL_SEMANA` | STRING | Indica abertura da escola nos finais de semana para a comunidade (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EXAME_SELECAO` | STRING | Indica processo seletivo/exame para ingresso de alunos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_RESERVA_PPI` | STRING | Indica reserva de vagas para pretos, pardos ou indígenas (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_RESERVA_RENDA` | STRING | Indica reserva de vagas por critério de renda (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_RESERVA_PUBLICA` | STRING | Indica reserva de vagas para oriundos da rede pública (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_RESERVA_PCD` | STRING | Indica reserva de vagas para pessoas com deficiência (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_RESERVA_OUTROS` | STRING | Indica outras modalidades de reserva de vagas (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_RESERVA_NENHUMA` | STRING | Indica inexistência de reserva de vagas (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_REDES_SOCIAIS` | STRING | Indica uso de redes sociais pela escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESPACO_ATIVIDADE` | STRING | Indica presença de espaço para atividades comunitárias (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESPACO_EQUIPAMENTO` | STRING | Indica compartilhamento de espaços/equipamentos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ORGAO_ASS_PAIS` | STRING | Indica existência de Associação de Pais (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ORGAO_ASS_PAIS_MESTRES` | STRING | Indica existência de Associação de Pais e Mestres (APM) (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ORGAO_CONSELHO_ESCOLAR` | STRING | Indica existência de Conselho Escolar (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ORGAO_GREMIO_ESTUDANTIL` | STRING | Indica existência de Grêmio Estudantil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ORGAO_OUTROS` | STRING | Indica presença de outros órgãos colegiados (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ORGAO_NENHUM` | STRING | Indica ausência de órgãos colegiados na escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `TP_PROPOSTA_PEDAGOGICA` | STRING | Tipo de proposta pedagógica adotada. — descrição gerada por IA. |
| `TP_AEE` | STRING | Tipo de Atendimento Educacional Especializado (AEE) oferecido. — descrição gerada por IA. |
| `TP_ATIVIDADE_COMPLEMENTAR` | STRING | Tipo de atividade complementar oferecida. — descrição gerada por IA. |
| `IN_MEDIACAO_PRESENCIAL` | STRING | Indica mediação didático-pedagógica presencial (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MEDIACAO_SEMIPRESENCIAL` | STRING | Indica mediação didático-pedagógica semipresencial (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MEDIACAO_EAD` | STRING | Indica mediação didático-pedagógica a distância (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_REGULAR` | STRING | Indica oferta de Ensino Regular (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_DIURNO` | STRING | Indica funcionamento em turno diurno (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_NOTURNO` | STRING | Indica funcionamento em turno noturno (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EAD` | STRING | Indica oferta de Educação a Distância (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_BAS` | STRING | Indica oferta de Educação Básica (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_INF` | STRING | Indica oferta de Educação Infantil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_INF_CRE` | STRING | Indica oferta de Creche na Educação Infantil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_INF_PRE` | STRING | Indica oferta de Pré-Escola na Educação Infantil (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FUND` | STRING | Indica oferta de Ensino Fundamental (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FUND_AI` | STRING | Indica oferta de Ensino Fundamental - Anos Iniciais (1º ao 5º ano) (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FUND_AF` | STRING | Indica oferta de Ensino Fundamental - Anos Finais (6º ao 9º ano) (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MED` | STRING | Indica oferta de Ensino Médio (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PROF` | STRING | Indica oferta de Educação Profissional (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PROF_TEC` | STRING | Indica oferta de Educação Profissional Técnica de Nível Médio (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EJA` | STRING | Indica oferta de Educação de Jovens e Adultos (EJA) (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EJA_FUND` | STRING | Indica oferta de EJA Ensino Fundamental (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EJA_MED` | STRING | Indica oferta de EJA Ensino Médio (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESP` | STRING | Indica oferta de Educação Especial (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESP_CC` | STRING | Indica oferta de Educação Especial em classe comum (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESP_CE` | STRING | Indica oferta de Educação Especial em classe exclusiva/especial (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_MAT_BAS` | STRING | Quantidade de matrículas na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_INF` | STRING | Quantidade de matrículas na Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_INF_CRE` | STRING | Quantidade de matrículas na Creche. — descrição gerada por IA. |
| `QT_MAT_INF_PRE` | STRING | Quantidade de matrículas na Pré-Escola. — descrição gerada por IA. |
| `QT_MAT_FUND` | STRING | Quantidade de matrículas no Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI` | STRING | Quantidade de matrículas no Ensino Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_FUND_AF` | STRING | Quantidade de matrículas no Ensino Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_MAT_MED` | STRING | Quantidade de matrículas no Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_PROF` | STRING | Quantidade de matrículas na Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC` | STRING | Quantidade de matrículas na Educação Profissional Técnica. — descrição gerada por IA. |
| `QT_MAT_EJA` | STRING | Quantidade de matrículas na EJA. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND` | STRING | Quantidade de matrículas na EJA Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_EJA_MED` | STRING | Quantidade de matrículas na EJA Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP` | STRING | Quantidade de matrículas na Educação Especial. — descrição gerada por IA. |
| `QT_MAT_ESP_CC` | STRING | Quantidade de matrículas na Educação Especial em classes comuns. — descrição gerada por IA. |
| `QT_MAT_ESP_CE` | STRING | Quantidade de matrículas na Educação Especial em classes exclusivas. — descrição gerada por IA. |
| `QT_MAT_BAS_FEM` | STRING | Quantidade de matrículas femininas na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_MASC` | STRING | Quantidade de matrículas masculinas na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_ND` | STRING | Quantidade de matrículas na Educação Básica com sexo não declarado. — descrição gerada por IA. |
| `QT_MAT_BAS_BRANCA` | STRING | Quantidade de matrículas de raça/cor branca na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_PRETA` | STRING | Quantidade de matrículas de raça/cor preta na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_PARDA` | STRING | Quantidade de matrículas de raça/cor parda na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_AMARELA` | STRING | Quantidade de matrículas de raça/cor amarela na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_INDIGENA` | STRING | Quantidade de matrículas de raça/cor indígena na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_0_3` | STRING | Quantidade de alunos matriculados de 0 a 3 anos de idade. — descrição gerada por IA. |
| `QT_MAT_BAS_4_5` | STRING | Quantidade de alunos matriculados de 4 a 5 anos de idade. — descrição gerada por IA. |
| `QT_MAT_BAS_6_10` | STRING | Quantidade de alunos matriculados de 6 a 10 anos de idade. — descrição gerada por IA. |
| `QT_MAT_BAS_11_14` | STRING | Quantidade de alunos matriculados de 11 a 14 anos de idade. — descrição gerada por IA. |
| `QT_MAT_BAS_15_17` | STRING | Quantidade de alunos matriculados de 15 a 17 anos de idade. — descrição gerada por IA. |
| `QT_MAT_BAS_18_MAIS` | STRING | Quantidade de alunos matriculados com 18 anos ou mais de idade. — descrição gerada por IA. |
| `QT_MAT_BAS_D` | STRING | Quantidade de matrículas no turno diurno. — descrição gerada por IA. |
| `QT_MAT_BAS_N` | STRING | Quantidade de matrículas no turno noturno. — descrição gerada por IA. |
| `QT_MAT_BAS_EAD` | STRING | Quantidade de matrículas na modalidade Educação a Distância. — descrição gerada por IA. |
| `QT_MAT_INF_INT` | STRING | Quantidade de matrículas em tempo integral na Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_INT` | STRING | Quantidade de matrículas em tempo integral na Creche. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_INT` | STRING | Quantidade de matrículas em tempo integral na Pré-Escola. — descrição gerada por IA. |
| `QT_MAT_FUND_INT` | STRING | Quantidade de matrículas em tempo integral no Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_INT` | STRING | Quantidade de matrículas em tempo integral no Ensino Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_INT` | STRING | Quantidade de matrículas em tempo integral no Ensino Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_MAT_MED_INT` | STRING | Quantidade de matrículas em tempo integral no Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_BAS` | STRING | Quantidade total de docentes da Educação Básica. — descrição gerada por IA. |
| `QT_DOC_INF` | STRING | Quantidade de docentes na Educação Infantil. — descrição gerada por IA. |
| `QT_DOC_INF_CRE` | STRING | Quantidade de docentes na Creche. — descrição gerada por IA. |
| `QT_DOC_INF_PRE` | STRING | Quantidade de docentes na Pré-Escola. — descrição gerada por IA. |
| `QT_DOC_FUND` | STRING | Quantidade de docentes no Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI` | STRING | Quantidade de docentes no Ensino Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_DOC_FUND_AF` | STRING | Quantidade de docentes no Ensino Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_DOC_MED` | STRING | Quantidade de docentes no Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_PROF` | STRING | Quantidade de docentes na Educação Profissional. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC` | STRING | Quantidade de docentes na Educação Profissional Técnica. — descrição gerada por IA. |
| `QT_DOC_EJA` | STRING | Quantidade de docentes na EJA. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND` | STRING | Quantidade de docentes na EJA Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_EJA_MED` | STRING | Quantidade de docentes na EJA Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_ESP` | STRING | Quantidade de docentes na Educação Especial. — descrição gerada por IA. |
| `QT_DOC_ESP_CC` | STRING | Quantidade de docentes na Educação Especial em classe comum. — descrição gerada por IA. |
| `QT_DOC_ESP_CE` | STRING | Quantidade de docentes na Educação Especial em classe exclusiva. — descrição gerada por IA. |
| `QT_TUR_BAS` | STRING | Quantidade total de turmas da Educação Básica. — descrição gerada por IA. |
| `QT_TUR_INF` | STRING | Quantidade de turmas de Educação Infantil. — descrição gerada por IA. |
| `QT_TUR_INF_CRE` | STRING | Quantidade de turmas de Creche. — descrição gerada por IA. |
| `QT_TUR_INF_PRE` | STRING | Quantidade de turmas de Pré-Escola. — descrição gerada por IA. |
| `QT_TUR_FUND` | STRING | Quantidade de turmas de Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI` | STRING | Quantidade de turmas de Ensino Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_TUR_FUND_AF` | STRING | Quantidade de turmas de Ensino Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_TUR_MED` | STRING | Quantidade de turmas de Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_PROF` | STRING | Quantidade de turmas de Educação Profissional. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC` | STRING | Quantidade de turmas de Educação Profissional Técnica. — descrição gerada por IA. |
| `QT_TUR_EJA` | STRING | Quantidade de turmas de EJA. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND` | STRING | Quantidade de turmas de EJA Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_EJA_MED` | STRING | Quantidade de turmas de EJA Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_ESP` | STRING | Quantidade de turmas de Educação Especial. — descrição gerada por IA. |
| `QT_TUR_ESP_CC` | STRING | Quantidade de turmas de Educação Especial em classe comum. — descrição gerada por IA. |
| `QT_TUR_ESP_CE` | STRING | Quantidade de turmas de Educação Especial em classe exclusiva. — descrição gerada por IA. |
| `IN_PODER_PUBLICO_PARCERIA` | STRING | Indica se há parceria/termo firmado com o poder público (1:Sim, 0:Não). — descrição gerada por IA. |
| `TP_PODER_PUBLICO_PARCERIA` | STRING | Tipo de parceria estabelecida com o poder público. — descrição gerada por IA. |
| `IN_FORMA_CONT_TERMO_COLABORA` | STRING | Indica parceria via Termo de Colaboração (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_TERMO_FOMENTO` | STRING | Indica parceria via Termo de Fomento (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ACORDO_COOP` | STRING | Indica parceria via Acordo de Cooperação (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_PRESTACAO_SERV` | STRING | Indica contrato de prestação de serviços (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_COOP_TEC_FIN` | STRING | Indica cooperação técnica/financeira (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_CONSORCIO_PUB` | STRING | Indica consórcio público (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_TIPO_ATEND_ESCOLARIZACAO` | STRING | Indica atendimento referente a escolarização (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_TIPO_ATEND_AC` | STRING | Indica atendimento complementar (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_TIPO_ATEND_AEE` | STRING | Indica Atendimento Educacional Especializado (AEE) (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_LABORATORIO_EDUC_PROF` | STRING | Indica laboratório específico para educação profissional (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_OFICINAS_EDUC_PROF` | STRING | Indica salas de oficina para educação profissional (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_PROFISSIONAL` | STRING | Indica materiais pedagógicos para formação profissional (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ESCOLARIZACAO` | STRING | Indica oferta de escolarização na escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `NO_REGIAO_GEOG_INTERM` | STRING | Nome da Região Geográfica Intermediária do IBGE. — descrição gerada por IA. |
| `CO_REGIAO_GEOG_INTERM` | STRING | Código da Região Geográfica Intermediária do IBGE. — descrição gerada por IA. |
| `NO_REGIAO_GEOG_IMED` | STRING | Nome da Região Geográfica Imediata do IBGE. — descrição gerada por IA. |
| `CO_REGIAO_GEOG_IMED` | STRING | Código da Região Geográfica Imediata do IBGE. — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_TERMO_COLAB` | STRING | Indica Termo de Colaboração com município (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_TERMO_FOMENTO` | STRING | Indica Termo de Fomento com município (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_ACORDO_COOP` | STRING | Indica Acordo de Cooperação com município (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_PREST_SERV` | STRING | Indica Prestação de Serviços com município (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_COOP_TEC_FIN` | STRING | Indica Cooperação Técnica/Financeira municipal (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_CONSORCIO_PUB` | STRING | Indica Consórcio Público municipal (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_TERMO_COLAB` | STRING | Indica Termo de Colaboração com estado (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_TERMO_FOMENTO` | STRING | Indica Termo de Fomento com estado (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_ACORDO_COOP` | STRING | Indica Acordo de Cooperação com estado (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_PREST_SERV` | STRING | Indica Prestação de Serviços com estado (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_COOP_TEC_FIN` | STRING | Indica Cooperação Técnica/Financeira estadual (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_CONSORCIO_PUB` | STRING | Indica Consórcio Público estadual (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_SALA_ESTUDIO_GRAVACAO` | STRING | Indica presença de estúdio de gravação de áudio/vídeo (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PROF_TRAD_LIBRAS` | STRING | Indica presença de tradutor/intérprete de Libras (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_TRAD_LIBRAS` | STRING | Quantidade de tradutores/intérpretes de Libras. — descrição gerada por IA. |
| `IN_MATERIAL_PED_BIL_SURDOS` | STRING | Indica uso de material pedagógico bilíngue para surdos (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_MAT_FUND_AI_1` | STRING | Quantidade de matrículas no 1º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_2` | STRING | Quantidade de matrículas no 2º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_3` | STRING | Quantidade de matrículas no 3º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_4` | STRING | Quantidade de matrículas no 4º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_5` | STRING | Quantidade de matrículas no 5º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_6` | STRING | Quantidade de matrículas no 6º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_7` | STRING | Quantidade de matrículas no 7º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_8` | STRING | Quantidade de matrículas no 8º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_9` | STRING | Quantidade de matrículas no 9º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_MED_PROP` | STRING | Quantidade de matrículas no Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_1` | STRING | Quantidade de matrículas na 1ª série do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_2` | STRING | Quantidade de matrículas na 2ª série do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_3` | STRING | Quantidade de matrículas na 3ª série do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_4` | STRING | Quantidade de matrículas na 4ª série do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_NS` | STRING | Quantidade de matrículas no Ensino Médio Propedêutico Não Seriado. — descrição gerada por IA. |
| `QT_MAT_MED_CT` | STRING | Quantidade de matrículas no Ensino Médio Concomitante Técnico. — descrição gerada por IA. |
| `QT_MAT_MED_CT_1` | STRING | Quantidade de matrículas na 1ª série do Ensino Médio Técnico Concomitante. — descrição gerada por IA. |
| `QT_MAT_MED_CT_2` | STRING | Quantidade de matrículas na 2ª série do Ensino Médio Técnico Concomitante. — descrição gerada por IA. |
| `QT_MAT_MED_CT_3` | STRING | Quantidade de matrículas na 3ª série do Ensino Médio Técnico Concomitante. — descrição gerada por IA. |
| `QT_MAT_MED_CT_4` | STRING | Quantidade de matrículas na 4ª série do Ensino Médio Técnico Concomitante. — descrição gerada por IA. |
| `QT_MAT_MED_CT_NS` | STRING | Quantidade de matrículas no Ensino Médio Técnico Concomitante Não Seriado. — descrição gerada por IA. |
| `QT_MAT_MED_NM` | STRING | Quantidade de matrículas no Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_1` | STRING | Quantidade de matrículas na 1ª série do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_2` | STRING | Quantidade de matrículas na 2ª série do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_3` | STRING | Quantidade de matrículas na 3ª série do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_4` | STRING | Quantidade de matrículas na 4ª série do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_CONC` | STRING | Quantidade de matrículas na Educação Profissional Técnica Concomitante. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_SUBS` | STRING | Quantidade de matrículas na Educação Profissional Técnica Subsequente. — descrição gerada por IA. |
| `QT_MAT_PROF_FIC_CONC` | STRING | Quantidade de matrículas na Formação Inicial e Continuada (FIC) Concomitante. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AI` | STRING | Quantidade de matrículas na EJA Ensino Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AF` | STRING | Quantidade de matrículas na EJA Ensino Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_FIC` | STRING | Quantidade de matrículas na EJA Ensino Fundamental Integrada à FIC. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_NPROF` | STRING | Quantidade de matrículas na EJA Ensino Médio Não Profissionalizante. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_FIC` | STRING | Quantidade de matrículas na EJA Ensino Médio Integrada à FIC. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_TEC` | STRING | Quantidade de matrículas na EJA Ensino Médio Integrada à Ed. Profissional Técnica. — descrição gerada por IA. |
| `QT_MAT_ZR_URB` | STRING | Quantidade de matrículas de alunos residentes em área urbana. — descrição gerada por IA. |
| `QT_MAT_ZR_RUR` | STRING | Quantidade de matrículas de alunos residentes em área rural. — descrição gerada por IA. |
| `QT_MAT_ZR_NA` | STRING | Quantidade de matrículas de alunos com zona de residência não informada. — descrição gerada por IA. |
| `QT_TRANSP_PUBLICO` | STRING | Quantidade de alunos que utilizam transporte escolar público. — descrição gerada por IA. |
| `QT_TRANSP_RESP_EST` | STRING | Quantidade de alunos que utilizam transporte escolar de responsabilidade estadual. — descrição gerada por IA. |
| `QT_TRANSP_RESP_MUN` | STRING | Quantidade de alunos que utilizam transporte escolar de responsabilidade municipal. — descrição gerada por IA. |
| `QT_TUR_BAS_D` | STRING | Quantidade de turmas diurnas na Educação Básica. — descrição gerada por IA. |
| `QT_TUR_BAS_N` | STRING | Quantidade de turmas noturnas na Educação Básica. — descrição gerada por IA. |
| `QT_TUR_BAS_EAD` | STRING | Quantidade de turmas EAD na Educação Básica. — descrição gerada por IA. |
| `QT_TUR_INF_INT` | STRING | Quantidade de turmas em tempo integral na Educação Infantil. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_INT` | STRING | Quantidade de turmas em tempo integral na Creche. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_INT` | STRING | Quantidade de turmas em tempo integral na Pré-Escola. — descrição gerada por IA. |
| `QT_TUR_FUND_INT` | STRING | Quantidade de turmas em tempo integral no Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_INT` | STRING | Quantidade de turmas em tempo integral no Ensino Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_INT` | STRING | Quantidade de turmas em tempo integral no Ensino Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_TUR_MED_INT` | STRING | Quantidade de turmas em tempo integral no Ensino Médio. — descrição gerada por IA. |
| `NO_DISTRITO` | STRING | Nome do distrito de localização da escola. — descrição gerada por IA. |
| `IN_AGUA_CARRO_PIPA` | STRING | Indica abastecimento de água por carro-pipa (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_AREA_PLANTIO` | STRING | Indica presença de área para plantio/horta na escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINALIZACAO` | STRING | Indica presença de sinalização de acessibilidade na escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_PROF_AGRICOLA` | STRING | Indica presença de profissional de ciências agrícolas/agronomia (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_AGRICOLA` | STRING | Quantidade de profissionais das ciências agrícolas. — descrição gerada por IA. |
| `IN_PROF_REVISOR_BRAILLE` | STRING | Indica presença de revisor de texto em Braille (1:Sim, 0:Não). — descrição gerada por IA. |
| `QT_PROF_REVISOR_BRAILLE` | STRING | Quantidade de revisores Braille. — descrição gerada por IA. |
| `IN_MATERIAL_PED_AGRICOLA` | STRING | Indica uso de materiais pedagógicos para agropecuária/agricultura (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_QUILOMBOLA` | STRING | Indica uso de materiais pedagógicos específicos para educação quilombola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_EDU_ESP` | STRING | Indica uso de materiais pedagógicos para Educação Especial (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EDUC_AMBIENTAL` | STRING | Indica abordagem de Educação Ambiental na escola (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_CONTEUDO` | STRING | Indica Educação Ambiental inserida em conteúdos disciplinares (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_CURRICULAR` | STRING | Indica Educação Ambiental como componente curricular/disciplina (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_EIXO` | STRING | Indica Educação Ambiental como eixo transversal do currículo (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_EVENTOS` | STRING | Indica Educação Ambiental desenvolvida por meio de eventos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_PROJETOS` | STRING | Indica Educação Ambiental desenvolvida por meio de projetos (1:Sim, 0:Não). — descrição gerada por IA. |
| `IN_EDUC_AMB_NENHUMA` | STRING | Indica ausência de ações de Educação Ambiental (1:Sim, 0:Não). — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_suplemento_cursos_tecnicos

File `raw__inep_censo_escolar_suplemento_cursos_tecnicos.parquet` · 50,740 rows · 34 columns

Raw Censo Escolar INEP. Familia de CSV: suplemento_cursos_tecnicos. Anos cobertos: 2023-2024 (2 ano(s)): 2023, 2024. Arquivos de origem: suplemento_cursos_tecnicos_2023.csv, suplemento_cursos_tecnicos_2024.csv. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano de realização da pesquisa do Censo Escolar (ex: 2023). — descrição gerada por IA. |
| `NO_REGIAO` | STRING | Nome da região geográfica onde a escola está localizada. — descrição gerada por IA. |
| `CO_REGIAO` | STRING | Código numérico IBGE da região geográfica. — descrição gerada por IA. |
| `NO_UF` | STRING | Nome da Unidade Federativa (estado) da escola. — descrição gerada por IA. |
| `SG_UF` | STRING | Sigla da Unidade Federativa da escola (ex: SP, RJ). — descrição gerada por IA. |
| `CO_UF` | STRING | Código IBGE de dois dígitos do estado. — descrição gerada por IA. |
| `NO_MUNICIPIO` | STRING | Nome do município de localização da escola. — descrição gerada por IA. |
| `CO_MUNICIPIO` | STRING | Código IBGE de 7 dígitos do município. — descrição gerada por IA. |
| `TP_LOCALIZACAO` | STRING | Código de localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `TP_LOCALIZACAO_DIFERENCIADA` | STRING | Código para áreas de localização diferenciada (ex: terra indígena, quilombola, assentamento). — descrição gerada por IA. |
| `TP_DEPENDENCIA` | STRING | Código da dependência administrativa (1: Federal, 2: Estadual, 3: Municipal, 4: Privada). — descrição gerada por IA. |
| `NO_ENTIDADE` | STRING | Nome oficial da escola ou instituição de ensino. — descrição gerada por IA. |
| `CO_ENTIDADE` | STRING | Código INEP (ID único) de 8 dígitos da escola. — descrição gerada por IA. |
| `NO_AREA_CURSO_PROFISSIONAL` | STRING | Nome do eixo tecnológico ou área do curso técnico. — descrição gerada por IA. |
| `ID_AREA_CURSO_PROFISSIONAL` | STRING | Código identificador do eixo tecnológico/área profissional. — descrição gerada por IA. |
| `NO_CURSO_EDUC_PROFISSIONAL` | STRING | Nome do curso técnico ou de educação profissional. — descrição gerada por IA. |
| `CO_CURSO_EDUC_PROFISSIONAL` | STRING | Código identificador do curso profissionalizante no INEP. — descrição gerada por IA. |
| `QT_CURSO_TEC` | STRING | Quantidade total de turmas/cursos técnicos ofertados. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC` | STRING | Quantidade total de matrículas em cursos técnicos. — descrição gerada por IA. |
| `QT_CURSO_TEC_CT` | STRING | Quantidade de cursos técnicos na modalidade integrada. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_CT` | STRING | Quantidade de matrículas em cursos técnicos integrados. — descrição gerada por IA. |
| `QT_CURSO_TEC_NM` | STRING | Quantidade de cursos técnicos de nível médio regular. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_NM` | STRING | Quantidade de matrículas em cursos técnicos de nível médio. — descrição gerada por IA. |
| `QT_CURSO_TEC_CONC` | STRING | Quantidade de cursos técnicos na modalidade concomitante. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_CONC` | STRING | Quantidade de matrículas na modalidade concomitante. — descrição gerada por IA. |
| `QT_CURSO_TEC_SUBS` | STRING | Quantidade de cursos técnicos na modalidade subsequente. — descrição gerada por IA. |
| `QT_MAT_TEC_SUBS` | STRING | Quantidade de matrículas na modalidade subsequente. — descrição gerada por IA. |
| `QT_CURSO_TEC_EJA` | STRING | Quantidade de cursos técnicos integrados à EJA. — descrição gerada por IA. |
| `QT_MAT_TEC_EJA` | STRING | Quantidade de matrículas em cursos técnicos da EJA. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## raw · inep_censo_escolar_turma

File `raw__inep_censo_escolar_turma.parquet` · 178,772 rows · 195 columns

Raw Censo Escolar INEP. Familia de CSV: turma. Anos cobertos: 2025-2025 (1 ano(s)): 2025. Arquivos de origem: Tabela_Turma_2025.csv. Dados brutos, sem regras de negócio, sem agregações e sem perda de informação. Campos do CSV carregados como STRING; metadados técnicos adicionados ao final: ano_censo, source_zip, source_file, ingested_at e raw_load_id.

**Feeds:** `trusted/inep_censo_escolar_turmas`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | STRING | Ano de referência da pesquisa do Censo Escolar (ex: 2025). — descrição gerada por IA. |
| `CO_ENTIDADE` | STRING | Código INEP único de identificação do estabelecimento de ensino. — descrição gerada por IA. |
| `QT_TUR_BAS` | STRING | Quantidade total de turmas de Educação Básica na escola. — descrição gerada por IA. |
| `QT_TUR_INF` | STRING | Quantidade de turmas de Educação Infantil. — descrição gerada por IA. |
| `QT_TUR_INF_CRE` | STRING | Quantidade de turmas de Creche (0 a 3 anos). — descrição gerada por IA. |
| `QT_TUR_INF_PRE` | STRING | Quantidade de turmas de Pré-Escola (4 e 5 anos). — descrição gerada por IA. |
| `QT_TUR_FUND` | STRING | Quantidade total de turmas de Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI` | STRING | Quantidade de turmas de Ensino Fundamental - Anos Iniciais (1º ao 5º ano). — descrição gerada por IA. |
| `QT_TUR_FUND_AI_1` | STRING | Quantidade de turmas de 1º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_2` | STRING | Quantidade de turmas de 2º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_3` | STRING | Quantidade de turmas de 3º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_4` | STRING | Quantidade de turmas de 4º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_5` | STRING | Quantidade de turmas de 5º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_MULTIETAPA` | STRING | Quantidade de turmas multietapa dos Anos Iniciais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF` | STRING | Quantidade de turmas de Ensino Fundamental - Anos Finais (6º ao 9º ano). — descrição gerada por IA. |
| `QT_TUR_FUND_AF_6` | STRING | Quantidade de turmas de 6º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_7` | STRING | Quantidade de turmas de 7º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_8` | STRING | Quantidade de turmas de 8º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_9` | STRING | Quantidade de turmas de 9º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_MULTI` | STRING | Quantidade de turmas multietapa dos Anos Finais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_CORRFLUXO` | STRING | Quantidade de turmas de correção de fluxo nos Anos Finais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_MED` | STRING | Quantidade total de turmas de Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_PROP` | STRING | Quantidade de turmas de Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_1` | STRING | Quantidade de turmas de 1ª série do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_2` | STRING | Quantidade de turmas de 2ª série do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_3` | STRING | Quantidade de turmas de 3ª série do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_4` | STRING | Quantidade de turmas de 4ª série do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_NS` | STRING | Quantidade de turmas de Ensino Médio Propedêutico Não Seriado. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT` | STRING | Quantidade de turmas de Ensino Médio com Itinerário Formativo Técnico Profissional Concomitante. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_1` | STRING | Quantidade de turmas de 1ª série com Itinerário Formativo Técnico Concomitante. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_2` | STRING | Quantidade de turmas de 2ª série com Itinerário Formativo Técnico Concomitante. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_3` | STRING | Quantidade de turmas de 3ª série com Itinerário Formativo Técnico Concomitante. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_4` | STRING | Quantidade de turmas de 4ª série com Itinerário Formativo Técnico Concomitante. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_NS` | STRING | Quantidade de turmas Não Seriadas com Itinerário Formativo Técnico Concomitante. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP` | STRING | Quantidade de turmas de Qualificação Profissional no Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_1` | STRING | Quantidade de turmas de 1ª série com Qualificação Profissional no Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_2` | STRING | Quantidade de turmas de 2ª série com Qualificação Profissional no Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_3` | STRING | Quantidade de turmas de 3ª série com Qualificação Profissional no Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_4` | STRING | Quantidade de turmas de 4ª série com Qualificação Profissional no Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_NS` | STRING | Quantidade de turmas Não Seriadas com Qualificação Profissional no Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_NM` | STRING | Quantidade de turmas de Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_1` | STRING | Quantidade de turmas de 1ª série do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_2` | STRING | Quantidade de turmas de 2ª série do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_3` | STRING | Quantidade de turmas de 3ª série do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_4` | STRING | Quantidade de turmas de 4ª série do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_EXC` | STRING | Quantidade de turmas de Ensino Médio com Itinerário Formativo de Aprofundamento Exclusivo. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_EXC` | STRING | Quantidade de turmas de Ensino Médio com Itinerário Formativo Técnico Exclusivo. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_EXC_QP` | STRING | Quantidade de turmas com Itinerário Formativo Técnico Exclusivo de Qualificação Profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFA` | STRING | Quantidade de turmas de Ensino Médio com Itinerário Formativo de Aprofundamento. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_LING` | STRING | Quantidade de turmas do Itinerário Formativo em Linguagens e suas Tecnologias. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_MATE` | STRING | Quantidade de turmas do Itinerário Formativo em Matemática e suas Tecnologias. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_CIENC` | STRING | Quantidade de turmas do Itinerário Formativo em Ciências da Natureza. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_HUMA` | STRING | Quantidade de turmas do Itinerário Formativo em Ciências Humanas e Sociais Aplicadas. — descrição gerada por IA. |
| `QT_TUR_PROF` | STRING | Quantidade total de turmas de Educação Profissional. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC` | STRING | Quantidade de turmas de Educação Profissional Técnica de nível médio. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_CONC` | STRING | Quantidade de turmas de Ensino Técnico Concomitante. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_SUBS` | STRING | Quantidade de turmas de Ensino Técnico Subsequente. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_MISTO` | STRING | Quantidade de turmas de Ensino Técnico Misto. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_IFTP_CT` | STRING | Quantidade de turmas de Técnico Concomitante integrado a Itinerário Formativo. — descrição gerada por IA. |
| `QT_TUR_PROF_NAO_TEC` | STRING | Quantidade de turmas de Educação Profissional não técnica (Formação Inicial e Continuada - FIC). — descrição gerada por IA. |
| `QT_TUR_PROF_IFTP_QP` | STRING | Quantidade de turmas de Qualificação Profissionalizante no itinerário formativo. — descrição gerada por IA. |
| `QT_TUR_PROF_FIC_CONC` | STRING | Quantidade de turmas de Formação Inicial e Continuada (FIC) Concomitante. — descrição gerada por IA. |
| `QT_TUR_EJA` | STRING | Quantidade total de turmas de Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |
| `QT_TUR_EJA_FUND` | STRING | Quantidade de turmas de EJA - Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_NPROF` | STRING | Quantidade de turmas de EJA Fundamental não profissionalizante. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_AI` | STRING | Quantidade de turmas de EJA Fundamental - Anos Iniciais. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_AF` | STRING | Quantidade de turmas de EJA Fundamental - Anos Finais. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_FIC` | STRING | Quantidade de turmas de EJA Fundamental com Qualificação Profissional (FIC). — descrição gerada por IA. |
| `QT_TUR_EJA_MED` | STRING | Quantidade de turmas de EJA - Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_NPROF` | STRING | Quantidade de turmas de EJA Médio não profissionalizante. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_FIC` | STRING | Quantidade de turmas de EJA Médio com Qualificação Profissional (FIC). — descrição gerada por IA. |
| `QT_TUR_EJA_MED_TEC` | STRING | Quantidade de turmas de EJA Médio com Ensino Técnico. — descrição gerada por IA. |
| `QT_TUR_ESP` | STRING | Quantidade total de turmas de Educação Especial. — descrição gerada por IA. |
| `QT_TUR_ESP_CC` | STRING | Quantidade de turmas de Educação Especial em Classe Comum (Inclusiva). — descrição gerada por IA. |
| `QT_TUR_ESP_CE` | STRING | Quantidade de turmas de Educação Especial em Classe Exclusiva. — descrição gerada por IA. |
| `QT_TUR_BAS_D` | STRING | Quantidade de turmas de Educação Básica no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_BAS_DM` | STRING | Quantidade de turmas de Educação Básica no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_BAS_DV` | STRING | Quantidade de turmas de Educação Básica no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_BAS_N` | STRING | Quantidade de turmas de Educação Básica no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_BAS_EAD` | STRING | Quantidade de turmas de Educação Básica na modalidade EaD. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_D` | STRING | Quantidade de turmas de Creche no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_DM` | STRING | Quantidade de turmas de Creche no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_DV` | STRING | Quantidade de turmas de Creche no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_N` | STRING | Quantidade de turmas de Creche no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_D` | STRING | Quantidade de turmas de Pré-Escola no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_DM` | STRING | Quantidade de turmas de Pré-Escola no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_DV` | STRING | Quantidade de turmas de Pré-Escola no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_N` | STRING | Quantidade de turmas de Pré-Escola no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_FUND_D` | STRING | Quantidade de turmas de Ensino Fundamental no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_FUND_DM` | STRING | Quantidade de turmas de Ensino Fundamental no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_FUND_DV` | STRING | Quantidade de turmas de Ensino Fundamental no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_FUND_N` | STRING | Quantidade de turmas de Ensino Fundamental no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_D` | STRING | Quantidade de turmas de Fundamental Anos Iniciais no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_DM` | STRING | Quantidade de turmas de Fundamental Anos Iniciais no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_DV` | STRING | Quantidade de turmas de Fundamental Anos Iniciais no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_N` | STRING | Quantidade de turmas de Fundamental Anos Iniciais no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_D` | STRING | Quantidade de turmas de Fundamental Anos Finais no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_DM` | STRING | Quantidade de turmas de Fundamental Anos Finais no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_DV` | STRING | Quantidade de turmas de Fundamental Anos Finais no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_N` | STRING | Quantidade de turmas de Fundamental Anos Finais no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_MED_D` | STRING | Quantidade de turmas de Ensino Médio no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_MED_DM` | STRING | Quantidade de turmas de Ensino Médio no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_MED_DV` | STRING | Quantidade de turmas de Ensino Médio no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_MED_N` | STRING | Quantidade de turmas de Ensino Médio no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_MED_EAD` | STRING | Quantidade de turmas de Ensino Médio na modalidade EaD. — descrição gerada por IA. |
| `QT_TUR_PROF_D` | STRING | Quantidade de turmas de Educação Profissional no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_PROF_DM` | STRING | Quantidade de turmas de Educação Profissional no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_PROF_DV` | STRING | Quantidade de turmas de Educação Profissional no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_PROF_N` | STRING | Quantidade de turmas de Educação Profissional no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_PROF_EAD` | STRING | Quantidade de turmas de Educação Profissional na modalidade EaD. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_D` | STRING | Quantidade de turmas de Ensino Técnico no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_DM` | STRING | Quantidade de turmas de Ensino Técnico no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_DV` | STRING | Quantidade de turmas de Ensino Técnico no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_N` | STRING | Quantidade de turmas de Ensino Técnico no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_EAD` | STRING | Quantidade de turmas de Ensino Técnico na modalidade EaD. — descrição gerada por IA. |
| `QT_TUR_EJA_D` | STRING | Quantidade de turmas de EJA no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_EJA_DM` | STRING | Quantidade de turmas de EJA no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_EJA_DV` | STRING | Quantidade de turmas de EJA no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_EJA_N` | STRING | Quantidade de turmas de EJA no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_EJA_EAD` | STRING | Quantidade de turmas de EJA na modalidade EaD. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_D` | STRING | Quantidade de turmas de EJA Fundamental no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_DM` | STRING | Quantidade de turmas de EJA Fundamental no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_DV` | STRING | Quantidade de turmas de EJA Fundamental no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_N` | STRING | Quantidade de turmas de EJA Fundamental no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_EAD` | STRING | Quantidade de turmas de EJA Fundamental na modalidade EaD. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_D` | STRING | Quantidade de turmas de EJA Médio no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_DM` | STRING | Quantidade de turmas de EJA Médio no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_DV` | STRING | Quantidade de turmas de EJA Médio no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_N` | STRING | Quantidade de turmas de EJA Médio no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_EAD` | STRING | Quantidade de turmas de EJA Médio na modalidade EaD. — descrição gerada por IA. |
| `QT_TUR_ESP_D` | STRING | Quantidade de turmas de Educação Especial no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_ESP_DM` | STRING | Quantidade de turmas de Educação Especial no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_ESP_DV` | STRING | Quantidade de turmas de Educação Especial no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_ESP_N` | STRING | Quantidade de turmas de Educação Especial no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_ESP_EAD` | STRING | Quantidade de turmas de Educação Especial na modalidade EaD. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_D` | STRING | Quantidade de turmas de Educação Especial Classe Comum no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_DM` | STRING | Quantidade de turmas de Educação Especial Classe Comum no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_DV` | STRING | Quantidade de turmas de Educação Especial Classe Comum no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_N` | STRING | Quantidade de turmas de Educação Especial Classe Comum no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_EAD` | STRING | Quantidade de turmas de Educação Especial Classe Comum em EaD. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_D` | STRING | Quantidade de turmas de Educação Especial Classe Exclusiva no turno Diurno. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_DM` | STRING | Quantidade de turmas de Educação Especial Classe Exclusiva no turno Matutino. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_DV` | STRING | Quantidade de turmas de Educação Especial Classe Exclusiva no turno Vespertino. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_N` | STRING | Quantidade de turmas de Educação Especial Classe Exclusiva no turno Noturno. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_EAD` | STRING | Quantidade de turmas de Educação Especial Classe Exclusiva em EaD. — descrição gerada por IA. |
| `QT_TUR_BAS_INT` | STRING | Quantidade de turmas de Educação Básica em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_INF_INT` | STRING | Quantidade de turmas de Educação Infantil em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_INT` | STRING | Quantidade de turmas de Creche em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_INT` | STRING | Quantidade de turmas de Pré-Escola em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_FUND_INT` | STRING | Quantidade de turmas de Ensino Fundamental em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_INT` | STRING | Quantidade de turmas de Fundamental Anos Iniciais em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_INT` | STRING | Quantidade de turmas de Fundamental Anos Finais em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_MED_INT` | STRING | Quantidade de turmas de Ensino Médio em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_PROF_INT` | STRING | Quantidade de turmas de Educação Profissional em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_INT` | STRING | Quantidade de turmas de Ensino Técnico em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_EJA_INT` | STRING | Quantidade de turmas de EJA em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_INT` | STRING | Quantidade de turmas de EJA Fundamental em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_INT` | STRING | Quantidade de turmas de EJA Médio em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_ESP_INT` | STRING | Quantidade de turmas de Educação Especial em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_INT` | STRING | Quantidade de turmas de Educação Especial Classe Comum em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_INT` | STRING | Quantidade de turmas de Educação Especial Classe Exclusiva em Tempo Integral. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_PORT` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Língua Portuguesa. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_EDUC_FISICA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Educação Física. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_ARTES` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Artes. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_ING` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Língua Inglesa. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_ESPA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Língua Espanhola. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_FRANC` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Língua Francesa. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_OUTRA` | STRING | Quantidade de turmas da Educação Básica com outras línguas estrangeiras. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LIBRAS` | STRING | Quantidade de turmas da Educação Básica com a disciplina de LIBRAS. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_INDIG` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Língua Indígena. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PORT_SEG_LINGUA` | STRING | Quantidade de turmas da Educação Básica com Língua Portuguesa como 2ª língua. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_MATEMATICA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Matemática. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_CIENCIAS` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Ciências. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_FISICA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Física. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_QUIMICA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Química. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_BIOLOGIA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Biologia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_HISTORIA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de História. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_GEOGRAFIA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Geografia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_SOCIOLOGIA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Sociologia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_FILOSOFIA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Filosofia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_EST_SOCIAIS` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Estudos Sociais. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_EST_SOCIAIS_SOCI` | STRING | Quantidade de turmas com a disciplina de Estudos Sociais / Sociologia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_INFO_COMPUTACAO` | STRING | Quantidade de turmas com a disciplina de Informática / Computação. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_ENSINO_RELIGIOSO` | STRING | Quantidade de turmas da Educação Básica com Ensino Religioso. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PROFISSIONA` | STRING | Quantidade de turmas com disciplinas de Formação Profissional. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_ESTAGIO_SUPER` | STRING | Quantidade de turmas da Educação Básica com Estágio Supervisionado. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PEDAGOGICAS` | STRING | Quantidade de turmas com Disciplinas Pedagógicas. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PROJETO_DE_VIDA` | STRING | Quantidade de turmas da Educação Básica com a disciplina de Projeto de Vida. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_OUTRAS` | STRING | Quantidade de turmas da Educação Básica com outras disciplinas não especificadas. — descrição gerada por IA. |
| `QT_TUR_BAS_LIBRAS` | STRING | Quantidade de turmas com ensino ministrado em LIBRAS na Educação Básica. — descrição gerada por IA. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `ingested_at` | TIMESTAMP | Timestamp UTC em que o arquivo foi ingerido no BigQuery. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |

## trusted · inep_censo_escolar_colunas_fonte

File `trusted__inep_censo_escolar_colunas_fonte.parquet` · 29,684 rows · 8 columns

Inventario de colunas por CSV/ano com descricao do dicionario quando disponivel.

**Feeds:** `semantic/obt_inep_censo_perguntas`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano do Censo Escolar. |
| `logical_table` | STRING | Família lógica do arquivo CSV. |
| `source_csv_name` | STRING | Nome do CSV de origem. |
| `column_position` | INTEGER | Posição ordinal da coluna no CSV de origem. |
| `column_name` | STRING | Nome original da coluna no CSV. |
| `column_name_normalized` | STRING | Nome normalizado da coluna usado no BigQuery. |
| `dictionary_description` | STRING | Descrição encontrada no dicionário oficial ou PDF legado. |
| `dictionary_source_kind` | STRING | Tipo de fonte da descrição encontrada. |

## trusted · inep_censo_escolar_cursos_tecnicos

File `trusted__inep_censo_escolar_cursos_tecnicos.parquet` · 82,876 rows · 39 columns

TRUSTED - Cursos técnicos e matrículas por escola/curso/eixo, incluindo modalidades integradas, concomitantes, subsequentes, EJA e IFTP conforme ano. Sem filtros que removam registros. Anos cobertos pelas fontes: 2023-2025 (2023, 2024, 2025).

| Column | Type | Description |
|---|---|---|
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `NU_ANO_CENSO` | INTEGER | Ano de realização e referência das informações do Censo Escolar. — descrição gerada por IA. |
| `NO_REGIAO` | STRING | Nome da região geográfica onde a escola está localizada. — descrição gerada por IA. |
| `CO_REGIAO` | INTEGER | Código IBGE da região geográfica da escola. — descrição gerada por IA. |
| `NO_UF` | STRING | Nome da Unidade Federativa (estado) da escola. — descrição gerada por IA. |
| `SG_UF` | STRING | Sigla da Unidade Federativa da escola. — descrição gerada por IA. |
| `CO_UF` | INTEGER | Código IBGE da Unidade Federativa da escola. — descrição gerada por IA. |
| `NO_MUNICIPIO` | STRING | Nome do município onde a escola está localizada. — descrição gerada por IA. |
| `CO_MUNICIPIO` | INTEGER | Código IBGE do município da escola. — descrição gerada por IA. |
| `TP_LOCALIZACAO` | INTEGER | Tipo de localização da escola (1: Urbana, 2: Rural). — descrição gerada por IA. |
| `TP_LOCALIZACAO_DIFERENCIADA` | INTEGER | Indica se a escola está em área diferenciada (ex: terra indígena, quilombola, assentamento). — descrição gerada por IA. |
| `TP_DEPENDENCIA` | INTEGER | Código da dependência administrativa da escola (1: Federal, 2: Estadual, 3: Municipal, 4: Privada). — descrição gerada por IA. |
| `NO_ENTIDADE` | STRING | Nome da escola ou instituição de ensino. — descrição gerada por IA. |
| `CO_ENTIDADE` | INTEGER | Código INEP único de identificação da escola. — descrição gerada por IA. |
| `NO_AREA_CURSO_PROFISSIONAL` | STRING | Nome do eixo tecnológico ou área do curso técnico. — descrição gerada por IA. |
| `ID_AREA_CURSO_PROFISSIONAL` | INTEGER | Código identificador da área do curso profissional. — descrição gerada por IA. |
| `NO_CURSO_EDUC_PROFISSIONAL` | STRING | Nome do curso técnico ou de educação profissional oferecido. — descrição gerada por IA. |
| `CO_CURSO_EDUC_PROFISSIONAL` | INTEGER | Código identificador do curso técnico no catálogo do INEP. — descrição gerada por IA. |
| `QT_CURSO_TEC` | INTEGER | Quantidade total de turmas/ofertas do curso técnico na escola. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC` | INTEGER | Quantidade total de matrículas no curso técnico na escola. — descrição gerada por IA. |
| `QT_CURSO_TEC_CT` | INTEGER | Quantidade de cursos técnicos oferecidos na modalidade concomitante. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_CT` | INTEGER | Quantidade de matrículas em cursos técnicos na modalidade concomitante. — descrição gerada por IA. |
| `QT_CURSO_TEC_NM` | INTEGER | Quantidade de cursos técnicos na modalidade Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_NM` | INTEGER | Quantidade de matrículas em cursos técnicos na modalidade Normal/Magistério. — descrição gerada por IA. |
| `QT_CURSO_TEC_CONC` | INTEGER | Quantidade de cursos técnicos na modalidade concomitante interplementar. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_CONC` | INTEGER | Quantidade de matrículas em cursos técnicos concomitantes em outra instituição. — descrição gerada por IA. |
| `QT_CURSO_TEC_SUBS` | INTEGER | Quantidade de cursos técnicos oferecidos na modalidade subsequente. — descrição gerada por IA. |
| `QT_MAT_TEC_SUBS` | INTEGER | Quantidade de matrículas em cursos técnicos subsequentes (campo alternativo da fonte). — descrição gerada por IA. |
| `QT_CURSO_TEC_EJA` | INTEGER | Quantidade de cursos técnicos integrados à EJA. — descrição gerada por IA. |
| `QT_MAT_TEC_EJA` | INTEGER | Quantidade de matrículas em cursos técnicos integrados à EJA (campo alternativo da fonte). — descrição gerada por IA. |
| `QT_CURSO_TEC_IFTP` | INTEGER | Quantidade de cursos técnicos do Itinerário de Formação Técnica e Profissional. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_IFTP` | INTEGER | Quantidade de matrículas no Itinerário de Formação Técnica e Profissional do Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_SUBS` | INTEGER | Quantidade de matrículas em cursos técnicos na modalidade subsequente. — descrição gerada por IA. |
| `QT_CURSO_TEC_IFTP_CT` | INTEGER | Quantidade de cursos do Itinerário de Formação Técnica e Profissional em concomitância. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_IFTP_CT` | INTEGER | Quantidade de matrículas do Itinerário de Formação Técnica e Profissional na modalidade concomitante. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_EJA` | INTEGER | Quantidade de matrículas em cursos técnicos integrados à Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |

## trusted · inep_censo_escolar_dicionario_campos

File `trusted__inep_censo_escolar_dicionario_campos.parquet` · 28,786 rows · 11 columns

Dicionario de campos do Censo Escolar extraido dos XLSX oficiais e snippets dos Leia-me legados quando possivel.

**Feeds:** `semantic/obt_inep_censo_perguntas`

| Column | Type | Description |
|---|---|---|
| `ano` | INTEGER | Ano do dicionário ou leia-me de origem. |
| `logical_table` | STRING | Família lógica ou aba à qual a variável pertence. |
| `source_dictionary_name` | STRING | Nome do arquivo de dicionário de origem. |
| `source_sheet` | STRING | Aba do XLSX ou página lógica, quando aplicável. |
| `column_name` | STRING | Nome original da variável no dicionário. |
| `column_name_normalized` | STRING | Nome normalizado usado no BigQuery. |
| `description` | STRING | Descrição oficial extraída do dicionário ou trecho do leia-me legado. |
| `inep_type` | STRING | Tipo informado pelo INEP no dicionário. |
| `length` | STRING | Tamanho informado pelo INEP no dicionário. |
| `category` | STRING | Categoria/domínio informado pelo INEP, quando disponível. |
| `source_kind` | STRING | Tipo da fonte do metadado: xlsx ou pdf_snippet. |

## trusted · inep_censo_escolar_docentes

File `trusted__inep_censo_escolar_docentes.parquet` · 4,237,236 rows · 160 columns

TRUSTED - Métricas agregadas de docentes por escola/ano, etapa, formação, disciplina e demais recortes disponíveis. Sem filtros que removam registros. Anos cobertos pelas fontes: 2007-2025 (2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025).

**Feeds:** `semantic/obt_inep_censo_docente_escola_ano`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | INTEGER | Ano de realização do Censo Escolar (YYYY). — descrição gerada por IA. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `CO_ENTIDADE` | INTEGER | Código INEP de identificação da escola. — descrição gerada por IA. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `QT_DOC_BAS` | INTEGER | Quantidade total de docentes atuando na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_INF` | INTEGER | Quantidade de docentes na Educação Infantil. — descrição gerada por IA. |
| `QT_DOC_INF_CRE` | INTEGER | Quantidade de docentes em turmas de Creche. — descrição gerada por IA. |
| `QT_DOC_INF_PRE` | INTEGER | Quantidade de docentes em turmas de Pré-Escola. — descrição gerada por IA. |
| `QT_DOC_FUND` | INTEGER | Quantidade de docentes no Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI` | INTEGER | Quantidade de docentes nos Anos Iniciais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AF` | INTEGER | Quantidade de docentes nos Anos Finais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_MED` | INTEGER | Quantidade de docentes no Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_PROF` | INTEGER | Quantidade de docentes na Educação Profissional. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC` | INTEGER | Quantidade de docentes em cursos de Educação Profissional Técnica de nível médio. — descrição gerada por IA. |
| `QT_DOC_EJA` | INTEGER | Quantidade de docentes na Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |
| `QT_DOC_EJA_FUND` | INTEGER | Quantidade de docentes na EJA do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_EJA_MED` | INTEGER | Quantidade de docentes na EJA do Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_ESP` | INTEGER | Quantidade de docentes atuando na Educação Especial. — descrição gerada por IA. |
| `QT_DOC_ESP_CC` | INTEGER | Quantidade de docentes na Educação Especial em classes comuns/inclusivas. — descrição gerada por IA. |
| `QT_DOC_ESP_CE` | INTEGER | Quantidade de docentes na Educação Especial em classes exclusivas/especiais. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_1` | INTEGER | Quantidade de docentes no 1º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_2` | INTEGER | Quantidade de docentes no 2º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_3` | INTEGER | Quantidade de docentes no 3º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_4` | INTEGER | Quantidade de docentes no 4º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_5` | INTEGER | Quantidade de docentes no 5º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_MULTIETAPA` | INTEGER | Quantidade de docentes em turmas multietapa dos Anos Iniciais. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_6` | INTEGER | Quantidade de docentes no 6º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_7` | INTEGER | Quantidade de docentes no 7º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_8` | INTEGER | Quantidade de docentes no 8º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_9` | INTEGER | Quantidade de docentes no 9º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_MULTI` | INTEGER | Quantidade de docentes em turmas multietapa dos Anos Finais. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_CORRFLUXO` | INTEGER | Quantidade de docentes em turmas de correção de fluxo nos Anos Finais. — descrição gerada por IA. |
| `QT_DOC_MED_PROP` | INTEGER | Quantidade de docentes no Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_1` | INTEGER | Quantidade de docentes no 1º ano do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_2` | INTEGER | Quantidade de docentes no 2º ano do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_3` | INTEGER | Quantidade de docentes no 3º ano do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_4` | INTEGER | Quantidade de docentes no 4º ano do Ensino Médio Propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_NS` | INTEGER | Quantidade de docentes no Ensino Médio Propedêutico em séries não seriadas. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT` | INTEGER | Quantidade de docentes no Ensino Médio integrado à Formação Técnica (Concomitante). — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_1` | INTEGER | Quantidade de docentes no 1º ano do Ensino Médio Integrado/Concomitante. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_2` | INTEGER | Quantidade de docentes no 2º ano do Ensino Médio Integrado/Concomitante. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_3` | INTEGER | Quantidade de docentes no 3º ano do Ensino Médio Integrado/Concomitante. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_4` | INTEGER | Quantidade de docentes no 4º ano do Ensino Médio Integrado/Concomitante. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_NS` | INTEGER | Quantidade de docentes no Ensino Médio Integrado/Concomitante em turmas não seriadas. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP` | INTEGER | Quantidade de docentes no Ensino Médio de Qualificação Profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_1` | INTEGER | Quantidade de docentes no 1º ano do Ensino Médio Qualificação Profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_2` | INTEGER | Quantidade de docentes no 2º ano do Ensino Médio Qualificação Profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_3` | INTEGER | Quantidade de docentes no 3º ano do Ensino Médio Qualificação Profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_4` | INTEGER | Quantidade de docentes no 4º ano do Ensino Médio Qualificação Profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_NS` | INTEGER | Quantidade de docentes no Ensino Médio Qualificação Profissional em turmas não seriadas. — descrição gerada por IA. |
| `QT_DOC_MED_NM` | INTEGER | Quantidade de docentes no Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_DOC_MED_NM_1` | INTEGER | Quantidade de docentes no 1º ano do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_DOC_MED_NM_2` | INTEGER | Quantidade de docentes no 2º ano do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_DOC_MED_NM_3` | INTEGER | Quantidade de docentes no 3º ano do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_DOC_MED_NM_4` | INTEGER | Quantidade de docentes no 4º ano do Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC_CONC` | INTEGER | Quantidade de docentes em cursos técnicos concomitantes. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC_SUBS` | INTEGER | Quantidade de docentes em cursos técnicos subsequentes. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC_MISTO` | INTEGER | Quantidade de docentes em cursos técnicos concomitantes/subsequentes. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC_IFTP_CT` | INTEGER | Quantidade de docentes em cursos técnicos integrados continuados. — descrição gerada por IA. |
| `QT_DOC_PROF_NAO_TEC` | INTEGER | Quantidade de docentes na Educação Profissional Não-Técnica (qualificação básica). — descrição gerada por IA. |
| `QT_DOC_PROF_IFTP_QP` | INTEGER | Quantidade de docentes de qualificação profissional integrada ao Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_PROF_FIC_CONC` | INTEGER | Quantidade de docentes em cursos FIC (Formação Inicial e Continuada) concomitantes. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND_NPROF` | INTEGER | Quantidade de docentes na EJA do Ensino Fundamental não profissionalizante. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND_AI` | INTEGER | Quantidade de docentes na EJA do Ensino Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND_AF` | INTEGER | Quantidade de docentes na EJA do Ensino Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND_FIC` | INTEGER | Quantidade de docentes na EJA Fundamental integrada à qualificação profissional (FIC). — descrição gerada por IA. |
| `QT_DOC_EJA_MED_NPROF` | INTEGER | Quantidade de docentes na EJA do Ensino Médio não profissionalizante. — descrição gerada por IA. |
| `QT_DOC_EJA_MED_FIC` | INTEGER | Quantidade de docentes na EJA Médio integrada à qualificação profissional (FIC). — descrição gerada por IA. |
| `QT_DOC_EJA_MED_TEC` | INTEGER | Quantidade de docentes na EJA Médio integrada ao ensino técnico. — descrição gerada por IA. |
| `QT_DOC_BAS_FEM` | INTEGER | Quantidade de docentes do sexo feminino na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_MASC` | INTEGER | Quantidade de docentes do sexo masculino na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_ND` | INTEGER | Quantidade de docentes com sexo não declarado na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_BRANCA` | INTEGER | Quantidade de docentes autodeclarados brancos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_PRETA` | INTEGER | Quantidade de docentes autodeclarados pretos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_PARDA` | INTEGER | Quantidade de docentes autodeclarados pardos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_AMARELA` | INTEGER | Quantidade de docentes autodeclarados amarelos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_INDIGENA` | INTEGER | Quantidade de docentes autodeclarados indígenas na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_0_24` | INTEGER | Quantidade de docentes até 24 anos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_25_29` | INTEGER | Quantidade de docentes com idade entre 25 e 29 anos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_30_39` | INTEGER | Quantidade de docentes com idade entre 30 e 39 anos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_40_49` | INTEGER | Quantidade de docentes com idade entre 40 e 49 anos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_50_54` | INTEGER | Quantidade de docentes com idade entre 50 e 54 anos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_55_59` | INTEGER | Quantidade de docentes com idade entre 55 e 59 anos na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_60_MAIS` | INTEGER | Quantidade de docentes com 60 anos ou mais na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_PCD` | INTEGER | Quantidade de docentes com deficiência/PCD na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_BAS_ZR_URB` | INTEGER | Quantidade de docentes residentes em zona urbana. — descrição gerada por IA. |
| `QT_DOC_BAS_ZR_RUR` | INTEGER | Quantidade de docentes residentes em zona rural. — descrição gerada por IA. |
| `QT_DOC_BAS_ZR_NA` | INTEGER | Quantidade de docentes com zona de residência não disponível/não declarada. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_EF` | INTEGER | Quantidade de docentes com escolaridade até o Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_EM` | INTEGER | Quantidade de docentes com Ensino Médio completo. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_GRAD` | INTEGER | Quantidade de docentes com Ensino Superior completo (Graduação). — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_GRAD_LICEN` | INTEGER | Quantidade de docentes com graduação com Licenciatura. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_GRAD_SLICEN` | INTEGER | Quantidade de docentes com graduação sem Licenciatura (Bacharelado/Tecnólogo). — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_POS_ESPEC` | INTEGER | Quantidade de docentes com Pós-Graduação nível Especialização. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_POS_MESTRA` | INTEGER | Quantidade de docentes com Pós-Graduação nível Mestrado. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_POS_DOUTO` | INTEGER | Quantidade de docentes com Pós-Graduação nível Doutorado. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_POS_NENHUM` | INTEGER | Quantidade de docentes com ensino superior sem pós-graduação. — descrição gerada por IA. |
| `QT_DOC_BAS_VINCULO_CONCUR` | INTEGER | Quantidade de docentes com vínculo efetivo/concursado. — descrição gerada por IA. |
| `QT_DOC_BAS_VINCULO_CONTRA` | INTEGER | Quantidade de docentes com contrato temporário. — descrição gerada por IA. |
| `QT_DOC_BAS_VINCULO_TERCEIR` | INTEGER | Quantidade de docentes com vínculo terceirizado. — descrição gerada por IA. |
| `QT_DOC_BAS_VINCULO_CLT` | INTEGER | Quantidade de docentes com vínculo regido pela CLT. — descrição gerada por IA. |
| `QT_DOC_BAS_DOCENTE` | INTEGER | Quantidade de profissionais atuando estritamente em função docente. — descrição gerada por IA. |
| `QT_DOC_BAS_AUXILIAR` | INTEGER | Quantidade de auxiliares/assistentes educacionais atuando em sala. — descrição gerada por IA. |
| `QT_DOC_BAS_PROFI_MONITOR` | INTEGER | Quantidade de monitores educacionais atuando na escola. — descrição gerada por IA. |
| `QT_DOC_BAS_TRADUTOR_LIBRAS` | INTEGER | Quantidade de tradutores e intérpretes de LIBRAS. — descrição gerada por IA. |
| `QT_DOC_BAS_TITULAR_EAD` | INTEGER | Quantidade de professores titulares na modalidade EAD. — descrição gerada por IA. |
| `QT_DOC_BAS_TUTOR_AUX_EAD` | INTEGER | Quantidade de tutores e auxiliares na modalidade EAD. — descrição gerada por IA. |
| `QT_DOC_BAS_GUIA_INTERPRETE` | INTEGER | Quantidade de guias-intérpretes para surdocegos. — descrição gerada por IA. |
| `QT_DOC_BAS_APOIO_PCD` | INTEGER | Quantidade de profissionais de apoio escolar para estudantes com deficiência. — descrição gerada por IA. |
| `QT_DOC_BAS_INSTRUTOR_EP` | INTEGER | Quantidade de instrutores de ensino profissionalizante. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_CRE` | INTEGER | Quantidade de docentes com formação específica na área de Creche. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_PRE_ESCOLA` | INTEGER | Quantidade de docentes com formação específica na área de Pré-Escola. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ANOS_INICIAIS` | INTEGER | Quantidade de docentes com formação específica para Anos Iniciais do EF. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ANOS_FINAIS` | INTEGER | Quantidade de docentes com formação específica para Anos Finais do EF. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ENS_MEDIO` | INTEGER | Quantidade de docentes com formação específica para Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_EJA` | INTEGER | Quantidade de docentes com formação específica para Educação de Jovens e Adultos. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ED_ESPECIAL` | INTEGER | Quantidade de docentes com formação específica em Educação Especial. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_BIL_SURDOS` | INTEGER | Quantidade de docentes com formação específica em Educação Bilingue de Surdos. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ED_INDIGENA` | INTEGER | Quantidade de docentes com formação específica em Educação Indígena. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_CAMPO` | INTEGER | Quantidade de docentes com formação específica em Educação do Campo. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_AMBIENTAL` | INTEGER | Quantidade de docentes com formação específica em Educação Ambiental. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_DIR_HUMANOS` | INTEGER | Quantidade de docentes com formação em Direitos Humanos. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_DIV_SEXUAL` | INTEGER | Quantidade de docentes com formação em Diversidade Sexual e de Gênero. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_DIR_ADOLESC` | INTEGER | Quantidade de docentes com formação em Direitos de Crianças e Adolescentes. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_AFRO` | INTEGER | Quantidade de docentes com formação em História/Cultura Afro-Brasileira e Africana. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_GESTAO` | INTEGER | Quantidade de docentes com formação específica em Gestão Escolar. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_EDUC_TIC` | INTEGER | Quantidade de docentes com formação no uso de TICs na educação. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_OUTROS` | INTEGER | Quantidade de docentes com outras formações continuadas/específicas. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_NENHUM` | INTEGER | Quantidade de docentes sem nenhuma formação específica continuada declarada. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_PORT` | INTEGER | Quantidade de docentes lecionando a disciplina de Língua Portuguesa. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_EDUC_FISICA` | INTEGER | Quantidade de docentes lecionando a disciplina de Educação Física. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_ARTES` | INTEGER | Quantidade de docentes lecionando a disciplina de Artes. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_ING` | INTEGER | Quantidade de docentes lecionando a disciplina de Língua Inglesa. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_ESPA` | INTEGER | Quantidade de docentes lecionando a disciplina de Língua Espanhola. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_FRANC` | INTEGER | Quantidade de docentes lecionando a disciplina de Língua Francesa. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_OUTRA` | INTEGER | Quantidade de docentes lecionando outra língua estrangeira. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LIBRAS` | INTEGER | Quantidade de docentes lecionando a disciplina de LIBRAS. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_INDIG` | INTEGER | Quantidade de docentes lecionando disciplina de Língua Indígena. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_PORT_SEG_LINGUA` | INTEGER | Quantidade de docentes lecionando Português como Segunda Língua. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_MATEMATICA` | INTEGER | Quantidade de docentes lecionando a disciplina de Matemática. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_CIENCIAS` | INTEGER | Quantidade de docentes lecionando a disciplina de Ciências. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_FISICA` | INTEGER | Quantidade de docentes lecionando a disciplina de Física. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_QUIMICA` | INTEGER | Quantidade de docentes lecionando a disciplina de Química. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_BIOLOGIA` | INTEGER | Quantidade de docentes lecionando a disciplina de Biologia. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_HISTORIA` | INTEGER | Quantidade de docentes lecionando a disciplina de História. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_GEOGRAFIA` | INTEGER | Quantidade de docentes lecionando a disciplina de Geografia. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_SOCIOLOGIA` | INTEGER | Quantidade de docentes lecionando a disciplina de Sociologia. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_FILOSOFIA` | INTEGER | Quantidade de docentes lecionando a disciplina de Filosofia. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_EST_SOCIAIS` | INTEGER | Quantidade de docentes lecionando Estudos Sociais. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_EST_SOCIAIS_SOCI` | INTEGER | Quantidade de docentes lecionando Estudos Sociais/Sociologia. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_INFO_COMPUTACAO` | INTEGER | Quantidade de docentes lecionando Informática/Computação. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_ENSINO_RELIGIOSO` | INTEGER | Quantidade de docentes lecionando Ensino Religioso. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_PROFISSIONA` | INTEGER | Quantidade de docentes lecionando disciplinas da Educação Profissional. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_ESTAGIO_SUPER` | INTEGER | Quantidade de docentes orientando Estágio Curricular Supervisionado. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_PEDAGOGICAS` | INTEGER | Quantidade de docentes lecionando disciplinas Pedagógicas. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_PROJETO_DE_VIDA` | INTEGER | Quantidade de docentes lecionando a disciplina de Projeto de Vida. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_OUTRAS` | INTEGER | Quantidade de docentes lecionando outras disciplinas curriculares. — descrição gerada por IA. |
| `QT_DOC_BAS_LIBRAS` | INTEGER | Quantidade de docentes com conhecimento ou atuantes com LIBRAS. — descrição gerada por IA. |

## trusted · inep_censo_escolar_educacao_profissional

File `trusted__inep_censo_escolar_educacao_profissional.parquet` · 4,911,299 rows · 295 columns

TRUSTED - Educação profissional em layouts legados e modernos: cursos/habilitações, ensino médio integrado, cursos técnicos, eixos, matrículas e oferta por escola. Sem filtros que removam registros. Anos cobertos pelas fontes: 1995-2025 (1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025).

| Column | Type | Description |
|---|---|---|
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `DEP` | STRING | Dependência administrativa ou código de departamento/curso histórico do censo. — descrição gerada por IA. |
| `CO_CURSO` | INTEGER | Código do curso no cadastro do MEC/INEP. — descrição gerada por IA. |
| `DS_CURSO` | STRING | Descrição ou nome do curso. — descrição gerada por IA. |
| `VEM3001` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3001). — descrição gerada por IA. |
| `VEM3002` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3002). — descrição gerada por IA. |
| `VEM3003` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3003). — descrição gerada por IA. |
| `VEM3004` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3004). — descrição gerada por IA. |
| `VEM3005` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3005). — descrição gerada por IA. |
| `VEM3006` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3006). — descrição gerada por IA. |
| `VEM3007` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3007). — descrição gerada por IA. |
| `VEM3008` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3008). — descrição gerada por IA. |
| `VEM3009` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3009). — descrição gerada por IA. |
| `VEM3010` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3010). — descrição gerada por IA. |
| `VEM3011` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3011). — descrição gerada por IA. |
| `VEM3012` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3012). — descrição gerada por IA. |
| `VEM3013` | STRING | Variável histórica do Censo Escolar para vaga/matrícula de Educação Profissional (VEM 3013). — descrição gerada por IA. |
| `CODCURSO` | STRING | Código identificador do curso técnico/profissionalizante. — descrição gerada por IA. |
| `DEP131` | STRING | Código/indicador de departamento ou etapa de ensino profissional (DEP131). — descrição gerada por IA. |
| `DEP132` | STRING | Código/indicador de departamento ou etapa de ensino profissional (DEP132). — descrição gerada por IA. |
| `DEP133` | STRING | Código/indicador de departamento ou etapa de ensino profissional (DEP133). — descrição gerada por IA. |
| `DEP134` | STRING | Código/indicador de departamento ou etapa de ensino profissional (DEP134). — descrição gerada por IA. |
| `DEP135` | STRING | Código/indicador de departamento ou etapa de ensino profissional (DEP135). — descrição gerada por IA. |
| `DEP136` | STRING | Código/indicador de departamento ou etapa de ensino profissional (DEP136). — descrição gerada por IA. |
| `DEP137` | STRING | Código/indicador de departamento ou etapa de ensino profissional (DEP137). — descrição gerada por IA. |
| `NEP141` | STRING | Indicador/código de nível de ensino profissional (NEP141). — descrição gerada por IA. |
| `NEP142` | STRING | Indicador/código de nível de ensino profissional (NEP142). — descrição gerada por IA. |
| `NEP143` | STRING | Indicador/código de nível de ensino profissional (NEP143). — descrição gerada por IA. |
| `NEP144` | STRING | Indicador/código de nível de ensino profissional (NEP144). — descrição gerada por IA. |
| `NEP145` | STRING | Indicador/código de nível de ensino profissional (NEP145). — descrição gerada por IA. |
| `NEP146` | STRING | Indicador/código de nível de ensino profissional (NEP146). — descrição gerada por IA. |
| `NEP147` | STRING | Indicador/código de nível de ensino profissional (NEP147). — descrição gerada por IA. |
| `DEP138` | STRING | Código/indicador de departamento ou etapa de ensino profissional (DEP138). — descrição gerada por IA. |
| `DEP139` | STRING | Código/indicador de departamento ou etapa de ensino profissional (DEP139). — descrição gerada por IA. |
| `NEP148` | STRING | Indicador/código de nível de ensino profissional (NEP148). — descrição gerada por IA. |
| `NEP149` | STRING | Indicador/código de nível de ensino profissional (NEP149). — descrição gerada por IA. |
| `EP111` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP111). — descrição gerada por IA. |
| `EP112` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP112). — descrição gerada por IA. |
| `EP113` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP113). — descrição gerada por IA. |
| `EP114` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP114). — descrição gerada por IA. |
| `EP115` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP115). — descrição gerada por IA. |
| `EP116` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP116). — descrição gerada por IA. |
| `EP117` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP117). — descrição gerada por IA. |
| `EP121` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP121). — descrição gerada por IA. |
| `EP122` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP122). — descrição gerada por IA. |
| `EP123` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP123). — descrição gerada por IA. |
| `EP124` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP124). — descrição gerada por IA. |
| `EP125` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP125). — descrição gerada por IA. |
| `EP126` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP126). — descrição gerada por IA. |
| `EP127` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP127). — descrição gerada por IA. |
| `EP118` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP118). — descrição gerada por IA. |
| `EP119` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP119). — descrição gerada por IA. |
| `EP128` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP128). — descrição gerada por IA. |
| `EP129` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP129). — descrição gerada por IA. |
| `EP131` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP131). — descrição gerada por IA. |
| `EP132` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP132). — descrição gerada por IA. |
| `EP133` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP133). — descrição gerada por IA. |
| `EP134` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP134). — descrição gerada por IA. |
| `EP135` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP135). — descrição gerada por IA. |
| `EP136` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP136). — descrição gerada por IA. |
| `EP137` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP137). — descrição gerada por IA. |
| `EP141` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP141). — descrição gerada por IA. |
| `EP142` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP142). — descrição gerada por IA. |
| `EP143` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP143). — descrição gerada por IA. |
| `EP144` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP144). — descrição gerada por IA. |
| `EP145` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP145). — descrição gerada por IA. |
| `EP146` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP146). — descrição gerada por IA. |
| `EP147` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP147). — descrição gerada por IA. |
| `EP138` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP138). — descrição gerada por IA. |
| `EP139` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP139). — descrição gerada por IA. |
| `EP148` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP148). — descrição gerada por IA. |
| `EP149` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP149). — descrição gerada por IA. |
| `EP211` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP211). — descrição gerada por IA. |
| `EP212` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP212). — descrição gerada por IA. |
| `EP213` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP213). — descrição gerada por IA. |
| `EP214` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP214). — descrição gerada por IA. |
| `EP215` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP215). — descrição gerada por IA. |
| `EP216` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP216). — descrição gerada por IA. |
| `EP217` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP217). — descrição gerada por IA. |
| `EP221` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP221). — descrição gerada por IA. |
| `EP222` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP222). — descrição gerada por IA. |
| `EP223` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP223). — descrição gerada por IA. |
| `EP224` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP224). — descrição gerada por IA. |
| `EP225` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP225). — descrição gerada por IA. |
| `EP226` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP226). — descrição gerada por IA. |
| `EP227` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP227). — descrição gerada por IA. |
| `EP218` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP218). — descrição gerada por IA. |
| `EP219` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP219). — descrição gerada por IA. |
| `EP228` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP228). — descrição gerada por IA. |
| `EP229` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP229). — descrição gerada por IA. |
| `EP23A` | STRING | Variável complementar de Ensino Profissional (EP23A). — descrição gerada por IA. |
| `EP233` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP233). — descrição gerada por IA. |
| `EP234` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP234). — descrição gerada por IA. |
| `EP235` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP235). — descrição gerada por IA. |
| `EP236` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP236). — descrição gerada por IA. |
| `EP237` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP237). — descrição gerada por IA. |
| `EP24A` | STRING | Variável complementar de Ensino Profissional (EP24A). — descrição gerada por IA. |
| `EP243` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP243). — descrição gerada por IA. |
| `EP244` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP244). — descrição gerada por IA. |
| `EP245` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP245). — descrição gerada por IA. |
| `EP246` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP246). — descrição gerada por IA. |
| `EP247` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP247). — descrição gerada por IA. |
| `EP238` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP238). — descrição gerada por IA. |
| `EP239` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP239). — descrição gerada por IA. |
| `EP248` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP248). — descrição gerada por IA. |
| `EP249` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP249). — descrição gerada por IA. |
| `EP311` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP311). — descrição gerada por IA. |
| `EP312` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP312). — descrição gerada por IA. |
| `EP313` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP313). — descrição gerada por IA. |
| `EP314` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP314). — descrição gerada por IA. |
| `EP315` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP315). — descrição gerada por IA. |
| `EP316` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP316). — descrição gerada por IA. |
| `EP317` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP317). — descrição gerada por IA. |
| `EP321` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP321). — descrição gerada por IA. |
| `EP322` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP322). — descrição gerada por IA. |
| `EP323` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP323). — descrição gerada por IA. |
| `EP324` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP324). — descrição gerada por IA. |
| `EP325` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP325). — descrição gerada por IA. |
| `EP326` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP326). — descrição gerada por IA. |
| `EP327` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP327). — descrição gerada por IA. |
| `EP351` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP351). — descrição gerada por IA. |
| `EP361` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP361). — descrição gerada por IA. |
| `EP371` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP371). — descrição gerada por IA. |
| `EP381` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP381). — descrição gerada por IA. |
| `EP391` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP391). — descrição gerada por IA. |
| `EP3A1` | STRING | Variável complementar de Ensino Profissional (EP3A1). — descrição gerada por IA. |
| `EP352` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP352). — descrição gerada por IA. |
| `EP362` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP362). — descrição gerada por IA. |
| `EP372` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP372). — descrição gerada por IA. |
| `EP382` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP382). — descrição gerada por IA. |
| `EP392` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP392). — descrição gerada por IA. |
| `EP3A2` | STRING | Variável complementar de Ensino Profissional (EP3A2). — descrição gerada por IA. |
| `EP33A` | STRING | Variável complementar de Ensino Profissional (EP33A). — descrição gerada por IA. |
| `EP333` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP333). — descrição gerada por IA. |
| `EP334` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP334). — descrição gerada por IA. |
| `EP335` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP335). — descrição gerada por IA. |
| `EP336` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP336). — descrição gerada por IA. |
| `EP337` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP337). — descrição gerada por IA. |
| `EP338` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP338). — descrição gerada por IA. |
| `EP339` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP339). — descrição gerada por IA. |
| `EP34A` | STRING | Variável complementar de Ensino Profissional (EP34A). — descrição gerada por IA. |
| `EP343` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP343). — descrição gerada por IA. |
| `EP344` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP344). — descrição gerada por IA. |
| `EP345` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP345). — descrição gerada por IA. |
| `EP346` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP346). — descrição gerada por IA. |
| `EP347` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP347). — descrição gerada por IA. |
| `EP348` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP348). — descrição gerada por IA. |
| `EP349` | STRING | Variável de estrutura/matrícula de Ensino Profissional (EP349). — descrição gerada por IA. |
| `HABILCOD` | STRING | Código da habilitação profissional vinculada ao curso. — descrição gerada por IA. |
| `HABILNOM` | STRING | Nome da habilitação profissional vinculada ao curso. — descrição gerada por IA. |
| `VEM1215` | STRING | Histórico de matrículas/vagas de Educação Profissional do ano de 2015. — descrição gerada por IA. |
| `VEM1216` | STRING | Histórico de matrículas/vagas de Educação Profissional do ano de 2016. — descrição gerada por IA. |
| `VEM1217` | STRING | Histórico de matrículas/vagas de Educação Profissional do ano de 2017. — descrição gerada por IA. |
| `VEM1218` | STRING | Histórico de matrículas/vagas de Educação Profissional do ano de 2018. — descrição gerada por IA. |
| `VEM1219` | STRING | Histórico de matrículas/vagas de Educação Profissional do ano de 2019. — descrição gerada por IA. |
| `VEM1214` | STRING | Histórico de matrículas/vagas de Educação Profissional do ano de 2014. — descrição gerada por IA. |
| `DEM1214` | STRING | Demanda de vagas/matrículas de Educação Profissional do ano de 2014. — descrição gerada por IA. |
| `VEM2015` | STRING | Variável de acompanhamento de matrículas de Educação Profissional em 2015. — descrição gerada por IA. |
| `VEM2016` | STRING | Variável de acompanhamento de matrículas de Educação Profissional em 2016. — descrição gerada por IA. |
| `VEM2017` | STRING | Variável de acompanhamento de matrículas de Educação Profissional em 2017. — descrição gerada por IA. |
| `VEM2018` | STRING | Variável de acompanhamento de matrículas de Educação Profissional em 2018. — descrição gerada por IA. |
| `VEM2019` | STRING | Variável de acompanhamento de matrículas de Educação Profissional em 2019. — descrição gerada por IA. |
| `COD_EM22` | STRING | Código do itinerário formativo do Ensino Médio no censo de 2022. — descrição gerada por IA. |
| `VEM2211` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2211). — descrição gerada por IA. |
| `VEM2212` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2212). — descrição gerada por IA. |
| `VEM2213` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2213). — descrição gerada por IA. |
| `VEM2214` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2214). — descrição gerada por IA. |
| `VEM2215` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2215). — descrição gerada por IA. |
| `VEM2216` | STRING | Variável específica do Censo 22022 para Ensino Médio/Profissional (VEM 2216). — descrição gerada por IA. |
| `VEM2217` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2217). — descrição gerada por IA. |
| `VEM2221` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2221). — descrição gerada por IA. |
| `VEM2222` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2222). — descrição gerada por IA. |
| `VEM2223` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2223). — descrição gerada por IA. |
| `VEM2224` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2224). — descrição gerada por IA. |
| `VEM2225` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2225). — descrição gerada por IA. |
| `VEM2226` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2226). — descrição gerada por IA. |
| `VEM2227` | STRING | Variável específica do Censo 2022 para Ensino Médio/Profissional (VEM 2227). — descrição gerada por IA. |
| `NU_ANO_CENSO` | INTEGER | Ano de realização do Censo Escolar (YYYY). — descrição gerada por IA. |
| `CO_ENTIDADE` | INTEGER | Código INEP único de identificação da escola. — descrição gerada por IA. |
| `NO_AREA_CURSO_PROFISSIONAL` | STRING | Nome da área tecnológica do curso de Educação Profissional. — descrição gerada por IA. |
| `ID_AREA_CURSO_PROFISSIONAL` | INTEGER | Código/ID da área do curso profissionalizante. — descrição gerada por IA. |
| `NO_CURSO_EDUC_PROFISSIONAL` | STRING | Nome oficial do curso de Educação Profissional ofertado. — descrição gerada por IA. |
| `CO_CURSO_EDUC_PROFISSIONAL` | INTEGER | Código oficial do curso de Educação Profissional. — descrição gerada por IA. |
| `QT_CURSO_TEC` | INTEGER | Quantidade de cursos técnicos ofertados na escola. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC` | INTEGER | Quantidade total de matrículas em cursos técnicos. — descrição gerada por IA. |
| `QT_CURSO_TEC_CT` | INTEGER | Quantidade de cursos técnicos na forma concomitante. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_CT` | INTEGER | Quantidade de matrículas em cursos técnicos concomitantes. — descrição gerada por IA. |
| `QT_CURSO_TEC_NM` | INTEGER | Quantidade de cursos técnicos de nível médio. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_NM` | INTEGER | Quantidade de matrículas em cursos técnicos de nível médio. — descrição gerada por IA. |
| `QT_CURSO_TEC_CONC` | INTEGER | Quantidade de cursos técnicos na modalidade concomitante. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_CONC` | INTEGER | Quantidade de matrículas em cursos técnicos concomitantes. — descrição gerada por IA. |
| `QT_CURSO_TEC_SUBS` | INTEGER | Quantidade de cursos técnicos na modalidade subsequente. — descrição gerada por IA. |
| `QT_MAT_TEC_SUBS` | INTEGER | Quantidade de matrículas em cursos técnicos subsequentes. — descrição gerada por IA. |
| `QT_CURSO_TEC_EJA` | INTEGER | Quantidade de cursos técnicos na modalidade EJA. — descrição gerada por IA. |
| `QT_MAT_TEC_EJA` | INTEGER | Quantidade de matrículas em cursos técnicos integrados à EJA. — descrição gerada por IA. |
| `QT_CURSO_TEC_IFTP` | INTEGER | Quantidade de cursos técnicos do itinerário de formação técnica e profissional. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_IFTP` | INTEGER | Quantidade de matrículas do itinerário de formação técnica e profissional. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_SUBS` | INTEGER | Quantidade de matrículas em cursos técnicos subsequentes (campo duplicado/específico). — descrição gerada por IA. |
| `QT_CURSO_TEC_IFTP_CT` | INTEGER | Quantidade de cursos técnicos IFTP em oferta concomitante. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_IFTP_CT` | INTEGER | Matrículas em cursos técnicos IFTP concomitantes. — descrição gerada por IA. |
| `QT_MAT_CURSO_TEC_EJA` | INTEGER | Matrículas em cursos técnicos na modalidade EJA (campo específico). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_TEMPLO_IGREJA` | INTEGER | Indicador se a escola funciona em templo/igreja (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_CASA_PROFESSOR` | INTEGER | Indicador se a escola funciona em casa de professor (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA` | INTEGER | Indicador de existência de biblioteca na escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA_SALA_LEITURA` | INTEGER | Indicador de existência de biblioteca ou sala de leitura (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_DORMITORIO_PROFESSOR` | INTEGER | Indicador de presença de dormitório para professores na escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_SALA_PROFESSOR` | INTEGER | Indicador de existência de sala de professores (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROF_ADMINISTRATIVOS` | INTEGER | Indicador de atuação de profissionais administrativos (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_ADMINISTRATIVOS` | INTEGER | Quantidade de profissionais de apoio administrativo. — descrição gerada por IA. |
| `IN_PROF_SERVICOS_GERAIS` | INTEGER | Indicador de atuação de profissionais de serviços gerais (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_SERVICOS_GERAIS` | INTEGER | Quantidade de profissionais de serviços gerais na escola. — descrição gerada por IA. |
| `IN_PROF_BIBLIOTECARIO` | INTEGER | Indicador de presença de bibliotecário na escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_BIBLIOTECARIO` | INTEGER | Quantidade de bibliotecários na escola. — descrição gerada por IA. |
| `IN_PROF_SAUDE` | INTEGER | Indicador de atuação de profissionais de saúde na escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_SAUDE` | INTEGER | Quantidade de profissionais da área da saúde na escola. — descrição gerada por IA. |
| `IN_PROF_COORDENADOR` | INTEGER | Indicador de presença de coordenador pedagógico (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_COORDENADOR` | INTEGER | Quantidade de coordenadores pedagógicos na escola. — descrição gerada por IA. |
| `IN_PROF_FONAUDIOLOGO` | INTEGER | Indicador de presença de fonoaudiólogo (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_FONAUDIOLOGO` | INTEGER | Quantidade de fonoaudiólogos na escola. — descrição gerada por IA. |
| `IN_PROF_NUTRICIONISTA` | INTEGER | Indicador de atuação de nutricionista (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_NUTRICIONISTA` | INTEGER | Quantidade de nutricionistas atuando na escola. — descrição gerada por IA. |
| `IN_PROF_PSICOLOGO` | INTEGER | Indicador de atuação de psicólogo escolar (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_PSICOLOGO` | INTEGER | Quantidade de psicólogos escolares na unidade. — descrição gerada por IA. |
| `IN_PROF_ALIMENTACAO` | INTEGER | Indicador de atuação de profissionais de alimentação/merenda (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_ALIMENTACAO` | INTEGER | Quantidade de profissionais responsáveis pela alimentação escolar. — descrição gerada por IA. |
| `IN_PROF_PEDAGOGIA` | INTEGER | Indicador de atuação de pedagogos/orientadores (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_PEDAGOGIA` | INTEGER | Quantidade de pedagogos/orientadores pedagógicos. — descrição gerada por IA. |
| `IN_PROF_SECRETARIO` | INTEGER | Indicador de presença de secretário escolar (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_SECRETARIO` | INTEGER | Quantidade de secretários escolares. — descrição gerada por IA. |
| `IN_PROF_SEGURANCA` | INTEGER | Indicador de presença de profissionais de segurança/vigilância (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_SEGURANCA` | INTEGER | Quantidade de profissionais de segurança na escola. — descrição gerada por IA. |
| `IN_PROF_MONITORES` | INTEGER | Indicador de atuação de monitores/auxiliares (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_MONITORES` | INTEGER | Quantidade de monitores ou auxiliares escolares. — descrição gerada por IA. |
| `IN_PROF_GESTAO` | INTEGER | Indicador de atuação da equipe de gestão escolar (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_GESTAO` | INTEGER | Quantidade de profissionais na equipe de gestão escolar. — descrição gerada por IA. |
| `IN_PROF_ASSIST_SOCIAL` | INTEGER | Indicador de atuação de assistente social escolar (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_ASSIST_SOCIAL` | INTEGER | Quantidade de assistentes sociais na escola. — descrição gerada por IA. |
| `IN_MATERIAL_PED_CIENTIFICO` | INTEGER | Indicador de disponibilidade de material pedagógico para ensino científico (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROF` | INTEGER | Indicador de oferta de cursos de Educação Profissional na escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROF_TEC` | INTEGER | Indicador de oferta de ensino técnico (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_EJA` | INTEGER | Indicador de oferta da modalidade EJA (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_EJA_FUND` | INTEGER | Indicador de oferta de EJA Ensino Fundamental (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_EJA_MED` | INTEGER | Indicador de oferta de EJA Ensino Médio (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_MAT_PROF` | INTEGER | Quantidade total de matrículas na Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC` | INTEGER | Quantidade de matrículas no ensino técnico profissional. — descrição gerada por IA. |
| `QT_MAT_EJA` | INTEGER | Quantidade total de matrículas na modalidade EJA. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND` | INTEGER | Quantidade de matrículas na EJA - Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_EJA_MED` | INTEGER | Quantidade de matrículas na EJA - Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_PROF` | INTEGER | Quantidade de docentes na Educação Profissional. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC` | INTEGER | Quantidade de docentes no ensino técnico. — descrição gerada por IA. |
| `QT_DOC_EJA` | INTEGER | Quantidade de docentes atuando na EJA. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND` | INTEGER | Quantidade de docentes na EJA Fundamental. — descrição gerada por IA. |
| `QT_DOC_EJA_MED` | INTEGER | Quantidade de docentes na EJA Médio. — descrição gerada por IA. |
| `QT_TUR_PROF` | INTEGER | Quantidade de turmas de Educação Profissional. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC` | INTEGER | Quantidade de turmas de Ensino Técnico. — descrição gerada por IA. |
| `QT_TUR_EJA` | INTEGER | Quantidade total de turmas de EJA. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND` | INTEGER | Quantidade de turmas de EJA Fundamental. — descrição gerada por IA. |
| `QT_TUR_EJA_MED` | INTEGER | Quantidade de turmas de EJA Médio. — descrição gerada por IA. |
| `IN_FORMA_CONT_COOP_TEC_FIN` | INTEGER | Indicador de forma de apoio via cooperação técnica e financeira (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_LABORATORIO_EDUC_PROF` | INTEGER | Indicador de existência de laboratório para Educação Profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_SALA_OFICINAS_EDUC_PROF` | INTEGER | Indicador de existência de sala de oficinas de Educação Profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_PROFISSIONAL` | INTEGER | Indicador de disponibilidade de material pedagógico para formação profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_COOP_TEC_FIN` | INTEGER | Indicador de cooperação técnica/financeira municipal (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_COOP_TEC_FIN` | INTEGER | Indicador de cooperação técnica/financeira estadual (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROF_TRAD_LIBRAS` | INTEGER | Indicador de presença de tradutor/intérprete de Libras (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_TRAD_LIBRAS` | INTEGER | Quantidade de tradutores/intérpretes de Libras. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_CONC` | INTEGER | Matrículas em curso técnico concomitante. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_SUBS` | INTEGER | Matrículas em curso técnico subsequente. — descrição gerada por IA. |
| `QT_MAT_PROF_FIC_CONC` | INTEGER | Matrículas em cursos FIC (Formação Inicial e Continuada) concomitantes. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AI` | INTEGER | Matrículas em EJA Fundamental nos Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AF` | INTEGER | Matrículas em EJA Fundamental nos Anos Finais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_FIC` | INTEGER | Matrículas em EJA Fundamental integrada à qualificação profissional (FIC). — descrição gerada por IA. |
| `QT_MAT_EJA_MED_NPROF` | INTEGER | Matrículas em EJA Médio não profissionalizante. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_FIC` | INTEGER | Matrículas em EJA Médio integrada à formação inicial e continuada. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_TEC` | INTEGER | Matrículas em EJA Médio integrada à Educação Técnica. — descrição gerada por IA. |
| `IN_PROF_AGRICOLA` | INTEGER | Indicador de atuação de profissional técnico agrícola (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_AGRICOLA` | INTEGER | Quantidade de profissionais de formação agrícola. — descrição gerada por IA. |
| `IN_PROF_REVISOR_BRAILLE` | INTEGER | Indicador de presença de revisor Braille (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_REVISOR_BRAILLE` | INTEGER | Quantidade de revisores Braille. — descrição gerada por IA. |
| `IN_ITINERARIO_APROFUNDAMENTO` | INTEGER | Indicador de oferta de itinerário formativo de aprofundamento (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ITINERARIO_TECN_PROF` | INTEGER | Indicador de oferta de itinerário técnico e profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROFISSIONALIZANTE` | INTEGER | Indicador de oferta de cursos profissionalizantes gerais (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_MEDIO_FIC` | INTEGER | Indicador de turma comum de Ensino Médio com FIC (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_MEDIO_FIC` | INTEGER | Indicador de turma exclusiva de Educação Especial no Médio com FIC (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_EJA_FUND` | INTEGER | Indicador de turma comum de EJA Fundamental (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_EJA_MEDIO` | INTEGER | Indicador de turma comum de EJA Médio (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_EJA_PROF` | INTEGER | Indicador de turma comum de EJA articulada à Educação Profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_EJA_FUND` | INTEGER | Indicador de turma exclusiva de Educação Especial na EJA Fundamental (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_EJA_MEDIO` | INTEGER | Indicador de turma exclusiva de Educação Especial na EJA Médio (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_EJA_PROF` | INTEGER | Indicador de turma exclusiva de Educação Especial na EJA Profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_PROF` | INTEGER | Indicador de turma comum de Educação Profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_PROF` | INTEGER | Indicador de turma exclusiva de Educação Especial na Educação Profissional (1=Sim, 0=Não). — descrição gerada por IA. |

## trusted · inep_censo_escolar_escolas

File `trusted__inep_censo_escolar_escolas.parquet` · 7,376,443 rows · 102 columns

TRUSTED - Escolas/unidades de coleta do Censo Escolar INEP, com identificadores, localização, situação de funcionamento, dependência administrativa e atributos cadastrais. Sem filtros que removam registros. Anos cobertos pelas fontes: 1995-2025 (1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025).

**Built from:** `raw/inep_censo_escolar_escola`

**Feeds:** `semantic/f_censo_escolar`, `semantic/f_censo_escolar_municipio`, `semantic/obt_inep_censo_escola_ano`, `semantic/obt_inep_censo_infraestrutura_escola`

| Column | Type | Description |
|---|---|---|
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `MASCARA` | STRING | Mascara/identificador legado para controle da escola. — descrição gerada por IA. |
| `CO_IBGE` | INTEGER | Codigo IBGE da localizacao da escola. — descrição gerada por IA. |
| `NU_ANO` | INTEGER | Ano do registro ou levantamento. — descrição gerada por IA. |
| `UF` | STRING | Sigla da Unidade Federativa (ex: SP, RJ). — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla do estado ou regiao administrativa. — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do municipio (formato legado). — descrição gerada por IA. |
| `DEP` | STRING | Codigo de dependencia administrativa da escola (legado). — descrição gerada por IA. |
| `LOC` | STRING | Codigo da localizacao da escola (1-Urbana, 2-Rural) (legado). — descrição gerada por IA. |
| `CODFUNC` | STRING | Codigo da situacao de funcionamento da escola (legado). — descrição gerada por IA. |
| `NOESTAB` | STRING | Nome do estabelecimento de ensino (legado). — descrição gerada por IA. |
| `FORAESTA` | STRING | Indicador de funcionamento fora da sede (legado). — descrição gerada por IA. |
| `FUNCION` | STRING | Status de funcionamento da escola (legado). — descrição gerada por IA. |
| `ANO` | STRING | Ano de referencia (campo legado). — descrição gerada por IA. |
| `CODMUNIC` | STRING | Codigo IBGE do municipio (formato legado). — descrição gerada por IA. |
| `REG_CNAS` | STRING | Numero do registro no Conselho Nacional de Assistencia Social (CNAS). — descrição gerada por IA. |
| `NU_ANO_CENSO` | INTEGER | Ano de referencia do Censo Escolar da informacao. — descrição gerada por IA. |
| `NO_REGIAO` | STRING | Nome da regiao geografica (ex: Sudeste, Nordeste). — descrição gerada por IA. |
| `CO_REGIAO` | INTEGER | Codigo IBGE da regiao geografica (ex: 3 para Sudeste). — descrição gerada por IA. |
| `NO_UF` | STRING | Nome completo da Unidade Federativa da escola. — descrição gerada por IA. |
| `SG_UF` | STRING | Sigla da Unidade Federativa (UF) da escola. — descrição gerada por IA. |
| `CO_UF` | INTEGER | Codigo IBGE da Unidade Federativa da escola. — descrição gerada por IA. |
| `NO_MUNICIPIO` | STRING | Nome do municipio onde a escola esta localizada. — descrição gerada por IA. |
| `CO_MUNICIPIO` | INTEGER | Codigo IBGE de 7 digitos do municipio da escola. — descrição gerada por IA. |
| `NO_MESORREGIAO` | STRING | Nome da mesorregiao geografica segundo o IBGE. — descrição gerada por IA. |
| `CO_MESORREGIAO` | INTEGER | Codigo IBGE da mesorregiao geografica. — descrição gerada por IA. |
| `NO_MICRORREGIAO` | STRING | Nome da microrregiao geografica segundo o IBGE. — descrição gerada por IA. |
| `CO_MICRORREGIAO` | INTEGER | Codigo IBGE da microrregiao geografica. — descrição gerada por IA. |
| `CO_DISTRITO` | INTEGER | Codigo IBGE do distrito de localizacao da escola. — descrição gerada por IA. |
| `CO_ENTIDADE` | INTEGER | Codigo INEP unico da escola/entidade (8 digitos). — descrição gerada por IA. |
| `NO_ENTIDADE` | STRING | Nome oficial da escola ou instituicao de ensino. — descrição gerada por IA. |
| `TP_DEPENDENCIA` | INTEGER | Tipo de dependencia administrativa (1-Federal, 2-Estadual, 3-Municipal, 4-Privada). — descrição gerada por IA. |
| `TP_CATEGORIA_ESCOLA_PRIVADA` | INTEGER | Categoria da escola privada (ex: Particular, Comunitaria, Confessional, Filantropica). — descrição gerada por IA. |
| `TP_LOCALIZACAO` | INTEGER | Tipo de localizacao da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `TP_LOCALIZACAO_DIFERENCIADA` | INTEGER | Indicador de localizacao diferenciada (ex: Area de assentamento, Terra indigena, Quilombola). — descrição gerada por IA. |
| `DS_ENDERECO` | STRING | Endereco/logradouro completo da escola. — descrição gerada por IA. |
| `NU_ENDERECO` | INTEGER | Numero do endereco do estabelecimento. — descrição gerada por IA. |
| `DS_COMPLEMENTO` | STRING | Complemento do endereco da escola. — descrição gerada por IA. |
| `NO_BAIRRO` | STRING | Nome do bairro onde a escola se localiza. — descrição gerada por IA. |
| `CO_CEP` | INTEGER | Codigo de Enderecamento Postal (CEP) da escola. — descrição gerada por IA. |
| `NU_DDD` | INTEGER | Codigo DDD de telefone para contato com a escola. — descrição gerada por IA. |
| `NU_TELEFONE` | INTEGER | Numero do telefone principal de contato com a escola. — descrição gerada por IA. |
| `TP_SITUACAO_FUNCIONAMENTO` | INTEGER | Situacao de funcionamento (1-Em atividade, 2-Paralisada, 3-Extinta). — descrição gerada por IA. |
| `CO_ORGAO_REGIONAL` | INTEGER | Codigo da Regional de Ensino/Diretoria de Ensino responsavel. — descrição gerada por IA. |
| `DT_ANO_LETIVO_INICIO` | STRING | Data oficial de inicio do ano letivo. — descrição gerada por IA. |
| `DT_ANO_LETIVO_TERMINO` | STRING | Data oficial de termino do ano letivo. — descrição gerada por IA. |
| `IN_VINCULO_SECRETARIA_EDUCACAO` | INTEGER | Indicador de vinculo com a Secretaria de Educacao (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_VINCULO_SEGURANCA_PUBLICA` | INTEGER | Indicador de vinculo com orgaos de Seguranca Publica (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_VINCULO_SECRETARIA_SAUDE` | INTEGER | Indicador de vinculo com a Secretaria de Saude (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_VINCULO_OUTRO_ORGAO` | INTEGER | Indicador de vinculo com outro orgao da administracao publica (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_CONVENIADA_PP` | INTEGER | Indicador se a escola privada possui convenio com o poder publico (1-Sim, 0-Nao). — descrição gerada por IA. |
| `TP_CONVENIO_PODER_PUBLICO` | INTEGER | Tipo de convenio com o poder publico (Municipal, Estadual, etc.). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_EMP` | INTEGER | Indicador se a mantenedora e empresa/grupo empresarial (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_ONG` | INTEGER | Indicador se a mantenedora e uma ONG (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_OSCIP` | INTEGER | Indicador se a mantenedora e uma OSCIP (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIV_ONG_OSCIP` | INTEGER | Indicador se a mantenedora e ONG ou OSCIP (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_SIND` | INTEGER | Indicador se a mantenedora e sindicato ou associacao de classe (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_SIST_S` | INTEGER | Indicador se a mantenedora pertence ao Sistema S (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_MANT_ESCOLA_PRIVADA_S_FINS` | INTEGER | Indicador se a mantenedora e associacao sem fins lucrativos (1-Sim, 0-Nao). — descrição gerada por IA. |
| `TP_REGULAMENTACAO` | INTEGER | Tipo de regulamentacao da escola junto ao Conselho de Educacao. — descrição gerada por IA. |
| `TP_RESPONSAVEL_REGULAMENTACAO` | INTEGER | Orgao responsavel pela regulamentacao da escola. — descrição gerada por IA. |
| `CO_ESCOLA_SEDE_VINCULADA` | INTEGER | Codigo INEP da escola sede em caso de unidade vinculada/extensao. — descrição gerada por IA. |
| `CO_IES_OFERTANTE` | INTEGER | Codigo da Instituicao de Ensino Superior ofertante. — descrição gerada por IA. |
| `IN_LOCAL_FUNC_PREDIO_ESCOLAR` | INTEGER | Indicador de funcionamento em predio escolar (1-Sim, 0-Nao). — descrição gerada por IA. |
| `TP_OCUPACAO_PREDIO_ESCOLAR` | INTEGER | Tipo de ocupacao do predio escolar (1-Proprio, 2-Alugado, 3-Cedido). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SALAS_EMPRESA` | INTEGER | Indicador de funcionamento em salas de empresa (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SOCIOEDUCATIVO` | INTEGER | Indicador de funcionamento em unidade socioeducativa (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_UNID_PRISIONAL` | INTEGER | Indicador de funcionamento em unidade prisional (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_PRISIONAL_SOCIO` | INTEGER | Indicador de funcionamento em unidade prisional ou socioeducativa (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_TEMPLO_IGREJA` | INTEGER | Indicador de funcionamento em templo ou igreja (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_CASA_PROFESSOR` | INTEGER | Indicador de funcionamento em casa do professor (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_GALPAO` | INTEGER | Indicador de funcionamento em galpao (1-Sim, 0-Nao). — descrição gerada por IA. |
| `TP_OCUPACAO_GALPAO` | INTEGER | Tipo de ocupacao do galpao utilizado. — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SALAS_OUTRA_ESC` | INTEGER | Indicador de funcionamento em salas de outra escola (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_OUTROS` | INTEGER | Indicador de funcionamento em outros locais (1-Sim, 0-Nao). — descrição gerada por IA. |
| `TP_REDE_LOCAL` | INTEGER | Tipo de estrutura de rede local de computadores (intranet) na escola. — descrição gerada por IA. |
| `TP_INDIGENA_LINGUA` | INTEGER | Indicador do tipo de lingua indigena utilizada na educacao. — descrição gerada por IA. |
| `CO_LINGUA_INDIGENA_1` | INTEGER | Codigo da primeira lingua indigena falada na escola. — descrição gerada por IA. |
| `CO_LINGUA_INDIGENA_2` | INTEGER | Codigo da segunda lingua indigena falada na escola. — descrição gerada por IA. |
| `CO_LINGUA_INDIGENA_3` | INTEGER | Codigo da terceira lingua indigena falada na escola. — descrição gerada por IA. |
| `IN_ORGAO_ASS_PAIS` | INTEGER | Indicador da existencia de Associacao de Pais (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_ORGAO_ASS_PAIS_MESTRES` | INTEGER | Indicador de existencia de Associacao de Pais e Mestres - APM (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_ORGAO_CONSELHO_ESCOLAR` | INTEGER | Indicador de existencia de Conselho Escolar (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_ORGAO_GREMIO_ESTUDANTIL` | INTEGER | Indicador de existencia de Gremio Estudantil (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_ORGAO_OUTROS` | INTEGER | Indicador de existencia de outros colegiados/orgaos (1-Sim, 0-Nao). — descrição gerada por IA. |
| `IN_ORGAO_NENHUM` | INTEGER | Indicador de ausencia de orgaos colegiados na escola (1-Sim, 0-Nao). — descrição gerada por IA. |
| `TP_PROPOSTA_PEDAGOGICA` | INTEGER | Tipo de proposta pedagogica diferenciada adotada. — descrição gerada por IA. |
| `TP_AEE` | INTEGER | Tipo de Atendimento Educacional Especializado ofertado. — descrição gerada por IA. |
| `TP_ATIVIDADE_COMPLEMENTAR` | INTEGER | Tipo de atividade complementar/extracurricular oferecida. — descrição gerada por IA. |
| `IN_PODER_PUBLICO_PARCERIA` | INTEGER | Indicador de parceria com o poder publico (1-Sim, 0-Nao). — descrição gerada por IA. |
| `TP_PODER_PUBLICO_PARCERIA` | INTEGER | Tipo da parceria firmada com o poder publico. — descrição gerada por IA. |
| `NO_REGIAO_GEOG_INTERM` | STRING | Nome da Regiao Geografica Intermediaria (IBGE). — descrição gerada por IA. |
| `CO_REGIAO_GEOG_INTERM` | INTEGER | Codigo da Regiao Geografica Intermediaria (IBGE). — descrição gerada por IA. |
| `NO_REGIAO_GEOG_IMED` | STRING | Nome da Regiao Geografica Imediata (IBGE). — descrição gerada por IA. |
| `CO_REGIAO_GEOG_IMED` | INTEGER | Codigo da Regiao Geografica Imediata (IBGE). — descrição gerada por IA. |
| `NO_DISTRITO` | STRING | Nome do distrito de localizacao da escola. — descrição gerada por IA. |
| `NO_REGIAO_ADMINISTRATIVA` | STRING | Nome da regiao administrativa de localizacao da escola. — descrição gerada por IA. |
| `CO_REGIAO_ADMINISTRATIVA` | INTEGER | Codigo da regiao administrativa. — descrição gerada por IA. |
| `TP_ITINERARIO_FORMATIVO` | INTEGER | Tipo de itinerario formativo do Ensino Medio ofertado pela escola. — descrição gerada por IA. |

## trusted · inep_censo_escolar_etapas_ensino

File `trusted__inep_censo_escolar_etapas_ensino.parquet` · 4,808,966 rows · 713 columns

TRUSTED - Oferta e quantitativos por etapas, modalidades e organização da educação básica: infantil, fundamental, médio, EJA, especial, profissional e correlatas. Sem filtros que removam registros. Anos cobertos pelas fontes: 2007-2025 (2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025).

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | INTEGER | Ano de referência do Censo Escolar (formato AAAA). — descrição gerada por IA. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `CO_ENTIDADE` | INTEGER | Código INEP de identificação da escola/entidade educacional. — descrição gerada por IA. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `IN_VINCULO_SECRETARIA_EDUCACAO` | INTEGER | Indicador de vínculo com a Secretaria de Educação (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_VINCULO_SECRETARIA_SAUDE` | INTEGER | Indicador de vínculo com a Secretaria de Saúde (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_PREDIO_ESCOLAR` | INTEGER | Indicador de funcionamento em prédio escolar (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SALAS_EMPRESA` | INTEGER | Indicador de funcionamento em salas de empresa (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_TEMPLO_IGREJA` | INTEGER | Indicador de funcionamento em templo/igreja (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_CASA_PROFESSOR` | INTEGER | Indicador de funcionamento em casa de professor (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PREDIO_COMPARTILHADO` | INTEGER | Indicador de prédio compartilhado com outra escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_BANHEIRO_FORA_PREDIO` | INTEGER | Indicador de banheiro fora do prédio escolar (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_BANHEIRO_DENTRO_PREDIO` | INTEGER | Indicador de banheiro dentro do prédio escolar (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA` | INTEGER | Indicador de existência de biblioteca (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA_SALA_LEITURA` | INTEGER | Indicador de sala de leitura (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_DESPENSA` | INTEGER | Indicador de existência de despensa (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_DORMITORIO_PROFESSOR` | INTEGER | Indicador de alojamento/dormitório para professores (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_LABORATORIO_INFORMATICA` | INTEGER | Indicador de laboratório de informática (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PARQUE_INFANTIL` | INTEGER | Indicador de parque infantil/playground (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES` | INTEGER | Indicador de quadra de esportes (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES_COBERTA` | INTEGER | Indicador de quadra de esportes coberta (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES_DESCOBERTA` | INTEGER | Indicador de quadra de esportes descoberta (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_SALA_PROFESSOR` | INTEGER | Indicador de sala para professores (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_SECRETARIA` | INTEGER | Indicador de sala de secretaria (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_SALA_ATENDIMENTO_ESPECIAL` | INTEGER | Indicador de sala de atendimento educacional especializado - AEE (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_EQUIP_IMPRESSORA` | INTEGER | Indicador de presença de impressoras simples (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_EQUIP_IMPRESSORA_MULT` | INTEGER | Indicador de presença de impressoras multifuncionais (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_EQUIP_IMPRESSORA` | INTEGER | Quantidade de impressoras simples na escola. — descrição gerada por IA. |
| `QT_EQUIP_IMPRESSORA_MULT` | INTEGER | Quantidade de impressoras multifuncionais na escola. — descrição gerada por IA. |
| `IN_INTERNET_APRENDIZAGEM` | INTEGER | Indicador de internet para uso no processo de aprendizagem (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROF_ADMINISTRATIVOS` | INTEGER | Indicador de presença de funcionários administrativos (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_ADMINISTRATIVOS` | INTEGER | Quantidade de profissionais na equipe administrativa. — descrição gerada por IA. |
| `IN_PROF_SERVICOS_GERAIS` | INTEGER | Indicador de presença de profissionais de serviços gerais (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_SERVICOS_GERAIS` | INTEGER | Quantidade de profissionais de limpeza e serviços gerais. — descrição gerada por IA. |
| `IN_PROF_BIBLIOTECARIO` | INTEGER | Indicador de presença de bibliotecário (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_BIBLIOTECARIO` | INTEGER | Quantidade de bibliotecários ou auxiliares de biblioteca. — descrição gerada por IA. |
| `IN_PROF_SAUDE` | INTEGER | Indicador de presença de profissionais de saúde (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_SAUDE` | INTEGER | Quantidade de profissionais da área de saúde na escola. — descrição gerada por IA. |
| `IN_PROF_COORDENADOR` | INTEGER | Indicador de presença de coordenador pedagógico (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_COORDENADOR` | INTEGER | Quantidade de coordenadores pedagógicos. — descrição gerada por IA. |
| `IN_PROF_FONAUDIOLOGO` | INTEGER | Indicador de presença de fonoaudiólogo (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_FONAUDIOLOGO` | INTEGER | Quantidade de fonoaudiólogos. — descrição gerada por IA. |
| `IN_PROF_NUTRICIONISTA` | INTEGER | Indicador de presença de nutricionista (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_NUTRICIONISTA` | INTEGER | Quantidade de nutricionistas. — descrição gerada por IA. |
| `IN_PROF_PSICOLOGO` | INTEGER | Indicador de presença de psicólogo escolar (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_PSICOLOGO` | INTEGER | Quantidade de psicólogos escolares. — descrição gerada por IA. |
| `IN_PROF_ALIMENTACAO` | INTEGER | Indicador de presença de merendeiras/profissionais de alimentação (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_ALIMENTACAO` | INTEGER | Quantidade de profissionais de alimentação/cozinha. — descrição gerada por IA. |
| `IN_PROF_PEDAGOGIA` | INTEGER | Indicador de presença de pedagogos orientadores (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_PEDAGOGIA` | INTEGER | Quantidade de pedagogos/orientadores educacionais. — descrição gerada por IA. |
| `IN_PROF_SECRETARIO` | INTEGER | Indicador de presença de secretário escolar (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_SECRETARIO` | INTEGER | Quantidade de secretários escolares. — descrição gerada por IA. |
| `IN_PROF_SEGURANCA` | INTEGER | Indicador de presença de porteiros/seguranças (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_SEGURANCA` | INTEGER | Quantidade de porteiros e seguranças. — descrição gerada por IA. |
| `IN_PROF_MONITORES` | INTEGER | Indicador de presença de monitores/estagiários (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_MONITORES` | INTEGER | Quantidade de monitores de apoio em sala. — descrição gerada por IA. |
| `IN_PROF_GESTAO` | INTEGER | Indicador de presença de equipe de gestão/direção (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_GESTAO` | INTEGER | Quantidade de profissionais na gestão/direção. — descrição gerada por IA. |
| `IN_PROF_ASSIST_SOCIAL` | INTEGER | Indicador de presença de assistente social (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_ASSIST_SOCIAL` | INTEGER | Quantidade de assistentes sociais na escola. — descrição gerada por IA. |
| `IN_FUNDAMENTAL_CICLOS` | INTEGER | Indicador de Ensino Fundamental organizado em ciclos (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_INFANTIL` | INTEGER | Indicador de acervo de materiais pedagógicos para Educação Infantil (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_CIENTIFICO` | INTEGER | Indicador de materiais para experimentos científicos (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_DESPORTIVA` | INTEGER | Indicador de materiais de educação física e esportes (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MATERIAL_ESP_QUILOMBOLA` | INTEGER | Indicador de acervo pedagógico específico para educação quilombola (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MATERIAL_ESP_INDIGENA` | INTEGER | Indicador de acervo pedagógico específico para educação indígena (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MATERIAL_ESP_NAO_UTILIZA` | INTEGER | Indicador de não utilização de materiais didáticos específicos (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESPACO_ATIVIDADE` | INTEGER | Indicador de espaço próprio para realização de atividades (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESPACO_EQUIPAMENTO` | INTEGER | Indicador de sala com equipamentos pedagógicos específicos (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MEDIACAO_PRESENCIAL` | INTEGER | Indicador de oferta de ensino presencial (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MEDIACAO_SEMIPRESENCIAL` | INTEGER | Indicador de oferta de ensino semipresencial (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MEDIACAO_EAD` | INTEGER | Indicador de oferta de ensino a distância (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_BAS` | INTEGER | Indicador de atendimento na Educação Básica (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_INF` | INTEGER | Indicador de atendimento na Educação Infantil (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_INF_CRE` | INTEGER | Indicador de atendimento na Creche (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_INF_PRE` | INTEGER | Indicador de atendimento na Pré-Escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FUND` | INTEGER | Indicador de atendimento no Ensino Fundamental (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FUND_AI` | INTEGER | Indicador de atendimento nos Anos Iniciais do EF (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FUND_AF` | INTEGER | Indicador de atendimento nos Anos Finais do EF (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MED` | INTEGER | Indicador de atendimento no Ensino Médio (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROF` | INTEGER | Indicador de atendimento em Educação Profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROF_TEC` | INTEGER | Indicador de atendimento em Educação Profissional Técnica (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_EJA` | INTEGER | Indicador de atendimento na EJA - Educação de Jovens e Adultos (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_EJA_FUND` | INTEGER | Indicador de atendimento na EJA Ensino Fundamental (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_EJA_MED` | INTEGER | Indicador de atendimento na EJA Ensino Médio (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP` | INTEGER | Indicador de atendimento em Educação Especial (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_CC` | INTEGER | Indicador de Educação Especial em classe comum (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_CE` | INTEGER | Indicador de Educação Especial em classe exclusiva (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_MAT_BAS` | INTEGER | Quantidade total de matrículas na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_INF` | INTEGER | Quantidade de matrículas na Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_INF_CRE` | INTEGER | Quantidade de matrículas na Creche. — descrição gerada por IA. |
| `QT_MAT_INF_PRE` | INTEGER | Quantidade de matrículas na Pré-Escola. — descrição gerada por IA. |
| `QT_MAT_FUND` | INTEGER | Quantidade de matrículas no Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI` | INTEGER | Quantidade de matrículas no Ensino Fundamental - Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_FUND_AF` | INTEGER | Quantidade de matrículas no Ensino Fundamental - Anos Finais. — descrição gerada por IA. |
| `QT_MAT_MED` | INTEGER | Quantidade de matrículas no Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_PROF` | INTEGER | Quantidade de matrículas na Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC` | INTEGER | Quantidade de matrículas na Educação Profissional Técnica de nível médio. — descrição gerada por IA. |
| `QT_MAT_EJA` | INTEGER | Quantidade de matrículas na EJA. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND` | INTEGER | Quantidade de matrículas na EJA do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_EJA_MED` | INTEGER | Quantidade de matrículas na EJA do Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP` | INTEGER | Quantidade total de matrículas na Educação Especial. — descrição gerada por IA. |
| `QT_MAT_ESP_CC` | INTEGER | Quantidade de matrículas de Educação Especial em classes comuns. — descrição gerada por IA. |
| `QT_MAT_ESP_CE` | INTEGER | Quantidade de matrículas de Educação Especial em classes exclusivas. — descrição gerada por IA. |
| `QT_MAT_BAS_FEM` | INTEGER | Quantidade de matrículas do sexo feminino na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_MASC` | INTEGER | Quantidade de matrículas do sexo masculino na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_ND` | INTEGER | Quantidade de matrículas na Educação Básica sem sexo/gênero declarado. — descrição gerada por IA. |
| `QT_MAT_BAS_BRANCA` | INTEGER | Quantidade de matrículas de raça/cor branca na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_PRETA` | INTEGER | Quantidade de matrículas de raça/cor preta na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_PARDA` | INTEGER | Quantidade de matrículas de raça/cor parda na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_AMARELA` | INTEGER | Quantidade de matrículas de raça/cor amarela na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_INDIGENA` | INTEGER | Quantidade de matrículas de raça/cor indígena na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_0_3` | INTEGER | Quantidade de alunos com idade de 0 a 3 anos na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_4_5` | INTEGER | Quantidade de alunos com idade de 4 a 5 anos na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_6_10` | INTEGER | Quantidade de alunos com idade de 6 a 10 anos na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_11_14` | INTEGER | Quantidade de alunos com idade de 11 a 14 anos na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_15_17` | INTEGER | Quantidade de alunos com idade de 15 a 17 anos na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_18_MAIS` | INTEGER | Quantidade de alunos com 18 anos ou mais na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_D` | INTEGER | Quantidade de matrículas no turno diurno na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_N` | INTEGER | Quantidade de matrículas no turno noturno na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_EAD` | INTEGER | Quantidade de matrículas na modalidade EAD na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_INF_INT` | INTEGER | Quantidade de matrículas em tempo integral na Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_INT` | INTEGER | Quantidade de matrículas em tempo integral na Creche. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_INT` | INTEGER | Quantidade de matrículas em tempo integral na Pré-Escola. — descrição gerada por IA. |
| `QT_MAT_FUND_INT` | INTEGER | Quantidade de matrículas em tempo integral no Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_INT` | INTEGER | Quantidade de matrículas em tempo integral no EF Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_INT` | INTEGER | Quantidade de matrículas em tempo integral no EF Anos Finais. — descrição gerada por IA. |
| `QT_MAT_MED_INT` | INTEGER | Quantidade de matrículas em tempo integral no Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_BAS` | INTEGER | Quantidade total de docentes atuantes na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_INF` | INTEGER | Quantidade de docentes na Educação Infantil. — descrição gerada por IA. |
| `QT_DOC_INF_CRE` | INTEGER | Quantidade de docentes na Creche. — descrição gerada por IA. |
| `QT_DOC_INF_PRE` | INTEGER | Quantidade de docentes na Pré-Escola. — descrição gerada por IA. |
| `QT_DOC_FUND` | INTEGER | Quantidade de docentes no Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI` | INTEGER | Quantidade de docentes no EF Anos Iniciais. — descrição gerada por IA. |
| `QT_DOC_FUND_AF` | INTEGER | Quantidade de docentes no EF Anos Finais. — descrição gerada por IA. |
| `QT_DOC_MED` | INTEGER | Quantidade de docentes no Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_PROF` | INTEGER | Quantidade de docentes na Educação Profissional. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC` | INTEGER | Quantidade de docentes na Educação Profissional Técnica. — descrição gerada por IA. |
| `QT_DOC_EJA` | INTEGER | Quantidade de docentes na EJA. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND` | INTEGER | Quantidade de docentes na EJA do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_EJA_MED` | INTEGER | Quantidade de docentes na EJA do Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_ESP` | INTEGER | Quantidade total de docentes em Educação Especial. — descrição gerada por IA. |
| `QT_DOC_ESP_CC` | INTEGER | Quantidade de docentes de Educação Especial em classe comum. — descrição gerada por IA. |
| `QT_DOC_ESP_CE` | INTEGER | Quantidade de docentes de Educação Especial em classe exclusiva. — descrição gerada por IA. |
| `QT_TUR_BAS` | INTEGER | Quantidade total de turmas da Educação Básica. — descrição gerada por IA. |
| `QT_TUR_INF` | INTEGER | Quantidade de turmas na Educação Infantil. — descrição gerada por IA. |
| `QT_TUR_INF_CRE` | INTEGER | Quantidade de turmas na Creche. — descrição gerada por IA. |
| `QT_TUR_INF_PRE` | INTEGER | Quantidade de turmas na Pré-Escola. — descrição gerada por IA. |
| `QT_TUR_FUND` | INTEGER | Quantidade de turmas no Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI` | INTEGER | Quantidade de turmas no EF Anos Iniciais. — descrição gerada por IA. |
| `QT_TUR_FUND_AF` | INTEGER | Quantidade de turmas no EF Anos Finais. — descrição gerada por IA. |
| `QT_TUR_MED` | INTEGER | Quantidade de turmas no Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_PROF` | INTEGER | Quantidade de turmas de Educação Profissional. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC` | INTEGER | Quantidade de turmas de Educação Profissional Técnica. — descrição gerada por IA. |
| `QT_TUR_EJA` | INTEGER | Quantidade de turmas da EJA. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND` | INTEGER | Quantidade de turmas da EJA Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_EJA_MED` | INTEGER | Quantidade de turmas da EJA Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_ESP` | INTEGER | Quantidade de turmas de Educação Especial. — descrição gerada por IA. |
| `QT_TUR_ESP_CC` | INTEGER | Quantidade de turmas de Educação Especial em classe comum. — descrição gerada por IA. |
| `QT_TUR_ESP_CE` | INTEGER | Quantidade de turmas de Educação Especial em classe exclusiva. — descrição gerada por IA. |
| `IN_FORMA_CONT_PRESTACAO_SERV` | INTEGER | Indicador de contratação por prestação de serviço (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_COOP_TEC_FIN` | INTEGER | Indicador de parceria por cooperação técnica/financeira (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_LABORATORIO_EDUC_PROF` | INTEGER | Indicador de laboratório específico para educação profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_SALA_OFICINAS_EDUC_PROF` | INTEGER | Indicador de sala de oficinas para cursos profissionais (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_PROFISSIONAL` | INTEGER | Indicador de material pedagógico para formação profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_PREST_SERV` | INTEGER | Indicador de convênio municipal para prestação de serviço (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_MU_COOP_TEC_FIN` | INTEGER | Indicador de convênio municipal de cooperação técnica/financeira (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_PREST_SERV` | INTEGER | Indicador de convênio estadual para prestação de serviço (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_FORMA_CONT_ES_COOP_TEC_FIN` | INTEGER | Indicador de convênio estadual de cooperação técnica/financeira (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROF_TRAD_LIBRAS` | INTEGER | Indicador de presença de tradutor/intérprete de LIBRAS (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_TRAD_LIBRAS` | INTEGER | Quantidade de tradutores/intérpretes de LIBRAS. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_1` | INTEGER | Matrículas no 1º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_2` | INTEGER | Matrículas no 2º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_3` | INTEGER | Matrículas no 3º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_4` | INTEGER | Matrículas no 4º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_5` | INTEGER | Matrículas no 5º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_6` | INTEGER | Matrículas no 6º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_7` | INTEGER | Matrículas no 7º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_8` | INTEGER | Matrículas no 8º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_9` | INTEGER | Matrículas no 9º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_MED_PROP` | INTEGER | Matrículas no Ensino Médio propedêutico tradicional. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_1` | INTEGER | Matrículas na 1ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_2` | INTEGER | Matrículas na 2ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_3` | INTEGER | Matrículas na 3ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_4` | INTEGER | Matrículas na 4ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_NS` | INTEGER | Matrículas no Ensino Médio propedêutico em série não seriada. — descrição gerada por IA. |
| `QT_MAT_MED_CT` | INTEGER | Matrículas no Ensino Médio Integrado/Técnico. — descrição gerada por IA. |
| `QT_MAT_MED_CT_1` | INTEGER | Matrículas na 1ª série do Ensino Médio Técnico. — descrição gerada por IA. |
| `QT_MAT_MED_CT_2` | INTEGER | Matrículas na 2ª série do Ensino Médio Técnico. — descrição gerada por IA. |
| `QT_MAT_MED_CT_3` | INTEGER | Matrículas na 3ª série do Ensino Médio Técnico. — descrição gerada por IA. |
| `QT_MAT_MED_CT_4` | INTEGER | Matrículas na 4ª série do Ensino Médio Técnico. — descrição gerada por IA. |
| `QT_MAT_MED_CT_NS` | INTEGER | Matrículas no Ensino Médio Técnico em série não seriada. — descrição gerada por IA. |
| `QT_MAT_MED_NM` | INTEGER | Matrículas no Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_1` | INTEGER | Matrículas na 1ª série do Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_2` | INTEGER | Matrículas na 2ª série do Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_3` | INTEGER | Matrículas na 3ª série do Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_4` | INTEGER | Matrículas na 4ª série do Magistério. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_CONC` | INTEGER | Matrículas em Educação Profissional Técnica concomitante. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_SUBS` | INTEGER | Matrículas em Educação Profissional Técnica subsequente. — descrição gerada por IA. |
| `QT_MAT_PROF_FIC_CONC` | INTEGER | Matrículas em cursos FIC (Qualificação Profissional) concomitantes. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AI` | INTEGER | Matrículas na EJA Fundamental - Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AF` | INTEGER | Matrículas na EJA Fundamental - Anos Finais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_FIC` | INTEGER | Matrículas na EJA Fundamental com qualificação profissional (FIC). — descrição gerada por IA. |
| `QT_MAT_EJA_MED_NPROF` | INTEGER | Matrículas na EJA Médio sem formação profissional. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_FIC` | INTEGER | Matrículas na EJA Médio com qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_TEC` | INTEGER | Matrículas na EJA Médio integrada à Educação Técnica. — descrição gerada por IA. |
| `QT_TRANSP_RESP_EST` | INTEGER | Quantidade de alunos atendidos pelo transporte escolar do estado. — descrição gerada por IA. |
| `QT_TRANSP_RESP_MUN` | INTEGER | Quantidade de alunos atendidos pelo transporte escolar do município. — descrição gerada por IA. |
| `QT_TUR_BAS_D` | INTEGER | Quantidade de turmas diurnas da Educação Básica. — descrição gerada por IA. |
| `QT_TUR_BAS_N` | INTEGER | Quantidade de turmas noturnas da Educação Básica. — descrição gerada por IA. |
| `QT_TUR_BAS_EAD` | INTEGER | Quantidade de turmas EAD da Educação Básica. — descrição gerada por IA. |
| `QT_TUR_INF_INT` | INTEGER | Quantidade de turmas em tempo integral da Educação Infantil. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_INT` | INTEGER | Quantidade de turmas em tempo integral na Creche. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_INT` | INTEGER | Quantidade de turmas em tempo integral na Pré-Escola. — descrição gerada por IA. |
| `QT_TUR_FUND_INT` | INTEGER | Quantidade de turmas em tempo integral no Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_INT` | INTEGER | Quantidade de turmas em tempo integral no EF Anos Iniciais. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_INT` | INTEGER | Quantidade de turmas em tempo integral no EF Anos Finais. — descrição gerada por IA. |
| `QT_TUR_MED_INT` | INTEGER | Quantidade de turmas em tempo integral no Ensino Médio. — descrição gerada por IA. |
| `IN_PROF_AGRICOLA` | INTEGER | Indicador de presença de técnico de agropecuária/monitores agrícolas (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_AGRICOLA` | INTEGER | Quantidade de monitores/técnicos agrícolas. — descrição gerada por IA. |
| `IN_PROF_REVISOR_BRAILLE` | INTEGER | Indicador de presença de revisor de textos em Braille (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_PROF_REVISOR_BRAILLE` | INTEGER | Quantidade de revisores de Braille. — descrição gerada por IA. |
| `IN_MATERIAL_PED_EDU_ESP` | INTEGER | Indicador de acervo pedagógico especial para PCD (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ITINERARIO_APROFUNDAMENTO` | INTEGER | Indicador de oferta de itinerários formativos de aprofundamento (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ITINERARIO_TECN_PROF` | INTEGER | Indicador de oferta de itinerário técnico-profissional no Novo Ensino Médio (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESPECIAL_EXCLUSIVA` | INTEGER | Indicador de escola exclusiva de Educação Especial (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_PROFISSIONALIZANTE` | INTEGER | Indicador de escola com oferta profissionalizante (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_CRECHE` | INTEGER | Indicador de turmas comuns de Creche (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_PRE` | INTEGER | Indicador de turmas comuns de Pré-Escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_FUND_AI` | INTEGER | Indicador de turmas comuns de EF Anos Iniciais (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_FUND_AF` | INTEGER | Indicador de turmas comuns de EF Anos Finais (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_MEDIO_MEDIO` | INTEGER | Indicador de turmas comuns de Ensino Médio Regular (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_MEDIO_INTEGRADO` | INTEGER | Indicador de turmas comuns de Ensino Médio Integrado (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_MEDIO_FIC` | INTEGER | Indicador de turmas comuns de Ensino Médio com FIC (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_MEDIO_NORMAL` | INTEGER | Indicador de turmas comuns de Ensino Médio Normal (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_CRECHE` | INTEGER | Indicador de turmas exclusivas de Educação Especial na Creche (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_PRE` | INTEGER | Indicador de turmas exclusivas de Ed. Especial na Pré-Escola (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_FUND_AI` | INTEGER | Indicador de turmas exclusivas de Ed. Especial no EF Anos Iniciais (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_FUND_AF` | INTEGER | Indicador de turmas exclusivas de Ed. Especial no EF Anos Finais (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_MEDIO_MEDIO` | INTEGER | Indicador de turmas exclusivas de Ed. Especial no Ensino Médio Regular (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_MEDIO_INTEGR` | INTEGER | Indicador de turmas exclusivas de Ed. Especial no Médio Integrado (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_MEDIO_FIC` | INTEGER | Indicador de turmas exclusivas de Ed. Especial no Médio FIC (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_MEDIO_NORMAL` | INTEGER | Indicador de turmas exclusivas de Ed. Especial no Normal (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_EJA_FUND` | INTEGER | Indicador de turmas comuns de EJA Ensino Fundamental (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_EJA_MEDIO` | INTEGER | Indicador de turmas comuns de EJA Ensino Médio (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_EJA_PROF` | INTEGER | Indicador de turmas comuns de EJA Profissionalizante (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_EJA_FUND` | INTEGER | Indicador de turmas exclusivas de Ed. Especial na EJA Fundamental (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_EJA_MEDIO` | INTEGER | Indicador de turmas exclusivas de Ed. Especial na EJA Médio (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_EJA_PROF` | INTEGER | Indicador de turmas exclusivas de Ed. Especial na EJA Profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_COMUM_PROF` | INTEGER | Indicador de turmas comuns de Educação Profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `IN_ESP_EXCLUSIVA_PROF` | INTEGER | Indicador de turmas exclusivas de Ed. Especial Profissional (1=Sim, 0=Não). — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT` | INTEGER | Quantidade de matrículas no itinerário de Formação Técnica e Profissional (Curso Técnico). — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_1` | INTEGER | Matrículas na 1ª série do Itinerário Técnico Profissionalizante. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_2` | INTEGER | Matrículas na 2ª série do Itinerário Técnico Profissionalizante. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_3` | INTEGER | Matrículas na 3ª série do Itinerário Técnico Profissionalizante. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_4` | INTEGER | Matrículas na 4ª série do Itinerário Técnico Profissionalizante. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_NS` | INTEGER | Matrículas não seriadas do Itinerário Técnico Profissionalizante. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP` | INTEGER | Matrículas do Itinerário Formativo voltadas à Qualificação Profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_1` | INTEGER | Matrículas na 1ª série do Itinerário de Qualificação Profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_2` | INTEGER | Matrículas na 2ª série do Itinerário de Qualificação Profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_3` | INTEGER | Matrículas na 3ª série do Itinerário de Qualificação Profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_4` | INTEGER | Matrículas na 4ª série do Itinerário de Qualificação Profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_NS` | INTEGER | Matrículas não seriadas do Itinerário de Qualificação Profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFA` | INTEGER | Matrículas em itinerários formativos de Aprofundamento no Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING` | INTEGER | Matrículas no itinerário de Aprofundamento em Linguagens. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING_MT` | INTEGER | Matrículas no itinerário de Linguagens e Matemática. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING_OTME` | INTEGER | Matrículas no itinerário de Linguagens e Exatas/Tecnologia. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING_OE` | INTEGER | Matrículas em Linguagens associado a outras áreas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE` | INTEGER | Matrículas no itinerário de Aprofundamento em Matemática. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE_MT` | INTEGER | Matrículas no itinerário específico de Matemática. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE_OTME` | INTEGER | Matrículas no itinerário de Matemática e Ciências da Natureza. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE_OE` | INTEGER | Matrículas em Matemática associado a outras áreas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC` | INTEGER | Matrículas no itinerário de Aprofundamento em Ciências da Natureza. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC_MT` | INTEGER | Matrículas em Ciências da Natureza integradas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC_OTME` | INTEGER | Matrículas em Ciências da Natureza e Matemática. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC_OE` | INTEGER | Matrículas em Ciências da Natureza associadas a outras áreas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA` | INTEGER | Matrículas no itinerário de Aprofundamento em Ciências Humanas e Sociais. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA_MT` | INTEGER | Matrículas em Ciências Humanas integradas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA_OTME` | INTEGER | Matrículas em Ciências Humanas e Linguagens. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA_OE` | INTEGER | Matrículas em Ciências Humanas associadas a outras áreas. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT` | INTEGER | Matrículas articuladas com itinerário técnico. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT_MT` | INTEGER | Matrículas integradas com matriz curricular técnica. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT_OTME` | INTEGER | Matrículas integradas no itinerário técnico com tecnologia. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT_OE` | INTEGER | Matrículas em outras formações articuladas técnicas. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP` | INTEGER | Matrículas articuladas com qualificação profissional de curta duração. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP_MT` | INTEGER | Matrículas integradas com qualificação profissional básica. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP_OTME` | INTEGER | Matrículas integradas com qualificação técnica tecnológica. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP_OE` | INTEGER | Matrículas articuladas de qualificação profissional diversas. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_IFTP_CT` | INTEGER | Matrículas em educação técnica atreladas aos itinerários. — descrição gerada por IA. |
| `QT_MAT_PROF_NAO_TEC` | INTEGER | Matrículas em cursos profissionalizantes de nível não técnico. — descrição gerada por IA. |
| `QT_MAT_PROF_IFTP_QP` | INTEGER | Matrículas de formação profissional de qualificação rápida. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_NPROF` | INTEGER | Matrículas na EJA Fundamental não profissionalizante. — descrição gerada por IA. |
| `QT_MAT_ESP_INF` | INTEGER | Matrículas de Educação Especial na Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_ESP_INF_CRE` | INTEGER | Matrículas de Educação Especial na Creche. — descrição gerada por IA. |
| `QT_MAT_ESP_INF_PRE` | INTEGER | Matrículas de Educação Especial na Pré-Escola. — descrição gerada por IA. |
| `QT_MAT_ESP_FUND` | INTEGER | Matrículas de Educação Especial no Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_FUND_AI` | INTEGER | Matrículas de Educação Especial no EF Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_ESP_FUND_AF` | INTEGER | Matrículas de Educação Especial no EF Anos Finais. — descrição gerada por IA. |
| `QT_MAT_ESP_MED` | INTEGER | Matrículas de Educação Especial no Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_PROF` | INTEGER | Matrículas de Educação Especial na Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_ESP_PROF_TEC` | INTEGER | Matrículas de Educação Especial no Ensino Técnico. — descrição gerada por IA. |
| `QT_MAT_ESP_EJA` | INTEGER | Matrículas de Educação Especial na EJA. — descrição gerada por IA. |
| `QT_MAT_ESP_EJA_FUND` | INTEGER | Matrículas de Educação Especial na EJA do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_EJA_MED` | INTEGER | Matrículas de Educação Especial na EJA do Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INF` | INTEGER | Matrículas de Educação Especial em classe comum na Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INF_CRE` | INTEGER | Matrículas de Educação Especial em classe comum na Creche. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INF_PRE` | INTEGER | Matrículas de Educação Especial em classe comum na Pré-Escola. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_FUND` | INTEGER | Matrículas de Educação Especial em classe comum no Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_FUND_AI` | INTEGER | Matrículas de Ed. Especial em classe comum no EF Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_FUND_AF` | INTEGER | Matrículas de Ed. Especial em classe comum no EF Anos Finais. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_MED` | INTEGER | Matrículas de Educação Especial em classe comum no Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_PROF` | INTEGER | Matrículas de Educação Especial em classe comum na Ed. Profissional. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_PROF_TEC` | INTEGER | Matrículas de Educação Especial em classe comum no Ensino Técnico. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EJA` | INTEGER | Matrículas de Educação Especial em classe comum na EJA. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EJA_FUND` | INTEGER | Matrículas de Ed. Especial em classe comum na EJA Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EJA_MED` | INTEGER | Matrículas de Ed. Especial em classe comum na EJA Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INF` | INTEGER | Matrículas de Educação Especial em classe exclusiva na Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INF_CRE` | INTEGER | Matrículas de Ed. Especial em classe exclusiva na Creche. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INF_PRE` | INTEGER | Matrículas de Ed. Especial em classe exclusiva na Pré-Escola. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_FUND` | INTEGER | Matrículas de Educação Especial em classe exclusiva no Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_FUND_AI` | INTEGER | Matrículas de Ed. Especial em classe exclusiva no EF Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_FUND_AF` | INTEGER | Matrículas de Ed. Especial em classe exclusiva no EF Anos Finais. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_MED` | INTEGER | Matrículas de Educação Especial em classe exclusiva no Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_PROF` | INTEGER | Matrículas de Ed. Especial em classe exclusiva na Ed. Profissional. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_PROF_TEC` | INTEGER | Matrículas de Ed. Especial em classe exclusiva no Ensino Técnico. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EJA` | INTEGER | Matrículas de Educação Especial em classe exclusiva na EJA. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EJA_FUND` | INTEGER | Matrículas de Ed. Especial em classe exclusiva na EJA Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EJA_MED` | INTEGER | Matrículas de Ed. Especial em classe exclusiva na EJA Médio. — descrição gerada por IA. |
| `QT_MAT_BAS_0_3_REF_31_03` | INTEGER | Matrículas de 0 a 3 anos na data de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_4_5_REF_31_03` | INTEGER | Matrículas de 4 a 5 anos na data de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_6_10_REF_31_03` | INTEGER | Matrículas de 6 a 10 anos na data de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_11_14_REF_31_03` | INTEGER | Matrículas de 11 a 14 anos na data de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_15_17_REF_31_03` | INTEGER | Matrículas de 15 a 17 anos na data de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_18_MAIS_REF_31_03` | INTEGER | Matrículas de 18 anos ou mais na data de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_DM` | INTEGER | Matrículas de alunos no turno matutino. — descrição gerada por IA. |
| `QT_MAT_BAS_DV` | INTEGER | Matrículas de alunos no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_D` | INTEGER | Matrículas de Creche no período diurno. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_DM` | INTEGER | Matrículas de Creche no turno matutino. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_DV` | INTEGER | Matrículas de Creche no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_N` | INTEGER | Matrículas de Creche no turno noturno. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_D` | INTEGER | Matrículas de Pré-Escola no período diurno. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_DM` | INTEGER | Matrículas de Pré-Escola no turno matutino. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_DV` | INTEGER | Matrículas de Pré-Escola no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_N` | INTEGER | Matrículas de Pré-Escola no turno noturno. — descrição gerada por IA. |
| `QT_MAT_FUND_D` | INTEGER | Matrículas no Ensino Fundamental no diurno. — descrição gerada por IA. |
| `QT_MAT_FUND_DM` | INTEGER | Matrículas no EF no turno matutino. — descrição gerada por IA. |
| `QT_MAT_FUND_DV` | INTEGER | Matrículas no EF no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_FUND_N` | INTEGER | Matrículas no EF no turno noturno. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_D` | INTEGER | Matrículas no EF Anos Iniciais no diurno. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_DM` | INTEGER | Matrículas no EF Anos Iniciais no turno matutino. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_DV` | INTEGER | Matrículas no EF Anos Iniciais no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_N` | INTEGER | Matrículas no EF Anos Iniciais no turno noturno. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_D` | INTEGER | Matrículas no EF Anos Finais no diurno. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_DM` | INTEGER | Matrículas no EF Anos Finais no turno matutino. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_DV` | INTEGER | Matrículas no EF Anos Finais no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_N` | INTEGER | Matrículas no EF Anos Finais no turno noturno. — descrição gerada por IA. |
| `QT_MAT_MED_D` | INTEGER | Matrículas do Ensino Médio no período diurno. — descrição gerada por IA. |
| `QT_MAT_MED_DM` | INTEGER | Matrículas do Ensino Médio no turno matutino. — descrição gerada por IA. |
| `QT_MAT_MED_DV` | INTEGER | Matrículas do Ensino Médio no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_MED_N` | INTEGER | Matrículas do Ensino Médio no turno noturno. — descrição gerada por IA. |
| `QT_MAT_MED_EAD` | INTEGER | Matrículas do Ensino Médio na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_PROF_D` | INTEGER | Matrículas de Ed. Profissional no diurno. — descrição gerada por IA. |
| `QT_MAT_PROF_DM` | INTEGER | Matrículas de Ed. Profissional no matutino. — descrição gerada por IA. |
| `QT_MAT_PROF_DV` | INTEGER | Matrículas de Ed. Profissional no vespertino. — descrição gerada por IA. |
| `QT_MAT_PROF_N` | INTEGER | Matrículas de Ed. Profissional no noturno. — descrição gerada por IA. |
| `QT_MAT_PROF_EAD` | INTEGER | Matrículas de Ed. Profissional na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_D` | INTEGER | Matrículas de Ensino Técnico no diurno. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_DM` | INTEGER | Matrículas de Ensino Técnico no matutino. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_DV` | INTEGER | Matrículas de Ensino Técnico no vespertino. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_N` | INTEGER | Matrículas de Ensino Técnico no noturno. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_EAD` | INTEGER | Matrículas de Ensino Técnico em EAD. — descrição gerada por IA. |
| `QT_MAT_EJA_D` | INTEGER | Matrículas na EJA no diurno. — descrição gerada por IA. |
| `QT_MAT_EJA_DM` | INTEGER | Matrículas na EJA no turno matutino. — descrição gerada por IA. |
| `QT_MAT_EJA_DV` | INTEGER | Matrículas na EJA no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_EJA_N` | INTEGER | Matrículas na EJA no turno noturno. — descrição gerada por IA. |
| `QT_MAT_EJA_EAD` | INTEGER | Matrículas na EJA na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_D` | INTEGER | Matrículas na EJA Fundamental no diurno. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_DM` | INTEGER | Matrículas na EJA Fundamental no matutino. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_DV` | INTEGER | Matrículas na EJA Fundamental no vespertino. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_N` | INTEGER | Matrículas na EJA Fundamental no noturno. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_EAD` | INTEGER | Matrículas na EJA Fundamental em EAD. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_D` | INTEGER | Matrículas na EJA Médio no diurno. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_DM` | INTEGER | Matrículas na EJA Médio no matutino. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_DV` | INTEGER | Matrículas na EJA Médio no vespertino. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_N` | INTEGER | Matrículas na EJA Médio no noturno. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_EAD` | INTEGER | Matrículas na EJA Médio em EAD. — descrição gerada por IA. |
| `QT_MAT_ESP_D` | INTEGER | Matrículas da Educação Especial no diurno. — descrição gerada por IA. |
| `QT_MAT_ESP_DM` | INTEGER | Matrículas da Educação Especial no matutino. — descrição gerada por IA. |
| `QT_MAT_ESP_DV` | INTEGER | Matrículas da Educação Especial no vespertino. — descrição gerada por IA. |
| `QT_MAT_ESP_N` | INTEGER | Matrículas da Educação Especial no noturno. — descrição gerada por IA. |
| `QT_MAT_ESP_EAD` | INTEGER | Matrículas da Educação Especial em EAD. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_D` | INTEGER | Matrículas de Ed. Especial em classe comum no diurno. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_DM` | INTEGER | Matrículas de Ed. Especial em classe comum no matutino. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_DV` | INTEGER | Matrículas de Ed. Especial em classe comum no vespertino. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_N` | INTEGER | Matrículas de Ed. Especial em classe comum no noturno. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EAD` | INTEGER | Matrículas de Ed. Especial em classe comum em EAD. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_D` | INTEGER | Matrículas de Ed. Especial em classe exclusiva no diurno. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_DM` | INTEGER | Matrículas de Ed. Especial em classe exclusiva no matutino. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_DV` | INTEGER | Matrículas de Ed. Especial em classe exclusiva no vespertino. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_N` | INTEGER | Matrículas de Ed. Especial em classe exclusiva no noturno. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EAD` | INTEGER | Matrículas de Ed. Especial em classe exclusiva em EAD. — descrição gerada por IA. |
| `QT_MAT_BAS_INT` | INTEGER | Quantidade total de matrículas em tempo integral na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_PROF_INT` | INTEGER | Quantidade de matrículas em tempo integral na Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_INT` | INTEGER | Quantidade de matrículas em tempo integral no Ensino Técnico. — descrição gerada por IA. |
| `QT_MAT_EJA_INT` | INTEGER | Quantidade de matrículas em tempo integral na EJA. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_INT` | INTEGER | Quantidade de matrículas em tempo integral na EJA Fundamental. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_INT` | INTEGER | Quantidade de matrículas em tempo integral na EJA Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_INT` | INTEGER | Quantidade de matrículas em tempo integral na Educação Especial. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INT` | INTEGER | Matrículas de Ed. Especial em classe comum em tempo integral. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INT` | INTEGER | Matrículas de Ed. Especial em classe exclusiva em tempo integral. — descrição gerada por IA. |
| `QT_MAT_BAS_LIBRAS` | INTEGER | Quantidade de matrículas de estudantes que utilizam LIBRAS na Educação Básica. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_1` | INTEGER | Docentes atuando no 1º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_2` | INTEGER | Docentes atuando no 2º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_3` | INTEGER | Docentes atuando no 3º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_4` | INTEGER | Docentes atuando no 4º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_5` | INTEGER | Docentes atuando no 5º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AI_MULTIETAPA` | INTEGER | Docentes em turmas multietapa do EF Anos Iniciais. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_6` | INTEGER | Docentes atuando no 6º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_7` | INTEGER | Docentes atuando no 7º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_8` | INTEGER | Docentes atuando no 8º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_9` | INTEGER | Docentes atuando no 9º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_MULTI` | INTEGER | Docentes em turmas multietapa do EF Anos Finais. — descrição gerada por IA. |
| `QT_DOC_FUND_AF_CORRFLUXO` | INTEGER | Docentes em turmas de correção de fluxo no EF Anos Finais. — descrição gerada por IA. |
| `QT_DOC_MED_PROP` | INTEGER | Docentes do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_1` | INTEGER | Docentes atuando na 1ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_2` | INTEGER | Docentes atuando na 2ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_3` | INTEGER | Docentes atuando na 3ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_4` | INTEGER | Docentes atuando na 4ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_DOC_MED_PROP_NS` | INTEGER | Docentes do Ensino Médio propedêutico não seriado. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT` | INTEGER | Docentes no itinerário de formação técnica do Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_1` | INTEGER | Docentes na 1ª série de itinerário técnico. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_2` | INTEGER | Docentes na 2ª série de itinerário técnico. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_3` | INTEGER | Docentes na 3ª série de itinerário técnico. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_4` | INTEGER | Docentes na 4ª série de itinerário técnico. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_CT_NS` | INTEGER | Docentes em itinerário técnico não seriado. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP` | INTEGER | Docentes em itinerário de qualificação profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_1` | INTEGER | Docentes na 1ª série de qualificação profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_2` | INTEGER | Docentes na 2ª série de qualificação profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_3` | INTEGER | Docentes na 3ª série de qualificação profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_4` | INTEGER | Docentes na 4ª série de qualificação profissional. — descrição gerada por IA. |
| `QT_DOC_MED_IFTP_QP_NS` | INTEGER | Docentes em qualificação profissional não seriada. — descrição gerada por IA. |
| `QT_DOC_MED_NM` | INTEGER | Docentes no Ensino Médio Normal/Magistério. — descrição gerada por IA. |
| `QT_DOC_MED_NM_1` | INTEGER | Docentes na 1ª série do Magistério. — descrição gerada por IA. |
| `QT_DOC_MED_NM_2` | INTEGER | Docentes na 2ª série do Magistério. — descrição gerada por IA. |
| `QT_DOC_MED_NM_3` | INTEGER | Docentes na 3ª série do Magistério. — descrição gerada por IA. |
| `QT_DOC_MED_NM_4` | INTEGER | Docentes na 4ª série do Magistério. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC_CONC` | INTEGER | Docentes do Ensino Técnico concomitante. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC_SUBS` | INTEGER | Docentes do Ensino Técnico subsequente. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC_MISTO` | INTEGER | Docentes atuando em turmas mistas de ensino técnico. — descrição gerada por IA. |
| `QT_DOC_PROF_TEC_IFTP_CT` | INTEGER | Docentes do itinerário de formação técnica e profissional. — descrição gerada por IA. |
| `QT_DOC_PROF_NAO_TEC` | INTEGER | Docentes em cursos de formação inicial/continuada (não técnicos). — descrição gerada por IA. |
| `QT_DOC_PROF_IFTP_QP` | INTEGER | Docentes em qualificação profissional técnica. — descrição gerada por IA. |
| `QT_DOC_PROF_FIC_CONC` | INTEGER | Docentes em cursos FIC concomitantes. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND_NPROF` | INTEGER | Docentes da EJA Fundamental não profissional. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND_AI` | INTEGER | Docentes da EJA Fundamental - Anos Iniciais. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND_AF` | INTEGER | Docentes da EJA Fundamental - Anos Finais. — descrição gerada por IA. |
| `QT_DOC_EJA_FUND_FIC` | INTEGER | Docentes da EJA Fundamental com qualificação profissional. — descrição gerada por IA. |
| `QT_DOC_EJA_MED_NPROF` | INTEGER | Docentes da EJA Médio não profissional. — descrição gerada por IA. |
| `QT_DOC_EJA_MED_FIC` | INTEGER | Docentes da EJA Médio com qualificação profissional. — descrição gerada por IA. |
| `QT_DOC_EJA_MED_TEC` | INTEGER | Docentes da EJA Médio integrada à Educação Técnica. — descrição gerada por IA. |
| `QT_DOC_BAS_FEM` | INTEGER | Quantidade de docentes do sexo feminino. — descrição gerada por IA. |
| `QT_DOC_BAS_MASC` | INTEGER | Quantidade de docentes do sexo masculino. — descrição gerada por IA. |
| `QT_DOC_BAS_ND` | INTEGER | Quantidade de docentes sem sexo declarado. — descrição gerada por IA. |
| `QT_DOC_BAS_BRANCA` | INTEGER | Docentes de cor/raça branca. — descrição gerada por IA. |
| `QT_DOC_BAS_PRETA` | INTEGER | Docentes de cor/raça preta. — descrição gerada por IA. |
| `QT_DOC_BAS_PARDA` | INTEGER | Docentes de cor/raça parda. — descrição gerada por IA. |
| `QT_DOC_BAS_AMARELA` | INTEGER | Docentes de cor/raça amarela. — descrição gerada por IA. |
| `QT_DOC_BAS_INDIGENA` | INTEGER | Docentes de cor/raça indígena. — descrição gerada por IA. |
| `QT_DOC_BAS_0_24` | INTEGER | Docentes até 24 anos de idade. — descrição gerada por IA. |
| `QT_DOC_BAS_25_29` | INTEGER | Docentes de 25 a 29 anos de idade. — descrição gerada por IA. |
| `QT_DOC_BAS_30_39` | INTEGER | Docentes de 30 a 39 anos de idade. — descrição gerada por IA. |
| `QT_DOC_BAS_40_49` | INTEGER | Docentes de 40 a 49 anos de idade. — descrição gerada por IA. |
| `QT_DOC_BAS_50_54` | INTEGER | Docentes de 50 a 54 anos de idade. — descrição gerada por IA. |
| `QT_DOC_BAS_55_59` | INTEGER | Docentes de 55 a 59 anos de idade. — descrição gerada por IA. |
| `QT_DOC_BAS_60_MAIS` | INTEGER | Docentes com 60 anos ou mais. — descrição gerada por IA. |
| `QT_DOC_BAS_PCD` | INTEGER | Quantidade de docentes com deficiência (PCD). — descrição gerada por IA. |
| `QT_DOC_BAS_ZR_URB` | INTEGER | Docentes residentes em zona urbana. — descrição gerada por IA. |
| `QT_DOC_BAS_ZR_RUR` | INTEGER | Docentes residentes em zona rural. — descrição gerada por IA. |
| `QT_DOC_BAS_ZR_NA` | INTEGER | Docentes com zona de residência não informada. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_EF` | INTEGER | Docentes com escolaridade até o Ensino Fundamental. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_EM` | INTEGER | Docentes com escolaridade até o Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_GRAD` | INTEGER | Docentes com curso superior concluído (Graduação). — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_GRAD_LICEN` | INTEGER | Docentes com Licenciatura concluída. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_GRAD_SLICEN` | INTEGER | Docentes com Bacharelado/Graduação sem Licenciatura. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_POS_ESPEC` | INTEGER | Docentes com pós-graduação lato sensu (Especialização). — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_POS_MESTRA` | INTEGER | Docentes com Mestrado concluído. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_POS_DOUTO` | INTEGER | Docentes com Doutorado concluído. — descrição gerada por IA. |
| `QT_DOC_BAS_ESCO_SUP_POS_NENHUM` | INTEGER | Docentes graduados sem pós-graduação. — descrição gerada por IA. |
| `QT_DOC_BAS_VINCULO_CONCUR` | INTEGER | Docentes concursados/efetivos. — descrição gerada por IA. |
| `QT_DOC_BAS_VINCULO_CONTRA` | INTEGER | Docentes contratados por tempo determinado/temporários. — descrição gerada por IA. |
| `QT_DOC_BAS_VINCULO_TERCEIR` | INTEGER | Docentes terceirizados. — descrição gerada por IA. |
| `QT_DOC_BAS_VINCULO_CLT` | INTEGER | Docentes contratados via CLT. — descrição gerada por IA. |
| `QT_DOC_BAS_DOCENTE` | INTEGER | Quantidade de profissionais exercendo função docente titular. — descrição gerada por IA. |
| `QT_DOC_BAS_AUXILIAR` | INTEGER | Quantidade de auxiliares de sala/docentes assistentes. — descrição gerada por IA. |
| `QT_DOC_BAS_PROFI_MONITOR` | INTEGER | Quantidade de monitores pedagógicos. — descrição gerada por IA. |
| `QT_DOC_BAS_TRADUTOR_LIBRAS` | INTEGER | Quantidade de docentes atuando como tradutores de LIBRAS. — descrição gerada por IA. |
| `QT_DOC_BAS_TITULAR_EAD` | INTEGER | Quantidade de docentes titulares na modalidade EAD. — descrição gerada por IA. |
| `QT_DOC_BAS_TUTOR_AUX_EAD` | INTEGER | Quantidade de tutores/auxiliares EAD. — descrição gerada por IA. |
| `QT_DOC_BAS_GUIA_INTERPRETE` | INTEGER | Quantidade de docentes guias-intérpretes. — descrição gerada por IA. |
| `QT_DOC_BAS_APOIO_PCD` | INTEGER | Docentes de apoio especializado para alunos PCD. — descrição gerada por IA. |
| `QT_DOC_BAS_INSTRUTOR_EP` | INTEGER | Instrutores da Educação Profissional. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_CRE` | INTEGER | Docentes especializados em Creche. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_PRE_ESCOLA` | INTEGER | Docentes especializados em Pré-Escola. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ANOS_INICIAIS` | INTEGER | Docentes especializados nos Anos Iniciais do EF. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ANOS_FINAIS` | INTEGER | Docentes especializados nos Anos Finais do EF. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ENS_MEDIO` | INTEGER | Docentes especializados no Ensino Médio. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_EJA` | INTEGER | Docentes especializados na Educação de Jovens e Adultos. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ED_ESPECIAL` | INTEGER | Docentes especializados em Educação Especial. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_BIL_SURDOS` | INTEGER | Docentes especializados em Educação Bilingue para Surdos. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_ED_INDIGENA` | INTEGER | Docentes especializados em Educação Indígena. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_CAMPO` | INTEGER | Docentes especializados em Educação do Campo. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_AMBIENTAL` | INTEGER | Docentes especializados em Educação Ambiental. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_DIR_HUMANOS` | INTEGER | Docentes especializados em Direitos Humanos. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_DIV_SEXUAL` | INTEGER | Docentes especializados em Diversidade Sexual/Gênero. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_DIR_ADOLESC` | INTEGER | Docentes especializados em Direitos da Criança e do Adolescente. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_AFRO` | INTEGER | Docentes especializados em História e Cultura Afro-Brasileira. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_GESTAO` | INTEGER | Docentes especializados em Gestão Escolar. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_EDUC_TIC` | INTEGER | Docentes especializados no uso de tecnologias digitais (TICs). — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_OUTROS` | INTEGER | Docentes com outras especializações específicas. — descrição gerada por IA. |
| `QT_DOC_BAS_ESPEC_NENHUM` | INTEGER | Docentes sem cursos de especialização continuada. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_PORT` | INTEGER | Docentes que lecionam Língua Portuguesa. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_EDUC_FISICA` | INTEGER | Docentes que lecionam Educação Física. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_ARTES` | INTEGER | Docentes que lecionam Artes. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_ING` | INTEGER | Docentes que lecionam Língua Inglesa. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_ESPA` | INTEGER | Docentes que lecionam Língua Espanhola. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_FRANC` | INTEGER | Docentes que lecionam Língua Francesa. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_OUTRA` | INTEGER | Docentes que lecionam outras línguas estrangeiras. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LIBRAS` | INTEGER | Docentes que lecionam a disciplina de LIBRAS. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_LINGUA_INDIG` | INTEGER | Docentes que lecionam Língua Indígena. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_PORT_SEG_LINGUA` | INTEGER | Docentes lecionando Português como segunda língua. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_MATEMATICA` | INTEGER | Docentes que lecionam Matemática. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_CIENCIAS` | INTEGER | Docentes que lecionam Ciências. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_FISICA` | INTEGER | Docentes que lecionam Física. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_QUIMICA` | INTEGER | Docentes que lecionam Química. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_BIOLOGIA` | INTEGER | Docentes que lecionam Biologia. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_HISTORIA` | INTEGER | Docentes que lecionam História. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_GEOGRAFIA` | INTEGER | Docentes que lecionam Geografia. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_SOCIOLOGIA` | INTEGER | Docentes que lecionam Sociologia. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_FILOSOFIA` | INTEGER | Docentes que lecionam Filosofia. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_EST_SOCIAIS` | INTEGER | Docentes lecionando Estudos Sociais. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_EST_SOCIAIS_SOCI` | INTEGER | Docentes lecionando Estudos Sociais/Sociologia integrados. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_INFO_COMPUTACAO` | INTEGER | Docentes lecionando Informática e Computação. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_ENSINO_RELIGIOSO` | INTEGER | Docentes lecionando Ensino Religioso. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_PROFISSIONA` | INTEGER | Docentes lecionando disciplinas da Formação Profissional. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_ESTAGIO_SUPER` | INTEGER | Docentes lecionando/supervisionando Estágio Supervisionado. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_PEDAGOGICAS` | INTEGER | Docentes lecionando disciplinas Pedagógicas. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_PROJETO_DE_VIDA` | INTEGER | Docentes lecionando a componente de Projeto de Vida. — descrição gerada por IA. |
| `QT_DOC_BAS_DISC_OUTRAS` | INTEGER | Docentes lecionando outras disciplinas curriculares. — descrição gerada por IA. |
| `QT_DOC_BAS_LIBRAS` | INTEGER | Quantidade total de docentes lecionando em LIBRAS. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_1` | INTEGER | Quantidade de turmas no 1º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_2` | INTEGER | Quantidade de turmas no 2º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_3` | INTEGER | Quantidade de turmas no 3º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_4` | INTEGER | Quantidade de turmas no 4º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_5` | INTEGER | Quantidade de turmas no 5º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_MULTIETAPA` | INTEGER | Quantidade de turmas multietapa nos Anos Iniciais do EF. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_6` | INTEGER | Quantidade de turmas no 6º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_7` | INTEGER | Quantidade de turmas no 7º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_8` | INTEGER | Quantidade de turmas no 8º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_9` | INTEGER | Quantidade de turmas no 9º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_MULTI` | INTEGER | Quantidade de turmas multietapa nos Anos Finais do EF. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_CORRFLUXO` | INTEGER | Turmas de correção de fluxo (aceleração) nos Anos Finais. — descrição gerada por IA. |
| `QT_TUR_MED_PROP` | INTEGER | Turmas de Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_1` | INTEGER | Turmas da 1ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_2` | INTEGER | Turmas da 2ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_3` | INTEGER | Turmas da 3ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_4` | INTEGER | Turmas da 4ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_NS` | INTEGER | Turmas não seriadas do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT` | INTEGER | Turmas de Ensino Médio no itinerário de formação técnica. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_1` | INTEGER | Turmas de 1ª série em itinerários técnicos. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_2` | INTEGER | Turmas de 2ª série em itinerários técnicos. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_3` | INTEGER | Turmas de 3ª série em itinerários técnicos. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_4` | INTEGER | Turmas de 4ª série em itinerários técnicos. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_NS` | INTEGER | Turmas não seriadas em itinerários técnicos. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP` | INTEGER | Turmas do Ensino Médio com foco em qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_1` | INTEGER | Turmas de 1ª série de qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_2` | INTEGER | Turmas de 2ª série de qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_3` | INTEGER | Turmas de 3ª série de qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_4` | INTEGER | Turmas de 4ª série de qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_NS` | INTEGER | Turmas não seriadas de qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_NM` | INTEGER | Turmas de Ensino Médio Magistério/Normal. — descrição gerada por IA. |
| `QT_TUR_MED_NM_1` | INTEGER | Turmas da 1ª série do Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_2` | INTEGER | Turmas da 2ª série do Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_3` | INTEGER | Turmas da 3ª série do Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_4` | INTEGER | Turmas da 4ª série do Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_EXC` | INTEGER | Turmas exclusivas para Aprofundamento no Novo Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_EXC` | INTEGER | Turmas exclusivas do itinerário de Formação Técnica. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_EXC_QP` | INTEGER | Turmas exclusivas de Qualificação Profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFA` | INTEGER | Turmas com itinerários formativos de aprofundamento. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_LING` | INTEGER | Turmas com aprofundamento na área de Linguagens. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_MATE` | INTEGER | Turmas com aprofundamento na área de Matemática. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_CIENC` | INTEGER | Turmas com aprofundamento em Ciências da Natureza. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_HUMA` | INTEGER | Turmas com aprofundamento em Ciências Humanas e Sociais. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_CONC` | INTEGER | Turmas de Ensino Técnico concomitante. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_SUBS` | INTEGER | Turmas de Ensino Técnico subsequente. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_MISTO` | INTEGER | Turmas mistas de Ensino Técnico. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_IFTP_CT` | INTEGER | Turmas de formação técnica associada ao itinerário formativo. — descrição gerada por IA. |
| `QT_TUR_PROF_NAO_TEC` | INTEGER | Turmas de formação profissional de nível não técnico. — descrição gerada por IA. |
| `QT_TUR_PROF_IFTP_QP` | INTEGER | Turmas de qualificação profissional acelerada. — descrição gerada por IA. |
| `QT_TUR_PROF_FIC_CONC` | INTEGER | Turmas de cursos FIC concomitantes. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_NPROF` | INTEGER | Turmas da EJA Fundamental regular (sem qualificação profissional). — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_AI` | INTEGER | Turmas da EJA Fundamental - Anos Iniciais. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_AF` | INTEGER | Turmas da EJA Fundamental - Anos Finais. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_FIC` | INTEGER | Turmas da EJA Fundamental integradas com FIC. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_NPROF` | INTEGER | Turmas da EJA Médio regular (sem formação profissional). — descrição gerada por IA. |
| `QT_TUR_EJA_MED_FIC` | INTEGER | Turmas da EJA Médio com qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_TEC` | INTEGER | Turmas da EJA Médio com habilitação técnica. — descrição gerada por IA. |
| `QT_TUR_BAS_DM` | INTEGER | Turmas da Educação Básica no turno matutino. — descrição gerada por IA. |
| `QT_TUR_BAS_DV` | INTEGER | Turmas da Educação Básica no turno vespertino. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_D` | INTEGER | Turmas de Creche no diurno. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_DM` | INTEGER | Turmas de Creche no matutino. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_DV` | INTEGER | Turmas de Creche no vespertino. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_N` | INTEGER | Turmas de Creche no noturno. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_D` | INTEGER | Turmas de Pré-Escola no diurno. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_DM` | INTEGER | Turmas de Pré-Escola no matutino. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_DV` | INTEGER | Turmas de Pré-Escola no vespertino. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_N` | INTEGER | Turmas de Pré-Escola no noturno. — descrição gerada por IA. |
| `QT_TUR_FUND_D` | INTEGER | Turmas de Ensino Fundamental no diurno. — descrição gerada por IA. |
| `QT_TUR_FUND_DM` | INTEGER | Turmas de Ensino Fundamental no matutino. — descrição gerada por IA. |
| `QT_TUR_FUND_DV` | INTEGER | Turmas de Ensino Fundamental no vespertino. — descrição gerada por IA. |
| `QT_TUR_FUND_N` | INTEGER | Turmas de Ensino Fundamental no noturno. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_D` | INTEGER | Turmas do EF Anos Iniciais no diurno. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_DM` | INTEGER | Turmas do EF Anos Iniciais no matutino. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_DV` | INTEGER | Turmas do EF Anos Iniciais no vespertino. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_N` | INTEGER | Turmas do EF Anos Iniciais no noturno. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_D` | INTEGER | Turmas do EF Anos Finais no diurno. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_DM` | INTEGER | Turmas do EF Anos Finais no matutino. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_DV` | INTEGER | Turmas do EF Anos Finais no vespertino. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_N` | INTEGER | Turmas do EF Anos Finais no noturno. — descrição gerada por IA. |
| `QT_TUR_MED_D` | INTEGER | Turmas do Ensino Médio no diurno. — descrição gerada por IA. |
| `QT_TUR_MED_DM` | INTEGER | Turmas do Ensino Médio no matutino. — descrição gerada por IA. |
| `QT_TUR_MED_DV` | INTEGER | Turmas do Ensino Médio no vespertino. — descrição gerada por IA. |
| `QT_TUR_MED_N` | INTEGER | Turmas do Ensino Médio no noturno. — descrição gerada por IA. |
| `QT_TUR_MED_EAD` | INTEGER | Turmas do Ensino Médio em EAD. — descrição gerada por IA. |
| `QT_TUR_PROF_D` | INTEGER | Turmas de Ed. Profissional no diurno. — descrição gerada por IA. |
| `QT_TUR_PROF_DM` | INTEGER | Turmas de Ed. Profissional no matutino. — descrição gerada por IA. |
| `QT_TUR_PROF_DV` | INTEGER | Turmas de Ed. Profissional no vespertino. — descrição gerada por IA. |
| `QT_TUR_PROF_N` | INTEGER | Turmas de Ed. Profissional no noturno. — descrição gerada por IA. |
| `QT_TUR_PROF_EAD` | INTEGER | Turmas de Ed. Profissional em EAD. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_D` | INTEGER | Turmas de Ensino Técnico no diurno. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_DM` | INTEGER | Turmas de Ensino Técnico no matutino. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_DV` | INTEGER | Turmas de Ensino Técnico no vespertino. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_N` | INTEGER | Turmas de Ensino Técnico no noturno. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_EAD` | INTEGER | Turmas de Ensino Técnico em EAD. — descrição gerada por IA. |
| `QT_TUR_EJA_D` | INTEGER | Turmas da EJA no diurno. — descrição gerada por IA. |
| `QT_TUR_EJA_DM` | INTEGER | Turmas da EJA no matutino. — descrição gerada por IA. |
| `QT_TUR_EJA_DV` | INTEGER | Turmas da EJA no vespertino. — descrição gerada por IA. |
| `QT_TUR_EJA_N` | INTEGER | Turmas da EJA no noturno. — descrição gerada por IA. |
| `QT_TUR_EJA_EAD` | INTEGER | Turmas da EJA em EAD. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_D` | INTEGER | Turmas da EJA Fundamental no diurno. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_DM` | INTEGER | Turmas da EJA Fundamental no matutino. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_DV` | INTEGER | Turmas da EJA Fundamental no vespertino. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_N` | INTEGER | Turmas da EJA Fundamental no noturno. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_EAD` | INTEGER | Turmas da EJA Fundamental em EAD. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_D` | INTEGER | Turmas da EJA Médio no diurno. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_DM` | INTEGER | Turmas da EJA Médio no matutino. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_DV` | INTEGER | Turmas da EJA Médio no vespertino. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_N` | INTEGER | Turmas da EJA Médio no noturno. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_EAD` | INTEGER | Turmas da EJA Médio em EAD. — descrição gerada por IA. |
| `QT_TUR_ESP_D` | INTEGER | Turmas de Educação Especial no diurno. — descrição gerada por IA. |
| `QT_TUR_ESP_DM` | INTEGER | Turmas de Educação Especial no matutino. — descrição gerada por IA. |
| `QT_TUR_ESP_DV` | INTEGER | Turmas de Educação Especial no vespertino. — descrição gerada por IA. |
| `QT_TUR_ESP_N` | INTEGER | Turmas de Educação Especial no noturno. — descrição gerada por IA. |
| `QT_TUR_ESP_EAD` | INTEGER | Turmas de Educação Especial em EAD. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_D` | INTEGER | Turmas de Ed. Especial em classe comum no diurno. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_DM` | INTEGER | Turmas de Ed. Especial em classe comum no matutino. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_DV` | INTEGER | Turmas de Ed. Especial em classe comum no vespertino. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_N` | INTEGER | Turmas de Ed. Especial em classe comum no noturno. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_EAD` | INTEGER | Turmas de Ed. Especial em classe comum em EAD. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_D` | INTEGER | Turmas de Ed. Especial em classe exclusiva no diurno. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_DM` | INTEGER | Turmas de Ed. Especial em classe exclusiva no matutino. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_DV` | INTEGER | Turmas de Ed. Especial em classe exclusiva no vespertino. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_N` | INTEGER | Turmas de Ed. Especial em classe exclusiva no noturno. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_EAD` | INTEGER | Turmas de Ed. Especial em classe exclusiva em EAD. — descrição gerada por IA. |
| `QT_TUR_BAS_INT` | INTEGER | Quantidade total de turmas em tempo integral da Educação Básica. — descrição gerada por IA. |
| `QT_TUR_PROF_INT` | INTEGER | Turmas em tempo integral na Educação Profissional. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_INT` | INTEGER | Turmas em tempo integral no Ensino Técnico. — descrição gerada por IA. |
| `QT_TUR_EJA_INT` | INTEGER | Turmas em tempo integral na EJA. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_INT` | INTEGER | Turmas em tempo integral na EJA Fundamental. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_INT` | INTEGER | Turmas em tempo integral na EJA Médio. — descrição gerada por IA. |
| `QT_TUR_ESP_INT` | INTEGER | Turmas em tempo integral na Educação Especial. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_INT` | INTEGER | Turmas de Ed. Especial em classe comum em tempo integral. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_INT` | INTEGER | Turmas de Ed. Especial em classe exclusiva em tempo integral. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_PORT` | INTEGER | Turmas com oferta da disciplina de Língua Portuguesa. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_EDUC_FISICA` | INTEGER | Turmas com oferta da disciplina de Educação Física. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_ARTES` | INTEGER | Turmas com oferta da disciplina de Artes. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_ING` | INTEGER | Turmas com oferta da disciplina de Língua Inglesa. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_ESPA` | INTEGER | Turmas com oferta da disciplina de Língua Espanhola. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_FRANC` | INTEGER | Turmas com oferta da disciplina de Língua Francesa. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_OUTRA` | INTEGER | Turmas com oferta de outras línguas estrangeiras. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LIBRAS` | INTEGER | Turmas com oferta da disciplina de LIBRAS. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_INDIG` | INTEGER | Turmas com oferta da disciplina de Língua Indígena. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PORT_SEG_LINGUA` | INTEGER | Turmas com Português como Segunda Língua. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_MATEMATICA` | INTEGER | Turmas com oferta da disciplina de Matemática. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_CIENCIAS` | INTEGER | Turmas com oferta da disciplina de Ciências. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_FISICA` | INTEGER | Turmas com oferta da disciplina de Física. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_QUIMICA` | INTEGER | Turmas com oferta da disciplina de Química. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_BIOLOGIA` | INTEGER | Turmas com oferta da disciplina de Biologia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_HISTORIA` | INTEGER | Turmas com oferta da disciplina de História. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_GEOGRAFIA` | INTEGER | Turmas com oferta da disciplina de Geografia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_SOCIOLOGIA` | INTEGER | Turmas com oferta da disciplina de Sociologia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_FILOSOFIA` | INTEGER | Turmas com oferta da disciplina de Filosofia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_EST_SOCIAIS` | INTEGER | Turmas com oferta da disciplina de Estudos Sociais. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_EST_SOCIAIS_SOCI` | INTEGER | Turmas com oferta de Estudos Sociais/Sociologia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_INFO_COMPUTACAO` | INTEGER | Turmas com oferta de Informática/Computação. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_ENSINO_RELIGIOSO` | INTEGER | Turmas com oferta de Ensino Religioso. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PROFISSIONA` | INTEGER | Turmas com oferta de disciplinas da formação profissional. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_ESTAGIO_SUPER` | INTEGER | Turmas com acompanhamento de Estágio Supervisionado. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PEDAGOGICAS` | INTEGER | Turmas com disciplinas pedagógicas. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PROJETO_DE_VIDA` | INTEGER | Turmas com a componente curricular de Projeto de Vida. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_OUTRAS` | INTEGER | Turmas com oferta de outras disciplinas específicas. — descrição gerada por IA. |
| `QT_TUR_BAS_LIBRAS` | INTEGER | Quantidade total de turmas com ensino ministrado em LIBRAS. — descrição gerada por IA. |

## trusted · inep_censo_escolar_gestores

File `trusted__inep_censo_escolar_gestores.parquet` · 4,239,004 rows · 69 columns

TRUSTED - Métricas agregadas de gestores escolares por escola/ano, sexo, raça/cor, escolaridade e formação. Sem filtros que removam registros. Anos cobertos pelas fontes: 2007-2025 (2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025).

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | INTEGER | Ano de realização do Censo Escolar (formato YYYY). — descrição gerada por IA. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `CO_ENTIDADE` | INTEGER | Código do estabelecimento de ensino no cadastro do INEP/Censo Escolar. — descrição gerada por IA. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `QT_GEST_BAS` | INTEGER | Quantidade total de gestores escolares na Educação Básica na escola. — descrição gerada por IA. |
| `QT_GEST_BAS_FEM` | INTEGER | Quantidade de gestores do sexo feminino. — descrição gerada por IA. |
| `QT_GEST_BAS_MASC` | INTEGER | Quantidade de gestores do sexo masculino. — descrição gerada por IA. |
| `QT_GEST_BAS_ND` | INTEGER | Quantidade de gestores com sexo não declarado. — descrição gerada por IA. |
| `QT_GEST_BAS_BRANCA` | INTEGER | Quantidade de gestores de cor ou raça branca. — descrição gerada por IA. |
| `QT_GEST_BAS_PRETA` | INTEGER | Quantidade de gestores de cor ou raça preta. — descrição gerada por IA. |
| `QT_GEST_BAS_PARDA` | INTEGER | Quantidade de gestores de cor ou raça parda. — descrição gerada por IA. |
| `QT_GEST_BAS_AMARELA` | INTEGER | Quantidade de gestores de cor ou raça amarela. — descrição gerada por IA. |
| `QT_GEST_BAS_INDIGENA` | INTEGER | Quantidade de gestores de cor ou raça indígena. — descrição gerada por IA. |
| `QT_GEST_BAS_NACIO_BRASILEIRA` | INTEGER | Quantidade de gestores de nacionalidade brasileira. — descrição gerada por IA. |
| `QT_GEST_BAS_NACIO_ESTRANG` | INTEGER | Quantidade de gestores de nacionalidade estrangeira. — descrição gerada por IA. |
| `QT_GEST_BAS_0_24` | INTEGER | Quantidade de gestores na faixa etária até 24 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_25_29` | INTEGER | Quantidade de gestores na faixa etária de 25 a 29 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_30_39` | INTEGER | Quantidade de gestores na faixa etária de 30 a 39 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_40_49` | INTEGER | Quantidade de gestores na faixa etária de 40 a 49 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_50_54` | INTEGER | Quantidade de gestores na faixa etária de 50 a 54 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_55_59` | INTEGER | Quantidade de gestores na faixa etária de 55 a 59 anos. — descrição gerada por IA. |
| `QT_GEST_BAS_60_MAIS` | INTEGER | Quantidade de gestores na faixa etária de 60 anos ou mais. — descrição gerada por IA. |
| `QT_GEST_BAS_PCD` | INTEGER | Quantidade de gestores com deficiência (PCD). — descrição gerada por IA. |
| `QT_GEST_BAS_ZR_URB` | INTEGER | Quantidade de gestores com residência em zona urbana. — descrição gerada por IA. |
| `QT_GEST_BAS_ZR_RUR` | INTEGER | Quantidade de gestores com residência em zona rural. — descrição gerada por IA. |
| `QT_GEST_BAS_ZR_NA` | INTEGER | Quantidade de gestores cuja zona de residência não se aplica ou não foi informada. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_EF` | INTEGER | Quantidade de gestores com nível de escolaridade até o Ensino Fundamental. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_EM` | INTEGER | Quantidade de gestores com nível de escolaridade Ensino Médio. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_GRAD` | INTEGER | Quantidade de gestores com curso de graduação superior completo. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_GRAD_LICEN` | INTEGER | Quantidade de gestores com graduação superior com licenciatura. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_GRAD_SLICEN` | INTEGER | Quantidade de gestores com graduação superior sem licenciatura (bacharelado/tecnólogo). — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_POS_ESPEC` | INTEGER | Quantidade de gestores com pós-graduação no nível de especialização. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_POS_MESTRA` | INTEGER | Quantidade de gestores com pós-graduação no nível de mestrado. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_POS_DOUTO` | INTEGER | Quantidade de gestores com pós-graduação no nível de doutorado. — descrição gerada por IA. |
| `QT_GEST_BAS_ESCO_SUP_POS_NENHUM` | INTEGER | Quantidade de gestores com curso superior que não possuem pós-graduação. — descrição gerada por IA. |
| `QT_GEST_BAS_VINCULO_CONCUR` | INTEGER | Quantidade de gestores com vínculo por concurso público (efetivos). — descrição gerada por IA. |
| `QT_GEST_BAS_VINCULO_CONTRA` | INTEGER | Quantidade de gestores com vínculo por contrato temporário/militar/outros. — descrição gerada por IA. |
| `QT_GEST_BAS_VINCULO_TERCEIR` | INTEGER | Quantidade de gestores com vínculo terceirizado. — descrição gerada por IA. |
| `QT_GEST_BAS_VINCULO_CLT` | INTEGER | Quantidade de gestores com vínculo consolidado pelas leis do trabalho (CLT). — descrição gerada por IA. |
| `QT_GEST_BAS_DIRETOR` | INTEGER | Quantidade de gestores que exercem a função de diretor. — descrição gerada por IA. |
| `QT_GEST_BAS_OUTRO` | INTEGER | Quantidade de gestores em outras funções de gestão escolar. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_PROP` | INTEGER | Quantidade de gestores que acessaram o cargo por serem proprietários ou sócios da escola. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_INDIC` | INTEGER | Quantidade de gestores que acessaram o cargo por indicação. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_SEL` | INTEGER | Quantidade de gestores que acessaram o cargo por processo seletivo simplificado. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_CONC` | INTEGER | Quantidade de gestores que acessaram o cargo por concurso público. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_ELEIC` | INTEGER | Quantidade de gestores que acessaram o cargo exclusivamente por eleição da comunidade escolar. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_P_SEL` | INTEGER | Quantidade de gestores que acessaram o cargo por processo seletivo e eleição. — descrição gerada por IA. |
| `QT_GEST_BAS_ACESSO_CARGO_OUTRO` | INTEGER | Quantidade de gestores que acessaram o cargo por outro tipo de processo. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_CRE` | INTEGER | Quantidade de gestores com formação continuada específica para creche. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_PRE_ESCOLA` | INTEGER | Quantidade de gestores com formação continuada específica para pré-escola. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ANOS_INICIAIS` | INTEGER | Quantidade de gestores com formação continuada específica para os anos iniciais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ANOS_FINAIS` | INTEGER | Quantidade de gestores com formação continuada específica para os anos finais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ENS_MEDIO` | INTEGER | Quantidade de gestores com formação continuada específica para o Ensino Médio. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_EJA` | INTEGER | Quantidade de gestores com formação continuada específica para Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ED_ESPECIAL` | INTEGER | Quantidade de gestores com formação continuada específica para Educação Especial. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_BIL_SURDOS` | INTEGER | Quantidade de gestores com formação continuada específica em Educação Bilíngue de Surdos. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_ED_INDIGENA` | INTEGER | Quantidade de gestores com formação continuada específica para Educação Indígena. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_CAMPO` | INTEGER | Quantidade de gestores com formação continuada específica para Educação do Campo. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_AMBIENTAL` | INTEGER | Quantidade de gestores com formação continuada em Educação Ambiental. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_DIR_HUMANOS` | INTEGER | Quantidade de gestores com formação continuada em Direitos Humanos. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_DIV_SEXUAL` | INTEGER | Quantidade de gestores com formação continuada em Gênero e Diversidade Sexual. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_DIR_ADOLESC` | INTEGER | Quantidade de gestores com formação continuada em Direitos de Crianças e Adolescentes. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_AFRO` | INTEGER | Quantidade de gestores com formação continuada em Educação das Relações Étnico-Raciais e História/Cultura Afro-Brasileira. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_GESTAO` | INTEGER | Quantidade de gestores com formação continuada em Gestão Escolar. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_EDUC_TIC` | INTEGER | Quantidade de gestores com formação continuada em Uso de Tecnologias da Informação e Comunicação. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_OUTROS` | INTEGER | Quantidade de gestores com formação continuada em outras áreas. — descrição gerada por IA. |
| `QT_GEST_BAS_ESPEC_NENHUM` | INTEGER | Quantidade de gestores que não possuem formação continuada específica para a função. — descrição gerada por IA. |

## trusted · inep_censo_escolar_infraestrutura

File `trusted__inep_censo_escolar_infraestrutura.parquet` · 7,376,443 rows · 134 columns

TRUSTED - Infraestrutura escolar, dependências físicas, equipamentos, conectividade, acessibilidade, água, energia, esgoto e recursos pedagógicos. Sem filtros que removam registros. Anos cobertos pelas fontes: 1995-2025 (1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025).

**Built from:** `raw/inep_censo_escolar_escola`

**Feeds:** `semantic/obt_inep_censo_infraestrutura_escola`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | INTEGER | Ano de referência da coleta do Censo Escolar (formato YYYY). — descrição gerada por IA. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `CO_ENTIDADE` | INTEGER | Código de identificação único da escola no INEP. — descrição gerada por IA. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `IN_LOCAL_FUNC_SALAS_EMPRESA` | INTEGER | Indica se a escola funciona em salas cedidas por empresa (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LOCAL_FUNC_SALAS_OUTRA_ESC` | INTEGER | Indica se a escola funciona em salas de outra escola (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AGUA_FILTRADA` | INTEGER | Indica se a escola possui água filtrada para consumo (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AGUA_POTAVEL` | INTEGER | Indica se a escola possui água potável (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AGUA_REDE_PUBLICA` | INTEGER | Indica se o abastecimento de água provém da rede pública (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AGUA_POCO_ARTESIANO` | INTEGER | Indica se a fonte de água é poço artesiano (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AGUA_CACIMBA` | INTEGER | Indica se a fonte de água é cacimba/poço/cisterna (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AGUA_FONTE_RIO` | INTEGER | Indica se a fonte de água é rio, riacho ou nascente (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AGUA_INEXISTENTE` | INTEGER | Indica não haver abastecimento de água na escola (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ENERGIA_REDE_PUBLICA` | INTEGER | Indica se a energia provém da rede pública de distribuição (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ENERGIA_GERADOR` | INTEGER | Indica se a escola possui gerador móvel ou fixo (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ENERGIA_GERADOR_FOSSIL` | INTEGER | Indica se possui gerador a combustível fósseis (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ENERGIA_OUTROS` | INTEGER | Indica utilização de outra fonte de energia (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ENERGIA_RENOVAVEL` | INTEGER | Indica utilização de fonte de energia renovável (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ENERGIA_INEXISTENTE` | INTEGER | Indica inexistência de energia elétrica no estabelecimento (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ESGOTO_REDE_PUBLICA` | INTEGER | Indica se o esgotamento sanitário é conectado à rede pública (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ESGOTO_FOSSA_SEPTICA` | INTEGER | Indica se possui fossa séptica (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ESGOTO_FOSSA_COMUM` | INTEGER | Indica se possui fossa rudimentar/comum (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ESGOTO_FOSSA` | INTEGER | Indica se utiliza algum tipo de fossa sanitária (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ESGOTO_INEXISTENTE` | INTEGER | Indica inexistência de esgotamento sanitário na escola (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LIXO_SERVICO_COLETA` | INTEGER | Indica se o lixo possui serviço de coleta pública (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LIXO_QUEIMA` | INTEGER | Indica se o lixo da escola é queimado no terreno (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LIXO_ENTERRA` | INTEGER | Indica se o lixo da escola é enterrado (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LIXO_DESTINO_FINAL_PUBLICO` | INTEGER | Indica se o lixo é descartado em destino final público (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LIXO_DESCARTA_OUTRA_AREA` | INTEGER | Indica descarte de lixo em outra área externa (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LIXO_JOGA_OUTRA_AREA` | INTEGER | Indica descarte irregular do lixo em áreas externas (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LIXO_OUTROS` | INTEGER | Indica outra destinação dada ao lixo escolar (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LIXO_RECICLA` | INTEGER | Indica se a escola faz reciclagem de resíduos sólidos (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_SEPARACAO` | INTEGER | Indica se a escola realiza separação de lixo (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_REUTILIZA` | INTEGER | Indica reutilização de resíduos/materiais recicláveis (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_RECICLAGEM` | INTEGER | Indica processo interno ou encaminhamento para reciclagem (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_TRATAMENTO_LIXO_INEXISTENTE` | INTEGER | Indica que não é feito tratamento nem separação de lixo (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ALMOXARIFADO` | INTEGER | Indica presença de almoxarifado no prédio escolar (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AREA_VERDE` | INTEGER | Indica presença de área verde/jardim (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AUDITORIO` | INTEGER | Indica presença de auditório (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BANHEIRO_FORA_PREDIO` | INTEGER | Indica existência de banheiro localizado fora do prédio principal (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BANHEIRO_DENTRO_PREDIO` | INTEGER | Indica existência de banheiro dentro do prédio principal (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BANHEIRO` | INTEGER | Indica presença de instalações sanitárias (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BANHEIRO_EI` | INTEGER | Indica banheiro adaptado para Educação Infantil (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BANHEIRO_PNE` | INTEGER | Indica banheiro adaptado a alunos/pessoas com deficiência (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BANHEIRO_FUNCIONARIOS` | INTEGER | Indica existência de banheiro exclusivo para funcionários (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BANHEIRO_CHUVEIRO` | INTEGER | Indica se o banheiro dispõe de chuveiro (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA` | INTEGER | Indica existência de espaço exclusivo para biblioteca (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BIBLIOTECA_SALA_LEITURA` | INTEGER | Indica se possui biblioteca ou sala de leitura integrada (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_COZINHA` | INTEGER | Indica presença de cozinha para preparo de refeições (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_DESPENSA` | INTEGER | Indica presença de despensa para armazenamento de insumos (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_DORMITORIO_ALUNO` | INTEGER | Indica disponibilidade de alojamento/dormitório para alunos (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_DORMITORIO_PROFESSOR` | INTEGER | Indica disponibilidade de alojamento/dormitório para professores (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LABORATORIO_CIENCIAS` | INTEGER | Indica presença de laboratório de ciências (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LABORATORIO_INFORMATICA` | INTEGER | Indica presença de laboratório de informática (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_PATIO_COBERTO` | INTEGER | Indica existência de pátio coberto na escola (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_PATIO_DESCOBERTO` | INTEGER | Indica existência de pátio descoberto (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_PARQUE_INFANTIL` | INTEGER | Indica presença de parque infantil/playground (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES` | INTEGER | Indica presença de quadra de esportes (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES_COBERTA` | INTEGER | Indica se a quadra de esportes é coberta (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_QUADRA_ESPORTES_DESCOBERTA` | INTEGER | Indica se a quadra de esportes é descoberta (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_REFEITORIO` | INTEGER | Indica presença de refeutório para refeições (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_ATELIE_ARTES` | INTEGER | Indica presença de sala de ateliê de artes (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_MUSICA_CORAL` | INTEGER | Indica presença de sala de música ou coral (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_ESTUDIO_DANCA` | INTEGER | Indica presença de estúdio de dança (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_MULTIUSO` | INTEGER | Indica presença de sala multiuso para diversas atividades (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_DIRETORIA` | INTEGER | Indica presença de sala dedicada à diretoria/gestão (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_LEITURA` | INTEGER | Indica presença de sala de leitura isolada (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_PROFESSOR` | INTEGER | Indica presença de sala reservada para professores (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_REPOUSO_ALUNO` | INTEGER | Indica existência de sala de repouso para alunos (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_ATENDIMENTO_ESPECIAL` | INTEGER | Indica presença de Sala de Recursos Multifuncionais para Atendimento Educacional Especializado - AEE (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_DEPENDENCIAS_PNE` | INTEGER | Indica se há dependências acessíveis a pessoas com deficiência (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_DEPENDENCIAS_OUTRAS` | INTEGER | Indica presença de outras dependências físicas não especificadas (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_CORRIMAO` | INTEGER | Indica presença de corrimão e guarda-corpos acessíveis (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_ELEVADOR` | INTEGER | Indica presença de elevador adaptado (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_PISOS_TATEIS` | INTEGER | Indica presença de pisos táteis para deficientes visuais (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_VAO_LIVRE` | INTEGER | Indica portas com vão livre adequado a cadeirantes (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_RAMPAS` | INTEGER | Indica presença de rampas de acesso (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINAL_SONORO` | INTEGER | Indica presença de sinalização sonora para deficientes visuais (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINAL_TATIL` | INTEGER | Indica presença de sinalização tátil (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINAL_VISUAL` | INTEGER | Indica presença de sinalização visual adaptada (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_INEXISTENTE` | INTEGER | Indica ausência total de recursos de acessibilidade na escola (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_PARABOLICA` | INTEGER | Indica se a escola dispõe de antena parabólica (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_COMPUTADOR` | INTEGER | Indica uso de computadores na escola (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_COPIADORA` | INTEGER | Indica se dispõe de máquina copiada/xerox (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_IMPRESSORA` | INTEGER | Indica disponibilidade de impressoras simples (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_IMPRESSORA_MULT` | INTEGER | Indica presença de impressoras multifuncionais (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_SCANNER` | INTEGER | Indica presença de equipamento scanner de documentos (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_NENHUM` | INTEGER | Indica ausência de equipamentos tecnológicos descritos (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_DVD` | INTEGER | Indica presença de aparelho de DVD/Blu-ray (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_SOM` | INTEGER | Indica presença de aparelho de som (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_TV` | INTEGER | Indica presença de aparelhos de televisão (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_LOUSA_DIGITAL` | INTEGER | Indica presença de lousa digital interativa (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_MULTIMIDIA` | INTEGER | Indica presença de projetor multimídia / data show (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_VIDEOCASSETE` | INTEGER | Indica presença de aparelho de videocassete (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_RETROPROJETOR` | INTEGER | Indica presença de retroprojetor (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_FAX` | INTEGER | Indica disponibilidade de aparelho de fax (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_EQUIP_FOTO` | INTEGER | Indica presença de máquina fotográfica ou filmadora (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_INTERNET` | INTEGER | Indica disponibilidade de acesso à internet na escola (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_INTERNET_ALUNOS` | INTEGER | Indica se a internet está disponível para uso dos alunos (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_INTERNET_ADMINISTRATIVO` | INTEGER | Indica uso de internet para gestão/uso administrativo (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_INTERNET_APRENDIZAGEM` | INTEGER | Indica uso da internet para processos pedagógicos e aprendizagem (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_INTERNET_COMUNIDADE` | INTEGER | Indica acesso à internet franqueado à comunidade (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSO_INTERNET_COMPUTADOR` | INTEGER | Indica acesso à internet via computadores da escola (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACES_INTERNET_DISP_PESSOAIS` | INTEGER | Indica acesso à internet permitido a dispositivos pessoais via Wi-Fi (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_BANDA_LARGA` | INTEGER | Indica se a conexão de internet é de banda larga (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_PROF_BIBLIOTECARIO` | INTEGER | Indica atuação de profissional bibliotecário habilitado (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_MULTIMIDIA` | INTEGER | Indica presença de materiais pedagógicos multimídia (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_INFANTIL` | INTEGER | Indica presença de material pedagógico para Educação Infantil (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_CIENTIFICO` | INTEGER | Indica existência de materiais pedagógicos científicos/laboratoriais (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_DIFUSAO` | INTEGER | Indica disponibilidade de materiais de difusão cultural (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_MUSICAL` | INTEGER | Indica disponibilidade de instrumentos ou material pedagógico musical (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_JOGOS` | INTEGER | Indica uso de jogos pedagógicos e educativos, relevante para the source organization (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_ARTISTICAS` | INTEGER | Indica materiais pedagógicos para atividades artísticas (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_DESPORTIVA` | INTEGER | Indica acervo de material para práticas desportivas (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_INDIGENA` | INTEGER | Indica uso de material pedagógico para Educação Escolar Indígena (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_ETNICO` | INTEGER | Indica acervo pedagógico para relações étnico-raciais (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_CAMPO` | INTEGER | Indica material pedagógico voltado à Educação do Campo (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_NENHUM` | INTEGER | Indica não dispor dos materiais pedagógicos listados (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_ESP_QUILOMBOLA` | INTEGER | Indica oferta de material específico para educação quilombola (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_ESP_INDIGENA` | INTEGER | Indica oferta de material específico para educação indígena (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_ESP_NAO_UTILIZA` | INTEGER | Indica que não utiliza materiais específicos direcionados (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ESPACO_EQUIPAMENTO` | INTEGER | Indica existência de espaço físico com equipamentos pedagógicos adequados (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_LABORATORIO_EDUC_PROF` | INTEGER | Indica presença de laboratório para Educação Profissional (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_OFICINAS_EDUC_PROF` | INTEGER | Indica sala de oficinas para cursos de Educação Profissional (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_PROFISSIONAL` | INTEGER | Indica presença de material didático para cursos profissionais (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_SALA_ESTUDIO_GRAVACAO` | INTEGER | Indica disponibilidade de estúdio de gravação de áudio/vídeo (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_BIL_SURDOS` | INTEGER | Indica acervo pedagógico bilíngue voltado a alunos surdos ou com deficiência auditiva (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_AGUA_CARRO_PIPA` | INTEGER | Indica se o abastecimento de água é realizado via caminhão pipa (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_ACESSIBILIDADE_SINALIZACAO` | INTEGER | Indica presença de sinalização tátil, visual ou sonora para acessibilidade (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_AGRICOLA` | INTEGER | Indica disponibilidade de material pedagógico para práticas agrícolas (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_QUILOMBOLA` | INTEGER | Indica presença de material pedagógico específico para comunidades quilombolas (1 para Sim, 0 para Não). — descrição gerada por IA. |
| `IN_MATERIAL_PED_EDU_ESP` | INTEGER | Indica disponibilidade de material pedagógico adaptado para Educação Especial (1 para Sim, 0 para Não). — descrição gerada por IA. |

## trusted · inep_censo_escolar_localizacao

File `trusted__inep_censo_escolar_localizacao.parquet` · 7,427,183 rows · 39 columns

TRUSTED - Localização geográfica e administrativa das escolas/unidades, incluindo região, UF, município, distrito, endereço e coordenadas quando disponíveis. Sem filtros que removam registros. Anos cobertos pelas fontes: 1995-2025 (1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025).

**Feeds:** `semantic/obt_inep_censo_escola_ano`

| Column | Type | Description |
|---|---|---|
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `CO_IBGE` | INTEGER | Codigo identificador territorial do IBGE associado a localidade da escola. — descrição gerada por IA. |
| `UF` | STRING | Nome por extenso do estado/Unidade Federativa. — descrição gerada por IA. |
| `SIGLA` | STRING | Sigla de duas letras da Unidade Federativa (ex: MG, AC, MA). — descrição gerada por IA. |
| `MUNIC` | STRING | Nome do municipio conforme constava no arquivo historico original. — descrição gerada por IA. |
| `LOC` | STRING | Tipo de localizacao da escola (ex: Urbana, Rural). — descrição gerada por IA. |
| `CODMUNIC` | STRING | Codigo numrico identificador do municipio. — descrição gerada por IA. |
| `NU_ANO_CENSO` | INTEGER | Ano do Censo Escolar em formato numerico. — descrição gerada por IA. |
| `CO_ENTIDADE` | INTEGER | Codigo INEP unico da escola/entidade de ensino. — descrição gerada por IA. |
| `NO_REGIAO` | STRING | Nome da grande regiao geografica (ex: Sudeste, Norte). — descrição gerada por IA. |
| `CO_REGIAO` | INTEGER | Codigo da grande regiao geografica segundo o IBGE. — descrição gerada por IA. |
| `NO_UF` | STRING | Nome oficial por extenso da Unidade Federativa. — descrição gerada por IA. |
| `SG_UF` | STRING | Sigla da Unidade Federativa (2 letras). — descrição gerada por IA. |
| `CO_UF` | INTEGER | Codigo IBGE do estado/Unidade Federativa. — descrição gerada por IA. |
| `NO_MUNICIPIO` | STRING | Nome oficial do municipio cadastrado no INEP/IBGE. — descrição gerada por IA. |
| `CO_MUNICIPIO` | INTEGER | Codigo IBGE de 7 digitos do municipio. — descrição gerada por IA. |
| `NO_MESORREGIAO` | STRING | Nome da mesorregiao geografica do IBGE. — descrição gerada por IA. |
| `CO_MESORREGIAO` | INTEGER | Codigo da mesorregiao geografica do IBGE. — descrição gerada por IA. |
| `NO_MICRORREGIAO` | STRING | Nome da microrregiao geografica do IBGE. — descrição gerada por IA. |
| `CO_MICRORREGIAO` | INTEGER | Codigo da microrregiao geografica do IBGE. — descrição gerada por IA. |
| `CO_DISTRITO` | INTEGER | Codigo do distrito municipal segundo a divisão territorial do IBGE. — descrição gerada por IA. |
| `TP_LOCALIZACAO` | INTEGER | Codigo numerico do tipo de localizacao da escola (1-Urbana, 2-Rural). — descrição gerada por IA. |
| `TP_LOCALIZACAO_DIFERENCIADA` | INTEGER | Codigo da localizacao diferenciada da escola (ex: area quilombola, terra indigena, assentamento). — descrição gerada por IA. |
| `DS_ENDERECO` | STRING | Endereco/logradouro completo onde a escola esta situada. — descrição gerada por IA. |
| `NU_ENDERECO` | INTEGER | Numero do endereco da escola. — descrição gerada por IA. |
| `NO_BAIRRO` | STRING | Nome do bairro ou localidade da escola. — descrição gerada por IA. |
| `CO_CEP` | INTEGER | Codigo de Enderecamento Postal (CEP) de 8 digitos. — descrição gerada por IA. |
| `NO_REGIAO_GEOG_INTERM` | STRING | Nome da Regiao Geografica Intermediaria definida pelo IBGE. — descrição gerada por IA. |
| `CO_REGIAO_GEOG_INTERM` | INTEGER | Codigo da Regiao Geografica Intermediaria do IBGE. — descrição gerada por IA. |
| `NO_REGIAO_GEOG_IMED` | STRING | Nome da Regiao Geografica Imediata definida pelo IBGE. — descrição gerada por IA. |
| `CO_REGIAO_GEOG_IMED` | INTEGER | Codigo da Regiao Geografica Imediata do IBGE. — descrição gerada por IA. |
| `NO_DISTRITO` | STRING | Nome do distrito municipal onde a escola esta localizada. — descrição gerada por IA. |
| `NO_REGIAO_ADMINISTRATIVA` | STRING | Nome da regiao administrativa do municipio ou DF. — descrição gerada por IA. |
| `CO_REGIAO_ADMINISTRATIVA` | INTEGER | Codigo da regiao administrativa municipal/DF. — descrição gerada por IA. |
| `LATITUDE` | STRING | Coordenada geografica de latitude do estabelecimento escolar em graus decimais. — descrição gerada por IA. |
| `LONGITUDE` | STRING | Coordenada geografica de longitude do estabelecimento escolar em graus decimais. — descrição gerada por IA. |

## trusted · inep_censo_escolar_matriculas

File `trusted__inep_censo_escolar_matriculas.parquet` · 4,237,230 rows · 247 columns

TRUSTED - Métricas agregadas de matrículas por escola/ano e recortes educacionais disponíveis no layout. Sem filtros que removam registros. Anos cobertos pelas fontes: 2007-2025 (2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025).

**Built from:** `raw/inep_censo_escolar_matricula`

**Feeds:** `semantic/f_censo_escolar`, `semantic/f_censo_escolar_municipio`, `semantic/obt_inep_censo_matricula_escola_ano`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | INTEGER | Ano de referência do Censo Escolar do INEP (formato AAAA). — descrição gerada por IA. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `CO_ENTIDADE` | INTEGER | Código de 8 dígitos do INEP que identifica unicamente a escola (entidade escolar). — descrição gerada por IA. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `QT_MAT_BAS` | INTEGER | Quantidade total de matrículas na Educação Básica na escola. — descrição gerada por IA. |
| `QT_MAT_INF` | INTEGER | Quantidade total de matrículas na Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_INF_CRE` | INTEGER | Quantidade de matrículas na Educação Infantil - etapa Creche. — descrição gerada por IA. |
| `QT_MAT_INF_PRE` | INTEGER | Quantidade de matrículas na Educação Infantil - etapa Pré-escola. — descrição gerada por IA. |
| `QT_MAT_FUND` | INTEGER | Quantidade total de matrículas no Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI` | INTEGER | Quantidade de matrículas no Ensino Fundamental - Anos Iniciais (1º ao 5º ano). — descrição gerada por IA. |
| `QT_MAT_FUND_AF` | INTEGER | Quantidade de matrículas no Ensino Fundamental - Anos Finais (6º ao 9º ano). — descrição gerada por IA. |
| `QT_MAT_MED` | INTEGER | Quantidade total de matrículas no Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_PROF` | INTEGER | Quantidade total de matrículas na Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC` | INTEGER | Quantidade de matrículas na Educação Profissional Técnica de Nível Médio. — descrição gerada por IA. |
| `QT_MAT_EJA` | INTEGER | Quantidade total de matrículas na Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |
| `QT_MAT_EJA_FUND` | INTEGER | Quantidade de matrículas na EJA - Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_EJA_MED` | INTEGER | Quantidade de matrículas na EJA - Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP` | INTEGER | Quantidade total de matrículas na Educação Especial. — descrição gerada por IA. |
| `QT_MAT_ESP_CC` | INTEGER | Quantidade de matrículas na Educação Especial em classes comuns (inclusivas). — descrição gerada por IA. |
| `QT_MAT_ESP_CE` | INTEGER | Quantidade de matrículas na Educação Especial em classes exclusivas/especiais. — descrição gerada por IA. |
| `QT_MAT_BAS_FEM` | INTEGER | Quantidade de matrículas de estudantes do sexo feminino na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_MASC` | INTEGER | Quantidade de matrículas de estudantes do sexo masculino na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_ND` | INTEGER | Quantidade de matrículas com sexo não declarado na Educação Básica. — descrição gerada por IA. |
| `QT_MAT_BAS_BRANCA` | INTEGER | Quantidade de matrículas de alunos autodeclarados de cor/raça branca. — descrição gerada por IA. |
| `QT_MAT_BAS_PRETA` | INTEGER | Quantidade de matrículas de alunos autodeclarados de cor/raça preta. — descrição gerada por IA. |
| `QT_MAT_BAS_PARDA` | INTEGER | Quantidade de matrículas de alunos autodeclarados de cor/raça parda. — descrição gerada por IA. |
| `QT_MAT_BAS_AMARELA` | INTEGER | Quantidade de matrículas de alunos autodeclarados de cor/raça amarela. — descrição gerada por IA. |
| `QT_MAT_BAS_INDIGENA` | INTEGER | Quantidade de matrículas de alunos autodeclarados de cor/raça indígena. — descrição gerada por IA. |
| `QT_MAT_BAS_0_3` | INTEGER | Quantidade de matrículas de alunos na faixa etária de 0 a 3 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_4_5` | INTEGER | Quantidade de matrículas de alunos na faixa etária de 4 a 5 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_6_10` | INTEGER | Quantidade de matrículas de alunos na faixa etária de 6 a 10 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_11_14` | INTEGER | Quantidade de matrículas de alunos na faixa etária de 11 a 14 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_15_17` | INTEGER | Quantidade de matrículas de alunos na faixa etária de 15 a 17 anos. — descrição gerada por IA. |
| `QT_MAT_BAS_18_MAIS` | INTEGER | Quantidade de matrículas de alunos com 18 anos ou mais. — descrição gerada por IA. |
| `QT_MAT_BAS_D` | INTEGER | Quantidade de matrículas da Educação Básica no turno diurno. — descrição gerada por IA. |
| `QT_MAT_BAS_N` | INTEGER | Quantidade de matrículas da Educação Básica no turno noturno. — descrição gerada por IA. |
| `QT_MAT_BAS_EAD` | INTEGER | Quantidade de matrículas da Educação Básica na modalidade a distância (EAD). — descrição gerada por IA. |
| `QT_MAT_INF_INT` | INTEGER | Quantidade de matrículas na Educação Infantil em tempo integral. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_INT` | INTEGER | Quantidade de matrículas em Creche em tempo integral. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_INT` | INTEGER | Quantidade de matrículas em Pré-escola em tempo integral. — descrição gerada por IA. |
| `QT_MAT_FUND_INT` | INTEGER | Quantidade de matrículas no Ensino Fundamental em tempo integral. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_INT` | INTEGER | Quantidade de matrículas nos Anos Iniciais do Ensino Fundamental em tempo integral. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_INT` | INTEGER | Quantidade de matrículas nos Anos Finais do Ensino Fundamental em tempo integral. — descrição gerada por IA. |
| `QT_MAT_MED_INT` | INTEGER | Quantidade de matrículas no Ensino Médio em tempo integral. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_1` | INTEGER | Quantidade de matrículas no 1º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_2` | INTEGER | Quantidade de matrículas no 2º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_3` | INTEGER | Quantidade de matrículas no 3º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_4` | INTEGER | Quantidade de matrículas no 4º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_5` | INTEGER | Quantidade de matrículas no 5º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_6` | INTEGER | Quantidade de matrículas no 6º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_7` | INTEGER | Quantidade de matrículas no 7º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_8` | INTEGER | Quantidade de matrículas no 8º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_9` | INTEGER | Quantidade de matrículas no 9º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_MED_PROP` | INTEGER | Quantidade de matrículas no Ensino Médio propedêutico (regular). — descrição gerada por IA. |
| `QT_MAT_MED_PROP_1` | INTEGER | Quantidade de matrículas na 1ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_2` | INTEGER | Quantidade de matrículas na 2ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_3` | INTEGER | Quantidade de matrículas na 3ª série do Ensino Médio propedêutico. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_4` | INTEGER | Quantidade de matrículas na 4ª série do Ensino Médio propedêutico/integrado. — descrição gerada por IA. |
| `QT_MAT_MED_PROP_NS` | INTEGER | Quantidade de matrículas no Ensino Médio propedêutico não seriado. — descrição gerada por IA. |
| `QT_MAT_MED_CT` | INTEGER | Quantidade de matrículas no Ensino Médio integrado à Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_MED_CT_1` | INTEGER | Quantidade de matrículas na 1ª série do Ensino Médio integrado. — descrição gerada por IA. |
| `QT_MAT_MED_CT_2` | INTEGER | Quantidade de matrículas na 2ª série do Ensino Médio integrado. — descrição gerada por IA. |
| `QT_MAT_MED_CT_3` | INTEGER | Quantidade de matrículas na 3ª série do Ensino Médio integrado. — descrição gerada por IA. |
| `QT_MAT_MED_CT_4` | INTEGER | Quantidade de matrículas na 4ª série do Ensino Médio integrado. — descrição gerada por IA. |
| `QT_MAT_MED_CT_NS` | INTEGER | Quantidade de matrículas no Ensino Médio integrado não seriado. — descrição gerada por IA. |
| `QT_MAT_MED_NM` | INTEGER | Quantidade de matrículas no Ensino Médio - Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_1` | INTEGER | Quantidade de matrículas na 1ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_2` | INTEGER | Quantidade de matrículas na 2ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_3` | INTEGER | Quantidade de matrículas na 3ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_MED_NM_4` | INTEGER | Quantidade de matrículas na 4ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_CONC` | INTEGER | Quantidade de matrículas na Educação Profissional Técnica concomitante. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_SUBS` | INTEGER | Quantidade de matrículas na Educação Profissional Técnica subsequente. — descrição gerada por IA. |
| `QT_MAT_PROF_FIC_CONC` | INTEGER | Quantidade de matrículas em Cursos de Formação Inicial e Continuada (FIC) concomitante. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AI` | INTEGER | Quantidade de matrículas na EJA Fundamental - Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_AF` | INTEGER | Quantidade de matrículas na EJA Fundamental - Anos Finais. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_FIC` | INTEGER | Quantidade de matrículas na EJA Fundamental qualificação profissional (FIC). — descrição gerada por IA. |
| `QT_MAT_EJA_MED_NPROF` | INTEGER | Quantidade de matrículas na EJA Médio não profissionalizante. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_FIC` | INTEGER | Quantidade de matrículas na EJA Médio qualificação profissional (FIC). — descrição gerada por IA. |
| `QT_MAT_EJA_MED_TEC` | INTEGER | Quantidade de matrículas na EJA Médio integrada à Educação Técnica. — descrição gerada por IA. |
| `QT_MAT_ZR_URB` | INTEGER | Quantidade de matrículas de alunos residentes em área urbana. — descrição gerada por IA. |
| `QT_MAT_ZR_RUR` | INTEGER | Quantidade de matrículas de alunos residentes em área rural. — descrição gerada por IA. |
| `QT_MAT_ZR_NA` | INTEGER | Quantidade de matrículas sem informação de zona de residência. — descrição gerada por IA. |
| `QT_TRANSP_PUBLICO` | INTEGER | Quantidade de alunos que utilizam transporte escolar público. — descrição gerada por IA. |
| `QT_TRANSP_RESP_EST` | INTEGER | Quantidade de alunos que utilizam transporte escolar sob responsabilidade estadual. — descrição gerada por IA. |
| `QT_TRANSP_RESP_MUN` | INTEGER | Quantidade de alunos que utilizam transporte escolar sob responsabilidade municipal. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT` | INTEGER | Quantidade de matrículas no Ensino Médio em itinerário técnico e profissional continuado. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_1` | INTEGER | Matrículas na 1ª série do Ensino Médio em itinerário técnico continuado. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_2` | INTEGER | Matrículas na 2ª série do Ensino Médio em itinerário técnico continuado. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_3` | INTEGER | Matrículas na 3ª série do Ensino Médio em itinerário técnico continuado. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_4` | INTEGER | Matrículas na 4ª série do Ensino Médio em itinerário técnico continuado. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_CT_NS` | INTEGER | Matrículas não seriadas do Ensino Médio em itinerário técnico continuado. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP` | INTEGER | Quantidade de matrículas no Ensino Médio em itinerário de qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_1` | INTEGER | Matrículas na 1ª série do Ensino Médio em itinerário de qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_2` | INTEGER | Matrículas na 2ª série do Ensino Médio em itinerário de qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_3` | INTEGER | Matrículas na 3ª série do Ensino Médio em itinerário de qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_4` | INTEGER | Matrículas na 4ª série do Ensino Médio em itinerário de qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFTP_QP_NS` | INTEGER | Matrículas não seriadas do Ensino Médio em itinerário de qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_IFA` | INTEGER | Total de matrículas em itinerários formativos de aprofundamento do Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING` | INTEGER | Matrículas no itinerário de aprofundamento da área de Linguagens. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING_MT` | INTEGER | Matrículas no itinerário de Linguagens e Matemática. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING_OTME` | INTEGER | Matrículas no itinerário de Linguagens combinado com outras áreas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_LING_OE` | INTEGER | Matrículas no itinerário de Linguagens em oferta exclusiva. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE` | INTEGER | Matrículas no itinerário de aprofundamento da área de Matemática. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE_MT` | INTEGER | Matrículas no itinerário de Matemática integrado com outras áreas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE_OTME` | INTEGER | Matrículas no itinerário de Matemática combinado com outras ofertas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_MATE_OE` | INTEGER | Matrículas no itinerário de Matemática em oferta exclusiva. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC` | INTEGER | Matrículas no itinerário de aprofundamento de Ciências da Natureza. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC_MT` | INTEGER | Matrículas no itinerário de Ciências da Natureza e Matemática. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC_OTME` | INTEGER | Matrículas no itinerário de Ciências da Natureza com outras áreas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_CIENC_OE` | INTEGER | Matrículas no itinerário de Ciências da Natureza em oferta exclusiva. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA` | INTEGER | Matrículas no itinerário de aprofundamento de Ciências Humanas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA_MT` | INTEGER | Matrículas no itinerário de Ciências Humanas e Matemática. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA_OTME` | INTEGER | Matrículas no itinerário de Ciências Humanas com outras áreas. — descrição gerada por IA. |
| `QT_MAT_MED_IFA_HUMA_OE` | INTEGER | Matrículas no itinerário de Ciências Humanas em oferta exclusiva. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT` | INTEGER | Matrículas em itinerário articulado com formação técnica continuada. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT_MT` | INTEGER | Matrículas em itinerário articulado técnico continuado multipropósito. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT_OTME` | INTEGER | Matrículas em itinerário articulado técnico continuado com outras ofertas. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_CT_OE` | INTEGER | Matrículas em itinerário articulado técnico continuado em oferta exclusiva. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP` | INTEGER | Matrículas em itinerário articulado de qualificação profissional. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP_MT` | INTEGER | Matrículas em itinerário articulado de qualificação profissional multipropósito. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP_OTME` | INTEGER | Matrículas em itinerário articulado de qualificação profissional com outras ofertas. — descrição gerada por IA. |
| `QT_MAT_MED_ARTI_IFTP_QP_OE` | INTEGER | Matrículas em itinerário articulado de qualificação profissional em oferta exclusiva. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_IFTP_CT` | INTEGER | Matrículas na Educação Profissional Técnica vinculada a itinerário continuado. — descrição gerada por IA. |
| `QT_MAT_PROF_NAO_TEC` | INTEGER | Matrículas na Educação Profissional não técnica. — descrição gerada por IA. |
| `QT_MAT_PROF_IFTP_QP` | INTEGER | Matrículas na Educação Profissional vinculadas a itinerário de qualificação. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_NPROF` | INTEGER | Matrículas na EJA Fundamental não profissionalizante. — descrição gerada por IA. |
| `QT_MAT_ESP_INF` | INTEGER | Matrículas na Educação Especial - Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_ESP_INF_CRE` | INTEGER | Matrículas na Educação Especial - Creche. — descrição gerada por IA. |
| `QT_MAT_ESP_INF_PRE` | INTEGER | Matrículas na Educação Especial - Pré-escola. — descrição gerada por IA. |
| `QT_MAT_ESP_FUND` | INTEGER | Matrículas na Educação Especial - Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_FUND_AI` | INTEGER | Matrículas na Educação Especial - Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_ESP_FUND_AF` | INTEGER | Matrículas na Educação Especial - Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_MAT_ESP_MED` | INTEGER | Matrículas na Educação Especial - Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_PROF` | INTEGER | Matrículas na Educação Especial - Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_ESP_PROF_TEC` | INTEGER | Matrículas na Educação Especial - Educação Técnica. — descrição gerada por IA. |
| `QT_MAT_ESP_EJA` | INTEGER | Matrículas na Educação Especial - EJA. — descrição gerada por IA. |
| `QT_MAT_ESP_EJA_FUND` | INTEGER | Matrículas na Educação Especial - EJA Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_EJA_MED` | INTEGER | Matrículas na Educação Especial - EJA Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INF` | INTEGER | Matrículas na Educação Especial em classe comum - Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INF_CRE` | INTEGER | Matrículas na Educação Especial em classe comum - Creche. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INF_PRE` | INTEGER | Matrículas na Educação Especial em classe comum - Pré-escola. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_FUND` | INTEGER | Matrículas na Educação Especial em classe comum - Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_FUND_AI` | INTEGER | Matrículas na Educação Especial em classe comum - Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_FUND_AF` | INTEGER | Matrículas na Educação Especial em classe comum - Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_MED` | INTEGER | Matrículas na Educação Especial em classe comum - Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_PROF` | INTEGER | Matrículas na Educação Especial em classe comum - Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_PROF_TEC` | INTEGER | Matrículas na Educação Especial em classe comum - Educação Técnica. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EJA` | INTEGER | Matrículas na Educação Especial em classe comum - EJA. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EJA_FUND` | INTEGER | Matrículas na Educação Especial em classe comum - EJA Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EJA_MED` | INTEGER | Matrículas na Educação Especial em classe comum - EJA Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INF` | INTEGER | Matrículas na Educação Especial em classe exclusiva - Educação Infantil. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INF_CRE` | INTEGER | Matrículas na Educação Especial em classe exclusiva - Creche. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INF_PRE` | INTEGER | Matrículas na Educação Especial em classe exclusiva - Pré-escola. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_FUND` | INTEGER | Matrículas na Educação Especial em classe exclusiva - Ensino Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_FUND_AI` | INTEGER | Matrículas na Educação Especial em classe exclusiva - Fundamental Anos Iniciais. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_FUND_AF` | INTEGER | Matrículas na Educação Especial em classe exclusiva - Fundamental Anos Finais. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_MED` | INTEGER | Matrículas na Educação Especial em classe exclusiva - Ensino Médio. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_PROF` | INTEGER | Matrículas na Educação Especial em classe exclusiva - Educação Profissional. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_PROF_TEC` | INTEGER | Matrículas na Educação Especial em classe exclusiva - Educação Técnica. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EJA` | INTEGER | Matrículas na Educação Especial em classe exclusiva - EJA. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EJA_FUND` | INTEGER | Matrículas na Educação Especial em classe exclusiva - EJA Fundamental. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EJA_MED` | INTEGER | Matrículas na Educação Especial em classe exclusiva - EJA Médio. — descrição gerada por IA. |
| `QT_MAT_BAS_0_3_REF_31_03` | INTEGER | Matrículas de alunos de 0 a 3 anos considerando a data oficial de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_4_5_REF_31_03` | INTEGER | Matrículas de alunos de 4 a 5 anos considerando a data oficial de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_6_10_REF_31_03` | INTEGER | Matrículas de alunos de 6 a 10 anos considerando a data oficial de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_11_14_REF_31_03` | INTEGER | Matrículas de alunos de 11 a 14 anos considerando a data oficial de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_15_17_REF_31_03` | INTEGER | Matrículas de alunos de 15 a 17 anos considerando a data oficial de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_18_MAIS_REF_31_03` | INTEGER | Matrículas de alunos de 18 anos ou mais considerando a data oficial de referência (31/03). — descrição gerada por IA. |
| `QT_MAT_BAS_DM` | INTEGER | Matrículas na Educação Básica no turno matutino. — descrição gerada por IA. |
| `QT_MAT_BAS_DV` | INTEGER | Matrículas na Educação Básica no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_D` | INTEGER | Matrículas em Creche no turno diurno. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_DM` | INTEGER | Matrículas em Creche no turno matutino. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_DV` | INTEGER | Matrículas em Creche no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_INF_CRE_N` | INTEGER | Matrículas em Creche no turno noturno. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_D` | INTEGER | Matrículas em Pré-escola no turno diurno. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_DM` | INTEGER | Matrículas em Pré-escola no turno matutino. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_DV` | INTEGER | Matrículas em Pré-escola no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_INF_PRE_N` | INTEGER | Matrículas em Pré-escola no turno noturno. — descrição gerada por IA. |
| `QT_MAT_FUND_D` | INTEGER | Matrículas no Ensino Fundamental no turno diurno. — descrição gerada por IA. |
| `QT_MAT_FUND_DM` | INTEGER | Matrículas no Ensino Fundamental no turno matutino. — descrição gerada por IA. |
| `QT_MAT_FUND_DV` | INTEGER | Matrículas no Ensino Fundamental no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_FUND_N` | INTEGER | Matrículas no Ensino Fundamental no turno noturno. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_D` | INTEGER | Matrículas no Fundamental Anos Iniciais no turno diurno. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_DM` | INTEGER | Matrículas no Fundamental Anos Iniciais no turno matutino. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_DV` | INTEGER | Matrículas no Fundamental Anos Iniciais no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_FUND_AI_N` | INTEGER | Matrículas no Fundamental Anos Iniciais no turno noturno. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_D` | INTEGER | Matrículas no Fundamental Anos Finais no turno diurno. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_DM` | INTEGER | Matrículas no Fundamental Anos Finais no turno matutino. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_DV` | INTEGER | Matrículas no Fundamental Anos Finais no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_FUND_AF_N` | INTEGER | Matrículas no Fundamental Anos Finais no turno noturno. — descrição gerada por IA. |
| `QT_MAT_MED_D` | INTEGER | Matrículas no Ensino Médio no turno diurno. — descrição gerada por IA. |
| `QT_MAT_MED_DM` | INTEGER | Matrículas no Ensino Médio no turno matutino. — descrição gerada por IA. |
| `QT_MAT_MED_DV` | INTEGER | Matrículas no Ensino Médio no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_MED_N` | INTEGER | Matrículas no Ensino Médio no turno noturno. — descrição gerada por IA. |
| `QT_MAT_MED_EAD` | INTEGER | Matrículas no Ensino Médio na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_PROF_D` | INTEGER | Matrículas na Educação Profissional no turno diurno. — descrição gerada por IA. |
| `QT_MAT_PROF_DM` | INTEGER | Matrículas na Educação Profissional no turno matutino. — descrição gerada por IA. |
| `QT_MAT_PROF_DV` | INTEGER | Matrículas na Educação Profissional no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_PROF_N` | INTEGER | Matrículas na Educação Profissional no turno noturno. — descrição gerada por IA. |
| `QT_MAT_PROF_EAD` | INTEGER | Matrículas na Educação Profissional na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_D` | INTEGER | Matrículas na Educação Técnica no turno diurno. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_DM` | INTEGER | Matrículas na Educação Técnica no turno matutino. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_DV` | INTEGER | Matrículas na Educação Técnica no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_N` | INTEGER | Matrículas na Educação Técnica no turno noturno. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_EAD` | INTEGER | Matrículas na Educação Técnica na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_EJA_D` | INTEGER | Matrículas na EJA no turno diurno. — descrição gerada por IA. |
| `QT_MAT_EJA_DM` | INTEGER | Matrículas na EJA no turno matutino. — descrição gerada por IA. |
| `QT_MAT_EJA_DV` | INTEGER | Matrículas na EJA no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_EJA_N` | INTEGER | Matrículas na EJA no turno noturno. — descrição gerada por IA. |
| `QT_MAT_EJA_EAD` | INTEGER | Matrículas na EJA na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_D` | INTEGER | Matrículas na EJA Fundamental no turno diurno. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_DM` | INTEGER | Matrículas na EJA Fundamental no turno matutino. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_DV` | INTEGER | Matrículas na EJA Fundamental no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_N` | INTEGER | Matrículas na EJA Fundamental no turno noturno. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_EAD` | INTEGER | Matrículas na EJA Fundamental na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_D` | INTEGER | Matrículas na EJA Médio no turno diurno. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_DM` | INTEGER | Matrículas na EJA Médio no turno matutino. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_DV` | INTEGER | Matrículas na EJA Médio no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_N` | INTEGER | Matrículas na EJA Médio no turno noturno. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_EAD` | INTEGER | Matrículas na EJA Médio na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_ESP_D` | INTEGER | Matrículas na Educação Especial no turno diurno. — descrição gerada por IA. |
| `QT_MAT_ESP_DM` | INTEGER | Matrículas na Educação Especial no turno matutino. — descrição gerada por IA. |
| `QT_MAT_ESP_DV` | INTEGER | Matrículas na Educação Especial no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_ESP_N` | INTEGER | Matrículas na Educação Especial no turno noturno. — descrição gerada por IA. |
| `QT_MAT_ESP_EAD` | INTEGER | Matrículas na Educação Especial na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_D` | INTEGER | Matrículas na Educação Especial em classe comum no turno diurno. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_DM` | INTEGER | Matrículas na Educação Especial em classe comum no turno matutino. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_DV` | INTEGER | Matrículas na Educação Especial em classe comum no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_N` | INTEGER | Matrículas na Educação Especial em classe comum no turno noturno. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_EAD` | INTEGER | Matrículas na Educação Especial em classe comum na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_D` | INTEGER | Matrículas na Educação Especial em classe exclusiva no turno diurno. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_DM` | INTEGER | Matrículas na Educação Especial em classe exclusiva no turno matutino. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_DV` | INTEGER | Matrículas na Educação Especial em classe exclusiva no turno vespertino. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_N` | INTEGER | Matrículas na Educação Especial em classe exclusiva no turno noturno. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_EAD` | INTEGER | Matrículas na Educação Especial em classe exclusiva na modalidade EAD. — descrição gerada por IA. |
| `QT_MAT_BAS_INT` | INTEGER | Quantidade total de matrículas na Educação Básica em tempo integral. — descrição gerada por IA. |
| `QT_MAT_PROF_INT` | INTEGER | Quantidade de matrículas na Educação Profissional em tempo integral. — descrição gerada por IA. |
| `QT_MAT_PROF_TEC_INT` | INTEGER | Quantidade de matrículas na Educação Técnica em tempo integral. — descrição gerada por IA. |
| `QT_MAT_EJA_INT` | INTEGER | Quantidade de matrículas na EJA em tempo integral. — descrição gerada por IA. |
| `QT_MAT_EJA_FUND_INT` | INTEGER | Quantidade de matrículas na EJA Fundamental em tempo integral. — descrição gerada por IA. |
| `QT_MAT_EJA_MED_INT` | INTEGER | Quantidade de matrículas na EJA Médio em tempo integral. — descrição gerada por IA. |
| `QT_MAT_ESP_INT` | INTEGER | Quantidade de matrículas na Educação Especial em tempo integral. — descrição gerada por IA. |
| `QT_MAT_ESP_CC_INT` | INTEGER | Quantidade de matrículas na Educação Especial em classe comum em tempo integral. — descrição gerada por IA. |
| `QT_MAT_ESP_CE_INT` | INTEGER | Quantidade de matrículas na Educação Especial em classe exclusiva em tempo integral. — descrição gerada por IA. |
| `QT_MAT_BAS_LIBRAS` | INTEGER | Quantidade de matrículas na Educação Básica com atendimento/ensino em Libras. — descrição gerada por IA. |

## trusted · inep_censo_escolar_turmas

File `trusted__inep_censo_escolar_turmas.parquet` · 4,237,236 rows · 194 columns

TRUSTED - Métricas agregadas de turmas por escola/ano, etapa, turno/modalidade e demais recortes disponíveis. Sem filtros que removam registros. Anos cobertos pelas fontes: 2007-2025 (2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025).

**Built from:** `raw/inep_censo_escolar_turma`

**Feeds:** `semantic/obt_inep_censo_turma_escola_ano`

| Column | Type | Description |
|---|---|---|
| `NU_ANO_CENSO` | INTEGER | Ano de realização do Censo Escolar (YYYY). — descrição gerada por IA. |
| `raw_load_id` | STRING | Identificador técnico da carga RAW para rastreabilidade. |
| `CO_ENTIDADE` | INTEGER | Código INEP de identificação única da escola (8 dígitos). — descrição gerada por IA. |
| `source_file` | STRING | Nome do arquivo CSV de origem dentro do pacote do INEP. |
| `source_zip` | STRING | Nome do arquivo ZIP oficial de origem. |
| `ano_censo` | INTEGER | Ano de referência do Censo Escolar INEP. |
| `QT_TUR_BAS` | INTEGER | Quantidade total de turmas da Educação Básica. — descrição gerada por IA. |
| `QT_TUR_INF` | INTEGER | Quantidade de turmas de Educação Infantil. — descrição gerada por IA. |
| `QT_TUR_INF_CRE` | INTEGER | Quantidade de turmas de Educação Infantil - Creche. — descrição gerada por IA. |
| `QT_TUR_INF_PRE` | INTEGER | Quantidade de turmas de Educação Infantil - Pré-escola. — descrição gerada por IA. |
| `QT_TUR_FUND` | INTEGER | Quantidade total de turmas do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI` | INTEGER | Quantidade de turmas do Ensino Fundamental - Anos Iniciais. — descrição gerada por IA. |
| `QT_TUR_FUND_AF` | INTEGER | Quantidade de turmas do Ensino Fundamental - Anos Finais. — descrição gerada por IA. |
| `QT_TUR_MED` | INTEGER | Quantidade total de turmas do Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_PROF` | INTEGER | Quantidade total de turmas de Educação Profissional. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC` | INTEGER | Quantidade de turmas de Educação Profissional Técnica de Nível Médio. — descrição gerada por IA. |
| `QT_TUR_EJA` | INTEGER | Quantidade total de turmas de Educação de Jovens e Adultos (EJA). — descrição gerada por IA. |
| `QT_TUR_EJA_FUND` | INTEGER | Quantidade de turmas de EJA de Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_EJA_MED` | INTEGER | Quantidade de turmas de EJA de Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_ESP` | INTEGER | Quantidade total de turmas voltadas para Educação Especial. — descrição gerada por IA. |
| `QT_TUR_ESP_CC` | INTEGER | Quantidade de turmas de Educação Especial em classes comuns/regulares. — descrição gerada por IA. |
| `QT_TUR_ESP_CE` | INTEGER | Quantidade de turmas exclusivas de Educação Especial (classes especiais). — descrição gerada por IA. |
| `QT_TUR_BAS_D` | INTEGER | Quantidade de turmas de Educação Básica no turno diurno. — descrição gerada por IA. |
| `QT_TUR_BAS_N` | INTEGER | Quantidade de turmas de Educação Básica no turno noturno. — descrição gerada por IA. |
| `QT_TUR_BAS_EAD` | INTEGER | Quantidade de turmas de Educação Básica na modalidade EAD. — descrição gerada por IA. |
| `QT_TUR_INF_INT` | INTEGER | Quantidade de turmas de Educação Infantil em tempo integral. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_INT` | INTEGER | Quantidade de turmas de Creche em tempo integral. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_INT` | INTEGER | Quantidade de turmas de Pré-escola em tempo integral. — descrição gerada por IA. |
| `QT_TUR_FUND_INT` | INTEGER | Quantidade de turmas de Ensino Fundamental em tempo integral. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_INT` | INTEGER | Quantidade de turmas de Ensino Fundamental - Anos Iniciais em tempo integral. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_INT` | INTEGER | Quantidade de turmas de Ensino Fundamental - Anos Finais em tempo integral. — descrição gerada por IA. |
| `QT_TUR_MED_INT` | INTEGER | Quantidade de turmas de Ensino Médio em tempo integral. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_1` | INTEGER | Quantidade de turmas de 1º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_2` | INTEGER | Quantidade de turmas de 2º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_3` | INTEGER | Quantidade de turmas de 3º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_4` | INTEGER | Quantidade de turmas de 4º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_5` | INTEGER | Quantidade de turmas de 5º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_MULTIETAPA` | INTEGER | Quantidade de turmas multietapa dos Anos Iniciais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_6` | INTEGER | Quantidade de turmas de 6º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_7` | INTEGER | Quantidade de turmas de 7º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_8` | INTEGER | Quantidade de turmas de 8º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_9` | INTEGER | Quantidade de turmas de 9º ano do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_MULTI` | INTEGER | Quantidade de turmas multietapa dos Anos Finais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_CORRFLUXO` | INTEGER | Quantidade de turmas de correção de fluxo nos Anos Finais do Ensino Fundamental. — descrição gerada por IA. |
| `QT_TUR_MED_PROP` | INTEGER | Quantidade de turmas de Ensino Médio Propropedeutico/Regular. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_1` | INTEGER | Quantidade de turmas de 1ª série do Ensino Médio Propropedeutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_2` | INTEGER | Quantidade de turmas de 2ª série do Ensino Médio Propropedeutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_3` | INTEGER | Quantidade de turmas de 3ª série do Ensino Médio Propropedeutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_4` | INTEGER | Quantidade de turmas de 4ª série do Ensino Médio Propropedeutico. — descrição gerada por IA. |
| `QT_TUR_MED_PROP_NS` | INTEGER | Quantidade de turmas de Ensino Médio Propedeutico não seriado. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT` | INTEGER | Quantidade de turmas de Ensino Médio integrado à Formação Técnica Integrada Continuada. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_1` | INTEGER | Quantidade de turmas de 1ª série do Ensino Médio Técnico Integrado. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_2` | INTEGER | Quantidade de turmas de 2ª série do Ensino Médio Técnico Integrado. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_3` | INTEGER | Quantidade de turmas de 3ª série do Ensino Médio Técnico Integrado. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_4` | INTEGER | Quantidade de turmas de 4ª série do Ensino Médio Técnico Integrado. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_CT_NS` | INTEGER | Quantidade de turmas de Ensino Médio Técnico Integrado não seriado. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP` | INTEGER | Quantidade de turmas de Ensino Médio integrado com qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_1` | INTEGER | Quantidade de turmas de 1ª série do Ensino Médio com qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_2` | INTEGER | Quantidade de turmas de 2ª série do Ensino Médio com qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_3` | INTEGER | Quantidade de turmas de 3ª série do Ensino Médio com qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_4` | INTEGER | Quantidade de turmas de 4ª série do Ensino Médio com qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_QP_NS` | INTEGER | Quantidade de turmas não seriadas de Ensino Médio com qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_NM` | INTEGER | Quantidade de turmas do Normal/Magistério em nível médio. — descrição gerada por IA. |
| `QT_TUR_MED_NM_1` | INTEGER | Quantidade de turmas de 1ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_2` | INTEGER | Quantidade de turmas de 2ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_3` | INTEGER | Quantidade de turmas de 3ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_NM_4` | INTEGER | Quantidade de turmas de 4ª série do Normal/Magistério. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_EXC` | INTEGER | Quantidade de turmas exclusivas de itinerário formativo aprofundado do Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_EXC` | INTEGER | Quantidade de turmas exclusivas de itinerário técnico profissionalizante no Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_IFTP_EXC_QP` | INTEGER | Quantidade de turmas exclusivas de itinerário técnico com qualificação profissional. — descrição gerada por IA. |
| `QT_TUR_MED_IFA` | INTEGER | Quantidade de turmas de itinerário formativo aprofundado no Ensino Médio. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_LING` | INTEGER | Quantidade de turmas de itinerário formativo em Linguagens e suas Tecnologias. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_MATE` | INTEGER | Quantidade de turmas de itinerário formativo em Matemática e suas Tecnologias. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_CIENC` | INTEGER | Quantidade de turmas de itinerário formativo em Ciências da Natureza. — descrição gerada por IA. |
| `QT_TUR_MED_IFA_HUMA` | INTEGER | Quantidade de turmas de itinerário formativo em Ciências Humanas e Sociais Aplicadas. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_CONC` | INTEGER | Quantidade de turmas de Educação Profissional Técnica Concomitante. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_SUBS` | INTEGER | Quantidade de turmas de Educação Profissional Técnica Subsequente. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_MISTO` | INTEGER | Quantidade de turmas de Educação Profissional Técnica concomitante e subsequente. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_IFTP_CT` | INTEGER | Quantidade de turmas de curso técnico integrado no ensino médio. — descrição gerada por IA. |
| `QT_TUR_PROF_NAO_TEC` | INTEGER | Quantidade de turmas de Educação Profissional não técnica. — descrição gerada por IA. |
| `QT_TUR_PROF_IFTP_QP` | INTEGER | Quantidade de turmas de qualificação profissional na educação profissional. — descrição gerada por IA. |
| `QT_TUR_PROF_FIC_CONC` | INTEGER | Quantidade de turmas de Formação Inicial e Continuada (FIC) concomitantes. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_NPROF` | INTEGER | Quantidade de turmas de EJA Fundamental não profissionalizante. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_AI` | INTEGER | Quantidade de turmas de EJA Fundamental dos Anos Iniciais. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_AF` | INTEGER | Quantidade de turmas de EJA Fundamental dos Anos Finais. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_FIC` | INTEGER | Quantidade de turmas de EJA Fundamental articuladas com FIC. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_NPROF` | INTEGER | Quantidade de turmas de EJA Médio não profissionalizante. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_FIC` | INTEGER | Quantidade de turmas de EJA Médio articuladas com FIC. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_TEC` | INTEGER | Quantidade de turmas de EJA Médio articuladas com Educação Técnica. — descrição gerada por IA. |
| `QT_TUR_BAS_DM` | INTEGER | Quantidade de turmas de Educação Básica no turno da manhã. — descrição gerada por IA. |
| `QT_TUR_BAS_DV` | INTEGER | Quantidade de turmas de Educação Básica no turno da tarde (vespertino). — descrição gerada por IA. |
| `QT_TUR_INF_CRE_D` | INTEGER | Quantidade de turmas de Creche no período diurno. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_DM` | INTEGER | Quantidade de turmas de Creche no período da manhã. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_DV` | INTEGER | Quantidade de turmas de Creche no período da tarde. — descrição gerada por IA. |
| `QT_TUR_INF_CRE_N` | INTEGER | Quantidade de turmas de Creche no período noturno. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_D` | INTEGER | Quantidade de turmas de Pré-escola no período diurno. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_DM` | INTEGER | Quantidade de turmas de Pré-escola no período da manhã. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_DV` | INTEGER | Quantidade de turmas de Pré-escola no período da tarde. — descrição gerada por IA. |
| `QT_TUR_INF_PRE_N` | INTEGER | Quantidade de turmas de Pré-escola no período noturno. — descrição gerada por IA. |
| `QT_TUR_FUND_D` | INTEGER | Quantidade de turmas de Ensino Fundamental no período diurno. — descrição gerada por IA. |
| `QT_TUR_FUND_DM` | INTEGER | Quantidade de turmas de Ensino Fundamental no período da manhã. — descrição gerada por IA. |
| `QT_TUR_FUND_DV` | INTEGER | Quantidade de turmas de Ensino Fundamental no período da tarde. — descrição gerada por IA. |
| `QT_TUR_FUND_N` | INTEGER | Quantidade de turmas de Ensino Fundamental no período noturno. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_D` | INTEGER | Quantidade de turmas de Anos Iniciais no período diurno. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_DM` | INTEGER | Quantidade de turmas de Anos Iniciais no período da manhã. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_DV` | INTEGER | Quantidade de turmas de Anos Iniciais no período da tarde. — descrição gerada por IA. |
| `QT_TUR_FUND_AI_N` | INTEGER | Quantidade de turmas de Anos Iniciais no período noturno. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_D` | INTEGER | Quantidade de turmas de Anos Finais no período diurno. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_DM` | INTEGER | Quantidade de turmas de Anos Finais no período da manhã. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_DV` | INTEGER | Quantidade de turmas de Anos Finais no período da tarde. — descrição gerada por IA. |
| `QT_TUR_FUND_AF_N` | INTEGER | Quantidade de turmas de Anos Finais no período noturno. — descrição gerada por IA. |
| `QT_TUR_MED_D` | INTEGER | Quantidade de turmas de Ensino Médio no período diurno. — descrição gerada por IA. |
| `QT_TUR_MED_DM` | INTEGER | Quantidade de turmas de Ensino Médio no período da manhã. — descrição gerada por IA. |
| `QT_TUR_MED_DV` | INTEGER | Quantidade de turmas de Ensino Médio no período da tarde. — descrição gerada por IA. |
| `QT_TUR_MED_N` | INTEGER | Quantidade de turmas de Ensino Médio no período noturno. — descrição gerada por IA. |
| `QT_TUR_MED_EAD` | INTEGER | Quantidade de turmas de Ensino Médio na modalidade a distância. — descrição gerada por IA. |
| `QT_TUR_PROF_D` | INTEGER | Quantidade de turmas de Educação Profissional no período diurno. — descrição gerada por IA. |
| `QT_TUR_PROF_DM` | INTEGER | Quantidade de turmas de Educação Profissional no período da manhã. — descrição gerada por IA. |
| `QT_TUR_PROF_DV` | INTEGER | Quantidade de turmas de Educação Profissional no período da tarde. — descrição gerada por IA. |
| `QT_TUR_PROF_N` | INTEGER | Quantidade de turmas de Educação Profissional no período noturno. — descrição gerada por IA. |
| `QT_TUR_PROF_EAD` | INTEGER | Quantidade de turmas de Educação Profissional a distância. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_D` | INTEGER | Quantidade de turmas de Educação Técnica no período diurno. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_DM` | INTEGER | Quantidade de turmas de Educação Técnica no período da manhã. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_DV` | INTEGER | Quantidade de turmas de Educação Técnica no período da tarde. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_N` | INTEGER | Quantidade de turmas de Educação Técnica no período noturno. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_EAD` | INTEGER | Quantidade de turmas de Educação Técnica a distância. — descrição gerada por IA. |
| `QT_TUR_EJA_D` | INTEGER | Quantidade de turmas de EJA no período diurno. — descrição gerada por IA. |
| `QT_TUR_EJA_DM` | INTEGER | Quantidade de turmas de EJA no período da manhã. — descrição gerada por IA. |
| `QT_TUR_EJA_DV` | INTEGER | Quantidade de turmas de EJA no período da tarde. — descrição gerada por IA. |
| `QT_TUR_EJA_N` | INTEGER | Quantidade de turmas de EJA no período noturno. — descrição gerada por IA. |
| `QT_TUR_EJA_EAD` | INTEGER | Quantidade de turmas de EJA a distância. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_D` | INTEGER | Quantidade de turmas de EJA Fundamental no período diurno. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_DM` | INTEGER | Quantidade de turmas de EJA Fundamental no período da manhã. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_DV` | INTEGER | Quantidade de turmas de EJA Fundamental no período da tarde. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_N` | INTEGER | Quantidade de turmas de EJA Fundamental no período noturno. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_EAD` | INTEGER | Quantidade de turmas de EJA Fundamental a distância. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_D` | INTEGER | Quantidade de turmas de EJA Médio no período diurno. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_DM` | INTEGER | Quantidade de turmas de EJA Médio no período da manhã. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_DV` | INTEGER | Quantidade de turmas de EJA Médio no período da tarde. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_N` | INTEGER | Quantidade de turmas de EJA Médio no período noturno. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_EAD` | INTEGER | Quantidade de turmas de EJA Médio a distância. — descrição gerada por IA. |
| `QT_TUR_ESP_D` | INTEGER | Quantidade de turmas de Educação Especial no período diurno. — descrição gerada por IA. |
| `QT_TUR_ESP_DM` | INTEGER | Quantidade de turmas de Educação Especial no período da manhã. — descrição gerada por IA. |
| `QT_TUR_ESP_DV` | INTEGER | Quantidade de turmas de Educação Especial no período da tarde. — descrição gerada por IA. |
| `QT_TUR_ESP_N` | INTEGER | Quantidade de turmas de Educação Especial no período noturno. — descrição gerada por IA. |
| `QT_TUR_ESP_EAD` | INTEGER | Quantidade de turmas de Educação Especial a distância. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_D` | INTEGER | Quantidade de turmas inclusivas (Classe Comum) no período diurno. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_DM` | INTEGER | Quantidade de turmas inclusivas (Classe Comum) no período da manhã. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_DV` | INTEGER | Quantidade de turmas inclusivas (Classe Comum) no período da tarde. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_N` | INTEGER | Quantidade de turmas inclusivas (Classe Comum) no período noturno. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_EAD` | INTEGER | Quantidade de turmas inclusivas (Classe Comum) a distância. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_D` | INTEGER | Quantidade de turmas exclusivas de Educação Especial no período diurno. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_DM` | INTEGER | Quantidade de turmas exclusivas de Educação Especial no período da manhã. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_DV` | INTEGER | Quantidade de turmas exclusivas de Educação Especial no período da tarde. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_N` | INTEGER | Quantidade de turmas exclusivas de Educação Especial no período noturno. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_EAD` | INTEGER | Quantidade de turmas exclusivas de Educação Especial a distância. — descrição gerada por IA. |
| `QT_TUR_BAS_INT` | INTEGER | Quantidade total de turmas de Educação Básica em tempo integral. — descrição gerada por IA. |
| `QT_TUR_PROF_INT` | INTEGER | Quantidade de turmas de Educação Profissional em tempo integral. — descrição gerada por IA. |
| `QT_TUR_PROF_TEC_INT` | INTEGER | Quantidade de turmas de Educação Técnica em tempo integral. — descrição gerada por IA. |
| `QT_TUR_EJA_INT` | INTEGER | Quantidade de turmas de EJA em tempo integral. — descrição gerada por IA. |
| `QT_TUR_EJA_FUND_INT` | INTEGER | Quantidade de turmas de EJA Fundamental em tempo integral. — descrição gerada por IA. |
| `QT_TUR_EJA_MED_INT` | INTEGER | Quantidade de turmas de EJA Médio em tempo integral. — descrição gerada por IA. |
| `QT_TUR_ESP_INT` | INTEGER | Quantidade de turmas de Educação Especial em tempo integral. — descrição gerada por IA. |
| `QT_TUR_ESP_CC_INT` | INTEGER | Quantidade de turmas inclusivas (Classe Comum) em tempo integral. — descrição gerada por IA. |
| `QT_TUR_ESP_CE_INT` | INTEGER | Quantidade de turmas exclusivas de Educação Especial em tempo integral. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_PORT` | INTEGER | Quantidade de turmas com a disciplina de Língua Portuguesa. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_EDUC_FISICA` | INTEGER | Quantidade de turmas com a disciplina de Educação Física. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_ARTES` | INTEGER | Quantidade de turmas com a disciplina de Artes. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_ING` | INTEGER | Quantidade de turmas com a disciplina de Língua Inglesa. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_ESPA` | INTEGER | Quantidade de turmas com a disciplina de Língua Espanhola. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_FRANC` | INTEGER | Quantidade de turmas com a disciplina de Língua Francesa. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_OUTRA` | INTEGER | Quantidade de turmas com outra língua estrangeira. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LIBRAS` | INTEGER | Quantidade de turmas com disciplina/ensino de Libras. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_LINGUA_INDIG` | INTEGER | Quantidade de turmas com a disciplina de Língua Indígena. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PORT_SEG_LINGUA` | INTEGER | Quantidade de turmas com Língua Portuguesa como Segunda Língua. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_MATEMATICA` | INTEGER | Quantidade de turmas com a disciplina de Matemática. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_CIENCIAS` | INTEGER | Quantidade de turmas com a disciplina de Ciências. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_FISICA` | INTEGER | Quantidade de turmas com a disciplina de Física. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_QUIMICA` | INTEGER | Quantidade de turmas com a disciplina de Química. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_BIOLOGIA` | INTEGER | Quantidade de turmas com a disciplina de Biologia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_HISTORIA` | INTEGER | Quantidade de turmas com a disciplina de História. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_GEOGRAFIA` | INTEGER | Quantidade de turmas com a disciplina de Geografia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_SOCIOLOGIA` | INTEGER | Quantidade de turmas com a disciplina de Sociologia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_FILOSOFIA` | INTEGER | Quantidade de turmas com a disciplina de Filosofia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_EST_SOCIAIS` | INTEGER | Quantidade de turmas com a disciplina de Estudos Sociais. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_EST_SOCIAIS_SOCI` | INTEGER | Quantidade de turmas com Estudos Sociais/Sociologia. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_INFO_COMPUTACAO` | INTEGER | Quantidade de turmas com a disciplina de Informática/Computação. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_ENSINO_RELIGIOSO` | INTEGER | Quantidade de turmas com a disciplina de Ensino Religioso. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PROFISSIONA` | INTEGER | Quantidade de turmas com disciplinas profissionalizantes. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_ESTAGIO_SUPER` | INTEGER | Quantidade de turmas com componente de Estágio Supervisionado. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PEDAGOGICAS` | INTEGER | Quantidade de turmas com disciplinas pedagógicas. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_PROJETO_DE_VIDA` | INTEGER | Quantidade de turmas com a disciplina/componente Projeto de Vida. — descrição gerada por IA. |
| `QT_TUR_BAS_DISC_OUTRAS` | INTEGER | Quantidade de turmas com outras disciplinas não especificadas. — descrição gerada por IA. |
| `QT_TUR_BAS_LIBRAS` | INTEGER | Quantidade de turmas da educação básica com uso de Libras. — descrição gerada por IA. |
