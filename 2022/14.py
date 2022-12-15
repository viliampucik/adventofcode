#!/usr/bin/env python
from itertools import count

step = lambda a: (a >= 0) - (a < 0)
m, bottom = set(), 0

for line in open(0).read().splitlines():
    path = [
        (int(x), int(y))
        for xy in line.split(" -> ")
        for x, y in [xy.split(",")]
    ]
    for a, b in zip(path, path[1:]):
        bottom = max(bottom, a[1], b[1])
        for i in range(a[0], b[0] + (xstep := step(b[0] - a[0])), xstep):
            for j in range(a[1], b[1] + (ystep := step(b[1] - a[1])), ystep):
                m.add((i, j))

# print(bottom, m)
# for y in range(11):
#     for x in range(493, 505):
#         print("#" if (x, y) in m else ".", end="")
#     print()

for u in count(1):
    s = (500, 0)

    while s[1] < bottom:
        while s + (0, 1) not in m and s[1] + 1 < bottom:
            s += (0, 1)

        if s + (-1, 1) not in m and s[1] + 1 < bottom:
            s += (-1, 1)
        elif s + (1, 1) not in m and s[1] + 1 < bottom:
            s += (1, 1)
        else:
            m.add(s)
            break


    if void or int(s.imag) >= bottom:
        break

print(u-1)

exit()



sign = lambda a: 1 if a == 0 else (a > 0) - (a < 0)
lines = open(0).read().splitlines()
for line in lines:
    path = []
    for xy in line.split(" -> "):
        x, y = xy.split(",")
        path.append(complex(int(x), int(y)))
    # print(path)
    # print(line)

    for a, b in zip(path, path[1:]):
        m.add(a)
        m.add(b)
        for x in range(int(a.real), int(b.real) + sign(b.real - a.real), sign(b.real - a.real)):
            for y in range(int(a.imag), int(b.imag) + sign(b.imag - a.imag), sign(b.imag - a.imag)):
                m.add(complex(x,y))

bottom = int(max(i.imag for i in m)) + 2
# print(bottom)
for u in count(1):
    void = False
    s = complex(500, 0)
    if s in m:
        break

    while True:
        # print(u, s)
        while s + 1j not in m and int(s.imag + 1) < bottom:
            s += 1j

            # if int(s.imag) >= bottom:
            #     void = True
            #     break

        if s + -1+1j not in m and int(s.imag + 1) < bottom:
            s += -1+1j
        elif s + 1+1j not in m and int(s.imag + 1) < bottom:
            s += 1+1j
        else:
            m.add(s)
            break


    # if void or int(s.imag) >= bottom:
    #     break

print(u-1)
# print(m)
# for y in range(11):
#     for x in range(493, 505):
#         print("#" if complex(x, y) in m else ".", end="")
#     print()

exit()
sign = lambda a: 1 if a == 0 else (a > 0) - (a < 0)
m = set()

lines = open(0).read().splitlines()
for line in lines:
    path = []
    for xy in line.split(" -> "):
        x, y = xy.split(",")
        path.append(complex(int(x), int(y)))
    # print(path)
    # print(line)

    for a, b in zip(path, path[1:]):
        m.add(a)
        m.add(b)
        for x in range(int(a.real), int(b.real) + sign(b.real - a.real), sign(b.real - a.real)):
            for y in range(int(a.imag), int(b.imag) + sign(b.imag - a.imag), sign(b.imag - a.imag)):
                m.add(complex(x,y))

bottom = int(max(i.imag for i in m))
# print(bottom)
for u in count(1):
    void = False
    s = complex(500, 0)
    if s in m:
        break

    while int(s.imag) < bottom:
        # print(u, s)
        while s + 1j not in m:
            s += 1j

            if int(s.imag) >= bottom:
                void = True
                break

        if s + -1+1j not in m:
            s += -1+1j
        elif s + 1+1j not in m:
            s += 1+1j
        else:
            m.add(s)
            break


    if void or int(s.imag) >= bottom:
        break

print(u-1)
# print(m)
# for y in range(11):
#     for x in range(493, 505):
#         print("#" if complex(x, y) in m else ".", end="")
#     print()
