def solveCoin(n):
    up = 0
    down = 0
    tmp1, tmp2 = n, n
    while tmp1 % 5 != 0:
        tmp1 = tmp1 + 1
        up += 1
    while tmp2 % 5 != 0:
        tmp2 = tmp2 - 1
        down += 1
    return min(up, down)


n = int(input())
print(solveCoin(n) if n % 5 != 0 else 0)
