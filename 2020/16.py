#!/usr/bin/env python
import re

raw_rules, your_ticket, nearby_tickets = open(0).read().split("\n\n")
regexp = re.compile(r"([^:]+): (\d+)-(\d+) or (\d+)-(\d+)")
rules = []

for line in raw_rules.splitlines():
    field, lo1, hi1, lo2, hi2 = regexp.fullmatch(line).groups()
    rules.append((field, int(lo1), int(hi1), int(lo2), int(hi2)))

error_rate = 0
rules_count = len(rules)
# start with all rules (indexes) being valid for each column
cols = [set(range(rules_count)) for _ in range(rules_count)]

for ticket in nearby_tickets.splitlines()[1:]:
    valid_ticket = True
    ticket_rules = []

    for number in map(int, ticket.split(",")):
        matching_rules = set(
            # fmt: off
            i
            for i, (_, lo1, hi1, lo2, hi2) in enumerate(rules)
            if lo1 <= number <= hi1 or lo2 <= number <= hi2
            # fmt: on
        )
        if not matching_rules:
            error_rate += number
            valid_ticket = False
        elif valid_ticket:
            ticket_rules.append(matching_rules)

    if valid_ticket:
        for col, matching_rules in zip(cols, ticket_rules):
            col &= matching_rules  # col is a reference, not a copy

print(error_rate)

total = 1
singles = set()
your_ticket = list(map(int, your_ticket.splitlines()[-1].split(",")))

while len(singles) != rules_count:
    for i, col in enumerate(cols):
        if len(col) > 1:
            col -= singles
        elif len(col) == 1:
            singles |= col
            if rules[col.pop()][0].startswith("departure"):
                total *= your_ticket[i]

print(total)
