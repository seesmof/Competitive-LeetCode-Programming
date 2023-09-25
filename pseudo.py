"""
An array M[1: N] of positive integers is given, ordered in non-decreasing order, i.e: M[1] ← M[2] ← ⋯ ← M[N]. Find the first positive integer that is not the sum of any elements of this array, the sum can consist of one term, but each element of the array can be included only once.
"""


def quickSort(arr):
    n = len(arr)
    if n < 2:
        return arr

    pivot = arr[n // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    more = [x for x in arr if x > pivot]

    return quickSort(less) + equal + quickSort(more)


def findSmallest(nums):
    res = 1
    for num in nums:
        if num > res:
            break
        else:
            res += num
    return res


nums = [3, 2, 9, 7]
nums = quickSort(nums)
print(findSmallest(quickSort(nums)))
