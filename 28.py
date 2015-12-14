curr = 1
stride = 2
sum = 1

while stride <= 1000:
    sum += curr * 4 + stride * 10
    curr += stride * 4
    stride += 2

print(sum)
