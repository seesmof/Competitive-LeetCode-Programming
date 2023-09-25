def binarySearch(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        if guess > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1
