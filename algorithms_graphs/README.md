# Graph Algorithms Demo

This small project contains reference implementations for:

- Dijkstra's single-source shortest path (`dijkstra.py`)
- Kruskal's minimum spanning tree (`kruskal.py`)
- DFS-based topological sort and cycle detection (`topo_dfs.py`)

Files:
- `dijkstra.py` — Dijkstra's algorithm implementation.
- `kruskal.py` — Kruskal's algorithm implementation.
- `topo_dfs.py` — Topological sort and cycle detection implementation.
- `requirements.txt` — minimal (Python standard library only)

## How to Run

Each algorithm can be run independently against the sample input files provided.

Open a terminal and execute the following commands from the `algorithms_graphs` directory:

### Dijkstra's Algorithm
To run Dijkstra's algorithm and see the shortest paths from a source node:
```powershell
python dijkstra.py
```

### Kruskal's Algorithm
To find the Minimum Spanning Tree (MST) for the sample graphs:
```powershell
python kruskal.py
```

### Topological Sort and Cycle Detection
To perform a topological sort or detect cycles in the sample directed graphs:
```powershell
python topo_dfs.py
```

Notes:
- Implementations use standard Python 3 (3.8+ recommended).
- No external dependencies required.
