from collections import Counter

perimap = Counter()

for a in range(1, 500):
    for b in range(1, a):
        for c in range(1, min(b, 999 - a - b)):
            perimeter = a + b + c
            if a * a == b * b + c * c:
                perimap[perimeter] += 1

print(perimap.most_common(1))
