#!/usr/bin/env python
from heapq import heappop, heappush

m = [list(map(int, line)) for line in open(0).read().splitlines()]
height, width = len(m), len(m[0])

# Fast Dijkstra version
for i in 1, 5:
    heap, seen = [(0, 0, 0)], {(0, 0)}

    while heap:
        risk, r, c = heappop(heap)
        if r == i * height - 1 and c == i * width - 1:
            print(risk)
            break

        for r_, c_ in (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1):
            if 0 <= r_ < i * height and 0 <= c_ < i * width and (r_, c_) not in seen:
                rd, rm = divmod(r_, height)
                cd, cm = divmod(c_, width)

                seen.add((r_, c_))
                heappush(heap, (risk + (m[rm][cm] + rd + cd - 1) % 9 + 1, r_, c_))

# Slower NetworkX version
import networkx as nx

for i in 1, 5:
    g = nx.grid_2d_graph(i * height, i * width, create_using=nx.DiGraph)

    for _, (x, y), data in g.edges(data=True):
        xd, xm = divmod(x, height)
        yd, ym = divmod(y, width)
        data["weight"] = (m[xm][ym] + xd + yd - 1) % 9 + 1

    print(nx.shortest_path_length(g, source=(0, 0), target=(i * height - 1, i * width - 1), weight="weight"))
