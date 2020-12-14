#!/usr/bin/env python
import fileinput


def write(memory, mask, address, value):
    if "X" in mask:
        i = mask.index("X")
        write(memory, mask[:i] + "0" + mask[i+1:], address, value)
        write(memory, mask[:i] + "1" + mask[i+1:], address, value)
    else:
        memory[int(mask, 2) | address] = value


m1 = {}
m2 = {}
mask = and_mask = or_mask = not_mask = None

for line in fileinput.input():
    key, value = line.strip().split(" = ")
    if key == "mask":
        mask = value
        and_mask = int(mask.replace("1", "0").replace("X", "1"), 2)
        or_mask = int(mask.replace("X", "0"), 2)
        not_mask = ~and_mask
    else:
        address = int(key[4:-1])
        value = int(value)
        m1[address] = value & and_mask | or_mask
        write(m2, mask, address & not_mask, value)

print(sum(m1.values()))
print(sum(m2.values()))
