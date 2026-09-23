# Golden organization ID without identity overreach

A stable key can make a public dataset easier to join. It can also invite claims the data cannot support. This repository uses a `golden_organization_id` for one narrow task: link eligible organization records after removing the original supplier document.

The policy starts with format classification. The classifier routes a fourteen-digit document to the organization candidate path, sends an eleven-digit document to the natural-person path, and labels every other value unknown. Only the organization path reaches a public layer. The code derives a SHA-256 key from the normalized document and then removes the document itself.

The derived key exposes only a stable linkage value. It supports consistent linkage inside a reviewed release, but it cannot show who owns an organization, whether the organization qualifies for an opportunity, whether a registration remains valid, or whether two records describe the same real-world business relationship. Those questions require evidence that this release does not carry.

The constraint matters in recommendation work. A model may rank a procurement record as relevant to a profile, yet the ranking should remain a relevance signal with a link back to the source record. It must not become a supplier endorsement or an eligibility decision merely because two records share a derived key.

The implementation makes that boundary visible. `apply_identifier_policy` excludes natural-person and unknown records, strips direct supplier fields, and creates the golden key only on the organization path. The fixture tests assert each behavior. The [identifier policy](../../contracts/identifier-policy.yaml) and [data dictionary](../data-dictionary.md) publish the same rule in reader-facing form.

This is a data-minimization pattern, not a privacy certificate. A future release still needs source-specific terms review, schema review, and a human decision about whether organization-level linkage remains necessary for the stated analysis.
