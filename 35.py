from collections import deque

def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

primes = set()
for i in range(1000000):
    if isPrime(i):
        primes.add(i)

circ = []
for i in primes:
    p = deque(str(i))
    rs = set()
    for unused in range(len(p)):
        p.rotate(1)
        rs.add(int(''.join(p)))
    if rs <= primes:
        circ.append(i)

print(circ)
print(len(circ))
