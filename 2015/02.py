#!/usr/bin/env python
import fileinput

paper = 0
ribbon = 0

for line in fileinput.input():
    a, b, c = sorted([int(i) for i in line.strip().split("x")])
    area = [2 * a * b, 2 * a * c, 2 * b * c]
    paper += sum(area) + min(area) // 2
    ribbon += a + a + b + b + a * b * c

print(paper)
print(ribbon)
