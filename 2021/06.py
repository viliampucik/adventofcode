#!/usr/bin/env python
from collections import deque

d = deque([0] * 9)

for i in map(int, open(0).read().split(",")):
    d[i] += 1

for part in (80, 256 - 80):
    for _ in range(part):
        d.rotate(-1)
        d[6] += d[-1]
    print(sum(d))
