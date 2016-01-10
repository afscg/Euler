pandigital = set('123456789')
result = set()

def isPan(x, y, z):
    return set(str(x) + str(y) + str(z)) == pandigital

for x in range(100):
    for y in range(10000):
        z = x * y
        if z > 10000:
            break
        if isPan(x, y, z):
            result.add(z)

print(result)
print(sum(result))
