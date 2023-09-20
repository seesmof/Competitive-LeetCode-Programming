def quickSort(arr: [int]):
    n = len(arr)
    if n < 2:
        return arr

    p = arr[n // 2]
    less = [x for x in arr if x < p]
    equal = [x for x in arr if x == p]
    more = [x for x in arr if x > p]

    return quickSort(less) + equal + quickSort(more)


arr = [31, 52, 21, 73, 62, 17, 42, 83]
print(quickSort(arr))
