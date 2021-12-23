#!/usr/bin/env python
aim = h = d = 0

for cmd, x in map(str.split, open(0).read().splitlines()):
    x = int(x)
    # fmt: off
    if cmd == "down": aim += x
    elif cmd == "up": aim -= x
    else: h += x; d += aim * x  # cmd == "forward"
    # fmt: on
print(h * aim)
print(h * d)
