def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def numDistinctPrimeFactors(n):
    if 'primes' not in numDistinctPrimeFactors.__dict__:
        numDistinctPrimeFactors.primes = [i for i in range(1000000) if isPrime(i)]
    ret = 0
    for p in numDistinctPrimeFactors.primes:
        if p > n:
            return ret
        if n % p != 0:
            continue
        ret += 1
        while n % p == 0:
            n //= p
    print('primes exhausted')

count = 0
target = 4
for i in range(1000000):
    if numDistinctPrimeFactors(i) == target:
        count += 1
        if count == target:
            print(i + 1 - target)
            break
    else:
        count = 0
