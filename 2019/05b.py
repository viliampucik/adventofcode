#!/usr/bin/env python
import fileinput

# Split comma separated strings and convert them to numbers
list = [int(i) for i in next(fileinput.input()).strip().split(",")]

i = 0
input = 5

while i < len(list):
    # print(f"{i}: {list}")
    instruction = list[i]
    opcode = instruction % 100

    if opcode in (1, 2, 7, 8):  # add, multiply, less than, equals
        a = list[i + 1]
        b = list[i + 2]

        if instruction % 1000 < 100:  # hundreds
            a = list[a]

        if instruction % 10000 < 1000:  # thousands
            b = list[b]

        if opcode == 1:
            list[list[i + 3]] = a + b
        elif opcode == 2:
            list[list[i + 3]] = a * b
        elif opcode == 7:
            list[list[i + 3]] = 1 if a < b else 0
        elif opcode == 8:
            list[list[i + 3]] = 1 if a == b else 0

        i += 4
    elif opcode == 3:  # input
        list[list[i + 1]] = input
        i += 2
    elif opcode == 4:  # output
        a = list[i + 1]

        if instruction % 1000 < 100:  # hundreds
            a = list[a]

        i += 2
        print(a)
    elif opcode in (5, 6):  # jump-if-true, jump-if-false
        a = list[i + 1]

        if instruction % 1000 < 100:  # hundreds
            a = list[a]

        if (opcode == 5 and a != 0) or (opcode == 6 and a == 0):
            b = list[i + 2]

            if instruction % 10000 < 1000:  # thousands
                b = list[b]

            i = b
        else:
            i += 3
    elif opcode == 99:
        break
