"""CPU-only fixed-graph consensus and single-edge failure measurements."""

import argparse
import json
import math
import random
from itertools import combinations

import networkx as nx
import numpy as np


def graphs(seed):
    # Polyhedral sizes are fixed. Rectangular and recursive graphs retain their
    # native boundaries. The analysis must compare only eligible budget strata.
    yield "star", nx.star_graph(19)
    yield "ring", nx.cycle_graph(20)
    yield "mesh", nx.grid_2d_graph(4, 5)
    yield "triangular", nx.triangular_lattice_graph(4, 6)
    yield "dodecahedral", nx.dodecahedral_graph()
    yield "icosahedral", nx.icosahedral_graph()
    yield "recursive", nx.hypercube_graph(4)
    yield "explicit_expander", nx.margulis_gabber_galil_graph(4)
    for n, degree in [(20, 3), (12, 5), (16, 4)]:
        yield f"random_regular_{n}_{degree}", nx.random_regular_graph(degree, n, seed)


def measure(graph, state, coordinates):
    n = len(state)
    adjacency = nx.to_numpy_array(graph, nodelist=range(n))
    # Weighted degrees preserve edge multiplicity for the Margulis graph.
    # Self-loops cancel from the Laplacian and incur no messages.
    np.fill_diagonal(adjacency, 0)
    degree = adjacency.sum(axis=1)
    laplacian = np.diag(degree) - adjacency
    transition = np.eye(n) - laplacian / (2 * max(degree.max(), 1))
    gap = float(1 - np.linalg.eigvalsh(transition)[-2])
    target = state.mean()
    initial_error = np.linalg.norm(state - target)
    x = state.copy()
    rounds = 0
    while rounds < 2000 and np.linalg.norm(x - target) > 1e-3 * initial_error:
        x = transition @ x
        rounds += 1
    converged = bool(np.linalg.norm(x - target) <= 1e-3 * initial_error)
    edge_count = int(degree.sum() / 2)
    return {
        "nodes": n,
        "nonloop_edges": edge_count,
        "degree_sequence": sorted(map(int, degree)),
        "connected": nx.is_connected(graph),
        "spectral_gap": round(gap, 12),
        "rounds_observed": rounds,
        "converged": converged,
        "directed_messages_observed": 2 * edge_count * rounds,
        "mean_drift": round(float(abs(x.mean() - target)), 12),
        "wire_cost": round(sum(
            math.dist(coordinates[u], coordinates[v]) for u, v in graph.edges()
        ), 12),
    }


def fixtures(graph, seed):
    graph = nx.convert_node_labels_to_integers(graph)
    n = len(graph)
    rng = random.Random(seed)
    state = np.array([rng.uniform(-1, 1) for _ in graph])
    coordinates = [(math.cos(math.tau*i/n), math.sin(math.tau*i/n)) for i in range(n)]
    return graph, state, coordinates


def remove_sampled_edge(graph, seed):
    # A common uniform quantile provides a paired draw on unequal edge sets.
    edges = sorted((min(u, v), max(u, v)) for u, v in graph.edges() if u != v)
    fault = edges[int(random.Random(seed + 10000).random() * len(edges))]
    graph.remove_edge(*fault)
    return fault


def smoke_check():
    graph, state, coordinates = fixtures(nx.cycle_graph(4), 7)
    reference = measure(graph, state, coordinates)
    # Independent analytic oracle: C4 Laplacian eigenvalues are 0, 2, 2, 4.
    assert reference["spectral_gap"] == 0.5
    assert reference["converged"] and reference["mean_drift"] == 0
    assert reference["directed_messages_observed"] == 8 * reference["rounds_observed"]
    # Exhaustive relabeling is unnecessary here, but every pairwise swap is checked.
    for u, v in combinations(range(4), 2):
        mapping = {u: v, v: u}
        indices = [mapping.get(i, i) for i in range(4)]
        result = measure(nx.relabel_nodes(graph, mapping), state[indices],
                         [coordinates[i] for i in indices])
        assert result == reference
    deformed = measure(graph, state, [(x * 2, y * 2) for x, y in coordinates])
    assert math.isclose(deformed["wire_cost"], 2 * reference["wire_cost"])
    assert all(deformed[key] == value for key, value in reference.items()
               if key != "wire_cost")
    disconnected, values, positions = fixtures(nx.empty_graph(4), 7)
    failed = measure(disconnected, values, positions)
    assert not failed["connected"] and not failed["converged"] and failed["spectral_gap"] == 0
    assert failed["rounds_observed"] == 2000 and failed["directed_messages_observed"] == 0
    fault = remove_sampled_edge(graph, 7)
    damaged_cycle = measure(graph, state, coordinates)
    assert damaged_cycle["connected"] and damaged_cycle["nonloop_edges"] == 3
    assert math.isclose(damaged_cycle["spectral_gap"], (2 - math.sqrt(2)) / 4,
                        abs_tol=1e-12)
    # Verify generator wiring without evaluating topology performance.
    generated = {name: len(graph) for name, graph in graphs(7)}
    assert len(generated) == 11
    return {"cycle4": reference, "uniform_rescaling": deformed,
            "disconnected": failed, "family_sizes": generated, "swap_checks": 6,
            "cycle4_edge_failure": {"removed": fault, **damaged_cycle}}


def run(seed):
    rows = []
    for name, source in graphs(seed):
        graph, state, coordinates = fixtures(source, seed)
        rows.append({"family": name, "seed": seed, "fault": None,
                     **measure(graph, state, coordinates)})
        fault = remove_sampled_edge(graph, seed)
        rows.append({"family": name, "seed": seed, "fault": fault,
                     **measure(graph, state, coordinates)})
    return rows


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--smoke", action="store_true")
    mode.add_argument("--seed", type=int)
    args = parser.parse_args()
    print(json.dumps(smoke_check() if args.smoke else run(args.seed),
                     indent=2, sort_keys=True))
