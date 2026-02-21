#!/usr/bin/env python
import sys

keys = list(map(int, sys.stdin.read().splitlines()))
subject, modulus, value, loop = 7, 20201227, 1, 1

while (value := (value * subject) % modulus) not in keys:
    loop += 1

subject = keys[keys.index(value) - 1]  # use the next key
print(pow(subject, loop, modulus))
