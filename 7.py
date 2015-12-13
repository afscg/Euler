def isPrime(x):
    for i in range(2, (x >> 1) + 2):
        if x % i == 0:
            return False
    return True

count = 0
factor = 1

while count < 10001:
    if isPrime(factor):
        count += 1
    factor += 1
print (factor - 1)
