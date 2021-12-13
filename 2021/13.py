#!/usr/bin/env python
import sys

positions, folds = sys.stdin.read().split("\n\n")
image, ab, first = set(), [0, 0], True

for position in positions.splitlines():
    image.add(tuple(map(int, position.split(","))))

for fold in folds.splitlines():
    i, j = int(fold[11] == "y"), int(fold[13:])
    ab[i] = j

    for pixel in list(image):
        if pixel[i] >= j:
            image.remove(pixel)
        if pixel[i] > j:
            pixel = list(pixel)
            pixel[i] = 2 * j - pixel[i]
            image.add(tuple(pixel))

    if first:
        print(len(image))
        first = False

for b in range(ab[1]):
    for a in range(ab[0]):
        print(" #"[(a, b) in image], end="")
    print()
