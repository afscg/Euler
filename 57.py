#!/usr/bin/env python3

a = 3
b = 2
ret = 0
for i in range(1000):
    a, b = a + b + b, a + b
    if len(str(a)) > len(str(b)):
        ret += 1
print(ret)
