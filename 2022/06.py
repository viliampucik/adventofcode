#!/usr/bin/env python
data = input()
for size in (4, 14):
    for i in range(size, len(data)):
        if len(set(data[i - size : i])) == size:
            print(i)
            break

# Less elegant, but way faster than "set()" approach
for size in (4, 14):
    distance, last_seen = size, {}

    for i, c in enumerate(data, start=1):
        if distance >= (d := i - last_seen.get(c, i - size)):
            distance = d
        else:
            distance += 1

        if distance >= size and i >= size:
            print(i)
            break

        last_seen[c] = i
