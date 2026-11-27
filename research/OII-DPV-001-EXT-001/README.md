# OII-DPV-001-EXT-001 — Computational Complexity and Hydra Optimization
Authorized 2026-11-26. Public research proposal; AI-assisted. Independent of claims in ../OII-DPV-001/README.md.

## Hypothesis
Memoization, subset-state compression and constraint-density-aware scheduling may reduce redundant search and improve Hydra resource allocation on bounded workloads. No claim of polynomial-time general NP-complete solving.

## Mathematical baseline
For permanent of n×n matrix, f(empty)=1 and f(S)=sum_{j in S} a_{|S|,j} f(S minus j). There are 2^n states and n*2^(n-1) transitions, versus n! direct permutation terms. At n=14: 16384 states, 114688 transitions, 87178291200 permutation terms. These are theoretical counts, not timings. O(n2^n) arithmetic time and O(2^n) stored values remain exponential. Compare Ryser and direct enumeration on small instances. Gaussian elimination O(n^3) field operations computes determinant, not general permanent. Random 3-SAT density near 4.27 is a distribution-dependent empirical transition, not a worst-case complexity guarantee. Proof checking and proof discovery are separate tasks.

## Gates
1. Implement deterministic seeded synthetic workloads and exact small-instance oracles.
2. Compare exhaustive search, memoized subset DP, established SAT solver and standard permanent algorithms; verify outputs before timing.
3. Sweep SAT densities including 3.85 and 4.27, sizes and random seeds; report SAT fraction separately from runtime and timeout fraction.
4. Measure wall time, peak memory, node counts, cache hit rate, overhead and correctness; use matched hardware and budgets, report uncertainty and failures.
5. Test Hydra branch equivalence keys including constraints, context and relevant state; reject unsafe merging; bound cache memory and handle invalidation.
6. Compare adaptive scheduling with fixed scheduling and ablations; hold out instances and report negative results.
7. Independent reproduction, provenance, dependency licenses, release review and publication of cleared code and data.

Acceptance: exact agreement with oracles on tractable cases, no incorrect pruning, reproducible benchmarks and measured benefit against baseline before integration. No experiments or Hydra integration completed in this note. Established algorithms are not claimed as novel. Preserve results even if hypothesis fails.
