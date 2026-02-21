#!/usr/bin/env python
from itertools import count
from collections import defaultdict, deque


def solve(elves, dirs, neighbors):
    moves, moved = defaultdict(list), False

    for e in elves:
        if all(e + n not in elves for n in neighbors):
            moves[e].append(e)
        else:
            moved = True
            for dir in dirs:
                if all(e + n not in elves for n in dir):
                    moves[e + dir[0]].append(e)
                    break
            else:
                moves[e].append(e)

    dirs.rotate(-1)

    elves = set()
    for k, v in moves.items():
        if len(v) == 1:  # Only one candidate for the position, using the new position
            elves.add(k)
        else:  # Multiple candidates, using their original positions instead
            elves.update(v)

    return elves, moved


elves = {
    complex(row, col)
    for row, line in enumerate(open(0).read().splitlines())
    for col, x in enumerate(line)
    if x == "#"
}
# fmt: off
dirs = deque([(-1, -1+1j, -1-1j), (1, 1+1j, 1-1j), (-1j, -1-1j, 1-1j), (1j, -1+1j, 1+1j)])
neighbors = (-1, 1, -1j, 1j, -1-1j, -1+1j, 1-1j, 1+1j)
# fmt: on
for i in count(1):
    elves, moved = solve(elves, dirs, neighbors)

    if i == 10:
        rows, cols = {e.real for e in elves}, {e.imag for e in elves}
        print(int((max(rows) - min(rows) + 1) * (max(cols) - min(cols) + 1) - len(elves)))

    if moved == False:
        print(i)
        break
