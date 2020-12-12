#!/usr/bin/env python
import fileinput


def solve(instructions, waypoint=1+0j):
    position = 0+0j
    actions = {
        "N": 1j,
        "S": -1j,
        "E": 1,
        "W": -1,
        "F": waypoint,  # orientation (of waypoint)
    }
    waypoint_mode = waypoint != 1+0j

    for action, value in instructions:
        if action == "L":
            actions["F"] *= 1j**(value / 90)
        elif action == "R":
            actions["F"] /= 1j**(value / 90)
        elif action == "F":
            position += actions["F"] * value
        elif waypoint_mode:
            actions["F"] += actions[action] * value
        else:
            position += actions[action] * value

    return abs(position.real) + abs(position.imag)


instructions = [(line[0], int(line[1:])) for line in fileinput.input()]
print(solve(instructions))
print(solve(instructions, 10+1j))