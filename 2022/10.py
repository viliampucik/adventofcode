#!/usr/bin/env python
x, signal, crt = 1, 0, ""

for cycle, ins in enumerate(open(0).read().split(), start=1):
    signal += cycle * x if cycle % 40 == 20 else 0
    crt += "#" if (cycle - 1) % 40 - x in (-1, 0, 1) else "."

    if ins[-1].isdigit():  # workaround for negative numbers
        x += int(ins)

print(signal)

for i in range(0, len(crt), 40):
    print(crt[i : i + 40])
