#!/usr/bin/env python
floor, basement = 0, None

for i, c in enumerate(input()):
    floor += 1 if c == "(" else -1
    if floor == -1 and basement is None:
        basement = i + 1

print(floor)
print(basement)
