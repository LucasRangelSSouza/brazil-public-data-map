# Public data is not automatically privacy-safe

The [PNCP open-data service](https://www.gov.br/pncp/pt-br/acesso-a-informacao/dados-abertos) makes procurement information available for consultation and download without registration. That access is useful for researchers, journalists, suppliers, and public bodies. It still leaves a practical question for anyone repackaging a dataset: which fields are necessary for the stated analysis, and which fields create avoidable exposure?

The question is wider than procurement. INEP's own [microdata guidance](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados) explains that public releases need privacy controls when detailed records can identify people. A public URL is therefore a starting point for a release decision, not the end of one.

This repository treats that boundary as software. The PNCP fixture enters an identifier policy before any raw, trusted, or semantic layer is built. A fourteen-digit supplier document becomes an organization candidate. An eleven-digit document becomes a natural-person record and is excluded. Any other value remains unknown and is excluded as well.

The organization path removes the source document and derives a stable `golden_organization_id`. That key supports linkage between eligible organization records. It does not prove ownership, qualification, legal status, or the suitability of a supplier.

The gate also blocks direct CPF, email, phone, and address fields. This matters because a release pipeline has more surfaces than a final table. Fixtures, logs, screenshots, tracing systems, and sample notebooks can all recreate the same exposure if they bypass the policy.

The release manifest records source lineage, file hashes, and the privacy gate status. A missing approval blocks the manifest. The incremental fixture tests pagination, a transient failure, duplicate records, and convergence to the latest natural key. These are ordinary software behaviors, which is why the privacy control belongs beside them.

The implementation is intentionally narrow. It uses synthetic records, does not claim legal certification, and does not publish to Kaggle yet. Its contribution is a testable release gate that can travel with the public-source pipeline when a reviewed dataset becomes ready. The claim-to-evidence map is kept with the article in [public-data-release-claim-map.md](public-data-release-claim-map.md).
