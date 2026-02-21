#!/usr/bin/env python
import sys
from collections import defaultdict
from itertools import permutations

cities = defaultdict(dict)

for line in sys.stdin:
    city_from, _, city_to, _, distance = line.strip().split()
    cities[city_from][city_to] = int(distance)
    cities[city_to][city_from] = int(distance)

paths = [
    # fmt: off
    sum(
        cities[city_from][city_to]
        for city_from, city_to in zip(locations, locations[1:])
    )
    # fmt: on
    for locations in permutations(cities)
]

print(min(paths))
print(max(paths))
