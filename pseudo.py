"""
The array M[1: N] of positive integers is given, ordered in increasing order.

Find the first positive integer that is not represented by the sum of any elements of this array, the sum can consist of one term, but each element of the array can be included only once.
"""

m = [21, 28, 9, 91, 88, 100, 41, 66, 7, 20, 76, 38, 45, 22, 5, 1, 35]
m = sorted(set(m))


def checkForSum(arr: [int], target: int) -> bool:
    min, max = 0, len(arr) - 1

    while min <= max:
        sum = arr[min] + arr[max]
        if sum == target:
            return True
        if sum > target:
            max -= 1
        else:
            min += 1
    return False


def findFirstEl(arr: [int]) -> int:
    for i in range(len(arr)):
        if not checkForSum(arr, arr[i]):
            return i
    return -1


ans = findFirstEl(m)
print(f"\n{ans}\n")
