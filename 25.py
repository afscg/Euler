x = 1
y = 1
i = 1

while x < 10 ** 999:
    x, y = y, x + y
    i += 1

print(i)
print(x)
