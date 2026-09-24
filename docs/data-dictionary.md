# Data dictionary

This dictionary describes the fields emitted by the synthetic PNCP release path. It is a contract for the repository example, not a substitute for the current source schema.

| Layer | Field | Meaning | Release rule |
|---|---|---|---|
| Raw | `id` | Source record identifier in the fixture. | Retained for lineage. |
| Raw | `updated_at` | Source update timestamp in the fixture. | Retained for incremental processing. |
| Raw | `item` | Synthetic procurement item description. | Retained after direct-identifier-like free text is redacted. |
| Raw | `source_id` | Registry source identifier. | Added by the pipeline. |
| Raw | `identifier_classification` | Result of document classification. | Only `organization` reaches a released layer. |
| Raw | `golden_organization_id` | SHA-256 derived organization linkage key. | Replaces the supplier document; it is not an identity or qualification claim. |
| Trusted | Raw fields except `source_id` | Latest eligible record per natural key. | Direct supplier fields remain prohibited. |
| Semantic | Trusted fields plus `natural_key` | Analysis-facing record identity. | Direct supplier fields remain prohibited. |

The privacy policy redacts CPF-like and email-like text before it writes a layer. The audit then blocks the keys `cpf`, `email`, `phone`, `address`, `supplier_document`, `supplier_name`, and `name`, plus any identifier-like value that remains in a retained string.
