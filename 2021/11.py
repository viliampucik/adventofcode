#!/usr/bin/env python
import sys

# fmt:off
octopuses = {
    complex(row, col): int(number)
    for row, line in enumerate(sys.stdin.read().splitlines())
    for col, number in enumerate(line)
}
# fmt:on
step, part1, part2 = 0, 0, None

while step := step + 1:
    flashing, flashed = set(), set()

    for o in octopuses.keys():
        octopuses[o] += 1
        if octopuses[o] > 9:
            flashing.add(o)

    while flashing:
        o = flashing.pop()
        octopuses[o] = 0
        flashed.add(o)

        for i in (
            # fmt:off
            -1 + 1j, -1j, +1 + 1j,
            -1,           +1,
            -1 - 1j, +1j, +1 - 1j
            # fmt:on
        ):
            if (x := o + i) in octopuses and x not in flashed:
                octopuses[x] += 1
                if octopuses[x] > 9:
                    flashing.add(x)

    if part2 is None and len(flashed) == len(octopuses):
        part2 = step

    if step <= 100:
        part1 += len(flashed)
    elif part2:
        break

print(part1)
print(part2)
