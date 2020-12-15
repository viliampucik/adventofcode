#!/usr/bin/env pypy3
import sys

numbers = [int(i) for i in next(sys.stdin).split(",")]
previous = current = None
age = {}

for i in range(30_000_000):
    if i < len(numbers):
        current = numbers[i]
    elif previous not in age:
        current = 0
    else:  # previous in age
        current = i - 1 - age[previous]

    age[previous] = i - 1
    previous = current

    if i == 2019:
        print(current)

print(current)
