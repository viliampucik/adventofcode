#!/usr/bin/env python
import sys

groups = sys.stdin.read().split("\n\n")

print(sum(
    len(
        set(''.join(group.split()))
    )
    for group in groups
))

print(sum(
    len(
        set.intersection(*list(
            set(member)
            for member in group.strip().split("\n")
        ))
    )
    for group in groups
))
