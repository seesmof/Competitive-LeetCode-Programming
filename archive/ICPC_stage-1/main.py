t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))

    minNumber = max(nums)
    for i in range(n - 1):
        tmp = 0
        if nums[i] < nums[i + 1]:
            tmp = nums[i + 1] - nums[i]
        if tmp < minNumber:
            minNumber = tmp
    print(minNumber)
