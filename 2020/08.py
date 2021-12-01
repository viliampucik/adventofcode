#!/usr/bin/env python
import fileinput


def run(code, visited, accumulator=0, i=0):
    while i not in visited and i < len(code):
        visited[i] = accumulator
        operation, number = code[i]

        if operation == "acc":
            accumulator += number
        elif operation == "jmp":
            i += number - 1

        i += 1

    return accumulator, i


code, visited = [], {}

for line in fileinput.input():
    operation, number = line.split()
    code.append((operation, int(number)))

accumulator, _ = run(code, visited)
print(accumulator)  # 1st part

# Non-brute force approach:
# Get a copy of the initial visited instrunctions
# because run() modifies the dict by accumulating
# newly visited instructions to prevent further loops
for j in set(visited.keys()):
    operation, number = code[j]
    # Skip instructions that would still continue in loop(s)
    # fmt: off
    if (operation == "nop" and (i := j + number) not in visited) or \
       (operation == "jmp" and (i := j + 1) not in visited):
    # fmt: on
       # And continue just from the next instruction with restored state
        accumulator, i = run(code, visited, visited[j], i)
        if i >= len(code):
            print(accumulator)  # 2nd part
            break
