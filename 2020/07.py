#!/usr/bin/env python
import fileinput
import re
from collections import defaultdict

bags_in = defaultdict(dict)  # values are bags inside the bag
bags_out = defaultdict(set)  # values are bags outside of the bag

for line in fileinput.input():
    parent, children = line.split(" bags contain ")
    for count, child in re.findall(r"(\d+) (\w+ \w+) bags?[,.]", children):
        bags_in[parent][child] = int(count)
        bags_out[child].add(parent)


def inside(name):
    c = 0
    for bag, count in bags_in[name].items():
        c += count
        c += count * inside(bag)
    return c


def outside(name):
    s = bags_out[name].copy()
    for bag in bags_out[name]:
        s.update(outside(bag))
    return s


print(len(outside("shiny gold")))
print(inside("shiny gold"))
