for a in range(10, 100):
    for b in range(a, 100):
        al = a // 10
        br = b % 10
        if br != 0 and al / br == a / b and a % 10 == b // 10 and a != b:
            print(a, b)
