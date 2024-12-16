#!/usr/bin/env python
from collections import defaultdict, deque
from functools import cache

caves = defaultdict(list)

for line in open(0).read().splitlines():
    a, b = line.split("-")
    caves[a].append(b)
    caves[b].append(a)


# Recursive version with result caching
@cache
def dfs(parent, lowers, duplicate):
    if parent == "end":
        return 1
    elif parent.islower():
        if parent in lowers:
            if duplicate:
                return 0
            duplicate = True
        lowers |= {parent}

    return sum(
        dfs(child, frozenset(lowers), duplicate) for child in caves[parent] if child != "start"
    )


for duplicate in True, False:
    print(dfs("start", frozenset(), duplicate))

# Slightly slower, non recursive version with result caching
for duplicate in True, False:
    count, search, cache = (
        0,
        deque((child, frozenset(), duplicate, None) for child in caves["start"]),
        {},
    )

    while search:
        parent, lowers, duplicate, start = search.popleft()

        # Caching
        if start is not None:
            cache[parent, lowers, duplicate] = count - start
            continue
        elif (parent, lowers, duplicate) in cache:
            count += cache[parent, lowers, duplicate]
            continue
        else:
            search.extendleft([(parent, lowers, duplicate, count)])

        if parent == "end":
            count += 1
            continue
        elif parent.islower():
            if parent in lowers:
                if duplicate:
                    continue
                duplicate = True
            lowers |= {parent}

        search.extendleft(
            (child, frozenset(lowers), duplicate, None)
            for child in caves[parent]
            if child != "start"
        )

    print(count)
