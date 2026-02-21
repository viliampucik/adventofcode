#!/usr/bin/env python
from itertools import chain

numbers, *data = open(0).read().strip().split("\n\n")

boards = []
for board in data:
    # fmt:off
    rows = [
        [int(x) for x in row.split()]
        for row in board.split("\n")
    ]
    # fmt:on
    boards.append([set(line) for line in chain(rows, zip(*rows))])

drawn, remaining = set(), set(range(len(boards)))

for number in map(int, numbers.split(",")):
    drawn.add(number)

    for i in remaining.copy():
        if any(line <= drawn for line in boards[i]):
            remaining.remove(i)

            if len(remaining) == len(boards) - 1 or not remaining:
                print(number * sum(set.union(*boards[i]) - drawn))
