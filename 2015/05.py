#!/usr/bin/env python
import fileinput
import re

nice1, nice2 = 0, 0

for line in fileinput.input():
    vowels = re.findall(r"[aeiou]", line)
    repeats = re.search(r"(.)\1", line)
    blacklist = re.search(r"ab|cd|pq|xy", line)

    if vowels and len(vowels) >= 3 and repeats and not blacklist:
        nice1 += 1

    nonoverlap_repeats = re.search(r"(..).*\1", line)
    between_repeats = re.search(r"(.).\1", line)

    if nonoverlap_repeats and between_repeats:
        nice2 += 1


print(nice1)
print(nice2)
