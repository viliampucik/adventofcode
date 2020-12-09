#!/usr/bin/env python
import fileinput
from itertools import combinations

n = [int(x) for x in fileinput.input()]

invalid = None

for i in range(25, len(n)):
    if n[i] not in map(sum, combinations(n[i-25: i], 2)):
        invalid = n[i]
        break

print(invalid)

start = stop = total = 0

while total != invalid:
    while total < invalid:
        total += n[stop]
        stop += 1
    while total > invalid:
        total -= n[start]
        start += 1

print(min(n[start:stop]) + max(n[start:stop]))
