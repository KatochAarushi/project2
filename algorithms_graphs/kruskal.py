"""
Kruskal's algorithm for Minimum Spanning Tree (MST).

Graph/edges representation expected:
- edges: iterable of (u, v, weight)

API:
- kruskal(edges) -> (mst_edges, total_weight)
    mst_edges: list of (u, v, w) in the MST
    total_weight: sum of weights in MST

Notes:
- If the input graph is disconnected, the algorithm returns a Minimum Spanning Forest (MST per component).
"""
from typing import List, Tuple, Any


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
            return x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def kruskal(edges: List[Tuple[Any, Any, float]]) -> Tuple[List[Tuple[Any, Any, float]], float]:
    """Compute MST (or forest for disconnected graphs) using Kruskal's algorithm.

    Args:
        edges: iterable of (u, v, weight)

    Returns:
        (mst_edges, total_weight)
    """
    # sort edges by weight
    sorted_edges = sorted(edges, key=lambda e: e[2])
    uf = UnionFind()
    mst = []
    total = 0.0

    for u, v, w in sorted_edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            total += w

    return mst, total


# convenience helper to derive edges from adjacency list
def edges_from_adjlist(adj: dict) -> List[Tuple[Any, Any, float]]:
    """Given adjacency dict node -> list of (neighbor, weight), returns an undirected edge list without duplicates.
    Assumes the adj list may contain both directions; duplicates are removed by ordering nodes.
    """
    seen = set()
    edges = []
    for u, neighbors in adj.items():
        for v, w in neighbors:
            key = tuple(sorted((u, v)))
            if key in seen:
                continue
            seen.add(key)
            edges.append((u, v, w))
    return edges


if __name__ == "__main__":
    import os

    for i in range(1, 6):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, f"kruskal_input_{i}.txt")

        if not os.path.exists(filename):
            print(f"File {filename} not found, skipping.")
            continue

        print(f"--- Processing {os.path.basename(filename)} ---")

        edges = []
        with open(filename, 'r') as f:
            lines = f.readlines()

        header = lines[0].strip().split()
        num_edges = int(header[1])

        edge_lines = lines[1:1 + num_edges]

        for line in edge_lines:
            parts = line.strip().split()
            if len(parts) == 3:
                u, v, weight_str = parts
                edges.append((u, v, float(weight_str)))

        mst_edges, total_cost = kruskal(edges)

        print("Edges of the Minimum Spanning Tree:")
        for u, v, w in mst_edges:
            print(f"  ({u}, {v}) - weight: {w}")

        print(f"\nTotal cost of MST: {total_cost}")
        print("-" * (len(os.path.basename(filename)) + 20) + "\n")
