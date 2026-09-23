# Public data is not automatically privacy-safe

The [PNCP open-data service](https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos) makes procurement information available for consultation and download without registration, so researchers, journalists, suppliers, and public bodies can work from the same official starting point. A dataset publisher still has to decide which fields serve the stated analysis and which create exposure the analysis does not need.

The question is wider than procurement. INEP's own [microdata guidance](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados) explains why public releases need privacy controls when detailed records can identify people, including when individual fields look harmless in isolation. A public URL is a starting point for a release decision.

This repository treats that boundary as software. Before it creates a raw, trusted, or semantic layer, the pipeline sends the PNCP fixture through an identifier policy that classifies each supplier document and keeps the rule visible in tests. A fourteen-digit supplier document becomes an organization candidate. The policy excludes an eleven-digit document as a natural-person record. It excludes any other value as unknown.

The organization path removes the source document and derives a stable `golden_organization_id`. That key supports linkage between eligible organization records. It says nothing about ownership, qualification, legal status, or whether a supplier suits a given opportunity.

The gate also blocks direct CPF, email, phone, and address fields. A release pipeline has more surfaces than a final table, and fixtures, logs, screenshots, tracing systems, or sample notebooks can recreate the same exposure when they bypass the policy. That is where a field-level rule earns its place.

The release manifest records source lineage, file hashes, and the privacy gate status. A missing approval blocks the manifest. The incremental fixture tests pagination, a transient failure, duplicate records, and convergence to the latest natural key. These are ordinary software behaviors, which is why the privacy control belongs beside them.

The implementation remains intentionally narrow. It uses synthetic records, makes no legal-certification claim, and does not publish to Kaggle yet. A reviewed dataset could reuse the same release gate alongside the public-source pipeline. The claim-to-evidence map is kept with the article in [public-data-release-claim-map.md](public-data-release-claim-map.md).
