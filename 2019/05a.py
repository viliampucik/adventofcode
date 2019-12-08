#!/usr/bin/env python
import fileinput

# Split comma separated strings and convert them to numbers
list = [int(i) for i in next(fileinput.input()).strip().split(",")]

i = 0
input = 1

while i < len(list):
    instruction = list[i]
    opcode = instruction % 100

    if opcode in (1, 2):
        a = list[i + 1]
        b = list[i + 2]

        if instruction % 1000 < 100:  # hundreds
            a = list[a]

        if instruction % 10000 < 1000:  # thousands
            b = list[b]

        list[list[i + 3]] = a + b if opcode == 1 else a * b

        i += 4
    elif opcode == 3:
        list[list[i + 1]] = input
        i += 2
    elif opcode == 4:
        a = list[i + 1]

        if instruction % 1000 < 100:  # hundreds
            a = list[a]

        i += 2
        print(a)
    elif opcode == 99:
        break
