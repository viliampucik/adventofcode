#!/usr/bin/env python
from collections import defaultdict
import re

data, mol = open(0).read().split("\n\n")
reps, mol = defaultdict(list), mol.strip()
for line in data.splitlines():
    src, dst = line.split(" => ")
    reps[src].append(dst)

combs, i = set(), 0
while i < len(mol):
    for size in (2, 1):
        if (j := i + size) - 1 < len(mol) and (m := mol[i:j]) in reps:
            for r in reps[m]:
                combs.add(mol[:i] + r + mol[j:])
            i += size
            break
    else:
        i += 1

print(len(combs))

# Kudos to https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4etju
print(
    len(re.findall(r"[A-Z]", mol))
    - 2 * len(re.findall(r"Rn", mol))
    - 2 * len(re.findall(r"Y", mol))
    - 1
)
