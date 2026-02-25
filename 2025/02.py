#!/usr/bin/env python
from re import compile, findall

s1, s2, a, b = 0, 0, compile(r"^(\d+)\1$"), compile(r"^(\d+)\1+$")

for start, end in findall(r"(\d+)-(\d+)", *open(0)):
    for i in range(int(start), int(end) + 1):
        s = str(i)
        if a.match(s):
            s1 += i
        elif b.match(s):
            s2 += i

print(s1, s1 + s2)
