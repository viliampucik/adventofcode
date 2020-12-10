#!/usr/bin/env python
import fileinput
from math import prod
from itertools import combinations


def solve(length):
    for c in combinations(n, length):
        if sum(c) == 2020:
            return prod(c)


n = list(map(int, fileinput.input()))
print(solve(2))
print(solve(3))
