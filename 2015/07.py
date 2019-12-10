#!/usr/bin/env python
import fileinput
from collections import defaultdict
import re

w = defaultdict(int)
kit = {
    r"^(\d+) -> (\w+)$": r'w["\2"] = \1',
    r"^(\w+) AND (\w+) -> (\w+)$": r'w["\3"] = w["\1"] & w["\2"]',
    r"^(\w+) OR (\w+) -> (\w+)$": r'w["\3"] = w["\1"] | w["\2"]',
    r"^(\w+) LSHIFT (\d+) -> (\w+)$": r'w["\3"] = w["\1"] << \2',
    r"^(\w+) RSHIFT (\d+) -> (\w+)$": r'w["\3"] = w["\1"] >> \2',
    r"NOT (\w+) -> (\w+)": r'w["\2"] = ~ w["\1"]',
}

for line in fileinput.input():
    line = line.strip()

    for p, r in kit.items():
        s, c = re.subn(p, r, line)
        if c:
            # print(s)
            exec(s)
            break

print(w)
