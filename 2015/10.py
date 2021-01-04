#!/usr/bin/env python
def solve(numbers, repeats):
    for _ in range(repeats):
        new_numbers, count, previous = [], 1, numbers[0]

        for current in numbers[1:]:
            if previous == current:
                count += 1
            else:
                new_numbers.extend((count, previous))
                count, previous = 1, current

        new_numbers.extend((count, previous))
        numbers = new_numbers

    return numbers


numbers = list(map(int, input()))

print(len(numbers := solve(numbers, 40)))
print(len(solve(numbers, 10)))
