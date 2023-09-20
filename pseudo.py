def quickSort(arr: [int]):
    if len(arr) < 2:
        return arr
    else:
        p = arr[0]
        less = [x for x in arr[1:] if x < p]
        more = [x for x in arr[1:] if x >= p]
        return quickSort(less) + [p] + quickSort(more)


arr = [31, 52, 21, 73, 62, 17, 42, 83]
print(quickSort(arr))
