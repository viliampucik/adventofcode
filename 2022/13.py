#!/usr/bin/env python
from math import prod
from functools import cmp_to_key


def cmp(left, right):
    match left, right:
        case int(), list():
            return cmp([left], right)
        case list(), int():
            return cmp(left, [right])
        case int(), int():
            return left - right
        case list(), list():
            for i, j in zip(left, right):
                if (r := cmp(i, j)) != 0:
                    return r
            return cmp(len(left), len(right))


# fmt: off
packets = [
    eval(line)
    for line in open(0).read().splitlines()
    if len(line)
]

print(sum(
    i
    for i, (left, right) in enumerate(zip(packets[::2], packets[1::2]), start=1)
    if cmp(left, right) <= 0
))

two_six = [[[2]], [[6]]]
print(prod(
    i
    for i, packet in enumerate(
        sorted(packets + two_six, key=cmp_to_key(cmp)),
        start=1
    )
    if packet in two_six
))
