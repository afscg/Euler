def unitDiv(n):
    mantissa = []
    rem = 10
    curr = 0
    idx = None
    while idx is None:
        curr += 1
        rem %= n
        try:
            idx = mantissa.index(rem)
            break
        except:
            pass
        mantissa.append(rem)
        rem *= 10
    return curr - idx - 1

cycle = [unitDiv(i) for i in range(10, 1000)]
print(10 + cycle.index(max(cycle)))

