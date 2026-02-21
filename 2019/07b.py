#!/usr/bin/env python
import fileinput
import itertools


def value(c, i, indirect):
    x = c[i]
    if indirect:
        x = c[x]
    return x


def compute(c, i, inp):
    while i < len(c):
        # print(f"{i}: {c}")
        instruction = c[i]
        opcode = instruction % 100

        if opcode in (1, 2, 7, 8):  # add, multiply, less than, equals
            a = value(c, i + 1, instruction % 1000 < 100)  # hundreds
            b = value(c, i + 2, instruction % 10000 < 1000)  # thousands

            if opcode == 1:
                c[c[i + 3]] = a + b
            elif opcode == 2:
                c[c[i + 3]] = a * b
            elif opcode == 7:
                c[c[i + 3]] = 1 if a < b else 0
            elif opcode == 8:
                c[c[i + 3]] = 1 if a == b else 0

            i += 4
        elif opcode == 3:  # input
            c[c[i + 1]] = inp.pop(0)
            i += 2
        elif opcode == 4:  # output
            a = value(c, i + 1, instruction % 1000 < 100)  # hundreds

            i += 2
            return i, a
        elif opcode in (5, 6):  # jump-if-true, jump-if-false
            a = value(c, i + 1, instruction % 1000 < 100)  # hundreds

            if (opcode == 5 and a != 0) or (opcode == 6 and a == 0):
                i = value(c, i + 2, instruction % 10000 < 1000)  # thousands
            else:
                i += 3
        elif opcode == 99:
            break

    return None, None


def amploop(phases):
    amp = [{"c": list(c), "i": 0, "inp": [p], "out": None} for p in phases]
    pos = 0
    out = 0

    while True:
        a = amp[pos]
        a["inp"].append(out)
        a["i"], out = compute(a["c"], a["i"], a["inp"])
        if out is None:
            break
        a["out"] = out
        pos = (pos + 1) % 5

    return amp[-1]["out"]


# Split comma separated strings and convert them to numbers
c = [int(i) for i in next(fileinput.input()).strip().split(",")]

print(max([amploop(ps) for ps in itertools.permutations(range(5, 10))]))
