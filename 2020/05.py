#!/usr/bin/env python
import fileinput

s = set()

for l in fileinput.input():
    l = l.strip().replace("F", "0").replace(
        "B", "1").replace("L", "0").replace("R", "1")
    s.add(int(l, 2))

print(max(s))

for i in range(min(s) + 1, max(s)):
    if i not in s:
        print(i)
        break
