left = 0
right = 0

for i in range(101):
    left += i * i
    right += i
right *= right

print (right - left)
