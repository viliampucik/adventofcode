#!/usr/bin/env python
from array import array
from cmath import polar
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import cache
from hashlib import md5
from heapq import heappop, heappush
from itertools import accumulate, chain, cycle, combinations, combinations_with_replacement, count, permutations, product
from math import factorial, gcd, prod, floor, sqrt
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

p = int(input())

# a = b = None

# for i in (2, 3, 5, 7, 11, 13, 17, 19, 23):
#     number = i
#     presents = 10 + i * 10

#     while presents < p:
#         number *= i
#         presents += number * 10

#     if b is None or b > number:
#         b = number
#     if a is None or a < number // i:
#         a = number // i

#     print(i, number // i, number, a, b, presents)

# print(a, b)


for i in count(1):
    presents = 0
    for j in range(1, i // 2 + 1):
        if i % j == 0:
            presents += j * 10
    if presents >= p:
        print(i)
        break
    if i % 1000 == 0:
        print(i, presents)

# 34_000_000
# 13_540_800
# 472_440

# 17600

# 1 1
# 2 1 2
# 3 1 3
# 4 1 2 4
# 5 1 5
# 6 1 2 3 6
# 7 1 7
# 8 1 2 4 8
# 9 1 3 9
# 10 1 2 5 10
# 15 1 3 5 15
# 16 1 2 4 8 16

# 2_097_152 20_971_510 41_943_030

# 2_476_099.0 2_097_152

1_236_880
