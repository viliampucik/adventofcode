#!/usr/bin/env python
import fileinput

map = {}

for line in fileinput.input():
    planet, orbit = line.strip().split(")")
    map[orbit] = planet

you = {}
distance = 0
planet = map["YOU"]
while planet != "COM":
    you[planet] = distance
    planet = map[planet]
    distance += 1

distance = 0
planet = map["SAN"]
while planet not in you:
    planet = map[planet]
    distance += 1

print(distance + you[planet])
