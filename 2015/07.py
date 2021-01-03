#!/usr/bin/env python
import sys
from functools import cache


@cache
def solve(wire):
    signal = []

    for instruction in wires[wire]:
        if instruction.isdigit() or instruction in ["&", "|", "~", "<<", ">>"]:
            signal.append(instruction)
        else:
            signal.append(solve(instruction))

    return str(eval(" ".join(signal)) & 65535)


wires = {}

for line in sys.stdin:
    instructions, wire = line.strip().split(" -> ")
    wires[wire] = instructions \
        .replace("AND", "&") \
        .replace("OR", "|") \
        .replace("NOT", "~") \
        .replace("LSHIFT", "<<") \
        .replace("RSHIFT", ">>") \
        .split()

print(a := solve("a"))
wires["b"] = [a]
solve.cache_clear()
print(solve("a"))
