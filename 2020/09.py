#!/usr/bin/env python
import fileinput
from collections import deque

n = [int(x) for x in fileinput.input()]

# Kudos to https://github.com/jakobsen/advent-of-code-2020/blob/master/09.py
preamble = deque(n[:25])
invalid = None

for i in n[25:]:
    seen = set()
    for j in preamble:
        if i - j in seen:
            preamble.popleft()
            preamble.append(i)
            break
        seen.add(j)
    else:
        invalid = i
        break

print(invalid)

start = stop = total = 0

while total != invalid:
    while total < invalid:
        total += n[stop]
        stop += 1
    while total > invalid:
        total -= n[start]
        start += 1

print(min(n[start:stop]) + max(n[start:stop]))
