#!/usr/bin/env python
import sys
from itertools import count
from hashlib import md5

h5, h6 = None, None

for i in count(1):
    hash = md5((sys.argv[1] + str(i)).encode("ascii")).hexdigest()
    if hash[:5] == "00000" and h5 is None:
        h5 = i
    if hash[:6] == "000000" and h6 is None:
        h6 = i
    if h5 and h6:
        break

print(h5)
print(h6)
