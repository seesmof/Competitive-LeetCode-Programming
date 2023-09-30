t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    resArr = []

    if sorted(arr) == arr:
        resArr = [0] * n
    else:
        for j in range(1, n + 1):
            tmp = arr[:]
            numOfSteps = 0
            for i in range(n):
                pass
            resArr.append(numOfSteps)

    for el in resArr:
        print(el, end=" ")
    print()
Ц
