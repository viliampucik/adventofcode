#!/usr/bin/env python

p, s1, s2 = 50, 0, 0

for number in (-int(line[1:]) if line[0] == 'L' else int(line[1:]) for line in open(0)):
  r, p = divmod(p + number, 100)
  s1 += p == 0
  s2 += abs(r)

print(s1, s2)
