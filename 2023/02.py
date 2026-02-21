#!/usr/bin/env python
import re
from math import prod

s1, s2, balls, r = 0, 0, {"red": 12, "green": 13, "blue": 14}, re.compile(r"(\d+) (\w+)")

for i, line in enumerate(open(0).read().splitlines(), start=1):
    maxes = {"red": 0, "green": 0, "blue": 0}

    for count, color in r.findall(line):
        maxes[color] = max(maxes[color], int(count))

    s1 += i * all(balls[color] >= count for color, count in maxes.items())
    s2 += prod(maxes.values())

print(s1)
print(s2)
