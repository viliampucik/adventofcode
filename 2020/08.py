#!/usr/bin/env python
import fileinput


def run(code, j=None):
    accumulator, i, visited = 0, 0, set()

    while i not in visited and i < len(code):
        visited.add(i)
        operation, number = code[i]

        if i == j:  # the place to replace nop with jmp and vice versa
            operation = "nop" if operation == "jmp" else "jmp"

        if operation == "acc":
            accumulator += number
            i += 1
        elif operation == "jmp":
            i += number
        else:  # nop
            i += 1

    return accumulator, i, visited


code = []

for line in fileinput.input():
    operation, number = line.split()
    code.append((operation, int(number)))

accumulator, _, visited = run(code)
print(accumulator)  # 1st part

for j in visited:
    if code[j][0] in ("nop", "jmp"):
        accumulator, i, _ = run(code, j)
        if i >= len(code):
            print(accumulator)  # 2nd part
            break
