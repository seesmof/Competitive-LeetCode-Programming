def quickSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    if n == 2:
        return [arr[0], arr[1]] if arr[0] <= arr[1] else [arr[1], arr[0]]
    else:
        less, more, pivot, res = [], [], arr[0], []

        for index in range(1, len(arr)):
            element = arr[index]
            more.append(element) if element >= pivot else less.append(element)

        less, more = quickSort(less), quickSort(more)
        res = less + [pivot] + more

        return res


arr = [33, 10, 15, 21, 32, 63, 21, 22, 39]
res = quickSort(arr)
print(res)
