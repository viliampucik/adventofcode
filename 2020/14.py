#!/usr/bin/env python
import fileinput
from itertools import chain, combinations


def powerset(s):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    return chain.from_iterable(
        combinations(s, r)
        for r in range(len(s) + 1)
    )


m1 = {}
m2 = {}
mask = mask_and = mask_or = mask_not = offsets = None

for line in fileinput.input():
    key, value = line.strip().split(" = ")
    if key == "mask":
        mask = value
        mask_and = int(mask.replace("1", "0").replace("X", "1"), 2)
        mask_or = int(mask.replace("X", "0"), 2)
        mask_not = ~mask_and
        offsets = [
            sum(x)
            for x in powerset([
                1 << (35 - i)  # 2 ** (35 - 1)
                for i, bit in enumerate(mask)
                if bit == "X"
            ])
        ]
    else:
        address = int(key[4:-1])
        value = int(value)

        m1[address] = value & mask_and | mask_or

        address &= mask_not
        for offset in offsets:
            m2[address | offset] = value

print(sum(m1.values()))
print(sum(m2.values()))
