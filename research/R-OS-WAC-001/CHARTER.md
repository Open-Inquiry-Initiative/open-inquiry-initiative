# R-OS-WAC-001 — Worlds as Code

Authorized 2026-11-28. Parent programs: Reality OS and OII-OEI-001. Status: authorized, not qualified.

## Objective
Evaluate 3DCodeVerse (https://github.com/gaoypeng/3dcodeverse) for executable, editable, verifiable persistent environments. Preserve existing Reality OS as control. Compare native generation, Hydra-assisted generation, and persistent reconstruction.

## Gates
- G00: Pin upstream revision; verify provenance, code and dataset licenses separately, dependencies and execution risks. No unreviewed dataset ingestion.
- G01: Sandbox CPU-first generation using small cleared fixtures; compare standalone agent and existing baseline. Record execution, visual fidelity, latency, failures and resource use.
- G02: Isolated Three.js adapter; validate scene schema, collision, resource disposal, navigation and fallback.
- G03: Matched Hydra versus standalone generation; preregister seeds and thresholds, measure correctness, wrong accepts, cost and latency.
- G04: Save/reload/edit/reconstruct generated rooms; test deterministic manifests and rollback.
- G05: Optional hybrid mesh/splat integration with existing portal tests.
- G06: Qualify on RTX 2070 SUPER and independent environments where available.

## Safeguards
Treat generated code as untrusted. No credentials, host filesystem access or unrestricted network in execution sandbox. Enforce time/memory limits and independent checks. No production deployment or dependency adoption before qualification. Publish cleared evidence, limitations and negative results; preserve private originals. Upstream claims remain unverified until reproduced. This charter is authorization to investigate, not evidence of successful integration.
