#!/usr/bin/env python3

def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

side = 1
val = 1
primes = 0
diags = 1

while side < 100000:
    side += 2
    diags += 4
    delta = side - 1
    for _ in range(4):
        val += delta
        if is_prime(val):
            primes += 1
    if primes * 10 < diags:
        print(side)
        break
