#!/usr/bin/env python
from hashlib import md5
from itertools import count

key, h5, h6 = input(), 0, 0

for i in count(1):
    h = md5(f"{key}{i}".encode()).hexdigest()
    # The nested conditions speed up evaluation
    if h.startswith("00000"):
        if not h5:
            h5 = i
            if h6:
                break
        if not h6 and h.startswith("000000"):
            h6 = i
            if h5:
                break

print(h5)
print(h6)
