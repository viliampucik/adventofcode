#!/usr/bin/env python
import fileinput

n = list(map(int, fileinput.input()))
for i in 1, 3:
    print(sum(a < b for a, b in zip(n, n[i:])))
