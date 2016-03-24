def sameDigit(n):
    digits = list(str(n))
    digits.sort()
    for i in range(6, 1, -1):
        m = list(str(n * i))
        m.sort()
        if m != digits:
            return False
    return True

for i in range(1, 1000000):
    if sameDigit(i):
        print(i)
        break
