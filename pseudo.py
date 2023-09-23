def findMissingNumber(arr):
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i + 1] != arr[i] + 1:
            return arr[i] + 1
    return arr[-1] + 1


print(findMissingNumber([1, 2, 4, 6, 3, 7, 8]))
