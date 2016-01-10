from itertools import permutations as perm

def isCon(base, n, remain):
    product = str(base * n)
    if remain.startswith(product):
        remain = remain[len(product):]
        if len(remain) == 0:
            return True
        return isCon(base, n + 1, remain)
    return False

def isConPan(num_str):
    for prefix in range(1, len(num_str) // 2 + 1):
        base = int(num_str[:prefix])
        if isCon(base, 1, num_str):
            return True
    return False

for s in perm('987654321'):
    candidate = ''.join(s)
    if isConPan(candidate):
        print(candidate)
        break
