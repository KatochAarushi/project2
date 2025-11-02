from heapq import heappush, heappop
from collections import defaultdict, deque
import math

class Graph:
    def __init__(self, n, directed=False):
        self.n, self.directed = n, directed
        self.adj = defaultdict(list)          # u -> [(v, w)]

    def add_edge(self, u, v, w):
        if w < 0: raise ValueError("No negative edges allowed.")
        self.adj[u].append((v, w))
        if not self.directed:
            self.adj[v].append((u, w))

def dijkstra(G, s):
    dist = {v: math.inf for v in range(G.n)}
    parent = {v: None for v in range(G.n)}
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:                     # lazy deletion
            continue
        for v, w in G.adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heappush(pq, (nd, v))
    return dist, parent

def path(parent, s, t):
    if t != s and parent[t] is None: return []
    out, cur = deque([t]), t
    while cur != s:
        cur = parent[cur]
        if cur is None: return []
        out.appendleft(cur)
    return list(out)

def print_paths(G, s):
    dist, parent = dijkstra(G, s)
    for v in range(G.n):
        if v == s:
            print(f"{s} -> {v}: path = [{v}], cost = 0")
            continue
        p = path(parent, s, v)
        if not p:
            print(f"{s} -> {v}: unreachable")
        else:
            print(f"{s} -> {v}: path = {p}, cost = {dist[v]}")
