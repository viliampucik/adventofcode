#!/usr/bin/env python
import fileinput
from itertools import chain, combinations


def powerset(s):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    return chain.from_iterable(
        combinations(s, r)
        for r in range(len(s) + 1)
    )


table = str.maketrans('1X', '01')
m1 = {}
m2 = {}

for line in fileinput.input():
    key, value = line.strip().split(" = ")
    if key == "mask":
        mask = value
        mask_clear = int(mask.translate(table), 2)
        mask_set = int(mask.replace("X", "0"), 2)
        offsets = [
            sum(x)
            for x in powerset([
                1 << (35 - i)  # 2 ** (35 - 1)
                for i, bit in enumerate(mask)
                if bit == "X"
            ])
        ]
    else:
        address, value = int(key[4:-1]), int(value)

        m1[address] = value & mask_clear | mask_set

        address = address & ~mask_clear | mask_set
        for offset in offsets:
            m2[address | offset] = value

print(sum(m1.values()))
print(sum(m2.values()))
