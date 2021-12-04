#!/usr/bin/env python
import sys

numbers = sys.stdin.read().splitlines()
# fmt:off
gamma = "".join(
    "10" if bits.count("1") > len(bits) / 2 else "01"
    for bits in zip(*numbers)
)
# fmt:on
print(int(gamma[::2], 2) * int(gamma[1::2], 2))


def rating(data, cmp):
    for i in range(len(data[0])):
        _01 = {"0": [], "1": []}

        for number in data:
            _01[number[i]].append(number)
        # fmt:off
        if len(data := _01[
            "1" if cmp(len(_01["1"]), len(_01["0"])) else "0"
           ]) == 1:
            return int(data[0], 2)
        # fmt:on


print(rating(numbers[:], int.__ge__) * rating(numbers[:], int.__lt__))
