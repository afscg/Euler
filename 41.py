from itertools import permutations

def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

for digit in range(9):
    for s in permutations('987654321'[digit:]):
        n = int(''.join(s))
        if isPrime(n):
            print(n)
            break
