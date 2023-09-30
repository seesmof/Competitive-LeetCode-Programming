t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    resArr = []

    if sorted(arr) == arr:
        resArr = [0] * n
    else:
        for i in range(n):
            

    for el in resArr:
        print(el, end=" ")
    print()
