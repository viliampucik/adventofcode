#!/usr/bin/env pypy3
import sys
from array import array

numbers = [int(i) for i in next(sys.stdin).split(",")]
last = numbers[-1]
size = 30_000_000
# age = {number: i+1 for i, number in enumerate(numbers)}  # slow dict alternative
# Despite more memory consumption the preallocated list approach is faster than dict
age = [0] * size
for i, number in enumerate(numbers):
    age[number] = i + 1

for i in range(len(numbers), size):
    if i == 2020: print(last)
    # age[last], last = i, i - age.get(last, i)  # slow dict alternative
    previous = age[last]
    age[last], last = i, i - previous if previous else 0

print(last)
