"""
DFS-based Topological Sort and Cycle Detection.

Graph representation:
- graph: dict node -> list of neighbors (directed edges u -> v)

API:
- topological_sort(graph) -> list of nodes in topological order
    Raises ValueError if a cycle is detected (cannot topologically sort).
- has_cycle(graph) -> bool

"""
from typing import Dict, List, Any
from collections import defaultdict


def topological_sort(graph: Dict[Any, List[Any]]) -> List[Any]:
    visited = set()
    temp = set()  # recursion stack
    order = []

    def dfs(u):
        if u in temp:
            raise ValueError("Graph contains a cycle; topological sort not possible")
        if u in visited:
            return
        temp.add(u)
        for v in graph.get(u, []):
            dfs(v)
        temp.remove(u)
        visited.add(u)
        order.append(u)

    # Ensure all nodes appear even if they have no outgoing edges
    nodes = set(graph.keys())
    for u in graph.values():
        for v in u:
            nodes.add(v)

    for node in nodes:
        if node not in visited:
            dfs(node)

    order.reverse()
    return order


def has_cycle(graph: Dict[Any, List[Any]]) -> bool:
    visited = set()
    temp = set()

    def dfs(u):
        if u in temp:
            return True
        if u in visited:
            return False
        temp.add(u)
        for v in graph.get(u, []):
            if dfs(v):
                return True
        temp.remove(u)
        visited.add(u)
        return False

    nodes = set(graph.keys())
    for u in graph.values():
        for v in u:
            nodes.add(v)

    for node in nodes:
        if node not in visited:
            if dfs(node):
                return True
    return False


if __name__ == "__main__":
    import os

    def find_all_cycles(graph):
        cycles = []
        path = []
        # path_set, visited_set
        visiting = set()
        visited = set()

        def dfs(u):
            path.append(u)
            visiting.add(u)

            for v in graph.get(u, []):
                if v in visiting:
                    try:
                        cycle_start_index = path.index(v)
                        cycle = path[cycle_start_index:]
                        # Store sorted tuple to handle duplicates from different start points
                        sorted_cycle = tuple(sorted(cycle))
                        if sorted_cycle not in [tuple(sorted(c)) for c in cycles]:
                            cycles.append(cycle)
                    except ValueError:
                        pass
                elif v not in visited:
                    dfs(v)

            path.pop()
            visiting.remove(u)
            visited.add(u)

        nodes = list(graph.keys())
        for node in nodes:
            if node not in visited:
                dfs(node)
        return cycles

    for i in range(1, 6):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(script_dir, f"topo_input_{i}.txt")

        if not os.path.exists(filename):
            print(f"File {filename} not found, skipping.")
            continue

        print(f"--- Processing {os.path.basename(filename)} ---")

        graph = defaultdict(list)
        all_nodes = set()

        with open(filename, 'r') as f:
            lines = f.readlines()

        header = lines[0].strip().split()
        num_edges = int(header[1])
        edge_lines = lines[1:1 + num_edges]

        for line in edge_lines:
            parts = line.strip().split()
            if len(parts) == 3:
                u, v, _ = parts
                graph[u].append(v)
                all_nodes.add(u)
                all_nodes.add(v)

        # Ensure all nodes are in the graph keys for topological sort
        for node in all_nodes:
            if node not in graph:
                graph[node] = []

        cycles = find_all_cycles(graph)

        if cycles:
            print("Graph contains cycles. Topological sort not possible.")
            print("Found cycles:")
            for cycle in cycles:
                cycle_path = " -> ".join(cycle) + f" -> {cycle[0]}"
                print(f"  - Cycle: {cycle_path} (Length: {len(cycle)})")
        else:
            print("Graph is a DAG. Topological Sort:")
            try:
                sorted_order = topological_sort(graph)
                print("  " + " -> ".join(sorted_order))
            except ValueError as e:
                # Fallback in case the main topo sort function has different cycle detection
                print(f"  Error during topological sort: {e}")


        print("-" * (len(os.path.basename(filename)) + 20) + "\n")
