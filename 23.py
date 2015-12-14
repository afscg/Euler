def sumDiv(n):
    left = 1
    right = n
    sum = -n
    while left < right:
        right = n // left
        if n % left == 0:
            sum += left
            if left != right:
                sum += right
        left += 1
    return sum

def isAbun(n):
    return sumDiv(n) > n

abun = [i for i in range(28124) if isAbun(i)]
numbers = [i for i in range(28124)]

for x in abun:
    for y in abun:
        if (x + y) < len(numbers):
            numbers[x + y] = 0

print(sum(numbers))
