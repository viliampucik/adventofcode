#!/usr/bin/env python
import sys

s1 = s2 = 0

for group in sys.stdin.read().split("\n\n"):
    s1 += len(set(group.replace("\n", "")))
    s2 += len(set.intersection(
        *map(set, group.strip().split("\n"))
    ))

print(s1)
print(s2)
