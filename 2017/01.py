#!/usr/bin/env python
c = [int(i) for i in input()]
print(sum(c[i] for i in range(len(c)) if c[i] == c[i - 1]))
n = len(c) // 2
print(sum(c[i] * 2 for i in range(n) if c[i] == c[i - n]))
