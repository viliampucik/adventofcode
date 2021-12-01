#!/usr/bin/env python
import fileinput

lines = [i.strip() for i in fileinput.input()]

d = {"U": -1, "D": +1, "L": -1j, "R": +1j}
p = 1 + 1j

for line in lines:
    for char in line:
        t = p + d[char]
        if 0 <= t.real <= 2 and 0 <= t.imag <= 2:
            p = t
    print(int(p.real * 3 + p.imag + 1), end="")
print()

m = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, "A", "B", "C", 0],
    [0, 0, "D", 0, 0],
]
p = 2 + 0j

for line in lines:
    for char in line:
        t = p + d[char]
        # fmt: off
        if 0 <= t.real < len(m) and \
           0 <= t.imag < len(m[int(t.real)]) and \
           m[int(t.real)][int(t.imag)] != 0:
           p = t
        # fmt: on
    print(m[int(p.real)][int(p.imag)], end="")
print()
