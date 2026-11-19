# Open Inquiry Initiative — Public project map

This preview covers selected projects and research directions.

## Public research

| Project | Evidence status |
|---|---|
| [Planetary Systems Integration (PSI-001)](https://github.com/Open-Inquiry-Initiative/planetary-systems-integration) | [Synthetic dispatch experiment](#psi-001-synthetic-dispatch-experiment) completed. No tested scenario met the 1% net savings threshold. |
| [OCS Baseline Prototype](https://github.com/Talos-Labs-documents/ocs-baseline-prototype) | All 100 deterministic trial records matched in a [fresh reproduction](#ocs-reproduction). |

### PSI-001 synthetic dispatch experiment

The preview ran 8,760 hourly electricity and district-heating dispatch steps with fixed equipment, no storage, and no ramping constraints. Both planners met all demand in the baseline, a 72-hour cold snap, and a 48-hour simulated thermal-trunk outage modeled as heat-pump unavailability.

| Scenario | Net savings with flat tariff | Net savings with hourly tariff |
|---|---:|---:|
| Baseline | 272,995 | −100,000 |
| Cold snap | 271,751 | −100,000 |
| Simulated thermal-trunk outage | 268,045 | −100,000 |

Values are rounded synthetic currency units. Net savings include an assumed annual coordination cost of 100,000 units. With a flat tariff for the independent planner, savings were about 0.57–0.58%, below the 1% threshold. With the same hourly prices available to both planners, dispatch decisions matched and coordination added its assumed overhead. The findings apply to the modeled scenarios. Field performance and independent reproduction remain open.

### OCS reproduction

On November 19, 2026, the preview reproduced the OCS v0.1.0 campaign from the [pinned source revision](https://github.com/Talos-Labs-documents/ocs-baseline-prototype/tree/e16b2ea002c2c510672ecf4d46f8d499c24cd180) on Windows 11 with CPython 3.15.2. All eight tests passed. The repository comparator and a separate direct comparison matched all 100 trial records after excluding only wall-clock runtime (`result.metrics.runtime_ms`).

Across the 25 synthetic scheduling instances, OCS scored better than the included baseline 7 times and tied 18 times before simulated resource removal. After removal, it scored better 6 times, tied 18 times, and scored worse once. These results apply to the published campaign and its scoring rule. Performance on other workloads and against other solvers remains open.

## Research directions

- **Reality OS** explores persistent spatial computing environments, recursive worlds, and human–AI tools. Public artifact mapping is pending.
- **Human–AI mutual grounding** explores how humans and AI establish, check, and repair shared task context. This preview presents it as proposed evaluation research.
- **Research cartography** explores how to map projects, assumptions, experiments, and uncertainty while preserving provenance. Public artifact mapping is pending.

See the [research status and evidence policy](RESEARCH_STATUS.md) for evidence requirements.
