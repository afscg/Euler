def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def isRightPrime(n):
    while n > 0:
        if not isPrime(n):
            return False
        n //= 10
    return True

def buildPrime(n, result):
    for i in [1, 2, 3, 5, 7, 9]:
        up = int(str(i) + str(n))
        if isPrime(up):
            if isRightPrime(up):
                result.append(up)
            buildPrime(up, result)

pds = [2, 3, 5, 7]
result = []
for i in pds:
    buildPrime(i, result)

print(len(result))
print(result)
print(sum(result))
