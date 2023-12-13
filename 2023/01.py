#!/usr/bin/env python
import re

lines = open(0).read().splitlines()
# fmt:off
print(sum(
    next(int(i) for i in line if i.isdigit()) * 10 +
    next(int(i) for i in reversed(line) if i.isdigit())
    for line in lines
))

digits = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
r = re.compile(f"(?=(\d|{ '|'.join(digits.keys()) }))")

print(sum(
    digits[x[0]] * 10 + digits[x[-1]]
    for line in lines
    for x in [r.findall(line)]
))
