#!/usr/bin/env python
import fileinput

# Split comma separated strings and convert them to numbers
list = [int(i) for i in next(fileinput.input()).strip().split(",")]

list[1] = 12
list[2] = 2

i = 0
while i < len(list):
    if list[i] == 1:
        list[list[i + 3]] = list[list[i + 1]] + list[list[i + 2]]
        i += 4
    elif list[i] == 2:
        list[list[i + 3]] = list[list[i + 1]] * list[list[i + 2]]
        i += 4
    elif list[i] == 99:
        break

print(list[0])
