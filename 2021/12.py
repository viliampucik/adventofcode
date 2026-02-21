#!/usr/bin/env python
from collections import defaultdict, deque
import fileinput

caves = defaultdict(list)

for line in fileinput.input():
    a, b = line.strip().split("-")
    caves[a].append(b)
    caves[b].append(a)

for duplicate in True, False:
    count, search = 0, deque((child, set(), duplicate) for child in caves["start"])

    while search:
        parent, lowers, duplicate = search.popleft()

        if parent == "end":
            count += 1
            continue
        elif parent.islower():
            if parent in lowers:
                if duplicate:
                    continue
                duplicate = True
            lowers.add(parent)

        search.extend((child, set(lowers), duplicate) for child in caves[parent] if child != "start")

    print(count)
