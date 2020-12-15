#!/usr/bin/env pypy3
import sys
from collections import defaultdict
from copy import deepcopy


def puzzle(last, seen, stop):
    for i in range(len(seen), stop):
        if last not in seen or len(seen[last]) == 1:
            last = 0
        else:
            last = seen[last][-1] - seen[last][-2]

        seen[last].append(i)

    return last


last = None
seen = defaultdict(list)
for i, n in enumerate(next(sys.stdin).split(",")):
    last = int(n)
    seen[last].append(i)

print(puzzle(last, deepcopy(seen), 2020))
print(puzzle(last, deepcopy(seen), 30000000))
