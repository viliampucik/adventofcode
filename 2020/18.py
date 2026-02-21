#!/usr/bin/env python
import re
import sys
from operator import add, mul


def same_precedence(line):
    a, *values = line.split()
    a, ivalues = int(a), iter(values)

    for o, b in zip(ivalues, ivalues):
        b = int(b)
        a = add(a, b) if o == "+" else mul(a, b)

    return a


def add_before_mul(line):
    regexp = re.compile(r"\d+ \+ \d+")
    changes = 1

    while changes:
        line, changes = regexp.subn(
            lambda m: str(eval(m.group())),
            line
        )

    return eval(line)


def solve(lines, func):
    regexp = re.compile(r"\([^()]+\)")
    total = 0

    for line in lines:
        changes = 1

        while changes:
            line, changes = regexp.subn(
                lambda m: str(func(m.group()[1:-1])),
                line
            )

        total += func(line)

    return total


lines = sys.stdin.read().splitlines()
print(solve(lines, same_precedence))
print(solve(lines, add_before_mul))
