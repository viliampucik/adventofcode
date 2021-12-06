#!/usr/bin/env python
import fileinput
from collections import Counter
from itertools import combinations

lines, two, three = [line.strip() for line in fileinput.input()], 0, 0

for line in lines:
    r = Counter(line).values()
    if 2 in r:
        two += 1
    if 3 in r:
        three += 1

print(two * three)

for a, b in combinations(lines, 2):
    d = None
    for i, x, y in zip(range(len(a)), a, b):
        if x != y:
            if d is not None:
                break
            d = i
    else:  # no break
        print(a[:d] + a[d + 1 :])
        exit
