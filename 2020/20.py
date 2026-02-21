#!/usr/bin/env python
import re
import sys
from math import prod
from operator import itemgetter


def add(tiles, borders, name, lines, include_flipped=True):
    top, bottom = lines[0], lines[-1]
    left, right = "".join(map(itemgetter(0), lines)), "".join(map(itemgetter(-1), lines))

    tile_borders = {}

    # Start with flipped sides first. If non-flipped side mirrors its flipped side,
    # the later will overwrite the previous.
    if include_flipped:
        tile_borders |= {
            top[::-1]:    (TOP,    LR_FLIP),  # flipped
            bottom[::-1]: (BOTTOM, LR_FLIP),  # flipped
            left[::-1]:   (LEFT,   TB_FLIP),  # flipped
            right[::-1]:  (RIGHT,  TB_FLIP),  # flipped
        }

    tile_borders |= {
        top:    (TOP,    NO_FLIP),
        bottom: (BOTTOM, NO_FLIP),
        left:   (LEFT,   NO_FLIP),
        right:  (RIGHT,  NO_FLIP),
    }

    tiles[name], borders[name] = lines, tile_borders


def transform(tiles, borders, name, matching_border, matching_side):
    lines, (orientation, flip) = tiles[name], borders[name][matching_border]

    if flip == TB_FLIP:
        lines = tb_flip(lines)
    elif flip == LR_FLIP:
        lines = lr_flip(lines)

    if destination := orientation + matching_side:  # != +0+0j
        if destination in [2 * TOP, 2 * BOTTOM]:
            lines = tb_flip(lines)
        elif destination in [2 * LEFT, 2 * RIGHT]:
            lines = lr_flip(lines)
        elif orientation.real:
            lines = l_rotate(lines)
            if orientation.real == matching_side.imag:
                lines = tb_flip(lines)
        else:  # orientation.imag
            lines = r_rotate(lines)
            if orientation.imag == matching_side.real:
                lines = lr_flip(lines)

    add(tiles, borders, name, lines, False)

    if matching_border in borders[name]:
        del borders[name][matching_border]


NO_FLIP, LR_FLIP, TB_FLIP = range(3)
TOP, BOTTOM, LEFT, RIGHT = 1j, -1j, -1, 1

tb_flip = lambda lines: list(reversed(lines))
lr_flip = lambda lines: [line[::-1] for line in lines]
l_rotate = lambda lines: list(map("".join, reversed(list(zip(*lines)))))
r_rotate = lambda lines: list(map("".join, zip(*reversed(lines))))
hashes = lambda matrix: sum(row.count("#") for row in matrix)

tiles, borders = {}, {}

for tile in sys.stdin.read().strip().split("\n\n"):
    name, *lines = tile.splitlines()
    add(tiles, borders, int(name[-5:-1]), lines)

stack = set(borders.keys())
center = stack.pop()  # Pick a random tile as a center
image = {+0+0j: center}
tile_size = len(tiles[center])
add(tiles, borders, center, tiles[center], False) # And assume it does not need flipping

min_row = max_row = min_col = max_col = 0

while stack:
    candidate = stack.pop()

    for position, source in image.items():
        if match := borders[source].keys() & borders[candidate].keys():
            break

    if not match:
        stack.add(candidate)
        continue

    matching_border = match.pop()  # Unpack the first (and only) matching border
    matching_side = borders[source][matching_border][0]

    position += matching_side
    image[position] = candidate

    min_row, max_row = min(min_row, int(position.imag)), max(max_row, int(position.imag))
    min_col, max_col = min(min_col, int(position.real)), max(max_col, int(position.real))

    transform(tiles, borders, candidate, matching_border, matching_side)
    del borders[source][matching_border]

print(prod(
    image[c + r * 1j]
    for r in (min_row, max_row)
    for c in (min_col, max_col)
))

grid = [
    "".join(
        tiles[image[col + row * 1j]][i][1:-1]
        for col in range(min_col, max_col + 1)
    )
    for row in range(max_row, min_row-1, -1)
    for i in range(1, tile_size-1)
]

monster = (
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
)
padding = len(grid[0]) - len(monster[0]) + len("\n")
# Regex search is elegant and fast, however because of overlapping strings
# lookahead approach needs to be used
r = re.compile(
    "(?=(" + f".{{{padding}}}".join(monster).replace(" ", ".") + "))",
    re.DOTALL
)

monsters = 0

for _ in range(2):  # no flip, flip
    for _ in range(4):  # 4 rotations
        monsters = max(monsters, len(r.findall("\n".join(grid))))
        grid = r_rotate(grid)  # or l_rotate
    grid = lr_flip(grid)  # or tb_flip

print(hashes(grid) - hashes(monster) * monsters)
