def intSqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def sumFactor(n):
    op = 1
    res = 0
    sq = intSqrt(n)
    for i in range(2, sq + 1):
        if n % i == 0:
            res += i + n // i
    if sq * sq == n:
        res -= sq
    return res + 1

res = 0
d = [0] * 10000

for i in range(2, 10000):
    d[i] = sumFactor(i)
for i in range(2, 10000):
    idx = d[i]
    if idx < 10000 and d[idx] == i and d[i] != i:
        res += i
        print(i, idx)

print(res)
