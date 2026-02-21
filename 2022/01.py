#!/usr/bin/env python
c = sorted(sum(map(int, e.splitlines())) for e in open(0).read().split("\n\n"))
print(c[-1])
print(sum(c[-3:]))
