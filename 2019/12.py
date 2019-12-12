#!/usr/bin/env python
import fileinput
import re


# reversed comparison
def cmp(a, b):
    return (a < b) - (a > b)


def simulate(p, v):
    # print(f"After {s} steps:")
    # gravity
    g = []
    for i, ii in enumerate(p):
        x = [0] * len(ii)
        for j, jj in enumerate(p):
            if i != j:
                for k in range(len(ii)):
                    x[k] += cmp(ii[k], jj[k])
        g.append(x)

    for i in range(len(p)):
        for j in range(len(v[i])):
            # velocity
            v[i][j] += g[i][j]
            # position
            p[i][j] += v[i][j]
        # print(f"{i} pos {p[i]} vel {v[i]}")
    return p, v


p = []  # positions
v = []  # velocities

for line in fileinput.input():
    x = [int(i) for i in re.findall(r"=(-?\d+)", line)]
    p.append(x)
    v.append([0] * len(x))

for s in range(1000):
    p, v = simulate(p, v)

e = 0
for i in range(len(p)):
    e += sum(abs(j) for j in p[i]) * sum(abs(j) for j in v[i])
print(e)
