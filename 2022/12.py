#!/usr/bin/env python
import networkx as nx

t = {
    k: ord(v) - ord("a")
    for r, line in enumerate(open(0))
    for c, v in enumerate(line.strip())
    for k in [complex(r, c)]
    if (v == "S" and (s := k)) or (v == "E" and (e := k)) or True
}
t[s], t[e] = 0, ord("z") - ord("a")
G = nx.DiGraph(
    incoming_graph_data=(
        (k, n)
        for k, v in t.items()
        for d in (-1, 1, -1j, 1j)
        if (n := k + d) in t and t[n] - v <= 1
    )
)
paths = list(nx.single_target_shortest_path_length(G, e))
print(next(v for k, v in paths if k == s))
print(min(v for k, v in paths if t[k] == 0))

## BFS example, but slower than networkx
#
# from collections import deque
#
#
# def bfs(t, s, e):
#     queue, seen = deque([(s, 0)]), set([s])
#
#     while queue:
#         k, size = queue.popleft()
#
#         if k == e:
#             return size
#
#         for d in (-1, 1, -1j, 1j):
#             if (n := k + d) in t and n not in seen and t[n] - t[k] <= 1:
#                 queue.append((n, size + 1))
#                 seen.add(n)
#
#
# print(bfs(t, s, e))
