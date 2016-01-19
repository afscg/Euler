from math import sqrt

def inSeq(m):
    n = int(sqrt(2 * m))
    return n * (n + 1) // 2 == m

def wordval(w):
    val = 0
    for alphabet in w:
        val += ord(alphabet) - ord('A') + 1
    return val

words = None
with open("data/42.txt") as f:
    words = f.readline()

words = words.split(',')
words = [n.strip('"') for n in words]

total = 0

for w in words:
    if inSeq(wordval(w)):
        total += 1

print(total)
