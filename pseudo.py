def searchInRotatedArray(arr, target):
    n = len(arr)
    if n == 1:
        return 0
    for i in range(n):
        if arr[i] == target:
            return i
    return -1


print(searchInRotatedArray([4, 5, 6, 7, 0, 1, 2], 0))
