# Public release contract

## Purpose

This contract defines the minimum evidence required before an extracted public-source package is distributed. It applies to the raw, trusted, and semantic layers described in the dataset card. It does not authorize collection, redistribution, or publication by itself.

## Required inputs

Each release candidate needs a source registry entry, a recorded retrieval window, a source-specific terms review, a privacy audit, and a file manifest. The registry is checked locally for a unique source identifier and an HTTPS official URL. The release owner records the actual terms review outside the code path because its conclusion depends on the source version and the intended distribution.

## Package gate

The pipeline builds all three layers from records that pass the identifier policy. Direct supplier documents, names, contacts, addresses, CPF-like values, and email-like values are prohibited in every layer. The audit returns record counts and fails on the first release candidate that contains a prohibited field or value pattern.

The manifest then records the declared package paths, SHA-256 hashes, byte counts, source lineage, and a `privacy_gate` status. It does not discover every file in an output directory, so stale files cannot silently enter a release record. A status other than `passed` prevents manifest validation. A valid manifest proves that the declared package matched this contract at the time it was built; it does not certify legal compliance or data quality.

## Release evidence

Store the following beside a future release without placing credentials or private infrastructure references in this repository:

- source terms review and retrieval window;
- privacy-audit result and record counts;
- manifest JSON and the exact package hashes;
- dataset card version, schema version, and change notes;
- reviewer decision for the proposed distribution channel.

## Operating boundary

The repository includes synthetic fixtures and local tests only. The future distribution target is intentionally absent until a reviewed public package and distribution account exist.
