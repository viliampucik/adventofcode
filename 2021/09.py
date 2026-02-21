#!/usr/bin/env python
from math import prod

m = [list(map(int, line)) for line in open(0).read().splitlines()]
h, w, part1, part2 = len(m), len(m[0]), 0, []

for r in range(h):
    for c in range(w):
        # fmt:off
        if any(
            m[r][c] >= m[x][y]
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1))
            if 0 <= (x := r + i) < h and 0 <= (y := c + j) < w
        ):
            continue
        # fmt:on
        part1 += m[r][c] + 1

        visited, visiting = set(), set([(r, c)])

        while visiting:
            a, b = visiting.pop()
            visited.add((a, b))

            for i, j in (-1, 0), (1, 0), (0, -1), (0, 1):
                # fmt:off
                if 0 <= (x := a + i) < h and 0 <= (y := b + j) < w \
                    and m[x][y] < 9 \
                    and (x, y) not in visited:
                    visiting.add((x, y))
                # fmt:on

        part2.append(len(visited))

print(part1)
print(prod(sorted(part2)[-3:]))
