def solve(nums: [int]) -> int:
    return sum(range(0, len(nums) + 1)) - sum(nums)


def tests():
    assert solve([3, 0, 1]) == 2
    assert solve([0, 1]) == 2
    assert solve([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert solve([0]) == 1
    assert solve([1]) == 0
    print("All tests passed")


tests()
