import itertools as it
import networkx as nx
import math
import sys

nodes = [tuple(map(int, ln.split(","))) for ln in iter(sys.stdin.readline, "")]
N = len(nodes)

edges = sorted(
    it.combinations(nodes, 2),
    key=lambda x: sum((i - j) ** 2 for i, j in zip(x[0], x[1])),
)

G = nx.Graph(edges[:1000])
G.add_nodes_from(nodes)

one = math.prod(sorted(map(len, nx.connected_components(G)), reverse=True)[:3])
print(f"ONE: {one}")

for i, j in edges:
    G.add_edge(i, j)
    if nx.is_connected(G):
        print(f"TWO: {i[0] * j[0]}")
        break
else:
    print("Graph never connected")
