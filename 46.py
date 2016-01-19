from math import sqrt

def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

primes = [2, 3]
composites = set()
search = 8000

for i in range(5, search, 2):
    if isPrime(i):
        primes.append(i)

for i in primes:
    for j in range(int(sqrt(search))):
        composites.add(i + 2 * j * j)

for i in range(3, search, 2):
    if i not in composites:
        print(i)
        break
