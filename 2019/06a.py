#!/usr/bin/env python
import fileinput

map = {}

for line in fileinput.input():
    planet, orbit = line.strip().split(")")
    map[orbit] = planet

orbits = 0

for orbit, planet in map.items():
    while True:
        orbits += 1
        if planet == "COM":
            break
        planet = map[planet]

print(orbits)
