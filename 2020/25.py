#!/usr/bin/env pypy3
import sys

keys = list(map(int, sys.stdin.read().splitlines()))
subject = 7
value = loop = 1
transform = lambda value, subject: (value * subject) % 20201227

while True:
    value = transform(value, subject)
    if value in keys:
        break
    loop += 1

subject = keys[keys.index(value) - 1]  # use the next key
value = 1

for _ in range(loop):
    value = transform(value, subject)

print(value)
