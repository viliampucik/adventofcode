#!/usr/bin/env python
import fileinput
from cmath import polar, pi


def rotate(phi):  # +90 degrees rotation
    phi -= 3 * pi / 2
    if phi < -pi:
        phi += 2 * pi
    return phi


a = {}
y = 0

for line in fileinput.input():
    for x, v in enumerate(line.strip()):
        if v == "#":
            a[complex(x, y)] = {}
    y += 1

for i in a.keys():
    for j in a.keys():
        if i != j:
            r, phi = polar(i - j)
            if phi not in a[i]:
                a[i][phi] = {}
            a[i][phi][r] = j

x = max(a, key=(lambda k: len(a[k])))
print(len(a[x]))

x = a[x]
i = 1
max = 200

while True:
    for phi in sorted(x.keys(), key=rotate):
        r = sorted(x[phi].keys())[0]

        i += 1
        if i > max:
            print(x[phi][r].real * 100 + x[phi][r].imag)
            break

        del x[phi][r]
        if len(x[phi]) == 0:
            del x[phi]

    if i > max or len(x) == 0:
        break
