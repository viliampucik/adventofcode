#!/usr/bin/env python
import fileinput
import re
from collections import Counter

# 1-3 a: abcde
p = re.compile(r"^(\d+)-(\d+) (.): (.*)$")

s1 = 0
s2 = 0

for line in fileinput.input():
    low, high, letter, password = p.findall(line.strip())[0]
    low, high = int(low), int(high)

    if low <= Counter(password)[letter] <= high:
        s1 += 1

    if (password[low - 1] == letter) ^ (password[high - 1] == letter):
        s2 += 1

print(s1)
print(s2)
