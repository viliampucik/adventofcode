#!/usr/bin/env python
# fmt:off
s = [
    [int(i) for i in l.split()]
    for l in open(0).read().splitlines()
]
print(sum(max(r) - min(r) for r in s))
print(sum(
    a // b
    for r in s
    for a in r
    for b in r
    if a != b and a % b == 0
))
