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
    return 0 if not arr else arr[0] + recursiveSum(arr[1:])


def recursiveCountItems(arr: [int]) -> int:
    return 0 if not arr else 1 + recursiveCountItems(arr[1:])


print(f"\nOriginla array: {arr}\n")
res = selectionSort(arr)
print(f"Sorted arr: {res}")
res = recursiveSum(arr)
print(f"Sum of all elements: {res}")
res = recursiveCountItems(arr)
print(f"Length: {res}")
print()
