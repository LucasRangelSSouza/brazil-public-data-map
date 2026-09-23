# Identifier governance

The PNCP release gate classifies a supplier document by normalized digit length. A fourteen-digit document is an organization candidate. An eleven-digit document is a natural-person record. Any other value is unknown. Natural-person and unknown records do not enter public layers.

For an organization candidate, the gate removes the source document and derives `golden_organization_id` from the normalized CNPJ. The derived value supports record linkage only. It does not establish legal status, ownership, eligibility, or identity.

The gate blocks direct CPF, email, phone, and address fields. Future extractors must run the same policy before they write fixtures, logs, screenshots, or release layers.

