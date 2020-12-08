#!/usr/bin/env python
import fileinput


def s(p, j=None):
    a, i, v = 0, 0, set()

    while i not in v and i < len(p):
        v.add(i)
        o, n = p[i]

        if i == j:
            o = "nop" if o == "jmp" else "jmp"

        if o == "acc":
            a += n
            i += 1
        elif o == "jmp":
            i += n
        else:  # nop
            i += 1

    return a, i, v


p = []

for l in fileinput.input():
    o, n = l.split()
    p.append((o, int(n)))

a, _, v = s(p)
print(a)

for j in v:
    if p[j][0] in ("nop", "jmp"):
        a, i, _ = s(p, j)
        if i >= len(p):
            print(a)
            break
