#!/usr/bin/env python
from collections import deque
import fileinput

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
part1, part2 = 0, []

for line in fileinput.input():
    stack = deque()
    for c in line.strip():
        if c in "([{<":
            stack.appendleft(pairs[c])
        elif c != stack.popleft():
            part1 += points[c]
            break
    else:
        score = 0
        for c in stack:
            score = score * 5 + ")]}>".index(c) + 1
        part2.append(score)

print(part1)
print(sorted(part2)[len(part2) // 2])
