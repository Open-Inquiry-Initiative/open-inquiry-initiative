# OII-CSG-001 · Gate G00 qualification report

**2026-11-27 · Conditional recommendation for CPU-only G01 · Independent review pending**

The prior art supports carrying forward a narrow question: do explicitly defined symmetry constraints improve fixed-graph communication under matched budgets, and under what conditions? The evidence supports preparing that experiment. Geometry-inspired performance, novelty, external reproduction and runtime integration remain unqualified. The framework is an OII *Prototype*. Its fixture results are local implementation checks. Gate acceptance remains an OII review decision.

Authority is the [canonical charter at commit 145ec4d](https://github.com/Open-Inquiry-Initiative/open-inquiry-initiative/blob/145ec4d788134e121e9cfdf4eda9a5ef9a6d47fb/research/OII-CSG-001/CHARTER.md), retrieved with `git clone https://github.com/Open-Inquiry-Initiative/open-inquiry-initiative.git canonical` and checked with `git log -1 --format=%H -- research/OII-CSG-001/CHARTER.md`. This submission follows [OII evidence policy](../../RESEARCH_STATUS.md) and [OII-EPI-001](../../governance/OII-EPI-001.md).

## Search record and scope

Searches on 2026-11-27 used publisher and author records, arXiv and PubMed discovery, Google Patents publication and claim text, GitHub repository search, GitHub API tree metadata and Git ref checks. The following queries describe the retained search paths. Ranking is search-engine dependent and result counts were not preserved.

| Source | Search terms and screening |
|---|---|
| Scholarly discovery | `"symmetry-constrained adaptive computational topology"`, `"cybernetic sacred geometry"`, sacred geometry / Flower of Life / triangular lattice / network optimization, adaptive coevolutionary networks, switching-topology consensus, fastest mixing Markov chain, sensor persistent homology, regular-polyhedral formation, GPTSwarm, AGP and AgentPrune. Charter identifiers `1805.07823` and `2505.22467` were opened directly. |
| Patents | `site:patents.google.com topology network reconfiguration failure mesh`, `multi-agent consensus formation geometric lattice`, `hexagonal mesh interconnection topology multiprocessor`. Screened independent claim language where applicable. US5574931A describes hexagonal mesh in its background, while its disclosed priority-control mechanism concerns a ring. Listing a shape in a specification is different from claiming that shape. |
| GitHub | Connector queries `OII-CSG-001` and `"Open Inquiry Initiative" in:name,description,readme`. Implementation queries included `site:github.com GPTSwarm resurgamm AGP`, `distributed graph multi agent optimization disropt`, `GUDHI`, `robotarium` and `adaptive network rewiring Gross Blasius`. The charter was recovered through the repository tree after the code index returned no hits. |

Retained sources specify a mechanism, comparator or historical construction. Excluded were unrelated uses of “topology,” GPU-first demonstrations as G01 dependencies, and symbolic interpretations as computational evidence. Partial matches include primary research that optimizes flows on an existing triangular substrate and work formalizing the Flower of Life as a recursive geometric pattern. Neither supports a claim about consensus under the proposed protocol. The exact-phrase search supplies no priority evidence. This is a cross-domain scoping review. Forward citation closure, systematic database coverage, patent-family and classification expansion, original-language review and independent screening remain open. [Triangular substrate study](https://doi.org/10.1103/PhysRevX.14.021050) · [Flower of Life formalization](https://doi.org/10.12732/ijam.v38i7s.651)

## Literature and novelty matrix

| Research question | Established prior art | Open application and distinguishing test |
|---|---|---|
| Can feedback govern a changing network? | Wiener and Ashby supply feedback and regulation foundations. Conant–Ashby gives a regulator theorem under specific assumptions. Gross–Blasius surveys the coupling of node dynamics and rewiring. Holme–Newman demonstrates an adaptive opinion-network phase transition. Tero et al. model adaptive transport design. [Wiener](https://mitpress.mit.edu/9780262537841/cybernetics-or-control-and-communication-in-the-animal-and-the-machine/) · [Ashby](https://ashby.info/Ashby-Introduction-to-Cybernetics.pdf) · [Conant–Ashby](https://doi.org/10.1080/00207727008920220) · [Gross–Blasius](https://pubmed.ncbi.nlm.nih.gov/17971320/) · [Holme–Newman](https://doi.org/10.1103/PhysRevE.74.056108) · [Tero et al.](https://pubmed.ncbi.nlm.nih.gov/20093467/) | Test an OII-specific controller at G03. Compare a fixed policy, unconstrained bounded adaptation and symmetry-constrained bounded adaptation with identical candidate budgets and observation streams. |
| Can regular geometric structure control agents? | Zhang, He, Hong and Hu (2018, arXiv:1805.07823v1) study attitude formation for the regular polyhedra. Euclid and Fuller provide geometric and historical context. [Zhang et al.](https://arxiv.org/abs/1805.07823v1) · [Euclid XIII](https://www.claymath.org/library/historical/euclid/index.html) · [Fuller Institute](https://www.bfi.org/about-fuller/big-ideas/synergetics/) | Compare graph skeletons on synthetic message passing. Distinguish degree and connectivity effects from symmetry with matched null graphs. Treat geometric embedding as an explicit cost input and historical terminology as attribution. |
| Can topology improve consensus? | Switching-topology consensus, randomized gossip and fastest mixing already connect graph structure, edge weights and convergence. Fastest mixing explicitly exploits symmetry. Persistent homology already supports coverage inference under separate geometric assumptions. [Olfati-Saber–Murray](https://www.ee.iitb.ac.in/~dc/EE749/Olfati.pdf) · [Boyd et al. gossip](https://stanford.edu/~boyd/papers/pdf/gossip.pdf) · [Boyd–Diaconis–Xiao](https://stanford.edu/~boyd/papers/fmmc.html) · [de Silva–Ghrist](https://msp.org/agt/2007/7-1/agt-v7-n1-p16-s.pdf) | Measure cost to a fixed accuracy under matched resources. An isomorphic relabeling carries state and preserves the update operator up to permutation. Alternative drawings can change measured length. |
| Can multi-agent communication graphs be optimized? | GPTSwarm optimizes agent graphs and prompts. AGP learns query-dependent pruning. AgentPrune removes redundant communication. Yang et al. (arXiv:2505.22467v3) is a position paper proposing a broader agenda. [GPTSwarm](https://arxiv.org/abs/2402.16823v3) · [AGP](https://resurgamm.github.io/AGP/) · [AgentPrune](https://arxiv.org/abs/2410.02506) · [Yang et al.](https://arxiv.org/abs/2505.22467v3) | A held-out, budget-matched Hydra evaluation may establish local utility of a particular constrained search and verifier policy. Novelty beyond that application remains undetermined. |
| Can geometry and topology support fault recovery? | Patent disclosures cover automatic rerouting, signal-driven link replacement, hierarchical healthy mesh construction and relative-position-based formation. | Use abstract faults, an explicit switching cost and an auditable rollback policy in simulation. Compare recovery against established fixed alternatives. |

## Patent screening

| Publication | Claim relevance and boundary |
|---|---|
| [US5138615A](https://patents.google.com/patent/US5138615A/en) | Mesh LAN reconfiguration with switch and routing machinery. Establishes an adjacent fault-recovery mechanism. |
| [EP2688342A1](https://patents.google.com/patent/EP2688342A1/en) | Claim 1 ties connection replacement to monitored signal strength. Claim 10 includes ranking by resulting topology. Follow family to EP2688342B1, WO2014014405A2 and US20150172991A1 for a deeper review. |
| [US5513313A](https://patents.google.com/patent/US5513313A/en) | Claim 1 configures a healthy target mesh using labeled blocks and prescribed edge construction. Hierarchical geometry and fault tolerance overlap conceptually. |
| [CN119165883B](https://patents.google.com/patent/CN119165883B/en) | Claim 1 describes self-organizing 3D formation-consensus control with graph and rigidity steps. This is the closest geometry/control hit among the reviewed publications. Screening relied on machine translation. |
| [CN121056333A](https://patents.google.com/patent/CN121056333A/en) | Claim 1 constructs a dynamic multi-agent communication graph from state and demand weights. The translated description includes link-symmetry constraints, which need to be distinguished from polyhedral automorphism constraints in follow-up screening. |

Boyd, Diaconis, Parrilo and Xiao give explicit orbit and block-diagonalization techniques for fastest mixing on symmetric graphs. This reduces optimization cost in their setting and provides a conventional comparator for any proposed benefit from symmetry. [Fastest mixing on graphs with symmetries](https://arxiv.org/abs/0709.0955)

Assessments describe technical overlap. Patent status, scope across jurisdictions and freedom to operate remain outside this evidence.

## Implementation and reproduction inventory

Repository pins were obtained using `git ls-remote https://github.com/<owner>/<repo>.git HEAD` and file paths checked against GitHub trees. The links pin the inspected source. Root licenses are scoped to the code they cover. Model weights, training data, bundled libraries and individual components may carry different terms. For cited literature and patents the publication scope is original summaries and links.

| Implementation | License and dependency observations | Reproduction feasibility |
|---|---|---|
| [NetworkX 3.4.2](https://github.com/networkx/networkx/tree/networkx-3.4.2) and [NumPy 2.2.6](https://github.com/numpy/numpy/tree/v2.2.6) | BSD-3-Clause root terms. NumPy binary distributions carry third-party notices. Both installed from wheels and passed pip check. | Used for CPU graph generators and dense eigensolver. Platform and hashes below. |
| [DISROPT](https://github.com/OPT4SMART/disropt/tree/04b4d523fdf6bffacec628ef658b73f167175826) | GPL-3.0. Requirements include mpi4py, CVXPY, CVXOPT, OSQP, NumPy, SciPy, autograd and dill. | Candidate independent CPU consensus check at G02 with MPI and an isolated environment. Pin native MPI and solvers, and review terms for distribution. |
| [Robotarium Python simulator](https://github.com/robotarium/robotarium_python_simulator/tree/2b1b6136a242c164e53081b794ebf10d904cbaae) | MIT. Setup lists NumPy, Matplotlib and CVXOPT. | Candidate for CPU formation and consensus demonstrations. Separate from the Zhang reduced-attitude reproduction. A pinned implementation for that specific paper remains to be located. |
| [GUDHI](https://github.com/GUDHI/gudhi-devel/tree/15432fb39a8e1eee629a97d1b96ef1138ebc1a06) | MIT root license. Source build declares NumPy, scikit-build-core, nanobind and CMake. Audit chosen component and packaged dependencies. | Useful for a separate persistence/coverage question. Keep out of graph-consensus core. |
| [GPTSwarm](https://github.com/metauto-ai/GPTSwarm/tree/c23a827f561c934ce21dd950408f7606aa4a8821) | MIT. Manifest declares Python ^3.10, Torch 2.1–2.2.2, Transformers and OpenAI client. | Inspect or reproduce a graph-only fixture with a stub if practical. Full results depend on model identity, data and an execution budget. |
| [AGP](https://github.com/Resurgamm/AGP/tree/4c5508361e6a1b0e799b2223403f61c144a4c492) | MIT. Python 3.10 instructions, Torch 2.3.0 + CUDA 12.1 and PyG extensions. README also describes API credentials, datasets and checkpoints. | The published dependency set is GPU-oriented. Use the idea as a comparator at G00. CPU-port feasibility and separate data/model terms remain to be checked. |
| [Physarum transport simulation](https://github.com/davideciccarese/Physarum-polycephalum-simulation/tree/66ce8e825bf59cdb64663b1952082a1a9fd7e1da) | MIT. Requirements list NumPy, SciPy, Matplotlib, openpyxl and pytest with lower bounds. | CPU candidate for adaptive transport. Its lattice growth extension requires a separate deviation log when comparing with Tero et al. |

Third-party implementations other than the two runner dependencies were inspected via metadata and manifests. Their reported numerical results await reproduction. A practical G02 first target is a fixed graph with a closed-form spectrum and a conventional fastest-mixing comparison, followed by a small distributed implementation if it adds independent evidence. Use synthetic inputs and an isolated environment.

## Local evidence and reproducibility

The CPU runner inherits standard NetworkX generators and implements synchronous lazy Laplacian averaging, `P = I - L / (2 d_max)` with a denominator fallback for zero degree. It logs the spectral gap of P, convergence to the original mean, observed rounds and two directed messages per nonloop edge per round. Edge multiplicities count as parallel links. Its synthetic wire cost sums Euclidean chord lengths on a unit circle, independently of the update rule. The seed mode emits fixed-graph trials and trials starting after one sampled link deletion.

Only analytic and generator smoke checks were evaluated for G00. For a four-cycle, the analytic Laplacian spectrum gives a transition gap of 0.5. The runner matched it and reached tolerance in 10 rounds. Removing one edge produced the analytic four-path gap of about 0.146447 and reached tolerance in 27 rounds. Six isomorphic swaps preserved all logged outcomes. Doubling drawing scale doubled wire length with identical graph-only outcomes. Four isolated vertices reached the 2,000-round cap without convergence. That failure is preserved. Two runs matched the committed JSON by line content. The analytic checks are independent of the eigensolver. An independent operator or alternate implementation has yet to rerun the campaign.

Recorded environment was Windows NT 10.0.26200 x64, CPython 3.11.15 AMD64, pip 24.0, NetworkX 3.4.2 and NumPy 2.2.6. There were no models, GPUs, remote calls at runtime or production changes. One initial environment command failed because the Windows Python launcher did not resolve the 3.11 selector. Selecting `-V:Astral/CPython3.11.15` recovered the experiment.

```powershell
# Run from research/OII-CSG-001 with CPython 3.11 on Windows x64.
python -m venv .venv
$python = ".\.venv\Scripts\python.exe"
& $python -m pip install --only-binary=:all: --require-hashes -r requirements-win-cp311.lock
& $python -m pip check
$env:OPENBLAS_NUM_THREADS = "1"
$observed = & $python benchmark.py --smoke
if ($LASTEXITCODE -ne 0) { throw "Smoke test failed" }
if (($observed -join "`n") -cne ((Get-Content g00-smoke.json) -join "`n")) {
    throw "Smoke output differed"
}
```

On other platforms use the version-only `requirements.txt`, record the resolved wheel hashes and compare floats at 1e-12 absolute tolerance where BLAS or rounding differs. The pinned Windows wheels are identified in [requirements-win-cp311.lock](requirements-win-cp311.lock). [Raw smoke output](g00-smoke.json) · [Artifact hashes](g00-sha256.txt)

## G01 execution recommendation

1. **Before evaluation**, publish a frozen protocol, executable revision and manifest. Proposed seeds are integers 1000–1099 with 100 paired trials per eligible stratum, using seed offset 10000 for a matched uniform edge-deletion quantile. Use seed 7 only as a fixture. Record exact graphs, initial vectors, removed edges, rerun commands and exclusion reasons. Treat seeds as variation in inputs, faults and random comparator draws. Fixed graphs gain no additional structural replication from reusing them across seeds.
2. **Budget strata.** Use dodecahedral versus random 3-regular at (20, 30), icosahedral versus random 5-regular at (12, 30) and 4-cube versus random 4-regular at (16, 32). Mesh, finite triangular lattice, ring and star are descriptive where budgets differ. Add degree-preserving edge-swap nulls for irregular structures and specify connectivity policy in advance. Report Margulis expansion as a multigraph stratum until there is a matched comparator. A raw family leaderboard would confound link count, degree and communication rate.
3. **Outcomes.** Use capped messages to reduce the centered L2 error to 0.001 of its initial value as the primary cost, alongside a mandatory convergence-rate constraint. The cap is 2,000 rounds. Keep failures in denominators and label their message counts as observed through the cap. Report gap, rounds, fault connectivity and mean drift. Report nominal wire cost as a separate scenario. Before making a geometry-specific wire claim, add normalized native planar/polyhedral embeddings and spatially matched nulls. Current circular placement is a diagnostic embedding.
4. **Decision criteria.** For each of the three matched contrasts, predeclare a paired message-count ratio, geometry-inspired divided by random regular, and a maximum allowed convergence-rate loss of two percentage points. Estimate the ratio on jointly convergent pairs with the pair count reported and use the outcome only if the convergence guardrail passes on all trials, with an interval for the difference. Require at least 10% lower message cost with an upper confidence bound at or below 0.90 in the intact condition and report the fault condition separately. Use seed-level paired bootstrap resampling with 10,000 draws and a fixed bootstrap seed of 20001. Adjust interval coverage for the three primary contrasts (Bonferroni, 98.33% per contrast). Report null, adverse, censored and inconclusive results. Limit interpretation to these graph instances and workload distributions.
5. **Independent checks.** Extend the fixture controls to every measured family. Permute adjacency, initial state and failed edge together and compare outputs with a frozen float tolerance. Change coordinates on the same graph, and compare against a separate edge-list averaging implementation with direct summation. Hand verification and independent reruns should review censoring and budgets before any next-gate performance claim. Add a common edge-weight policy sensitivity, such as symmetric Metropolis weights, before attributing a difference to graph structure.

These are proposed design choices prepared before the comparative run. The current runner handles graph generation and single-seed records. The campaign orchestration, per-family invariance harness, spatial matching, independent evaluator and statistical analysis belong to G01. G01 scope is fixed graphs. Adaptive feedback, hysteresis, bounded rewiring and rollback are G03 experiments.

## Candidate integration surfaces

| Project | Evaluation boundary |
|---|---|
| Hydra | At G04, consume candidate adjacency through a sandbox adapter with a fixed specialist pool and identical token/time caps. Compare direct, fixed topology, fixed specialist and constrained/unconstrained adaptive ablations on held-out tasks. Log accuracy, wrong accepts, uncertainty, latency and tokens. A verifier outside the controller's write permissions scores the evidence. |
| Reality OS | At G05, use an observer that reads an event log and replays graph state, decisions, faults and recovery. Evaluate display coordinate mappings independently of the underlying state. |
| OII Runtime | Propose a versioned evidence and budget contract containing graph hash, allowed-edge policy, inputs, run ID, resource counters, decision records and rollback target. Test this against simulated admission and replay before proposing any interface changes. |

These opportunities follow the public [R-OS-HRI-001 charter](../R-OS-HRI-001/CHARTER.md). Runtime interfaces and access controls require verification with their maintainers.

## Submission scope

AI-assisted search, synthesis, implementation and local checks. The public review package contains original prose, original benchmark glue, synthetic fixture results and upstream references. It carries no copied third-party code, papers, weights, datasets or private integration material. Publication is for review. The charter and its status remain authoritative.
