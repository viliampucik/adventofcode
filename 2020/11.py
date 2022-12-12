#!/usr/bin/env python
from collections import defaultdict


def solve(seats, neighbors, limit):
    while True:
        new_seats = {}
        for seat, occupied in seats.items():
            count = (seats[neighbor] for neighbor in neighbors[seat])
            new_seats[seat] = sum(count) < limit if occupied else not any(count)

        if seats == new_seats:
            return sum(new_seats.values())

        seats = new_seats


lines = open(0).read().splitlines()
size = len(lines)  # grid width and height are the same
# fmt: off
seats = {
    row + col*1j: False
    for row, line in enumerate(lines)
    for col, char in enumerate(line)
    if char == "L"
}

directions = {
    direction
    for row in (-1, 0, 1)
    for col in (-1, 0, 1)
    if (direction := row + col*1j)  # skip 0+0*j
}

# Precompute all possible (in)direct neighbors of each seat

neighbors_direct = {
    seat: [
        neighbor
        for direction in directions
        if (neighbor := seat + direction) in seats
    ]
    for seat in seats
}
# fmt: on
neighbors_adjacent = defaultdict(list)
for seat in seats:
    for direction in directions:
        neighbor = seat + direction
        while 0 <= neighbor.real < size and 0 <= neighbor.imag < size:
            if neighbor in seats:
                neighbors_adjacent[seat].append(neighbor)
                break
            neighbor += direction

print(solve(seats, neighbors_direct, 4))
print(solve(seats, neighbors_adjacent, 5))
