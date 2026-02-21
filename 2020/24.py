#!/usr/bin/env python
import re
import fileinput
from collections import Counter

coordinates = {
    # fmt: off
    "ne": 0+1j, "nw": -1+1j,
    "e":  1+0j, "w":  -1+0j,
    "se": 1-1j, "sw":  0-1j,
    # fmt: on
}
r = re.compile("|".join(coordinates))
tiles = set()  # black tiles only

for line in fileinput.input():
    tile = sum(map(coordinates.__getitem__, r.findall(line)))
    tiles ^= {tile}

print(len(tiles))

for _ in range(100):
    # fmt: off
    neighbors = Counter(
        tile + coordinate
        for tile in tiles
        for coordinate in coordinates.values()
    )  # possibility of a future neighbor

    tiles = {
        neighbor
        for neighbor, count in neighbors.items()
        if count == 2 or (count == 1 and neighbor in tiles)
    }
    # fmt: on

print(len(tiles))
