from math import sqrt, ceil

def isTri(m):
    n = int(sqrt(2 * m))
    return n * (n + 1) // 2 == m

def isPen(m):
    n = ceil(sqrt(2 * m // 3))
    return n * (3 * n - 1) // 2 == m

target = 2
op = 0

while target > 0:
    op += 1
    hexagonal = op * (2 * op - 1)
    if isTri(hexagonal) and isPen(hexagonal):
        target -= 1
        print(hexagonal)
