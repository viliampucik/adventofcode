#!/usr/bin/env python
from itertools import combinations

containers = list(map(int, open(0).read().splitlines()))
# fmt: off
k = [
    sum(
        sum(comb) == 150
        for comb in combinations(containers, i)
    )
    for i in range(2, len(containers) + 1)
]
# fmt: on
print(sum(k))
print(next(i for i in k if i > 0))
