MOD = 10 ** 9 + 7
n = int(input())
a = [int(x) for x in input().split()]


def calculateNumberOfArrays(n, a):
    for i in range(n):
        try:
            if 2 <= a[i] <= n - 1:
                x = a[i]
                a[i-1] += x
                a[i+1] += x
                a[i] = -x
            else:
                continue
        except:
            continue
    return a


print(calculateNumberOfArrays(n, a))
