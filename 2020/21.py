#!/usr/bin/env python
import sys
from collections import Counter

ing_counts = Counter()
alg_ings = {}  # possible allergen -> ingredients candidates

for line in sys.stdin.read().splitlines():
    ings, algs = line.split(" (contains ")
    ings, algs = ings.split(), algs[:-1].split(", ")

    ing_counts.update(ings)

    for alg in algs:
        if alg in alg_ings:
            alg_ings[alg] &= set(ings)
        else:
            alg_ings[alg] = set(ings)

singles = set()
while len(singles) != len(alg_ings):
    for alg, ings in alg_ings.items():
        if len(ings) > 1:
            ings -= singles
        else:  # len(ings) == 1
            singles |= ings

print(sum(
    count
    for ing, count in ing_counts.items()
    if ing not in set.union(*alg_ings.values())
))

print(",".join(
    alg_ings[alg].pop()
    for alg in sorted(alg_ings)
))
