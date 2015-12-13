def isPrime(x):
    for i in range(2, (x >> 1) + 2):
        if x % i == 0:
            return False
    return True

n = 600851475143
factor = 2
maxPrime = 0

while n > factor:
    remain = n % factor
    if remain != 0:
        factor += 1
        continue
    if factor > maxPrime and isPrime(factor):
        maxPrime = factor
    n /= factor
    print(factor, n)
print(maxPrime)
