def isPrime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

candidates = ['0', '1', '2']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def isPrimeFamily8Sub(n, d):
    count = 3
    for i in digits:
        substitute = n.replace(d, i)
        if substitute[0] == '0' or not isPrime(int(substitute)):
            count -= 1
            if count == 0:
                return False
    return True

def isPrimeFamily8(n):
    n = str(n)
    for d in candidates:
        if d in n:
            if isPrimeFamily8Sub(n, d):
                print(n, d)
                return True
    return False

for i in range(0, 1000000):
    if isPrimeFamily8(i):
        break
