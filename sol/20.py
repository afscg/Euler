from math import factorial

res = 0
n = factorial(100)

while n > 0:
    res += n % 10
    n //= 10
print(res)
