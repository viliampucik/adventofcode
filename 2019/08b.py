#!/usr/bin/env python
import fileinput

list = list(next(fileinput.input()).strip())

w, h = 25, 6
size = w * h
image = ["2"] * size

for i in range(0, len(list), size):
    for c, v in enumerate(list[i : i + size]):  # noqa: E203
        if image[c] == "2":
            image[c] = v

for i in range(0, len(image), w):
    print("".join(image[i : i + w]).replace("0", " "))  # noqa: E203
