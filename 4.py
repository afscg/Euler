def isPalindrome(x):
    div = 1
    while x // div >= 10:
        div *= 10
    while x != 0:
        if x // div != x % 10:
            return False
        x = (x % div) // 10;
        div //= 100;
    return True;

numbers = []

for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        numbers.append(i * j)

numbers.sort()
while len(numbers) > 0:
    last = numbers.pop()
    if isPalindrome(last):
        print (last)
        break
