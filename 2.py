result = 0
left = 0
right = 1

while right <= 4000000:
    if right % 2 == 0:
        result += right
    left, right = right, left + right

print (result)
