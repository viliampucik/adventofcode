#!/usr/bin/env python
data = input()
for size in (4, 14):
    for i in range(size, len(data)):
        if len(set(data[i - size : i])) == size:
            print(i)
            break
