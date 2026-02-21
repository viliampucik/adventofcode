#!/usr/bin/env python
from math import factorial
from itertools import permutations
from collections import defaultdict


def solve(first, people):
    limit = factorial(len(people)) // 2

    return max(
        sum(data[frozenset([a, b])] for a, b in zip(first + table, table + first))
        for i, table in enumerate(permutations(people))
        if i < limit  # avoid cyclic permutations and reversals
    )


people, data = set(), defaultdict(int)

for a, _, gain, n, *_, b in map(str.split, open(0).read().splitlines()):
    people.add(a)
    data[frozenset([a, b[:-1]])] += int(n) * (-1) ** (gain != "gain")

first = people.pop()
print(solve(tuple([first]), people))

people.add(first)
print(solve(tuple("0"), people))
