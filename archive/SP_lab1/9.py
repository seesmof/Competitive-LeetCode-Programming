"""
Задані Q та Y – дві послідовності. Чи можна отримати послідовність Q шляхом викреслення елементів з Y?
"""


def solve(Q: [int], Y: [int]):
    Q, Y = sorted(Q), sorted(Y)
    return set(Q).issubset(Y)


def tests():
    assert solve([1, 2, 3], [1, 2, 3, 4, 5]) == True, "Test 1 failed"
    assert solve([1, 2, 3], [1, 2]) == False, "Test 2 failed"
    assert solve([], [1, 2, 3]) == True, "Test 3 failed"
    assert solve([1, 2, 3], []) == False, "Test 4 failed"
    assert solve([1, 2, 3], [3, 2, 1]) == True, "Test 5 failed"
    print("All tests passed")


tests()
