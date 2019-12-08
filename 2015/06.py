#!/usr/bin/env python
import fileinput
import re

grid1 = [[0 for _ in range(1000)] for _ in range(1000)]
grid2 = [[0 for _ in range(1000)] for _ in range(1000)]

for line in fileinput.input():
    g = re.match(
        r"(?P<state>turn on|turn off|toggle) (?P<fx>\d+),(?P<fy>\d+) through (?P<tx>\d+),(?P<ty>\d+)",  # noqa: E501
        line,
    )
    if not g:
        pass

    for i in range(int(g.group("fx")), int(g.group("tx")) + 1):
        for j in range(int(g.group("fy")), int(g.group("ty")) + 1):
            if g.group("state") == "turn on":
                grid1[i][j] = 1
                grid2[i][j] += 1
            elif g.group("state") == "turn off":
                grid1[i][j] = 0
                grid2[i][j] = max(0, grid2[i][j] - 1)
            else:  # toggle
                grid1[i][j] = 0 if grid1[i][j] == 1 else 1
                grid2[i][j] += 2

print(sum([sum(row) for row in grid1]))
print(sum([sum(row) for row in grid2]))
