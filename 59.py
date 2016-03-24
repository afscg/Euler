#!/usr/bin/env python3

with open('data/59.txt') as f:
    ln = [int(x) for x in f.readline()[:-1].split(',')]

def keys():
    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                yield [a, b, c]

for key in keys():
    mask = (key * (len(ln) // len(key) + 1))[:len(ln)]
    cleartext = ''.join([chr(x ^ y) for x, y in zip(ln, mask)])
    if ' the ' in cleartext:
        print(sum([ord(x) for x in cleartext]))
        break
