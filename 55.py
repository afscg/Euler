#!/usr/bin/env python3

def is_palin(x):
    s = str(x)
    return s == s[::-1]

def is_lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if is_palin(n):
            return False
    return True

count = 0
for i in range(10000):
    if is_lychrel(i):
        count += 1
print(count)
