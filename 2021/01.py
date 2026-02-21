#!/usr/bin/env python
n = list(map(int, open(0).read().splitlines()))
for i in 1, 3:
    print(sum(a < b for a, b in zip(n, n[i:])))
