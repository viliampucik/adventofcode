#!/usr/bin/env python
def race(reindeers, s):
    # fmt: off
    return max(
        (speed * ( s // (fly + rest) * fly + min(fly, s % (fly + rest))), i, )
        for i, (speed, fly, rest) in enumerate(reindeers)
    )
    # fmt: on


reindeers = [
    # fmt: off
    list(map(int, (speed, fly, rest)))
    for _, _, _, speed, _, _, fly, *_, rest, _ in map(str.split, open(0).read().splitlines())
    # fmt: on
]
winners = [0] * len(reindeers)

print(race(reindeers, 2503)[0])

for s in range(1, 2503 + 2):
    winners[race(reindeers, s)[1]] += 1

print(max(winners))
