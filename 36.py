def isPalin(x):
    s = str(x)
    return s == s[::-1]

def isBinPalin(x):
    b = bin(x)[2:]
    return b == b[::-1]

sum = 0

for i in range(1000000):
    if isPalin(i) and isBinPalin(i):
        sum += i

print(sum)
