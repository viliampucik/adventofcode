#!/usr/bin/env python
import re
from collections import defaultdict
from math import prod


def parse(lines):
    re_number = re.compile(r"\d+")
    re_symbol = re.compile(r"[^\d.]")

    for y, line in enumerate(lines):
        for m in re_number.finditer(line):
            number, x0, x1 = int(m.group()), m.start() - 1, m.end() + 1
            for yy in range(max(y - 1, 0), min(y + 2, len(lines))):
                for m in re_symbol.finditer(lines[yy], x0, x1):
                    yield number, m.group(), m.start(), yy


s1, gears = 0, defaultdict(list)

for number, symbol, x, y in parse(open(0).read().splitlines()):
    s1 += number
    if symbol == "*":
        gears[x, y].append(number)

print(s1)
print(sum(prod(numbers) for numbers in gears.values() if len(numbers) == 2))
