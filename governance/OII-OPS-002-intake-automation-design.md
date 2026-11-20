# OII-OPS-002 — Research Intake Automation Design

**Status:** Proposed implementation specification (not deployed)  
**Depends on:** OII-OPS-001 governance review  
**Priority:** Secondary to the Reality OS 72-hour Track A demonstration

## Objective
Convert user-authorized, substantive research conversations into reviewable Track B records in GitHub without fabricating automatic access to chat history or claiming background execution.

## Trigger and consent
- A user instruction such as "document this research" or an authorized end-of-conversation handoff initiates intake.
- A chat response is not an always-on webhook. Unattended collection requires a separately configured, permissioned integration and explicit approval.
- Do not automatically export private conversations or personal details.

## Pipeline
1. **Capture:** Receive explicitly provided discussion text, links, files or approved structured summary.
2. **Segment:** Identify distinct research branches; preserve source references.
3. **Normalize:** Produce a record using TRACK-B-RESEARCH-RECORD.md. Label claims as observed, sourced, hypothesized or untested.
4. **Deduplicate:** Compare title, source fingerprint and related IDs against registry; flag near-duplicates for review.
5. **Classify:** Apply privacy, third-party licensing, security and safety review. Route sensitive records to authorized private preservation only.
6. **Reserve ID:** Read latest registry from target branch; allocate OII-B-YYYYMMDD-NNN; resolve concurrent collisions with fresh read and retry.
7. **Stage:** Commit to review branch in an appropriate repository. Default to draft PR for public-bound content; do not create one repo per idea.
8. **Verify:** Confirm file path, commit SHA, record completeness and registry linkage. Report any failed steps rather than claiming success.
9. **Promote:** Track A promotion only after explicit scope, feasibility, priority, resources and acceptance-criteria review.

## Proposed repository layout
`research/intake/YYYY/MM/OII-B-YYYYMMDD-NNN/README.md` for individual records, plus a versioned registry. The governance repository holds templates and procedures, not necessarily every research artifact.

## Acceptance tests
- One conversation, one topic → one correctly numbered record.
- One conversation, three distinct topics → three linked records.
- Duplicate input → review instead of duplicate publication.
- Concurrent requests for same next ID → unique IDs or blocked retry.
- Missing references → explicit unknowns, no invented citations.
- Personal/sensitive content → no public commit.
- Unauthorized third-party text → no wholesale republication.
- GitHub failure → clear error, no phantom record.
- Track A deadline activity → intake work cannot block or mutate the demo branch.
- Draft PR review → no auto-merge or visibility changes.

## Initial implementation gates
- **002-G1:** Confirm repositories, permissions, and current registry; define privacy decision tree.
- **002-G2:** Build local deterministic record generator and fixture tests.
- **002-G3:** Implement GitHub staging with collision detection and idempotency.
- **002-G4:** Validate private/public routing and failure recovery.
- **002-G5:** Pilot with one explicitly approved non-sensitive research discussion.
- **002-G6:** Document operation and propose release only after maintainer review.

## Explicit non-claims
No background ingestion, automatic transcript access, live agent, or GitHub sync has been implemented by this design document.
