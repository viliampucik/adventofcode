#!/usr/bin/env pypy3
import re
from array import array

r = re.compile(r"(.+) (\d+),(\d+) through (\d+),(\d+)")
lights1 = array("B", [0] * 1_000_000)
lights2 = array("I", [0] * 1_000_000)

for line in open(0):
    action, *numbers = r.match(line).groups()
    col_min, row_min, col_max, row_max = map(int, numbers)

    for row in range(row_min, row_max + 1):
        for col in range(col_min, col_max + 1):
            bulb = row * 1000 + col
            if action == "turn on":
                lights1[bulb] = 1
                lights2[bulb] += 1
            elif action == "turn off":
                lights1[bulb] = 0
                if lights2[bulb] > 0:
                    lights2[bulb] -= 1
            else:  # action == "toggle":
                lights1[bulb] = 0 if lights1[bulb] else 1
                lights2[bulb] += 2

print(sum(lights1))
print(sum(lights2))
