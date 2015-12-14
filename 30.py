ret = 0

for num in range(2, 354294):
    if num == sum([int(i) ** 5 for i in list(str(num))]):
        ret += num

print(ret)
