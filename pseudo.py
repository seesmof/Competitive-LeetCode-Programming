"""
The array M[1: N] of positive integers is given, ordered in increasing order.

Find the first positive integer that is not represented by the sum of any elements of this array, the sum can consist of one term, but each element of the array can be included only once.
"""

arrs = [
    {
        "ans": 0,
        "arr": [1, 2, 3, 4, 1],
    },
    {
        "ans": 0,
        "arr": [1, 2, 4, 7, 11],
    },
    {
        "ans": 0,
        "arr": [1, 3, 6, 10],
    },
    {
        "ans": 0,
        "arr": [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13],
    },
    {
        "ans": -1,
        "arr": [],
    },
    {
        "ans": 0,
        "arr": [1000, 2000, 3000],
    },
    {
        "ans": 0,
        "arr": [21, 28, 9, 91, 88, 100, 41, 66, 7, 20, 76, 38, 45, 22, 5, 1, 35],
    },
    {
        "ans": 0,
        "arr": [10, 12, 14, 16, 18, 20],
    },
]


def checkForSum(arr: [int], target: int) -> bool:
    # use a set to store the possible sums
    sums = set()
    # loop through the array and add each element to the existing sums
    for x in arr:
        # if x is equal to or greater than the target, no need to continue
        if x >= target:
            break
        # add x to the set
        sums.add(x)
        # loop through the existing sums and add x to them
        for y in list(sums):
            # if the new sum is equal to or greater than the target, no need to continue
            if x + y >= target:
                break
            # add the new sum to the set
            sums.add(x + y)
    # check if the target is in the set
    return target in sums


def findFirstEl(arr: [int]) -> int:
    # start from 1 and increment until we find a number that is not in the array or a sum of its elements
    i = 1
    while True:
        # if i is not in the array and not a sum of its elements, return i
        if i not in arr and not checkForSum(arr, i):
            return i
        # otherwise, increment i
        i += 1


def tests():
    for a in arrs:
        assert findFirstEl(a["arr"]) == a["ans"]
    print("All test have passed")


arr = sorted(set(arrs[-2]["arr"]))
print(f"{findFirstEl(arr)} in {arr}")
