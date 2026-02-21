#!/usr/bin/env python
def solve(data, size):
    for i in range(size, len(data)):
        if len(set(data[i - size : i])) == size:
            return i


print(solve(data := input(), 4))
print(solve(data, 14))
