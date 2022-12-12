#!/usr/bin/env python
card, door = list(map(int, open(0).read().splitlines()))
subject, modulus, loop = 7, 20201227, 0

# Baby-Step Giant-Step Algorithm
n = int(card**0.5)
babies = {pow(subject, j, modulus): j for j in range(n + 1)}
# Fermat’s Little Theorem
fermat = pow(subject, n * (modulus - 2), modulus)

while card not in babies.keys():
    loop += 1
    card = (card * fermat) % modulus

print(pow(door, loop * n + babies[card], modulus))
