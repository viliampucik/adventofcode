#!/usr/bin/env python
from collections import defaultdict

lines = map(str.split, open(0).read().splitlines())
path, dirs = [], defaultdict(int)

for l in lines:
    if l[0] == "$":
        if l[1] == "cd":
            if l[2] == "..":
                path.pop()
            else:
                path.append(l[2])
    elif l[0] != "dir":
        for i in range(len(path)):
            dirs[tuple(path[: i + 1])] += int(l[0])

print(sum(size for size in dirs.values() if size <= 100000))

required = 30000000 - (70000000 - dirs[("/",)])

print(min(size for size in dirs.values() if size >= required))
