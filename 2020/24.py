#!/usr/bin/env python3
import re
import fileinput
from collections import defaultdict

coordinates = {
    "ne": 1+1j, "nw": -1+1j,
     "e": 2,     "w": -2,
    "se": 1-1j, "sw": -1-1j,
}
r = re.compile(r"[ns][ew]?|e|w")
tiles = {}

for line in fileinput.input():
    tile = sum(map(coordinates.__getitem__, r.findall(line)))
    tiles[tile] = (tiles.get(tile, 0) + 1) % 2

print(sum(tiles.values()))

for d in range(100):
    neighbors = {
        neighbor: 0
        for tile in tiles
        for coordinate in coordinates.values()
        if (neighbor := (tile + coordinate)) not in tiles # Python 3.8
    }

    tiles |= neighbors  # Python 3.9+

    new_tiles = {}

    for tile, color in tiles.items():
        blacks = sum(
            tiles.get(tile + coordinate, 0)
            for coordinate in coordinates.values()
        )
        new_tiles[tile] = int(blacks == 2 or (blacks == 1 and color == 1))

    tiles = new_tiles

print(sum(tiles.values()))
