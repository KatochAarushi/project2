"""
Dijkstra's algorithm (single-source shortest paths) implementation.

Graph representation expected:
- graph: dict where keys are nodes and values are lists of (neighbor, weight)

API:
- dijkstra(graph, source) -> (dist, prev)
    dist: dict node -> shortest distance from source (float('inf') if unreachable)
    prev: dict node -> predecessor in shortest path (None for source or unreachable)

Notes:
- This implementation uses a heap (priority queue) and standard relaxation.
- It does not support negative edge weights (will raise ValueError if any negative weight found).

Example:
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    dist, prev = dijkstra(graph, 'A')

"""
from heapq import heappush, heappop
from typing import Dict, Tuple, Any, List
import os

def dijkstra(graph: Dict[Any, List[Tuple[Any, float]]], source: Any) -> Tuple[Dict[Any, float], Dict[Any, Any]]:
    """Compute shortest paths from source to all reachable nodes.

    Args:
        graph: adjacency list mapping node -> list of (neighbor, weight)
        source: source node

    Returns:
        (dist, prev)
        dist: dict of shortest distances
        prev: dict of predecessors for path reconstruction
    """
    # basic validation and negative-weight check
    for u, edges in graph.items():
        for v, w in edges:
            if w < 0:
                raise ValueError("Dijkstra's algorithm does not support negative weights")

    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}

    if source not in graph:
        # allow source not in graph: return empty-ish results with source unreachable
        return dist, prev

    dist[source] = 0.0
    heap = [(0.0, source)]

    while heap:
        d_u, u = heappop(heap)
        if d_u > dist[u]:
            continue
        for v, w in graph.get(u, []):
            alt = d_u + w
            if alt < dist.get(v, float('inf')):
                dist[v] = alt
                prev[v] = u
                heappush(heap, (alt, v))

    return dist, prev


def reconstruct_path(prev: Dict[Any, Any], source: Any, target: Any) -> List[Any]:
    """Reconstruct path from source to target using predecessor map.

    Returns an empty list if target is unreachable from source.
    """
    if prev.get(target) is None and source != target:
        # either unreachable or target == source
        if source == target:
            return [source]
        return []
    path = []
    node = target
    while node is not None:
        path.append(node)
        if node == source:
            break
        node = prev.get(node)
    path.reverse()
    if path[0] != source:
        return []
    return path

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for i in range(1, 6):
        filename = os.path.join(script_dir, f"dijkstra_input_{i}.txt")
        if not os.path.exists(filename):
            print(f"File {filename} not found, skipping.")
            continue

        print(f"--- Processing {filename} ---")

        graph = {}
        source_node = None
        nodes = set()

        with open(filename, 'r') as f:
            lines = f.readlines()
        
        header = lines[0].strip().split()
        num_vertices, num_edges, graph_type = int(header[0]), int(header[1]), header[2]

        edge_lines = lines[1:1 + num_edges]
        
        # Populate adjacency list
        for line in edge_lines:
            parts = line.strip().split()
            if len(parts) == 3:
                u, v, weight_str = parts
                weight = float(weight_str)

                if u not in graph:
                    graph[u] = []
                if v not in graph:
                    graph[v] = []

                graph[u].append((v, weight))
                if graph_type == 'U':
                    graph[v].append((u, weight))
        
        if len(lines) > 1 + num_edges:
            source_node = lines[1 + num_edges].strip()

        if source_node and source_node in graph:
            distances, predecessors = dijkstra(graph, source_node)

            print(f"Shortest paths from source node '{source_node}':")
            sorted_nodes = sorted(graph.keys())

            for target_node in sorted_nodes:
                path = reconstruct_path(predecessors, source_node, target_node)
                cost = distances.get(target_node, float('inf'))
                
                if path:
                    path_str = " -> ".join(path)
                    print(f"  To {target_node}: Path = {path_str}, Cost = {cost}")
                else:
                    if source_node == target_node:
                         print(f"  To {target_node}: Path = {source_node}, Cost = 0.0")
                    else:
                         print(f"  To {target_node}: No path found.")
        else:
            print("Source node not found or not specified in the input file.")
        
        print("-" * (len(filename) + 20) + "\n")
