"""
Задані Q та Y – дві послідовності. Чи можна отримати послідовність Q шляхом викреслення елементів з Y?
"""


def solve(Q: [int], Y: [int]) -> bool:
    takeFrom, lookIn = sorted(Q), sorted(Y)
    count = 0
    for item in takeFrom:
        if item in lookIn:
            count += 1
        else:
            return False
    return True if count == len(takeFrom) else False


def tests():
    assert solve([1, 2, 3], [1, 2, 3, 4, 5]) == True, "Test 1 failed"
    assert solve([1, 2, 3], [1, 2]) == False, "Test 2 failed"
    assert solve([], [1, 2, 3]) == True, "Test 3 failed"
    assert solve([1, 2, 3], []) == False, "Test 4 failed"
    assert solve([1, 2, 3], [3, 2, 1]) == True, "Test 5 failed"
    print("All tests passed")


tests()
