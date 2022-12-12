#!/usr/bin/env python
dirs = {"U": 1j, "D": -1j, "L": -1, "R": 1}
sign = lambda a: (a > 0) - (a < 0)
rope, s1, s2 = [0] * 10, {0}, {0}

for line in open(0).read().splitlines():
    d, s = line.split()

    for _ in range(int(s)):
        rope[0] += dirs[d]

        for i in range(1, len(rope)):
            if abs(diff := rope[i - 1] - rope[i]) >= 2:
                rope[i] += complex(sign(diff.real), sign(diff.imag))

        s1.add(rope[1])
        s2.add(rope[-1])

print(len(s1))
print(len(s2))
