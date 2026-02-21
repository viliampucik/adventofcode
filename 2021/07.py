#!/usr/bin/env python
c = sorted(map(int, input().split(",")))
median, mean = c[len(c) // 2], sum(c) // len(c)
# fmt:off
print(sum(
    abs(median - i)
    for i in c
))
print(sum(
    (y := abs(mean - i)) * (y + 1) // 2
    for i in c
))
# fmt:on
