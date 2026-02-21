#!/usr/bin/env python
# fmt: off
def solve(lines, ticker):
    return next(
        sue
        for sue, line in enumerate(lines, start=1)
        if all(ticker[key](value) for key, value in line.items())
    )


ticker = {
    "children":    lambda a: a == 3,
    "cats":        lambda a: a == 7,
    "samoyeds":    lambda a: a == 2,
    "pomeranians": lambda a: a == 3,
    "akitas":      lambda a: a == 0,
    "vizslas":     lambda a: a == 0,
    "goldfish":    lambda a: a == 5,
    "trees":       lambda a: a == 3,
    "cars":        lambda a: a == 2,
    "perfumes":    lambda a: a == 1,
}

lines = [
    {
        l[i]: int(l[i + 1])
        for l in [line.replace(":", "").replace(",", "").split()]
        for i in range(2, len(l), 2)
    }
    for line in open(0).read().splitlines()
]

print(solve(lines, ticker))

ticker["cats"]        = lambda a: a > 7
ticker["trees"]       = lambda a: a > 3
ticker["pomeranians"] = lambda a: a < 3
ticker["goldfish"]    = lambda a: a < 5

print(solve(lines, ticker))
