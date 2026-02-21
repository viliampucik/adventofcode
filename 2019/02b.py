#!/usr/bin/env python
import fileinput


def calculate(list, noun, verb):
    list[1] = noun
    list[2] = verb

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

    return list[0]


# Split comma separated strings and convert them to numbers
list = [int(i) for i in next(fileinput.input()).strip().split(",")]

for i in range(100):
    for j in range(100):
        # Using list slicing to clone the list and prevent modification
        # of the original
        if calculate(list[:], i, j) == 19690720:
            print(100 * i + j)
            break
