#!/usr/bin/env python
from collections import defaultdict
import re

xmin, xmax, ymin, ymax = map(int, re.findall(r"-?\d+", input()))
print((ymin + 1) * ymin // 2)

v, n = 0, int((xmin * 2) ** 0.5 - 1)  # n-th member of arithmetic progression

# Fast, precomputed steps version
dxs = defaultdict(set)
for dx_init in range(n, xmax + 1):
    x, dx, step = 0, dx_init, 0
    while x <= xmax and (dx == 0 and xmin <= x or dx != 0):
        x += dx
        # fmt:off
        if dx > 0: dx -= 1
        # fmt:on
        step += 1
        if xmin <= x <= xmax:
            dxs[dx_init].add(step)
            if dx == 0:
                dxs[dx_init] = min(dxs[dx_init])
                break

dys = defaultdict(set)
for dy_init in range(ymin, -ymin):
    y, dy, step = 0, dy_init, 0
    while ymin <= y:
        y += dy
        dy -= 1
        step += 1
        if ymin <= y <= ymax:
            dys[dy_init].add(step)

for xsteps in dxs.values():
    for ysteps in dys.values():
        if type(xsteps) is int:
            if xsteps <= max(ysteps):
                v += 1
        elif xsteps & ysteps:
            v += 1

# Slower, brute force version
#
# for dy_init in range(ymin, -ymin):
#     for dx_init in range(n, xmax + 1):
#         x, y, dx, dy = 0, 0, dx_init, dy_init
#         while x <= xmax and y >= ymin and (dx == 0 and xmin <= x or dx != 0):
#             x += dx
#             y += dy
#             # fmt:off
#             if dx > 0: dx -= 1
#             # fmt:on
#             dy -= 1
#             if xmin <= x <= xmax and ymin <= y <= ymax:
#                 v += 1
#                 break

print(v)
