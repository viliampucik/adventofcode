#!/usr/bin/env python
from collections import defaultdict
import fileinput
import re

c, r, v = defaultdict(int), re.compile(r"\d+"), []

for l in fileinput.input():
    x1, y1, x2, y2 = map(int, r.findall(l))
    v.append((complex(x1, y1), complex(x2, y2)))

for diagonal in (False, True):
    for a, b in v:
        if diagonal ^ (a.real == b.real or a.imag == b.imag):
            i = b - a
            i /= max(abs(i.real), abs(i.imag))
            while a != b + i:
                c[a] += 1
                a += i

    print(sum(v > 1 for v in c.values()))
