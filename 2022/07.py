#!/usr/bin/env python
from collections import defaultdict

lines = map(str.split, open(0).read().splitlines())
path, dirs, dir_sizes = [], defaultdict(int), defaultdict(int)

for l in lines:
    if l[0] == "$":
        if l[1] == "cd":
            if l[2] == "..":
                path.pop()
            else:
                path.append(l[2])
    elif l[0] != "dir":
        dirs[tuple(path)] += int(l[0])

for dir, size in dirs.items():
    for i in range(len(dir)):
        dir_sizes[tuple(dir[: i + 1])] += size

print(sum(size for size in dir_sizes.values() if size <= 100000))

required = 30000000 - (70000000 - dir_sizes[("/",)])

print(min(size for size in dir_sizes.values() if size >= required))
