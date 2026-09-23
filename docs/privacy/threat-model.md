# Privacy threat model

The release boundary faces five main risks: natural-person supplier identifiers, free-text leakage, fixture leakage, logs or traces that retain raw fields, and linkage beyond the intended organization-level analysis. The current gate excludes natural-person and unknown supplier documents and blocks direct contact fields.

Residual risk remains. A public record can contain context that enables re-identification when combined with other sources. The release process therefore minimizes fields, keeps document links as metadata rather than copied binaries, reviews schemas, and treats a passed gate as a technical control rather than legal certification.

