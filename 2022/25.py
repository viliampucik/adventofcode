#!/usr/bin/env python
SNAFU = "=-012"

s1, s = "", sum(
    sum(5**i * (SNAFU.index(c) - 2) for i, c in enumerate(n[::-1]))
    for n in open(0).read().splitlines()
)

while s:
    s, m = divmod(s + 2, 5)
    s1 = SNAFU[m] + s1

print(s1)
