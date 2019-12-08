#!/usr/bin/env python
import fileinput

floor = 0
basement = None

for i, c in enumerate(next(fileinput.input()).strip()):
    if c == "(":
        floor += 1
    else:  # c == ")"
        floor -= 1
    if floor == -1 and basement is None:
        basement = i + 1

print(floor)
print(basement)
