#!/usr/bin/env python
def solve(stacks, lines, step=1):
    for count, src, dst in lines:
        stacks[dst] += stacks[src][-count:][::step]
        stacks[src] = stacks[src][:-count]

    return "".join(s[-1] for s in stacks)


data, lines = open(0).read().split("\n\n")
stacks = [
    "".join(column).rstrip()
    for i, column in enumerate(zip(*data.splitlines()[-2::-1]))
    if i % 4 == 1
]
lines = [
    (int(line[1]), int(line[3]) - 1, int(line[5]) - 1)
    for line in map(str.split, lines.splitlines())
]

print(solve(stacks.copy(), lines, -1))
print(solve(stacks.copy(), lines))
