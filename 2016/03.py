#!/usr/bin/env python
import fileinput

count = 0
l = [[], [], []]

for line in fileinput.input():
    a, b, c = [int(i) for i in line.strip().split()]
    if a + b > c and a + c > b and b + c > a:
        count += 1
    l[0].append(a)
    l[1].append(b)
    l[2].append(c)

print(count)

count = 0

for i in l:
    for j in range(0, len(i), 3):
        a, b, c = i[j : j + 3]
        if a + b > c and a + c > b and b + c > a:
            count += 1

print(count)
