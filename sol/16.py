n = 2 ** 1000
res = 0

while n > 0:
    res += n % 10
    n //= 10
print(res)
