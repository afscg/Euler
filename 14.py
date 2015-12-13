tableSize = 100000000
chainTable = [0] * tableSize
chainTable[1] = 1

def chainLen(n):
    global chainTable
    if n < tableSize and chainTable[n] != 0:
        return chainTable[n]
    elif n < tableSize:
        if n % 2 == 0:
            chainTable[n] = 1 + chainLen(n // 2)
        else:
            chainTable[n] = 1 + chainLen(n * 3 + 1)
    else:
        if (n % 2 == 0):
            return 1 + chainLen(n // 2)
        else:
            return 1 + chainLen(n * 3 + 1)
    return chainTable[n]

seed = 0
res = 0
for i in range(1, 1000000):
    temp = chainLen(i)
    if temp > res:
        seed = i
        res = temp
print(seed, res)
