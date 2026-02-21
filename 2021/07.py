#!/usr/bin/env python
from collections import Counter
from itertools import accumulate
import sys

c = Counter(map(int, sys.stdin.read().split(",")))
h_min, h_max = min(c), max(c)
a = list(accumulate(range(h_max - h_min + 1)))

for p in (abs, lambda x: a[abs(x)]):
    # fmt:off
    print(min(
        sum(
            p(k - h) * v
            for k, v in c.items()
        )
        for h in range(h_min, h_max + 1)
    ))
    # fmt:on
