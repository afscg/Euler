n = []

with open("../67.txt", "r") as f:
    n = [int(f.readline())]
    for ln in f:
        op = [int(x) for x in ln.split()]
        op[0] += n[0]
        op[-1] += n[-1]
        for i in range(1, len(op) - 1):
            op[i] += n[i - 1] if n[i - 1] > n[i] else n[i]
        n = op

print(max(n))
