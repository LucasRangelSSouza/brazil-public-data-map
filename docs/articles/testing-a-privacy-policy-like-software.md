# Testing a privacy policy like software

Privacy controls fail when they live only in a document. The most useful rule is the one that stops a bad release candidate in the same workflow that checks a malformed date or a missing column.

The release path in this project classifies supplier documents, removes direct supplier fields, scans retained string values for CPF-like and email-like patterns, and records the audit outcome before writing the manifest. When the audit fails, the release function raises an exception before it emits a manifest, which makes the failing record part of the engineering workflow instead of a warning for a later reader to interpret.

The tests cover three kinds of failure. First, the policy excludes an eleven-digit document from every public layer. Masking would leave a record that the stated analytical use case does not need. Second, a direct field such as `email` prevents a release. Third, identifier-like content in an otherwise allowed text field is redacted before layer construction, then the audit rejects any identifier-like content that remains. A safe schema can still carry unsafe text.

The same discipline applies outside the tables. The project keeps synthetic fixtures, validates the walkthrough notebook as JSON, and treats screenshots and logs as release surfaces that need the same minimization rule. A future operational pipeline should add trace redaction and checks against its own logging system before it handles live responses.

The tests cannot prove that a dataset is harmless. They do prove that a documented set of forbidden fields and patterns has a repeatable failure mode. A policy that runs before the data moves gives a reviewer something concrete to inspect.
