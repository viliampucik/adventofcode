#!/usr/bin/env python
import fileinput
from math import prod
from itertools import combinations

# Slower, but works in case of "n" containing duplicates or single 1010

def solve(length):
    for c in combinations(n, length):
        if sum(c) == 2020:
            return prod(c)


n = list(map(int, fileinput.input()))
print(solve(2))
print(solve(3))

# Faster alternatives, but could lead into false positives if "n" contains duplicates or single 1010

def two(n):
    s = set(n)
    for x in s:
        if (y := 2020 - x) in s:
            return x * y


def tree(n):
    s = set(n)
    for i, x in enumerate(n):
        yz = 2020 - x
        for y in n[i + 1:]:
            if (z := yz - y) in s:
                return x * y * z


print(two(n))
print(tree(n))
