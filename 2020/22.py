#!/usr/bin/env python
import sys
from collections import deque


def play(p1, p2, recursive):
    p1, p2, loop = deque(p1), deque(p2), set()

    while len(p1) and len(p2):
        if recursive:  # loop detection
            decks = (tuple(p1), tuple(p2))
            if decks in loop:
                return True, list(p1)
            else:
                loop.add(decks)

        a, b = p1.popleft(), p2.popleft()

        if recursive and len(p1) >= a and len(p2) >= b:
            p1winner = play(list(p1)[:a], list(p2)[:b], recursive)[0]
        else:
            p1winner = a > b

        if p1winner:
            p1.extend([a, b])
        else:
            p2.extend([b, a])

    return len(p1) > len(p2), list(p1) + list(p2)


def score(p1, p2, recursive):
    p = play(p1, p2, recursive)[1]
    print(sum(
        (len(p) - i) * card
        for i, card in enumerate(p)
    ))


p1, p2 = sys.stdin.read().split("\n\n")
p1 = list(map(int, p1.splitlines()[1:]))
p2 = list(map(int, p2.splitlines()[1:]))
score(p1, p2, False)
score(p1, p2, True)
