#!/usr/bin/env python
import fileinput
from collections import Counter

m = None

for line in fileinput.input():
    line = line.strip()

    if m is None:
        m = [Counter() for _ in range(len(line))]

    for i, c in enumerate(line):
        m[i][c] += 1

most = ""
least = ""

for n in m:
    most += n.most_common(1)[0][0]
    least += n.most_common()[-1][0]

print(most)
print(least)
