#!/usr/bin/env python3

def digi_sum(n):
    return sum([int(i) for i in str(n)])

ret = 0
for a in range(100):
    for b in range(100):
        s = digi_sum(a ** b)
        if s > ret:
            ret = s
print(ret)
