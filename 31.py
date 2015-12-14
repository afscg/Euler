coins = [0, 1, 2, 5, 10, 20, 50, 100, 200]

def ways(total, up):
    if total == 0:
        return 1

    if up == 0:
        return 0

    idx = coins.index(up)
    if total < up:
        return ways(total, coins[idx - 1])

    ret = 0
    rem = total
    while rem >= up:
        rem -= up
        ret += ways(rem, coins[idx - 1])

    ret += ways(total, coins[idx - 1])

    return ret

print(ways(200, 200))
