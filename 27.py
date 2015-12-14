def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def primeCount(a, b):
    n = 0
    while isPrime(n * n + a * n + b):
        n += 1
    return n

maxCount = 0
maxA = 0
maxB = 0

for a in range(-999, 1000):
    for b in range(-999, 1000):
        c = primeCount(a, b)
        if c > maxCount:
            maxCount = c
            maxA = a
            maxB = b

print(maxCount)
print(maxA * maxB)
