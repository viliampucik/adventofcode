#!/usr/bin/env python
import fileinput
from math import prod
from itertools import combinations


def solve(length):
    for c in combinations(n, length):
        if sum(c) == 2020:
            return prod(c)


n = [int(line.strip()) for line in fileinput.input()]
print(solve(2))
print(solve(3))
