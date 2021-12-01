#!/usr/bin/env python
import sys
from math import prod


# Kudos to https://github.com/hltk/adventofcode/blob/main/2020/22.py
def game(player1, player2, recursive):
    seen = set()

    while player1 and player2:
        if (state := (tuple(player1), tuple(player2))) in seen:
            return True, player1
        seen.add(state)

        (card1, *player1), (card2, *player2) = player1, player2

        if recursive and len(player1) >= card1 and len(player2) >= card2:
            cards1, cards2 = player1[:card1], player2[:card2]
            # fmt: off
            if (cards1_max := max(cards1)) > max(cards2) and \
               (cards1_max > (len(cards1) + len(cards2) - 2)):
                player1win = True
            else:
                player1win = game(cards1, cards2, recursive)[0]
            # fmt: on
        else:
            player1win = card1 > card2

        if player1win:
            player1.extend((card1, card2))
        else:
            player2.extend((card2, card1))

    return (True, player1) if player1 else (False, player2)


players = [
    # fmt: off
    list(map(int, player.splitlines()[1:]))
    for player in sys.stdin.read().split("\n\n")
    # fmt: on
]

for recursive in False, True:
    player = game(*players, recursive)[1]
    print(sum(map(prod, enumerate(reversed(player), 1))))
