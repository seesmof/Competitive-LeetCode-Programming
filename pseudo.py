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


# recursively rewrite binary search
def recursiveBinarySearch(arr: [int], target: int) -> int:
    pass


print(f"\nOriginla array: {arr}\n")
res = selectionSort(arr)
print(f"Sorted arr: {res}")
res = recursiveSum(arr)
print(f"Sum of all elements: {res}")
res = recursiveCountItems(arr)
print(f"Length: {res}")
res = recursiveFindMax(arr)
print(f"Max element: {res}")
res = recursiveBinarySearch(arr, random.choice(arr))
print(f"Found at index: {res}")
print("\n")


def recursiveFacotrial(n):
    return 1 if n == 1 else n * recursiveFacotrial(n - 1)


x = random.choice(range(12))
res = recursiveFacotrial(x)
print(f"{x}! = {res}")
