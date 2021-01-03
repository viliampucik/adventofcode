#!/usr/bin/env python
import sys
from functools import cache
from operator import iand, ior, lshift, rshift


@cache
def solve(wire):
    if wire.isdigit():
        return int(wire)

    ins = wires[wire]

    if len(ins) == 3:
        return ops[ins[1]](solve(ins[0]), solve(ins[2]))
    elif len(ins) == 2:
        return ~ solve(ins[1]) & 65535
    else:
        return solve(ins[0])


ops = {"AND": iand, "OR": ior, "RSHIFT": rshift, "LSHIFT": lshift}
wires = {}

for line in sys.stdin:
    ins, wire = line.strip().split(" -> ")
    wires[wire] = ins.split()

print(a := solve("a"))
wires["b"] = [str(a)]
solve.cache_clear()
print(solve("a"))
