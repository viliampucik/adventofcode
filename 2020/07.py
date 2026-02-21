#!/usr/bin/env python
import fileinput
import re
from collections import defaultdict

bags_in = defaultdict(dict)  # values are bags inside the bag
bags_out = defaultdict(set)  # values are bags outside of the bag

for line in fileinput.input():
    parent, children = line.strip().replace("no other bags", "").split("s contain ")
    children = re.findall(r"\d+ \w+ \w+ bag", children)

    for child in children:
        count, child = child.split(" ", 1)
        bags_in[parent][child] = int(count)
        bags_out[child].add(parent)

    if len(children) == 0:
        bags_in[parent] = None


def inside(bags):
    if bags == None:
        return 0

    c = 0
    for bag, count in bags.items():
        c += count
        c += count * inside(bags_in[bag])

    return c


def outside(bags):
    if len(bags) == 0:
        return set()

    s = bags.copy()
    for bag in bags:
        s.update(outside(bags_out[bag]))

    return s


print(len(outside(bags_out["shiny gold bag"])))
print(inside(bags_in["shiny gold bag"]))
