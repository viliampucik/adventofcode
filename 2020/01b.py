#!/usr/bin/env python
import fileinput

numbers = [int(line.strip()) for line in fileinput.input()]
length = len(numbers)

for i in range(length - 2):
    for j in range(1, length - 1):
        for k in range(2, length):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
                quit()
