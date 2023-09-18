"""
The array M[1: N] of positive integers is given, ordered in increasing order.

Find the first positive integer that is not represented by the sum of any elements of this array, the sum can consist of one term, but each element of the array can be included only once.
"""

arrs = [
    {
        "ans": 0,
        "arr": {1, 2, 3, 4, 1},
    },
    {
        "ans": 0,
        "arr": {1, 2, 4, 7, 11},
    },
    {
        "ans": 0,
        "arr": {1, 3, 6, 10},
    },
    {
        "ans": 0,
        "arr": {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13},
    },
    {
        "ans": -1,
        "arr": {},
    },
    {
        "ans": 0,
        "arr": {1000, 2000, 3000},
    },
    {
        "ans": 0,
        "arr": {21, 28, 9, 91, 88, 100, 41, 66, 7, 20, 76, 38, 45, 22, 5, 1, 35},
    },
    {
        "ans": 0,
        "arr": {10, 12, 14, 16, 18, 20},
    },
]


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
    # Initialize a variable to keep track of the smallest positive integer
    smallest_missing = 1

    # Iterate through the array
    for num in arr:
        # If the current number is less than or equal to the smallest missing positive integer,
        # update the smallest_missing by adding the current number to it.
        if num <= smallest_missing:
            smallest_missing += num
        else:
            # If the current number is greater than the smallest_missing, it means we found the first
            # missing positive integer, so we can return it.
            return smallest_missing

    # If all elements in the array are accounted for, return the next positive integer.
    return smallest_missing


def tests():
    for a in arrs:
        assert findFirstEl(a["arr"]) == a["ans"]
    print("All test have passed")


arr = sorted(arrs[-2]["arr"])
print(f"{findFirstEl(arr)} in {arr}")
