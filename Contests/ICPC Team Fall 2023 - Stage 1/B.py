def getWeight(arr):
    sortedArr = sorted(arr)
    return sum(1 for i in range(len(arr)) if arr[i] == sortedArr[i])


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    res = 0
    for i in range(n):
        for j in range(i, n):
            sublist = arr[i : j + 1]
            weight = getWeight(sublist)
            res += weight

    print(res)
