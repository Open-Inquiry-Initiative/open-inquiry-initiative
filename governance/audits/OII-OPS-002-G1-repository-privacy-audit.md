# OII-OPS-002-G1 — Repository and Privacy Boundary Audit

**Date:** 2026-11-19  
**Gate:** G1 — completed for repository-level discovery; content-level checks deferred  
**Source:** Connected GitHub repository metadata, not a full code/content security scan

## Verified repositories
| Repository | Visibility | Connected account access | Proposed role |
|---|---|---|---|
| open-inquiry-initiative | Public | Admin/push | Governance documents and sanitized public process |
| planetary-systems-integration | Public | Admin/push | Existing published project; not default intake |
| research-projects | Private | Admin/push | Track B draft research records, subject to review |
| research-archive | Private | Admin/push | Private source/evidence preservation |
| publication-staging | Private | Admin/push | Release review and sanitized publication candidates |
| ai-systems | Private | Admin/push | AI engineering artifacts, not generic intake |

All six report default branch `main`. Permissions and visibility are API metadata snapshots, not authorization to disclose any particular record.

## Routing policy
1. **Unreviewed discussion:** do not publish; stage only after explicit capture authorization in `research-projects` on a review branch.
2. **Sensitive/private source:** preserve only in an appropriately authorized private location, or withhold entirely if retention is not authorized.
3. **Public candidate:** produce a minimal sanitized summary, review source rights and privacy, then stage in `publication-staging` for approval. Its private visibility does not itself prove content is safe.
4. **Approved publication:** choose an appropriate public destination and obtain maintainer approval before merge or visibility change. No automated repository creation or public release.
5. **Governance:** `open-inquiry-initiative` holds protocols/templates only, not raw conversation dumps.

## Privacy decision tree
- Does capture include family/personal information, health, private correspondence, credentials, exact locations or other identifiers? **Yes:** redact or withhold; no public staging.
- Does source contain copyrighted/restricted third-party material or unclear licensing? **Yes/unknown:** link and summarize minimally; require review.
- Could the material disclose unsafe operational detail or secrets? **Yes/unknown:** hold for review.
- Are claims labeled by evidence status and provenance? **No:** revise before publication.
- Has publication been expressly authorized and reviewed? **No:** keep private/draft.
- Only then propose a public PR; never auto-merge.

## G1 findings
- Six organization repositories discovered: two public and four private.
- Connected account has push/admin permissions on all six.
- No repository visibility was changed.
- No sensitive data was read or moved during this metadata audit.
- No evidence yet that GitHub Actions, webhooks, tokens, branch protection, or per-path policies are configured.
- Content-level secrets scanning, effective branch protections and end-to-end permission checks remain **unverified** and must be completed before any automated public publication.

## G2 entry criteria
Implement an offline, deterministic, schema-validated record generator with synthetic fixtures only. Do not connect it to chat transcript retrieval or GitHub writes yet. Include deduplication hints and redaction flags; treat these as aids, not substitutes for review.
