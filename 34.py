from math import factorial as fact

for i in range(362880):
    if i == sum([fact(int(c)) for c in list(str(i))]):
        print(i)
