#!/usr/bin/env python
from collections import Counter

template, _, *rules = open(0).read().splitlines()
rules = dict(rule.split(" -> ") for rule in rules)
pairs, elements = Counter(map(str.__add__, template, template[1:])), Counter(template)

for i in 10, 30:
    for _ in range(i):
        for (a, b), count in pairs.copy().items():
            c = rules[a + b]
            pairs[a + b] -= count
            pairs[a + c] += count
            pairs[c + b] += count
            elements[c] += count

    print(max(elements.values()) - min(elements.values()))
