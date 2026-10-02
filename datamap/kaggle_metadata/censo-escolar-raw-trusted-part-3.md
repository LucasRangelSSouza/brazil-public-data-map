# School Census (INEP): Raw and Trusted

30 tables, 55,639,423 rows, snapshot 2026-10-01. Yearly School Census microdata at school level: schools, classes, teachers, enrolments and infrastructure, with the historical series recovered from 1995. Student-level and teacher-level microdata are not released.

## Where the data comes from

- **Publisher:** Instituto Nacional de Estudos e Pesquisas Educacionais Anísio Teixeira (INEP)
- **Official source:** https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar
- **How it is fetched:** INEP publishes one ZIP of microdata per year on the open-data page. Download the year, read the CSV inside and apply the data dictionary shipped in the same ZIP.
- **Grain and keys:** School by year for the school tables; the semantic tables aggregate to school-year and municipality-year. The 2025 edition changed the enrolment file from student level to school-level aggregates.

## How the files are organised

Every table is one Parquet file at the dataset root, named `<layer>__<table>.parquet`. `raw` is the source snapshot as delivered; `trusted` is typed, deduplicated and consistently named. `release_manifest.json` holds the SHA-256 and size of every file, `schemas.json` the schema of every table and `audit.json` the export counts.

## Documentation, field by field

- Interactive data map (search, lineage, joins): https://rangeltech.net/datamap/#/dataset/censo-escolar-raw-trusted-part-3
- Data dictionary of this dataset, every column: https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/docs/datamap/censo-escolar-raw-trusted-part-3.md
- How the raw layer is obtained from the official source (notebook): https://github.com/LucasRangelSSouza/brazil-public-data-map/blob/main/notebooks/sources/censo-escolar.ipynb
- Code and release contracts: https://github.com/LucasRangelSSouza/brazil-public-data-map

Column descriptions come from the source lake's catalogue, in Portuguese; a share is marked there as AI generated. They are a reading aid, not a legal definition.

## Tables

| Layer | Table | Rows | Columns |
|---|---|---:|---:|
| raw | `inep_censo_escolar_curso_tecnico` | 32,136 | 25 |
| raw | `inep_censo_escolar_dados_desp` | 49,642 | 29 |
| raw | `inep_censo_escolar_dadoscurso` | 25,572 | 33 |
| raw | `inep_censo_escolar_educprof` | 323,177 | 184 |
| raw | `inep_censo_escolar_em11` | 19,617 | 21 |
| raw | `inep_censo_escolar_em12` | 58,310 | 18 |
| raw | `inep_censo_escolar_em22` | 1,201 | 22 |
| raw | `inep_censo_escolar_em8` | 24,893 | 24 |
| raw | `inep_censo_escolar_es6` | 406 | 20 |
| raw | `inep_censo_escolar_escola` | 214,192 | 307 |
| raw | `inep_censo_escolar_gestor_escolar` | 180,540 | 70 |
| raw | `inep_censo_escolar_indicesc` | 877,062 | 199 |
| raw | `inep_censo_escolar_indicreg` | 270,956 | 195 |
| raw | `inep_censo_escolar_matricula` | 178,766 | 242 |
| raw | `inep_censo_escolar_medprof` | 102,591 | 43 |
| raw | `inep_censo_escolar_microdados_ed_basica` | 4,058,464 | 479 |
| raw | `inep_censo_escolar_suplemento_cursos_tecnicos` | 50,740 | 34 |
| raw | `inep_censo_escolar_turma` | 178,772 | 195 |
| trusted | `inep_censo_escolar_colunas_fonte` | 29,684 | 8 |
| trusted | `inep_censo_escolar_cursos_tecnicos` | 82,876 | 39 |
| trusted | `inep_censo_escolar_dicionario_campos` | 28,786 | 11 |
| trusted | `inep_censo_escolar_docentes` | 4,237,236 | 160 |
| trusted | `inep_censo_escolar_educacao_profissional` | 4,911,299 | 295 |
| trusted | `inep_censo_escolar_escolas` | 7,376,443 | 102 |
| trusted | `inep_censo_escolar_etapas_ensino` | 4,808,966 | 713 |
| trusted | `inep_censo_escolar_gestores` | 4,239,004 | 69 |
| trusted | `inep_censo_escolar_infraestrutura` | 7,376,443 | 134 |
| trusted | `inep_censo_escolar_localizacao` | 7,427,183 | 39 |
| trusted | `inep_censo_escolar_matriculas` | 4,237,230 | 247 |
| trusted | `inep_censo_escolar_turmas` | 4,237,236 | 194 |

## Read a table

```python
import kagglehub, pandas as pd
path = kagglehub.dataset_download("lucasrangelss/censo-escolar-raw-trusted-part-3", path="raw__inep_censo_escolar_curso_tecnico.parquet")
df = pd.read_parquet(path)
```

Values are published as held in the snapshot, without masking. Source terms apply; credit the original publisher.

My portfolio: https://rangeltech.net
