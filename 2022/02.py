#!/usr/bin/env python
s1 = s2 = 0

for i, j in map(str.split, open(0).read().splitlines()):
    i, j = ord(i) - ord("A"), ord(j) - ord("X")
    s1 += 1 + j + (j - i + 1) % 3 * 3
    s2 += 1 + j * 3 + (j + i - 1) % 3

print(s1)
print(s2)
