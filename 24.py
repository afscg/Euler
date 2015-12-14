from math import factorial

i = 9
idx = 999999
seq = []

while i >= 0:
    rem, idx = divmod(idx, factorial(i))
    i -= 1
    seq.append(rem)

digits = [i for i in range(10)]

for i in seq:
    print(digits.pop(i), end='')

print()
