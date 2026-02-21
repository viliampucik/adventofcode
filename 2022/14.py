#!/usr/bin/env python
from itertools import pairwise
from collections import deque

# Kudos to https://www.reddit.com/r/adventofcode/comments/zli1rd/comment/j061f6z
def solve(check, path=deque([500])):
    while True:
        pos = path[-1]
        for dst in pos + 1j, pos - 1 + 1j, pos + 1 + 1j:
            if dst not in blocked and dst.imag < bottom + 2:
                path.append(dst)
                break
        else:
            if check(pos):
                return len(blocked) - rocks
            blocked.add(pos)
            path.pop()


blocked = {
    complex(x, y)
    for line in open(0).read().splitlines()
    for (x1, y1), (x2, y2) in pairwise(map(eval, line.split("->")))
    for x in range(min(x1, x2), max(x1, x2) + 1)
    for y in range(min(y1, y2), max(y1, y2) + 1)
}

rocks, bottom = len(blocked), int(max(i.imag for i in blocked))

print(solve(lambda pos: pos.imag > bottom))
print(solve(lambda pos: pos == 500) + 1)
