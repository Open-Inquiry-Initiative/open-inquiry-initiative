# OII-OPS-001 — Dual-Track Research & Development Protocol

**Version:** 0.1.0 (proposed)  
**Date:** 2026-11-19  
**Owner:** Open Inquiry Initiative  
**Status:** Working policy; pending maintainer review and merge

## Purpose
Preserve open-ended discovery without interrupting disciplined engineering. Maintain traceable research records and promote selected ideas into reproducible prototypes.

## Track A — Engineering and Delivery
Track A owns specifications, implementation, tests, integration, validation, demonstrations and release readiness. Reality OS is its first time-boxed priority.

### Reality OS 72-hour target
Start: 2026-11-19 20:30 America/Chicago. Deadline: 2026-11-22 20:30 America/Chicago.

Target: a demonstrable, reproducible alpha candidate that can (1) launch a spatial environment, (2) navigate at least two environments, (3) persist and restore workspace state, (4) recover from failed environment loading, and (5) build and test from documented instructions. Report measured results, blockers and limitations; do not claim success without evidence.

Existing Three.js/browser and Linux/native-shell initiatives are sub-workstreams within Track A. Preserve compatibility and safe rollback. No unreviewed merges, host boot changes, or automatic publication.

## Track B — Exploration and Research Intake
Capture substantive ideas from conversations, social media, references and experiments without disrupting Track A. For each substantive discussion, prepare one or more designated research records, with separate identifiers for distinct branches. Use the pattern `OII-B-YYYYMMDD-NNN` (assign the next available number after checking the registry to prevent collisions).

Each record includes:
- Title, identifier, date, author/source context and status
- Summary and research questions
- Hypotheses clearly distinguished from evidence
- References, related projects and branch relationships
- Methods, preliminary findings, limitations and next steps
- Privacy, licensing and publication review
- Promotion decision/status

Initial records may be a README in an existing repository; a new repository is optional, not required. Records are committed only through an authorized workflow; conversation alone does not guarantee automatic GitHub synchronization.

## Promotion gate: B → A
Promote only when scope, feasibility, evidence, priority, ownership, acceptance criteria and resource constraints are sufficiently defined. Preserve the originating Track B record and cross-link implementation artifacts. Rejected or deferred concepts remain searchable in Track B.

## Publication and preservation
Public by default **after review**, not immediately or indiscriminately. Protect personal/family data, credentials, sensitive telemetry, unsafe details, third-party rights and restricted material. Preserve raw evidence privately when public disclosure is unsuitable. Distinguish hypothesis, prototype, validated result and published release. Preserve checksums, provenance, test logs, negative findings and reproducibility instructions where appropriate.

## Workflow and governance
1. Capture and classify new research into Track B.
2. Write designated records at the conclusion of substantive research discussions; identify branches separately.
3. Review for sensitivity, licensing, duplication and accuracy before GitHub publication.
4. Promote qualified records to Track A through an explicit decision.
5. Implement in reviewable increments with regression tests, documentation and rollback.
6. Require maintainer review before merging or changing visibility.
7. Revisit this protocol through versioned amendments; do not silently redefine track labels.

## Scope clarification
This policy supersedes earlier use of “Track A” for Three.js and “Track B” for Linux. Both are now engineering workstreams under the new Track A; the new Track B is research intake.
