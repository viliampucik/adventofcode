#!/usr/bin/env pypy3
# Kudos to https://github.com/taddeus/advent-of-code/blob/master/2020/23_cups.py
from array import array

def move(cups, moves, pad):
    nex = array("I", range(1, pad + 2))

    for label, next_label in zip(cups, cups[1:] + cups[:1]):
        nex[label] = next_label

    nex[0] = cups[0]  # head, points to the current cup

    if pad > len(cups):
        nex[-1] = nex[0]
        nex[cups[-1]] = max(cups) + 1

    for _ in range(moves):
        rem = nex[nex[0]]
        nex[nex[0]] = nex[nex[nex[rem]]]
        allrem = rem, nex[rem], nex[nex[rem]]

        dest = nex[0] - 1 if nex[0] > 1 else pad
        while dest in allrem:
            dest = pad if dest == 1 else dest - 1

        nex[nex[nex[rem]]] = nex[dest]
        nex[dest] = rem

        nex[0] = nex[nex[0]]

    cup = nex[1]
    while cup != 1:
        yield cup
        cup = nex[cup]


cups = list(map(int, input()))
print("".join(map(str, move(cups, 100, len(cups)))))
m = move(cups, 10_000_000, 1_000_000)
print(next(m) * next(m))
