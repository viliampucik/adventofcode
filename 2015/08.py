#!/usr/bin/env python
s1 = s2 = 0

for line in open(0).read().splitlines():
    s1 += len(line) - len(eval(line))
    s2 += 2 + line.count("\\") + line.count('"')

print(s1)
print(s2)
