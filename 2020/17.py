#!/usr/bin/env python
import sys
from collections import Counter
from itertools import product


def solve(lines, dimensions):
    zeros = [0] * (dimensions - 2)
    coordinates = {*product((-1, 0, 1), repeat=dimensions)} - {(0, 0, *zeros)}
    # fmt: off
    cubes = {
        (row, col, *zeros)
        for row, line in enumerate(lines)
        for col, char in enumerate(line)
        if char == "#"
    }
    # fmt: on

    for _ in range(6):
        # fmt: off
        # Kudos to https://github.com/dionyziz/advent-of-code/blob/master/2020/17/17.py
        neighbors = Counter(
            tuple(sum(x) for x in zip(cube, coordinate))
            for cube in cubes
            for coordinate in coordinates
        )  # possibility of a future neighbor

        cubes = {
            neighbor
            for neighbor, count in neighbors.items()
            if count == 3 or (count == 2 and neighbor in cubes)
        }
        # fmt: on

    return len(cubes)


lines = sys.stdin.read().splitlines()
print(solve(lines, 3))
print(solve(lines, 4))
