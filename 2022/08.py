#!/usr/bin/env python
t = [list(map(int, l)) for l in open(0).read().splitlines()]
height, width = len(t), len(t[0])
# fmt:off
print(2 * height + 2 * width - 4 + sum(
    (
           all(t[row][col] > t[row][c  ] for c in range(0,       col))
        or all(t[row][col] > t[row][c  ] for c in range(col + 1, width))
        or all(t[row][col] > t[r  ][col] for r in range(0,       row))
        or all(t[row][col] > t[r  ][col] for r in range(row + 1, height))
    )
    for row in range(1, height - 1)
    for col in range(1, width - 1)
))
# fmt:on
max_score = 0

for row in range(1, height - 1):
    for col in range(1, width - 1):
        score = 1

        for x, y in ((0, -1), (0, 1), (1, 0), (-1, 0)):
            r, c, dist = row + x, col + y, 0

            while 0 <= r < height and 0 <= c < width:
                dist += 1
                if t[row][col] <= t[r][c]:
                    break
                r += x
                c += y

            score *= dist
        max_score = max(max_score, score)

print(max_score)
