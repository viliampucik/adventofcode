#!/usr/bin/env python
import fileinput

numbers = set()

for line in fileinput.input():
    a = int(line.strip())
    b = 2020 - a
    if b in numbers:
        print(a * b)
        exit
    else:
        numbers.add(a)
