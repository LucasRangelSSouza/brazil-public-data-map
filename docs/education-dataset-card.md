# Dataset card: Brazil education data lake

## Status

Kaggle hosts version 1 as [Brazil Education Data Lake: SIOPE 2019-2023](https://www.kaggle.com/datasets/lucasrangelss/brazil-education-data-lake): 27,830 municipality-year records for 2019 through 2023. The [release evidence](evidence/education-kaggle-release-v1.md) records the manifest hash and the clean-download check.

## Content

One record per municipality and year, from the annual (sixth-bimester) municipal declarations to FNDE's SIOPE, joined to the IBGE municipality reference. Coverage years and row counts are facts of each release manifest.

| Field | Meaning | Source |
|---|---|---|
| `id` | `<municipality_code>-<year>` | derived |
| `updated_at` | Declaration date of the latest declaration kept for that municipality-year | SIOPE `DAT_DECL` |
| `year` | Reporting year | SIOPE `NUM_ANO` |
| `municipality_code` | Seven-digit IBGE code | IBGE Localidades `id`, matched on the six-digit SIOPE `COD_MUNI` |
| `municipality_name` | Official municipality name | IBGE Localidades `nome` |
| `state_code` | Two-letter state | IBGE Localidades |
| `population` | Population used in the declaration | SIOPE `NUM_POPU` |
| `total_revenue_realized` | Realized revenue reported in SIOPE general data, BRL | SIOPE `VAL_RECE_REAL` |
| `total_expenditure_paid` | Paid expenditure reported in SIOPE general data, BRL. This is the municipality-wide total, not education spending. | SIOPE `VAL_DESP_PAGA` |
| `mde_minimum_share_pct` | Share of tax and transfer revenue applied to education maintenance and development (constitutional minimum 25%) | SIOPE indicator 24 |
| `fundeb_remuneration_share_pct` | Share of FUNDEB applied to education-professional pay (minimum 70% under the FUNDEB rules in force from 2021) | SIOPE indicator 67 |
| `fundeb_unspent_share_pct` | Share of FUNDEB revenue not applied in the year (maximum 10%) | SIOPE indicator 27 |
| `education_share_of_total_expenditure_pct` | Education expenditure as a share of expenditure in all areas | SIOPE indicator 35 |
| `investment_per_basic_education_student` | Educational investment per basic-education student, BRL | SIOPE indicator 56 |
| `identifier_classification` | Always `not_present`: the table carries no supplier or person identifier | pipeline |
| `natural_key` | Semantic-layer identity, equal to `id` | pipeline |

Indicator values are the declared values as FNDE computes them. They are not audited figures. A missing indicator is null. Indicator 67 is not defined in the same form before 2021, so earlier years are expected to be null there.

## Exclusions

The package leaves out the SIOPE responsible-person entity (names, emails, phones, addresses), free-text justifications, rectification narratives, the receipt number, and every column outside the list above. State-level declarations are out of scope for version 1.

## Terms

SIOPE data is published by FNDE through its open-data service, and the IBGE reference through the IBGE locality API. Neither page states a dataset-specific license. The federal open-data policy (Decree 8,777/2016, art. 2, III) defines open data as released under a license that allows free use, limited to crediting authorship or source. The package therefore uses Kaggle's `other` setting, credits FNDE and IBGE, and asserts no new license over their data. Apache-2.0 covers this repository's code only.

## Reproduce

```powershell
python -m brazil_data_map capture-siope --start-year 2019 --end-year 2023 --output .local-siope-capture
python -m brazil_data_map build-education-release --capture .local-siope-capture --output .local-edu-a --retrieved-at <capture time> --git-commit <commit>
```

Two builds from the same capture must produce identical manifests. The live SIOPE service can change as municipalities rectify declarations, so a new capture may differ from the published version; the published manifest remains the reference.
