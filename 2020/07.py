#!/usr/bin/env python
import fileinput
import re
from collections import defaultdict, deque
from functools import cache

bags_in = defaultdict(dict)  # values are bags inside the bag
bags_out = defaultdict(set)  # values are bags outside of the bag

for line in fileinput.input():
    parent, children = line.split(" bags contain ")
    for count, child in re.findall(r"(\d+) (\w+ \w+) bags?[,.]", children):
        bags_in[parent][child] = int(count)
        bags_out[child].add(parent)


@cache
def inside(name):
    return sum(
        count + count * inside(bag)
        for bag, count in bags_in[name].items()
    )


@cache
def outside(name):
    s = bags_out[name].copy()
    for bag in bags_out[name]:
        s.update(outside(bag))
    return s


print(len(outside("shiny gold")))
print(inside("shiny gold"))

# Nonrecursive alternatives, faster then non-cached recursive ones, but slower than cached ones

def search_inside(name):
    colors, total = deque([(name, 1)]), -1  # compensate the total count for the "name" bag itself

    while colors:
        color, multiplier = colors.pop()
        total += multiplier
        for child, count in bags_in[color].items():
            colors.appendleft((child, multiplier * count))

    return total


def search_outside(name):
    colors, parents = deque([name]), set()

    while colors:
        for parent in bags_out[colors.pop()]:
            if parent not in parents:
                parents.add(parent)
                colors.appendleft(parent)

    return len(parents)


print(search_outside("shiny gold"))
print(search_inside("shiny gold"))
