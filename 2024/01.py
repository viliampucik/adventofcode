#!/usr/bin/env python
from collections import Counter

left, right = zip(*(map(int, line.split()) for line in open(0)))
rcounts = Counter(right)

print(sum(abs(l - r) for l, r in zip(sorted(left), sorted(right))))
print(sum(l * rcounts[l] for l in left))
