#!/usr/bin/env python
import fileinput
from math import prod
from itertools import count


def trees(r_init, d_init, m):
    r, d, w, t = r_init, d_init, len(m[0]), 0

    while d < len(m):
        t += m[d][r % w] == "#"
        r += r_init
        d += d_init

    return t


m = [l.strip() for l in fileinput.input()]
print(trees(3, 1, m))
print(prod(trees(*init, m)
           for init in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))

# Faster alternative

def toboggan(m, right, down):
    return sum(
        m[row][col % len(m[row])] == "#"
        for row, col in zip(
            range(0, len(m), down),
            count(0, right)
        )
    )


print(toboggan(m, 3, 1))
print(prod(toboggan(m, *init)
           for init in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))