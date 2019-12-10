#!/usr/bin/env python
import fileinput
from cmath import polar

a = {}

for y, line in enumerate(fileinput.input()):
    for x, v in enumerate(line.strip()):
        if v == "#":
            a[complex(x, y)] = {}

for i in a.keys():
    for j in a.keys():
        if i != j:
            r, phi = polar((j - i) / 1j)  # rotate 90 degrees
            if phi not in a[i]:
                a[i][phi] = {}
            a[i][phi][r] = j

x = max(a, key=(lambda k: len(a[k])))
print(len(a[x]))

x = a[x]
i = 200

while True:
    for phi in sorted(x.keys()):
        r = sorted(x[phi].keys())[0]

        i -= 1
        if i <= 0:
            print(x[phi][r].real * 100 + x[phi][r].imag)
            break

        del x[phi][r]
        if len(x[phi]) == 0:
            del x[phi]

    if i <= 0 or len(x) == 0:
        break
