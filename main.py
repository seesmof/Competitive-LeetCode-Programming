def solve(arr: [int]) -> bool:
    res = False
    for i in range(len(arr) - 2):
        j = i + 1
        k = i + 2
        if i < j < k and arr[i] < arr[k] < arr[j]:
            res = True
    return res


def tests():
    assert solve([1, 2, 3, 4]) == False
    assert solve([3, 1, 4, 2]) == True
    assert solve([-1, 3, 2, 0]) == True
    print("All tests passed")


tests()
