#!/usr/bin/env python
import fileinput
from collections import defaultdict

mem = {}


def get(c, i):
    if i < len(c):
        return c[i]
    elif i in mem:
        return mem[i]
    else:
        return 0


def read(c, i, mode, base):
    i = get(c, i)
    if mode == 0:
        i = get(c, i)
    elif mode == 2:
        i = get(c, i + base)
    return i


def write(c, i, v, mode, base):
    if i < len(c):
        i = c[i]
    elif i in mem:
        i = mem[i]
    else:
        i = 0

    if mode == 2:
        i += base

    if i < len(c):
        c[i] = v
    else:
        mem[i] = v


def compute(c, white=False):
    i = 0
    base = 0

    pm = 0  # paint, move
    t = [-1, +1]  # -90 left, +90 right,
    d = [+1j, 1, -1j, -1]  # North, East, South, West
    di = 0
    p = 0 + 0j  # position
    panels = defaultdict(int)

    if white:
        panels[p] = 1

    def input():
        return panels[p]

    def output(a):
        nonlocal pm, di, p
        if pm == 0:  # paint
            panels[p] = a

        else:  # move
            di = (di + t[a]) % len(d)
            p += d[di]

        pm = (pm + 1) % 2

    while i < len(c):
        opcode = c[i] % 100
        modes = str(c[i]).zfill(5)[0:-2]

        if opcode in (1, 2, 7, 8):  # add, multiply, less than, equals
            a = read(c, i + 1, int(modes[-1]), base)  # hundreds
            b = read(c, i + 2, int(modes[-2]), base)  # thousands

            if opcode == 1:
                write(c, i + 3, a + b, int(modes[-3]), base)
            elif opcode == 2:
                write(c, i + 3, a * b, int(modes[-3]), base)
            elif opcode == 7:
                write(c, i + 3, 1 if a < b else 0, int(modes[-3]), base)
            elif opcode == 8:
                write(c, i + 3, 1 if a == b else 0, int(modes[-3]), base)

            i += 4
        elif opcode == 3:  # input
            write(c, i + 1, input(), int(modes[-1]), base)
            i += 2
        elif opcode == 4:  # output
            a = read(c, i + 1, int(modes[-1]), base)  # hundreds
            output(a)
            i += 2
        elif opcode in (5, 6):  # jump-if-true, jump-if-false
            a = read(c, i + 1, int(modes[-1]), base)  # hundreds

            if (opcode == 5 and a != 0) or (opcode == 6 and a == 0):
                i = read(c, i + 2, int(modes[-2]), base)  # thousands
            else:
                i += 3
        elif opcode == 9:  # base
            base += read(c, i + 1, int(modes[-1]), base)  # hundreds
            i += 2
        elif opcode == 99:
            break

    return panels


code = [int(i) for i in next(fileinput.input()).strip().split(",")]

print(len(compute(code[:], False)))

panels = compute(code[:], True)
reals = [int(i.real) for i in panels.keys()]
imags = [int(i.imag) for i in panels.keys()]

for i in range(max(imags), min(imags) - 1, -1):
    for j in range(min(reals), max(reals) + 1):
        print("#" if panels[complex(j, i)] == 1 else " ", end="")
    print()
