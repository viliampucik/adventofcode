#!/usr/bin/env pypy3
import sys

numbers = [int(i) for i in next(sys.stdin).split(",")]
last = numbers[-1]
age = {number: i+1 for i, number in enumerate(numbers)}

for i in range(len(numbers), 30_000_000):
    if i == 2020: print(last)
    age[last], last = i, i - age.get(last, i)

print(last)
