#!/usr/bin/env python
import re
import fileinput
from collections import Counter


def descrypt(c, r):
    if c == "-":
        return " "

    return chr((ord(c) - ord("a") + r) % 26 + ord("a"))


s = 0
nos = None

for line in fileinput.input():
    name, sector, checksum = re.match(r"^(.*)-(\d+)\[(.+)\]$", line.strip()).groups()
    sector = int(sector)

    if "northpole" in "".join([descrypt(c, sector) for c in name]):
        nos = sector

    name = "".join(sorted(name.replace("-", "")))
    room = "".join([i[0] for i in Counter(name).most_common(len(checksum))])

    if room == checksum:
        s += sector

print(s)
print(nos)
