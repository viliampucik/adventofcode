#!/usr/bin/env python
lines = open(0).read().splitlines()
# fmt:off
print(sum(
    (ord(x) - ord("a")) % 58 + 1
    for l in lines
    for x in set(l[: len(l) // 2]) & set(l[len(l) // 2 :])
))

print(sum(
    (ord(x) - ord("a")) % 58 + 1
    for a, b, c in zip(*[iter(lines)] * 3)
    for x in set(a) & set(b) & set(c)
))
