#!/usr/bin/env python
import fileinput

list = list(next(fileinput.input()).strip())

size = 25 * 6
min = float("inf")
sum = None

for i in range(0, len(list), size):
    layer = "".join(list[i : i + size])  # noqa: E203
    zeros = layer.count("0")
    if zeros < min:
        min = zeros
        sum = layer.count("1") * layer.count("2")

print(sum)
