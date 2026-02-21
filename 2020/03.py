#!/usr/bin/env python
import fileinput
from math import prod


def trees(r_init, d_init, m):
    r, w, t = 0, len(m[0]), 0

    for d in range(d_init, len(m), d_init):
        r += r_init
        r %= w
        t += m[d][r] == "#"

    return t


m = [l.strip() for l in fileinput.input()]
print(trees(3, 1, m))
print(prod(trees(*init, m)
           for init in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
