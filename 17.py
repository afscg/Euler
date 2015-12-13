twenty = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8, 6]
tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

# 1-20
n = sum(twenty)

# 21-99
for i in range(21, 100):
    n += tens[i // 10] + twenty[i % 10]

# 100 - 999
n *= 10
n += (sum(twenty[1:10]) + 10 * 9) * 100 - 3 * 9

# 1000
n += twenty[1] + 8

print(n)
