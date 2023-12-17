#!/usr/bin/env python
import re

lines = open(0).read().splitlines()
# fmt:off
digits = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
# fmt:on
keys = "|".join(digits.keys())


def solve(lines, r_first, r_last):
    return sum(
        # fmt:off
        digits[r_first.search(line)[1]] * 10 + digits[r_last.search(line)[1]]
        for line in lines
        # fmt:on
    )


print(solve(lines, re.compile(r"(\d)"), re.compile(r".*(\d)")))
print(solve(lines, re.compile(rf"({keys})"), re.compile(rf".*({keys})")))
