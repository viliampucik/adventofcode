#!/usr/bin/env python
from collections import Counter
import sys

c = Counter(map(int, sys.stdin.read().split(",")))
h_min, h_max = min(c), max(c)

for p in (abs, lambda x: ((y := abs(x)) * (y + 1)) // 2):
    # fmt:off
    print(min(
        sum(
            p(k - h) * v
            for k, v in c.items()
        )
        for h in range(h_min, h_max + 1)
    ))
    # fmt:on
