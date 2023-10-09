def dumbSearch(arr, target) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
