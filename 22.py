names = None

with open("data/22.txt") as f:
    names = f.readline()

names = names.split(',')
names = [n.strip('"') for n in names]
names.sort()

ret = 0

for i in range(len(names)):
    score = (i + 1) * sum([ord(c) - ord('A') + 1 for c in list(names[i])])
    ret += score

print(ret)
