# Graph Algorithms Demo

This small project contains reference implementations for:

- Dijkstra's single-source shortest path (`dijkstra.py`)
- Kruskal's minimum spanning tree (`kruskal.py`)
- DFS-based topological sort and cycle detection (`topo_dfs.py`)

Files:
- `dijkstra.py` — dijkstra(graph, source) and a path reconstruction helper
- `kruskal.py` — kruskal(edges) and an `edges_from_adjlist` helper
- `topo_dfs.py` — topological_sort(graph) and has_cycle(graph)
- `runner.py` — simple demo that runs each algorithm and prints results
- `requirements.txt` — minimal (Python standard library only)

How to run:

Open PowerShell and run:

```powershell
python "c:\Users\admin\PROJ 2\algorithms_graphs\runner.py"
```

Notes:
- Implementations use standard Python 3 (3.8+ recommended).
- No external dependencies required.
