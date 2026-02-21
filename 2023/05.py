#!/usr/bin/env python
from collections import deque

seeds, *maps = open(0).read().split("\n\n")
seeds = list(map(int, seeds.split(":")[1].split()))
maps = [
    sorted(
        [
            (src, src + length, dst - src)
            for line in m.splitlines()[1:]
            for dst, src, length in [map(int, line.split())]
        ]
    )
    for m in maps
]
# print(seeds, maps, len(maps))


def solve(s):
    for m in maps:
        for start, stop, offset in m:
            if start <= s < stop:
                s += offset
                break
    return s


def solve2(seeds):
    queue = deque([(a, a + b, 0) for a, b in zip(seeds[::2], seeds[1::2])])
    print(queue)

    while queue:
        a, b, i = queue.popleft()
        # print(a, b, i)

        if i == len(maps) - 1:
            yield a
            yield b
        else:
            m = maps[i]

            for start, stop, offset in m:
                if start < b and a < stop:
                    queue.append((max(start, a) + offset, min(stop, b) + offset, i + 1))

            first, last = m[0][0], m[-1][1]
            if b <= first or last <= a:
                queue.append((a, b, i + 1))
            else:
                if a < first < b:
                    queue.append((a, first, i + 1))
                if a < last < b:
                    queue.append((last, b, i + 1))


print(min(solve(s) for s in seeds))
print(min(solve2(seeds)))
