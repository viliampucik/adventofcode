#!/usr/bin/env python
import numpy as np
import sys
from collections import deque, defaultdict
from itertools import combinations
from math import prod, sqrt
from random import choice

tiles = {}
raw_tiles = sys.stdin.read().strip().split("\n\n")
w = int(sqrt(len(raw_tiles)))

for tile in raw_tiles:
    name, *lines = tile.replace(".", "0").replace("#", "1").splitlines()

    top, bottom, left, right = lines[0], lines[-1], "", ""
    for line in lines:
        left += line[0]
        right += line[-1]

    tiles[int(name[5:-1])] = set((
        int(top, 2),
        int(bottom, 2),
        int(left, 2),
        int(right, 2),
        int(top[::-1], 2),
        int(bottom[::-1], 2),
        int(left[::-1], 2),
        int(right[::-1], 2),
    ))

matching_sides = defaultdict(int)

for a, b in combinations(tiles.keys(), 2):
    matches = len(tiles[a] & tiles[b])
    matching_sides[a] += matches
    matching_sides[b] += matches

corners = sorted(matching_sides, key=matching_sides.get)[:4]
print(prod(corners))

for tile in raw_tiles:
    name, *lines = tile.replace(".", "0").replace("#", "1").splitlines()
    tiles[int(name[5:-1])] = np.array(
        [int(x) for x in "".join(lines)]
    ).reshape(10, -1)

search = deque(tiles.keys())
last_name = search.pop()

picture = {0+0j: last_name}
used_tiles = {last_name: 0+0j}
top_left = 0+0j

loop = len(search)  # stupid loop detection

while len(search):
    name = search.pop()
    tile = tiles[name]
    last_tile = tiles[last_name]

    found = False

    for _ in range(2):  # no flip, flip
        for _ in range(4):  # 4x left rotations
            if np.array_equal(last_tile[0], tile[-1]):  # tile on top
                position = used_tiles[last_name] + 1j
                found = True
            elif np.array_equal(last_tile[-1], tile[0]):  # tile at bottom
                position = used_tiles[last_name] - 1j
                found = True
            elif np.array_equal(last_tile[:, 0], tile[:, -1]):  # tile on left
                position = used_tiles[last_name] - 1
                found = True
            elif np.array_equal(last_tile[:, -1], tile[:, 0]):  # tile on right
                position = used_tiles[last_name] + 1
                found = True

            if found:
                break
            tile = np.rot90(tile)  # nothing found before another rotation

        if found:
            break
        tile = np.fliplr(tile)

    if found:
        loop = len(search)
        picture[position] = name
        used_tiles[name] = position
        tiles[name] = tile  # store back probably rotated or flipped tile
        last_name = name

        if (top_left.real >= position.real and top_left.imag < position.imag) or \
           (top_left.real > position.real and top_left.imag <= position.imag):
            # print(top_left, position, top_left.real > position.real and top_left.imag < position.imag)
            top_left = position
    else:
        search.appendleft(name)
        loop -= 1
        if loop <= 0:
            loop = len(search)
            # pick randomly a differed last_name from working used_tiles to break the loop
            last_name = choice(list(used_tiles.keys()))

# remove borders
for name, tile in tiles.items():
    tiles[name] = tile[1:-1, 1:-1]

image = np.hstack([
    np.vstack([
        tiles[picture[row+col*1j]]
        for col in range(int(top_left.imag), int(top_left.imag) - w, -1)
    ])
    for row in range(int(top_left.real), int(top_left.real) + w)
])
image_water = image.sum()

monster = np.array(
    [int(x) for x in "                  # #    ##    ##    ### #  #  #  #  #  #   ".replace(" ", "0").replace("#", "1")]
).reshape(3, -1)
monster_water = monster.sum()

for a in range(2):  # no flip, flip
    for b in range(4):  # 4 rotations
        monster_count = 0
        for row in range(image.shape[0] - monster.shape[0] + 1):
            for col in range(image.shape[1] - monster.shape[1] + 1):
                s = np.bitwise_and(
                    image[row:row + monster.shape[0], col:col + monster.shape[1]],
                    monster
                ).sum()
                monster_count += s == monster.sum()
        
        if monster_count:
            print(image.sum() - monster_count * monster.sum())
            quit()
            break

        image = np.rot90(image)
    image = np.fliplr(image)
