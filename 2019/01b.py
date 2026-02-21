#!/usr/bin/env python
import fileinput


def fuel(mass):
    fuel = 0

    # while mass > 8:
    #     mass = int(mass / 3) - 2
    #     fuel += mass
    while True:
        mass = int(mass / 3) - 2
        if mass <= 0:
            break
        fuel += mass

    return fuel


sum = 0

for line in fileinput.input():
    sum += fuel(int(line.strip()))

print(sum)
