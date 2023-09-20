def quickSort(arr):
    n = len(arr)
    if n < 2:
        return arr

    pivot = arr[n // 2]
    less = [el for el in arr if el < pivot]
    equal = [el for el in arr if el == pivot]
    more = [el for el in arr if el > pivot]

    return quickSort(less) + equal + quickSort(more)


arr = [33, 10, 15, 21, 32, 63, 21, 22, 39]
res = quickSort(arr)
print(res)
