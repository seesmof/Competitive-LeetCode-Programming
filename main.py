def solve(nums: [int]) -> int:
    arr = sorted(nums)
    n = len(arr)
    for i in range(n + 1):
        if i not in arr:
            return i
    return 0


def tests():
    assert solve([3, 0, 1]) == 2
    assert solve([0, 1]) == 2
    assert solve([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("All tests passed")


tests()
