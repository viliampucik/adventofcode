#!/usr/bin/env python
import fileinput
from cmath import phase

a = {}
y = 0

for line in fileinput.input():
    for x, v in enumerate(line.strip()):
        if v == "#":
            a[complex(x, y)] = set()
    y += 1

for i in a.keys():
    for j in a.keys():
        if i != j:
            a[i].add(phase(i - j))

print(max([len(v) for (k, v) in a.items()]))
