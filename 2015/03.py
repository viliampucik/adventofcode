#!/usr/bin/env python
orientation = {"^": 1j, "v": -1j, ">": 1, "<": -1}
location, locations = 0, [0, 0]
houses1, houses2 = set((location,)), set(locations)

for i, c in enumerate(input()):
    location += orientation[c]
    houses1.add(location)

    locations[(j := i % 2)] += orientation[c]
    houses2.add(locations[j])

print(len(houses1))
print(len(houses2))
