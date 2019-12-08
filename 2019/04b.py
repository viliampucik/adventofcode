#!/usr/bin/env python
import sys

start, end = 264360, 746325

if len(sys.argv) == 2:
    start, end = [int(x) for x in sys.argv[1].strip().split("-")]

count = 0

while start <= end:
    previous = None
    duplicate = 0
    double = False
    nondecrease = True

    for i, c in enumerate(str(start)):
        c = int(c)

        if i > 0:
            if previous > c:
                nondecrease = False
                break
            elif previous == c:
                duplicate += 1
            else:  # previous < c
                if duplicate == 1:
                    double = True
                duplicate = 0

        previous = c

    if nondecrease and (double or duplicate == 1):
        # print(f"{count}: {start} {end}")
        count += 1

    start += 1

print(count)
