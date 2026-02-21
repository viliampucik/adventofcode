#!/usr/bin/env python
import fileinput

t = {"R": +1, "L": -1}  # +90 right, -90 left
d = [+1j, 1, -1j, -1]  # North, East, South, West
di = 0
p = 0  # position

ls = {p}  # locations
lo = None

for s in [
    (t[i[0]], int(i[1:])) for i in next(fileinput.input()).strip().split(", ")
]:
    di = (di + s[0]) % len(d)

    for i in range(s[1]):
        p += d[di]
        if lo is None and p in ls:
            lo = p
        ls.add(p)

print(abs(p.real) + abs(p.imag))
print(abs(lo.real) + abs(lo.imag))
