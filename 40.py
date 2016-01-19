def nthDigit(n):
    length = 1
    number = 1
    while n >= length:
        deduction = min(9 * (10 ** (length - 1)), n // length)
        n -= deduction * length
        number += deduction
        length += 1
    return int(str(number)[n])

product = 1

for i in range(7):
    product *= nthDigit(10 ** i - 1)

print(product)
