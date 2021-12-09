#!/usr/bin/env python
from collections import defaultdict
import fileinput

part1 = part2 = 0

for line in fileinput.input():
    signals, output = line.strip().split(" | ")

    # fmt:off
    d = {
        l: set(s)
        for s in signals.split()
        if (l := len(s)) in (2, 4)
    }

    n = ""
    for o in output.split():
        l = len(o)
        if   l == 2: n += "1"; part1 += 1
        elif l == 4: n += "4"; part1 += 1
        elif l == 3: n += "7"; part1 += 1
        elif l == 7: n += "8"; part1 += 1
        elif l == 5:
            s = set(o)
            if   len(s & d[2]) == 2: n += "3"
            elif len(s & d[4]) == 2: n += "2"
            else:                    n += "5"
        else: # l == 6
            s = set(o)
            if   len(s & d[2]) == 1: n += "6"
            elif len(s & d[4]) == 4: n += "9"
            else:                    n += "0"
    # fmt:on
    part2 += int(n)

print(part1)
print(part2)
