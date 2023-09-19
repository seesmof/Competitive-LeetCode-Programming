arr = [4, 9, 3, 6, 2]


def selectionSort(arr: [int]) -> [int]:
    tmp = arr[:]
    res = []
    n = len(tmp)
    for _ in range(n):
        smallest = min(tmp)
        res.append(smallest)
        tmp.remove(smallest)
    return res


def recursiveSum(arr: [int]) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + recursiveSum(arr[1:])


print(f"\nOriginla array: {arr}\n")
res = selectionSort(arr)
print(f"Sorted arr: {res}")
res = recursiveSum(arr)
print(f"Sum of all elements: {res}")
