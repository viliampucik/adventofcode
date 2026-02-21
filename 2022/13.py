#!/usr/bin/env python
def cmp(left, right):
    match left, right:
        case int(), list():
            return cmp([left], right)
        case list(), int():
            return cmp(left, [right])
        case int(), int():
            return left - right
        case list(), list():
            for i, j in zip(left, right):
                if (r := cmp(i, j)) != 0:
                    return r
            return cmp(len(left), len(right))


# fmt:off
s1, two, six, packets = 0, 1, 2, [
    eval(line)
    for line in open(0).read().splitlines()
    if len(line)
]
# fmt:on
for i, (left, right) in enumerate(zip(packets[::2], packets[1::2])):
    if cmp(left, right) <= 0:
        s1 += i + 1
    for x in left, right:
        two += cmp(x, [[2]]) <= 0
        six += cmp(x, [[6]]) <= 0

print(s1)
print(two * six)
