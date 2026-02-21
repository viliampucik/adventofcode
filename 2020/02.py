#!/usr/bin/env python
import fileinput
import re
from collections import Counter

# 1-3 a: abcde
p = re.compile(r"^(?P<min>\d+)-(?P<max>\d+) (?P<letter>.): (?P<password>.*)$")

s1 = 0
s2 = 0

for line in fileinput.input():
    d = p.match(line.strip()).groupdict()
    min = int(d["min"])
    max = int(d["max"])

    c = Counter(d["password"]).get(d["letter"], 0)
    if min <= c <= max:
        s1 += 1

    a = d["password"][min - 1]
    b = d["password"][max - 1]
    if a != b and (a == d["letter"] or b == d["letter"]):
        s2 += 1

print(s1)
print(s2)
