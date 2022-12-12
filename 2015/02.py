#!/usr/bin/env python
paper = ribbon = 0

for line in open(0):
    a, b, c = sorted(map(int, line.split("x")))
    paper += 2 * (a * b + b * c + c * a) + a * b
    ribbon += 2 * (a + b) + a * b * c

print(paper)
print(ribbon)
