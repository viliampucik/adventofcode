#!/usr/bin/env python
import re
import sys

# fmt: off
r1 = re.compile(
    r"^"
    r"(?=(.*[aeiou]){3})"
    r"(?=.*(?P<twin>.)(?P=twin))"
    r"(?!.*(ab|cd|pq|xy))"
)
r2 = re.compile(
    r"^"
    r"(?=.*(?P<twins>..).*(?P=twins))"
    r"(?=.*(?P<repeat>.).(?P=repeat))"
)
# fmt: on
lines = sys.stdin.read().splitlines()
for r in r1, r2:
    print(sum(bool(r.search(line)) for line in lines))
