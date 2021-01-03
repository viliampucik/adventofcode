#!/usr/bin/env python
import sys
from functools import cache


@cache
def solve(wire):
    if wire.isdigit():
        return int(wire)

    ins = wires[wire]

    if "AND" in ins:
        return solve(ins[0]) & solve(ins[2])
    elif "OR" in ins:
        return solve(ins[0]) | solve(ins[2])
    elif "NOT" in ins:
        return ~ solve(ins[1]) & 65535
    elif "LSHIFT" in ins:
        return solve(ins[0]) << solve(ins[2])
    elif "RSHIFT" in ins:
        return solve(ins[0]) >> solve(ins[2])
    else:
        return solve(ins[0])


wires = {}

for line in sys.stdin:
    ins, wire = line.strip().split(" -> ")
    wires[wire] = ins.split()

print(a := solve("a"))
wires["b"] = [str(a)]
solve.cache_clear()
print(solve("a"))
