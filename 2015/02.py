#!/usr/bin/env python
import sys

paper = ribbon = 0

for line in sys.stdin.read().splitlines():
    a, b, c = sorted(map(int, line.split("x")))
    paper += 2 * (a * b + b * c + c * a) + a * b
    ribbon += 2 * (a + b) + a * b * c

print(paper)
print(ribbon)
