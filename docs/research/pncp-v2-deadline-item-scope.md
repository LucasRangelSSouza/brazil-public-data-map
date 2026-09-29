# PNCP v2 deadline and item scope assessment

**Status:** research decision, not a release approval  
**Date:** 2026-09-28

## Question

Can a second PNCP release add proposal deadlines and procurement-item information while keeping the public-data contract narrow enough for a reproducible recommendation demonstration?

## Source capability

The official PNCP consultation material documents `dataEncerramentoProposta` as the closing date and time for proposal receipt. The current integration manual also documents a separate item endpoint, `GET /v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens`, whose response includes an item number, material-or-service classification, description, quantity, and unit of measure. The public listing endpoint already provides the organization CNPJ, purchase year, and purchase sequence needed to address that item route.

Sources:

- [PNCP data-access page](https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos)
- [PNCP consultation API manual, version 1.0](https://www.gov.br/pncp/pt-br/central-de-conteudo/manuais/versoes-anteriores/ManualPNCPAPIConsultasVerso1.0.pdf)
- [PNCP item-consultation manual, version 2.5](https://pncp.gov.br/manual/pt-br/2.5/contratacao/consultar_itens_de_uma_contratacao.html)

The public pages establish availability and technical access. They do not by themselves settle redistribution terms for a derived Parquet release. The v2 approval must repeat the source and distribution assessment at publication time.

## Proposed fields

The candidate starts with the v1 procurement fields and proposes the following additions.

| Field | Source field | Purpose | Proposed handling |
|---|---|---|---|
| `proposal_deadline_at` | `dataEncerramentoProposta` | Time-bounded opportunity filtering | Retain only as a parsed timestamp; reject malformed values. |
| `item_number` | `numeroItem` | Stable position within a procurement | Retain as an integer after uniqueness validation within the procurement key. |
| `item_kind` | `materialOuServico` | Material or service distinction | Retain only the documented domain value. |
| `item_quantity` | `quantidade` | Basic item scale | Retain as a non-negative numeric value. |
| `item_unit` | `unidadeMedida` | Quantity interpretation | Retain only after a length and identifier-pattern check. |
| `item_category` | derived from `descricao` | Retrieval and recommendation feature | Retain a controlled taxonomy only. Do not publish the source description in the first v2 candidate. |

`descricao` can contain up to 2,048 characters. It is therefore not approved for the first v2 public release. It may carry contacts, names, addresses, process references, or information unrelated to retrieval. Replacing it with a controlled category preserves a useful ranking feature while keeping the review surface bounded.

The candidate excludes document files, links to source systems, process links, justification fields, person names, contacts, addresses, supplier-result records, and the unbounded item description. It also excludes any field absent from the v2 allowlist.

## Required implementation gates

1. Add a dedicated item-fetch client with bounded pagination, retry handling, a request budget, and local checkpointing.
2. Build a new procurement-item grain. The natural key must combine the PNCP control identifier and item number; it must not collapse every item into the parent procurement record.
3. Add field validators for timestamp parsing, item-number uniqueness, non-negative quantity, and bounded unit text.
4. Classify and redact direct identifiers in every retained string. Exclude a string that cannot pass the gate.
5. Run the privacy audit, two deterministic builds, schema review, source/terms review, release approval, Kaggle upload, and clean-download verification.
6. Rebuild the recommendation index and report a separate evaluation. Historical data must remain labelled as historical; a deadline does not establish present eligibility or supplier fit.

## Decision

Proceed with a local v2 candidate only after the item client and the new privacy tests exist. The first candidate may contain a deadline, an item position, material-or-service classification, quantity, unit, and a controlled item category. It must not contain raw item descriptions. Publication remains blocked until all release gates pass.
