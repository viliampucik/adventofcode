#!/usr/bin/env python
import fileinput

str = next(fileinput.input()).strip()

d = {"<": -1, ">": +1, "^": +1j, "v": -1j}

# 1
s = 0
houses = {s}

for p in str:
    s += d[p]
    houses.add(s)

print(len(houses))

# 2
s, r = 0, 0
houses = {s, r}

for i, p in enumerate(str):
    if i % 2 == 0:
        s += d[p]
        houses.add(s)
    else:
        r += d[p]
        houses.add(r)

print(len(houses))
