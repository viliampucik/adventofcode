#!/usr/bin/env python
from math import prod

timestamp, busses = open(0).read().splitlines()
timestamp, busses = int(timestamp), {
    # fmt: off
    i: int(bus)
    for i, bus in enumerate(busses.split(","))
    if bus != "x"
    # fmt: on
}

print(prod(min((-timestamp % bus, bus) for bus in busses.values())))

# Slower, but probably easier to understand

t, step = 0, 1

for delta, bus in busses.items():
    while (t + delta) % bus:
        t += step
    step *= bus  # All busses are co-primes, so their LCM is their multiplication

print(t)

# Faster alternative, but requires understanding of the Chinese remainder theorem

t, P = 0, prod(busses.values())

for a, p in busses.items():
    n = P // p
    inv = pow(n, -1, p)
    t = (t - a * n * inv) % P

print(t)
