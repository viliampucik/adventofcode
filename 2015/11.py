#!/usr/bin/env python
import re
from itertools import product


def solve(password):
    found = None

    for i in range(1, len(password) + 1):
        if password[-i] == letters[-1]:
            next

        prefix = password[:-i]

        for suffix in product(letters[letters.index(password[-i]) + 1:], *([letters] * (i-1))):
            candidate = prefix + "".join(suffix)
            if r.search(candidate) and any(candidate[j:j+3] in triplets for j in range(len(candidate) - 2)):
                found = candidate
                break

        if found is not None:
            break

    return found


letters = "abcdefghjkmnpqrstuvwxyz"
triplets = set(
    "".join(triplet)
    for triplet in zip(letters, letters[1:], letters[2:])
)
r = re.compile(rf"([{letters}])\1.*([{letters}])\2")

print(password := solve(input()))
print(solve(password))
