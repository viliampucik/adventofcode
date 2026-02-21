#!/usr/bin/env python
from collections import Counter
from functools import cache
import sys


@cache
def dfs(a, b, d):
    if d == 0:
        return {b: 1}

    x = pairs[a + b]
    # @cache does not work properly with Counter objects, using dict instead
    return dict(Counter(dfs(a, x, d - 1)) + Counter(dfs(x, b, d - 1)))


t, lines = sys.stdin.read().split("\n\n")
pairs = {}
for line in lines.splitlines():
    a, b = line.split(" -> ")
    pairs[a] = b

for i in 10, 40:
    c = Counter({t[0]: 1})
    for a, b in zip(t, t[1:]):
        c.update(dfs(a, b, i))

    print(max(c.values()) - min(c.values()))
