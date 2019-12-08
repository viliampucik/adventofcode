#!/usr/bin/env python
import fileinput


def positions(path):
    x = y = 0
    for p in path:
        for i in range(int(p[1:])):
            if p[0] == "U":
                y += 1
            elif p[0] == "D":
                y -= 1
            elif p[0] == "R":
                x += 1
            elif p[0] == "L":
                x -= 1
            # print(f"{p} {p[0]} {int(p[1:])} {x} {y}")
            yield (x, y)


input = iter(fileinput.input())
wire1 = next(input).strip().split(",")
wire2 = next(input).strip().split(",")

unique_positions1 = set(positions(wire1))
unique_positions2 = set(positions(wire2))
crossings = unique_positions1.intersection(unique_positions2)

min_distance = None
for i in crossings:
    distance = abs(i[0]) + abs(i[1])
    # print(f"{i} {distance}")
    if min_distance is None or min_distance > distance:
        min_distance = distance

print(min_distance)
