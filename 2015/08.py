#!/usr/bin/env python
import sys

s1 = s2 = 0

for line in sys.stdin:
    line = line.strip()
    s1 += len(line) - len(eval(line))
    s2 += 2 + line.count("\\") + line.count('"')

print(s1)
print(s2)
