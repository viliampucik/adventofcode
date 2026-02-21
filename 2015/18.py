#!/usr/bin/env python
def solve(t, size, corners):
    for _ in range(100):
        t = {
            light
            for r in range(size)
            for c in range(size)
            for light in [complex(r, c)]
            # fmt: off
            for neighbors in [sum(
                light + d in t
                for d in (1, -1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j)
            )]
            # fmt: on
            if neighbors == 3 or (neighbors == 2 and light in t) or light in corners
        }

    return len(t)


# fmt: off
t = {
    complex(r, c)
    for r, line in enumerate(open(0))
    for c, s in enumerate(line.strip())
    if s == "#"
}
# fmt: on
size = int(max(i.real for i in t)) + 1
corners = {0, size - 1, complex(0, size - 1), complex(size - 1, size - 1)}

print(solve(t.copy(), size, set()))
print(solve(t | corners, size, corners))
