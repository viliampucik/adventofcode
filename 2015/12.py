#!/usr/bin/env python
def solve(data, ignore=None):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(solve(d, ignore) for d in data)
    elif isinstance(data, dict) and ignore not in data.values():
        return sum(solve(d, ignore) for d in data.values())

    return 0


print(solve(data := eval(input())))
print(solve(data, "red"))
