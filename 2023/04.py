#!/usr/bin/env python
lines = open(0).read().splitlines()
s1, copies = 0, [1] * len(lines)

for i, line in enumerate(lines):
    matches = len(set.intersection(*map(set, map(str.split, line.split(":")[1].split("|")))))
    s1 += 2 ** (matches - 1) if matches else 0
    for j in range(matches):
        copies[i + j + 1] += copies[i]

print(s1)
print(sum(copies))
