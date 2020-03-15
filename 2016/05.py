#!/usr/bin/env python
import sys
from hashlib import md5
from itertools import count

c1 = c2 = 8
t1 = ""
t2 = [" "] * c2

for i in count(1):
    hash = md5((sys.argv[1] + str(i)).encode("ascii")).hexdigest()
    if hash[:5] == "00000":
        if c1 > 0:
            c1 -= 1
            t1 += hash[5]

        if c2 > 0 and hash[5].isdigit():
            j = int(hash[5])
            if 0 <= j < len(t2) and t2[j] == " ":
                c2 -= 1
                t2[j] = hash[6]

        if c1 <= 0 and c2 <= 0:
            break

print(t1)
print("".join(t2))
