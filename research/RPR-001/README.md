# RPR-001 — Recursive Predictive Realization

Status: **experimental prototype / not validated**. Date: 2026-11-22.

## Hypothesis
A provenance-aware, time-bounded research graph can recommend useful next engineering steps earlier and more accurately than simple chronological or frequency baselines.

## Philosophy
Imaginative hypotheses become computational models, then independently tested implementations. These stages overlap; predictions are proposals, not established future facts.

## Experiment 001 — historical replay
1. Collect dated, permission-cleared research events, dependencies, and evidence with immutable source references.
2. Choose a cutoff. Training input must contain only events observed by the cutoff; label later outcomes separately.
3. Rank candidate next capabilities based on prerequisites completed **at the cutoff**. Compare to frequency and recency baselines.
4. Report precision@k, recall@k, lead time, dependency accuracy, calibration (if probabilities are produced), and engineering cost.
5. Perform prospective preregistered trials. Distinguish historical occurrence from independent usefulness.

## Data contract
JSON list of events: `id`, `timestamp` (ISO-8601 UTC), `title`, `kind`, `dependencies` (event IDs), `source` (traceable link or reference), `evidence_status` (idea, simulated, implemented, verified). No later event or derived feature may leak across the cutoff.

## Reproducible starter
Run `python3 research/RPR-001/predict.py research/RPR-001/example_synthetic.json 2026-11-03T00:00:00Z`.
Run `python3 -m unittest discover -s research/RPR-001 -p 'test_*.py'`.

The bundled dataset is **synthetic**, not the user's actual history. Its output is a software smoke test, not scientific validation. No predictive probabilities are claimed.

## Acceptance gates
- G0: Data provenance, rights, cutoff and leakage audit.
- G1: Deterministic replay and automated tests.
- G2: Real dated dataset with held-out outcomes and baseline comparison.
- G3: Prospective timestamped predictions and independently scored outcomes.
- G4: Optional RABE integration and resource-constrained execution planning.

No physical validation, AI model training, or measured predictive advantage is claimed at this stage.
