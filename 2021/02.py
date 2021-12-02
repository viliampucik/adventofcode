#!/usr/bin/env python
import fileinput

aim = h = d = 0

for l in fileinput.input():
    cmd, x = l.strip().split()
    x = int(x)
    # fmt: off
    if cmd == "down": aim += x
    elif cmd == "up": aim -= x
    else: h += x; d += aim * x  # cmd == "forward"
    # fmt: on
print(h * aim)
print(h * d)
