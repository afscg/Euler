def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def findConsecutivePrimes(primes):
    for chain in range(len(primes), 0, -1):
        target = sum(primes[:chain])
        index = chain
        while True:
            if target >= 1000000:
                break
            if isPrime(target):
                print('prime', target, 'has', chain, 'elements')
                return
            if index > len(primes):
                break
            target = target - primes[index - chain] + primes[index]
            index += 1

primes = [i for i in range(50000) if isPrime(i)]
findConsecutivePrimes(primes)
