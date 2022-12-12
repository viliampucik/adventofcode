#!/usr/bin/env python
cycle, x, signal, pos, crt = 0, 1, 0, 0, [" "] * 40 * 6


def step():
    global cycle, signal, pos

    cycle += 1
    if cycle in (20, 60, 100, 140, 180, 220):
        signal += cycle * x

    if pos % 40 in (x - 1, x, x + 1):
        crt[pos] = "#"
    else:
        crt[pos] = "."
    pos += 1


for line in open(0).read().splitlines():
    step()
    if line.startswith("addx"):
        step()
        x += int(line.split()[-1])

print(signal)

for i in range(0, len(crt), 40):
    print("".join(crt[i : i + 40]))
