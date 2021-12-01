#!/usr/bin/env python
import fileinput

n = list(map(int, fileinput.input()))
print(sum(a < b for a, b in zip(n, n[1:])))
print(sum(a < b for a, b in zip(n, n[3:])))  # n[1:] and n[2:] would be repeated on both sides of the comparison statement
