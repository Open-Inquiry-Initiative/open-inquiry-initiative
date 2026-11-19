# Open Inquiry Initiative — Public project map

This preview covers selected projects and research directions.

## Public research

| Project | Evidence status |
|---|---|
| [Planetary Systems Integration (PSI-001)](https://github.com/Open-Inquiry-Initiative/planetary-systems-integration) | Conceptual hypothesis with a proposed comparison. The project reports no measured outcomes. |
| [OCS Baseline Prototype](https://github.com/Talos-Labs-documents/ocs-baseline-prototype) | All 100 deterministic trial records matched in a [fresh reproduction](#ocs-reproduction). |

### OCS reproduction

On November 19, 2026, the preview reproduced the OCS v0.1.0 campaign from the [pinned source revision](https://github.com/Talos-Labs-documents/ocs-baseline-prototype/tree/e16b2ea002c2c510672ecf4d46f8d499c24cd180) on Windows 11 with CPython 3.15.2. All eight tests passed. The repository comparator and a separate direct comparison matched all 100 trial records after excluding only wall-clock runtime (`result.metrics.runtime_ms`).

Across the 25 synthetic scheduling instances, OCS scored better than the included baseline 7 times and tied 18 times before simulated resource removal. After removal, it scored better 6 times, tied 18 times, and scored worse once. These results apply to the published campaign and its scoring rule. Performance on other workloads and against other solvers remains open.

## Research directions

- **Reality OS** explores persistent spatial computing environments, recursive worlds, and human–AI tools. Public artifact mapping is pending.
- **Human–AI mutual grounding** explores how humans and AI establish, check, and repair shared task context. This preview presents it as proposed evaluation research.
- **Research cartography** explores how to map projects, assumptions, experiments, and uncertainty while preserving provenance. Public artifact mapping is pending.

See the [research status and evidence policy](RESEARCH_STATUS.md) for evidence requirements.
