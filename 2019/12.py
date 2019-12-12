#!/usr/bin/env python
import fileinput
import re
from copy import deepcopy
from math import gcd


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


def cycle(p, v, p_copy, v_copy):
    # print(p, v, p_copy, v_copy)
    # return -1
    s = 0
    while True:
        p, v = simulate(p, v)
        s += 1

        same = True
        for i in range(len(p)):
            if p[i] != p_copy[i]:
                same = False
                break
            if v[i] != v_copy[i]:
                same = False
                break

        if same:
            return s


p = []  # positions
v = []  # velocities

for line in fileinput.input():
    x = [int(i) for i in re.findall(r"=(-?\d+)", line)]
    p.append(x)
    v.append([0] * len(x))

p_copy = deepcopy(p)
v_copy = deepcopy(v)

# A

for s in range(1000):
    p, v = simulate(p, v)

e = 0
for i in range(len(p)):
    e += sum(abs(j) for j in p[i]) * sum(abs(j) for j in v[i])
print(e)

# B

n = []
for i in range(len(p_copy[0])):
    p = [[c[i]] for c in p_copy]
    v = [[c[i]] for c in v_copy]
    n.append(cycle(p, v, deepcopy(p), deepcopy(v)))

lcm = n[0]
for i in n[1:]:
    lcm = lcm * i // gcd(lcm, i)
print(lcm)
