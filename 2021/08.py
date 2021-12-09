#!/usr/bin/env python
from collections import defaultdict
import fileinput

part1 = part2 = 0

for line in fileinput.input():
    signals, output = line.strip().split(" | ")

    part1 += sum(len(o) in (2, 4, 3, 7) for o in output.split())

    s = defaultdict(list)
    for i in signals.split():
        s[len(i)].append(set(i))

    _1, _4, _7, _8 = s[2][0], s[4][0], s[3][0], s[7][0]
    _235 = set.intersection(*s[5])
    _069 = set.intersection(*s[6])

    n = {
        # fmt:off
        "".join(sorted(_8 - (_235 - _069))): "0",
        "".join(sorted(_1                )): "1",
        "".join(sorted(_8 - (_069 - _235))): "2",
        "".join(sorted(_235 | _1         )): "3",
        "".join(sorted(_4                )): "4",
        "".join(sorted(_235 | _069       )): "5",
        "".join(sorted(_8 - (_1 - _069)  )): "6",
        "".join(sorted(_7                )): "7",
        "".join(sorted(_8                )): "8",
        "".join(sorted(_235 | _4         )): "9",
        # fmt:on
    }

    part2 += int("".join(n["".join(sorted(o))] for o in output.split()))

print(part1)
print(part2)
