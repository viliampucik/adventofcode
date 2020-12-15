#!/usr/bin/env pypy3
import sys
from collections import defaultdict


def puzzle(last, seen, number):
    for i in range(len(seen), number):
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

print(puzzle(last, seen.copy(), 2020))
print(puzzle(last, seen.copy(), 30000000))
