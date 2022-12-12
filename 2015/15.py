#!/usr/bin/env python
import re
from math import prod


def divide(number, buckets):
    if buckets == 1:
        yield (number,)
    else:
        for bucket in range(number + 1):
            for rest in divide(number - bucket, buckets - 1):
                yield (bucket,) + rest


ingredients = [tuple(map(int, re.findall(r"-?\d+", line))) for line in open(0)]
s1 = s2 = 0

for buckets in divide(100, len(ingredients)):
    # fmt:off
    *props, cals = (
        max(sum(b * s for b, s in zip(buckets, slice)), 0)
        for slice in zip(*ingredients)
    )
    # fmt:on
    if s1 < (total := prod(props)):
        s1 = total
    if cals == 500 and s2 < total:
        s2 = total

print(s1)
print(s2)
