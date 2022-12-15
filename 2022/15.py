#!/usr/bin/env python
from array import array
from cmath import polar
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache
from hashlib import md5
from heapq import heappop, heappush
from itertools import accumulate, chain, cycle, combinations, combinations_with_replacement, count, permutations, product
from math import factorial, gcd, prod
from operator import add, mul, gt, lt, eq, iand, ior, lshift, rshift, itemgetter
import networkx as nx
import re
#import regex

# lights1 = array("B", [0] * 1_000_000)
# lights2 = array("I", [0] * 1_000_000)

# r, phi = polar((j - i) / 1j)  # rotate 90 degrees

# @cache
# def solve(x):
#     return x
#
# solve.cache_clear()

# h = md5(f"{key}{i}".encode()).hexdigest()

# heap = [(0, 0, 0)]
# while heap:
#     risk, r, c = heappop(heap)
#     heappush(heap, (risk * 2, r_, c_))

# lcm = lcm * i // gcd(lcm, i)

# regexp = re.compile(r"([^:]+): (\d+)-(\d+) or (\d+)-(\d+)")
# (field, lo1, hi1, lo2, hi2) = regexp.fullmatch(line).groups()

# r = regex.compile("(?P<R> 42 (?&R)? 31 )")  # recursive pattern
# r.fullmatch(m)


# row = 2000000
# row_scanned = set()
# row_elements = set()
# lines = open(0).read().splitlines()

# for line in lines:
#     sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", line))
#     d = abs(sx - bx) + abs(sy - by)
#     if sy - d <= row <= sy + d:
#         w = d - abs(sy - row)

#         for x in range(sx - w, sx + w + 1):
#             row_scanned.add(x)

#         # print(sx, sy, bx, by, d, w, row_scanned, line)

#     if sy == row:
#         row_elements.add(sx)

#     if by == row:
#         row_elements.add(bx)

# print(len(row_scanned - row_elements))
import z3

s = z3.Solver()
x, y = z3.Int("x"), z3.Int("y")

s.add(0 <= x); s.add(x <= 4000000)
s.add(0 <= y); s.add(y <= 4000000)

def z3_abs(x):
    return z3.If(x >= 0, x, -x)

lines = open(0).read().splitlines()
for line in lines:
    sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", line))
    d = abs(sx - bx) + abs(sy - by)
    s.add(z3_abs(sx - x) + z3_abs(sy - y) > d)

s.check()
model = s.model()

print("Part 2:", model[x].as_long() * 4000000 + model[y].as_long())


# # m = set()
# lines = open(0).read().splitlines()
# r = defaultdict(list)

# for line in lines:
#     sx, sy, bx, by = map(int, re.findall(r"(-?\d+)", line))
#     d = abs(sx - bx) + abs(sy - by)

#     for y in range(sy - d, sy + d + 1):
#         w = d - abs(sy - y)
#         # for x in range(sx - w, sx + w + 1):
#             # m.add((x, y))
#         r[y].append((sx - w, sx + w))
#         # print(sx, sy, bx, by, d, w, row_scanned, line)

#     # m.add((sx, sy))
#     # m.add((bx, by))

# print("Searching...")
# space = 20
# space = 4_000_001
# for y in range(0, space):
#     if y % 1000 == 0:
#         print("Searching", y)

#     for x in range(0, space):
#         for a, b in r[y]:
#             if a <= x <= b:
#                 break
#         else:
#             print(x * 4000000 + y)
#             exit()

#     # # row = list()
#     # # for a, b in r[y]:
#     # #     if a <= (sx - w) <= b \
#     # #     or a <= (sx + w) <= b \
#     # #     or (sx - w) <= a <= (sx + w) \
#     # #     or (sx - w) <= b <= (sx + w):
#     # #         row.append((min(sx - w, a), max(sx + w, b)))
#     # #     else:
#     # #         row.append((a, b))
#     # # r[y] = row

#     # row = array("B", [0] * space)

#     # # print(r[y])
#     # for a, b in r[y]:
#     #     # print(a, b, end=", ")
#     #     for i in range( max(0, a), min(space, b+1) ):
#     #         row[i] = 1
#     # # print(row)
#     # for x in range(0, space):
#     #     if row[x] == 0:
#     # #     # if (x, y) not in m:
#     #         print(x * 4000000 + y)
#     #         exit()

# # print(len(m))
