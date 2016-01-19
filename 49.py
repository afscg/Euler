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

def checkSeq(candidates):
    for i in range(len(candidates)):
        for j in range(i + 1, len(candidates)):
            t = candidates[j] + candidates[j] - candidates[i]
            if t in candidates:
                print(candidates[i], candidates[j], t)

primes = set([i for i in range(10000) if isPrime(i)])

while primes:
    p = primes.pop()
    candidates = [p]
    for s in permutations(str(p)):
        s = int(''.join(s))
        if s in primes:
            candidates.append(s)
            primes.remove(s)
    candidates.sort()
    checkSeq(candidates)
