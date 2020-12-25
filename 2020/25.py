#!/usr/bin/env pypy3
import sys

keys = list(map(int, sys.stdin.read().splitlines()))
subject = 7
value = loop = 1
modulo = 20201227

while True:
    value = (value * subject) % modulo
    if value in keys:
        break
    loop += 1

subject = keys[keys.index(value) - 1]  # use the next key

print(pow(subject, loop, modulo))
