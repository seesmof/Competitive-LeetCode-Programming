def quickSort(arr):
    n = len(arr)
    if n < 2:
        return arr

    p = arr[n // 2]
    less = [x for x in arr if x < p]
    eq = [x for x in arr if x == p]
    more = [x for x in arr if x > p]

    return quickSort(less) + eq + quickSort(more)
