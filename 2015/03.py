#!/usr/bin/env python

o = {"^": 1j, "v": -1j, ">": 1, "<": -1}
location, locations = 0, [0, 0]
houses1, houses2 = set((location,)), set(locations)

for i, c in enumerate(input()):
    location += o[c]
    houses1.add(location)

    locations[i % 2] += o[c]
    houses2.update(locations)

print(len(houses1))
print(len(houses2))
