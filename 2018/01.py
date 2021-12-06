#!/usr/bin/env python
import fileinput
from itertools import accumulate, cycle

n = list(map(int, fileinput.input()))
print(sum(n))

seen = set([0])
print(next(f for f in accumulate(cycle(n)) if f in seen or seen.add(f)))
