from itertools import permutations

primes = [0, 2, 3, 5, 7, 11, 13, 17]

def isSubStrDiv(n):
    n = str(n)
    for i in range(1, 8):
        if int(n[i:i+3]) % primes[i] != 0:
            return False
    return True

sum = 0

for s in permutations('1234567890'):
    num = int(''.join(s))
    if isSubStrDiv(num):
        print(num)
        sum += num

print(sum)
