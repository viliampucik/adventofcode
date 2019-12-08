#!/usr/bin/env python
import fileinput
import re


def lights(instructions, brightness=False):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for mode, fx, fy, tx, ty in instructions:
        for i in range(fx, tx + 1):
            for j in range(fy, ty + 1):
                if mode == "turn on":
                    grid[i][j] = grid[i][j] + 1 if brightness else 1
                elif mode == "turn off":
                    grid[i][j] = max(0, grid[i][j] - 1) if brightness else 0
                else:  # toggle
                    if brightness:
                        grid[i][j] += 2
                    else:
                        grid[i][j] = 0 if grid[i][j] == 1 else 1

    return sum([sum(row) for row in grid])


instructions = []

for line in fileinput.input():
    mode, fx, fy, tx, ty = re.match(
        r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", line,
    ).groups()
    instructions.append((mode, int(fx), int(fy), int(tx), int(ty)))

print(lights(instructions))
print(lights(instructions, True))
