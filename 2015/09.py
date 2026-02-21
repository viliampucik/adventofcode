#!/usr/bin/env python
from collections import defaultdict
from itertools import permutations

cities = defaultdict(dict)

for city_from, _, city_to, _, distance in map(str.split, open(0).read().splitlines()):
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
