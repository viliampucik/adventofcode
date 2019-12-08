#!/usr/bin/env python
import sys

start, end = 264360, 746325

if len(sys.argv) == 2:
    start, end = [int(x) for x in sys.argv[1].strip().split("-")]

count = 0

while start <= end:
    previous = None
    double = False
    nondecrease = True

    for i, c in enumerate(str(start)):
        c = int(c)
        if i > 0:
            if previous == c:
                double = True
            elif previous > c:
                nondecrease = False
                break
        previous = c

    if double and nondecrease:
        # print(f"{count}: {start} {end}")
        count += 1

    start += 1

print(count)
