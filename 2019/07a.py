#!/usr/bin/env python
import fileinput
import itertools


def compute(code_copy, inputs):
    code = list(code_copy)
    i = 0

    while i < len(code):
        # print(f"{i}: {code}")
        instruction = code[i]
        opcode = instruction % 100

        if opcode in (1, 2, 7, 8):  # add, multiply, less than, equals
            a = code[i + 1]
            b = code[i + 2]

            if instruction % 1000 < 100:  # hundreds
                a = code[a]

            if instruction % 10000 < 1000:  # thousands
                b = code[b]

            if opcode == 1:
                code[code[i + 3]] = a + b
            elif opcode == 2:
                code[code[i + 3]] = a * b
            elif opcode == 7:
                code[code[i + 3]] = 1 if a < b else 0
            elif opcode == 8:
                code[code[i + 3]] = 1 if a == b else 0

            i += 4
        elif opcode == 3:  # input
            code[code[i + 1]] = inputs.pop(0)
            i += 2
        elif opcode == 4:  # output
            a = code[i + 1]

            if instruction % 1000 < 100:  # hundreds
                a = code[a]

            i += 2
            output = a
        elif opcode in (5, 6):  # jump-if-true, jump-if-false
            a = code[i + 1]

            if instruction % 1000 < 100:  # hundreds
                a = code[a]

            if (opcode == 5 and a != 0) or (opcode == 6 and a == 0):
                b = code[i + 2]

                if instruction % 10000 < 1000:  # thousands
                    b = code[b]

                i = b
            else:
                i += 3
        elif opcode == 99:
            break

    return output


# Split comma separated strings and convert them to numbers
code = [int(i) for i in next(fileinput.input()).strip().split(",")]

max_output = 0

for phases in itertools.permutations(range(5)):
    output = 0
    for phase in phases:
        output = compute(code, [phase, output])
        # print(phases, phase, output)
    if max_output < output:
        max_output = output

print(max_output)
