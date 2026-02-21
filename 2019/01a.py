#!/usr/bin/env python
import fileinput

sum = 0

for line in fileinput.input():
    sum += int(int(line.strip()) / 3) - 2

print(sum)
