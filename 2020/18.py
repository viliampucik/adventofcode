#!/usr/bin/env python
import re
import sys
from operator import add, mul


def same_precedence(line):
    operations = {"+": add, "*": mul}
    values = line.split()
    a = int(values[0])

    for i in range(1, len(values)-1, 2):
        o = operations[values[i]]
        b = int(values[i + 1])
        a = o(a, b)

    return a


def add_before_mul(line):
    while m := re.search(r"\d+ \+ \d+", line):
        line = line[:m.start()] \
            + str(eval(m.group(0))) \
            + line[m.end():]

    return eval(line)


def solve(lines, func):
    total = 0

    for line in lines:
        while m := re.search(r"\([^()]+\)", line):
            line = line[: m.start()] \
                + str(func(m.group()[1:-1])) \
                + line[m.end():]

        total += func(line)

    return total


lines = sys.stdin.read().splitlines()
print(solve(lines, same_precedence))
print(solve(lines, add_before_mul))
