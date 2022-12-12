#!/usr/bin/env python
s1 = s2 = 0

for l in open(0):
    a1, a2, b1, b2 = map(int, l.replace(",", "-").split("-"))
    s1 += a1 <= b1 and b2 <= a2 or b1 <= a1 and a2 <= b2
    s2 += b1 <= a2 and a1 <= b2

print(s1)
print(s2)
