def findMissingNumber(arr):
    arr = sorted(arr)
    for i in range(len(arr)):
        if arr[i + 1] != arr[i] + 1:
            return arr[i] + 1
    return -1
