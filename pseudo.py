import random

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


# recursively sum all elements
def recursiveSum(arr: [int]) -> int:
    return 0 if not arr else arr[0] + recursiveSum(arr[1:])


# recursively count number of elements
def recursiveCountItems(arr: [int]) -> int:
    return 0 if not arr else 1 + recursiveCountItems(arr[1:])


# recursively find the largest element
def recursiveFindMax(arr: [int]) -> int:
    n = len(arr)
    if n == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        return (
            arr[0] if arr[0] > recursiveFindMax(arr[1:]) else recursiveFindMax(arr[1:])
        )


# recursively rewrite binary search
def recursiveBinarySearch(arr: [int], target: int, low: int, high: int) -> int:
    if high >= low:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            return recursiveBinarySearch(arr, target, low, mid - 1)
        else:
            return recursiveBinarySearch(arr, target, mid + 1, high)
    else:
        return -1


print(f"\nOriginal array: {arr}\n")
res = selectionSort(arr)
print(f"Sorted arr: {res}")
res = recursiveSum(arr)
print(f"Sum of all elements: {res}")
res = recursiveCountItems(arr)
print(f"Length: {res}")
res = recursiveFindMax(arr)
print(f"Max element: {res}")
el = random.choice(arr)
res = recursiveBinarySearch(sorted(arr), el, 0, len(arr) - 1)
print(f"Found {el} at index: {res}")
print("\n")


def recursiveFacotrial(n):
    return 1 if n < 2 else n * recursiveFacotrial(n - 1)


def iterativeFactorial(n):
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac


x = random.choice(range(12))
res = recursiveFacotrial(x)
print(f"{x}! = {res}")
res = iterativeFactorial(x)
print(f"{x}! = {res}")
