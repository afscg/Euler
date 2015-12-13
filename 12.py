def intSqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def numFactor(n):
    'n > 1, need subtract 1 if n is perfect square'
    op = 1
    count = 0
    sq = intSqrt(n)
    for i in range(1, sq + 1):
        if n % i == 0:
            count += 2
    return count

count = 2
op = 3
res = 0
while res < 500:
    count += 1
    op += count
    res = numFactor(op)
print(count, op, res)
