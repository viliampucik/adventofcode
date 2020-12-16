#!/usr/bin/env python
from math import prod
import re
import sys

groups = sys.stdin.read().strip().split("\n\n")
regexp = re.compile(r"([^:]+): (\d+)-(\d+) or (\d+)-(\d+)")
rules = []

for idx, line in enumerate(groups[0].split("\n")):
    (field, lo1, hi1, lo2, hi2) = regexp.fullmatch(line).groups()
    rules.append((idx, field, int(lo1), int(hi1), int(lo2), int(hi2)))

error_rate = 0
rules_count = len(rules)
cols = [
    set(range(rules_count))
    for _ in range(rules_count)
]  # start with all rules being valid for each column

for ticket in groups[2].split("\n")[1:]:
    valid_ticket = True
    ticket_rules = []

    for number in map(int, ticket.split(",")):
        valid_rules = set(
            idx
            for idx, _, lo1, hi1, lo2, hi2 in rules
            if lo1 <= number <= hi1 or lo2 <= number <= hi2
        )
        if len(valid_rules) == 0:
            error_rate += number
            valid_ticket = False
        elif valid_ticket:
            ticket_rules.append(valid_rules)

    if valid_ticket:
        for col, valid_rules in zip(cols, ticket_rules):
            col &= valid_rules  # col is a reference, not a copy

print(error_rate)

singles = set()
while len(singles) != rules_count:
    for col in cols:
        if len(col) == 1:
            singles |= col
        else:
            col -= singles

your_ticket = map(int, groups[1].split("\n")[-1].split(","))

print(prod(
    number
    for col, number in zip(cols, your_ticket)
    if rules[col.pop()][1].startswith("departure")
))
