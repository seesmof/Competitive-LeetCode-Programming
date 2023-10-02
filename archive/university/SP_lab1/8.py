"""
Звести число A в натуральну ступінь N за якомога меншу кількість множень.
"""


def solve(A: int, N: int) -> int:
    return A**N


def tests():
    assert solve(2, 3) == 8, "Test 1 failed"
    assert solve(3, 1) == 3, "Test 2 failed"
    assert solve(5, 0) == 1, "Test 3 failed"
    assert solve(2, 10) == 1024, "Test 4 failed"
    assert solve(0, 10) == 0, "Test 5 failed"
    assert solve(10, 2) == 100, "Test 6 failed"
    assert solve(2, 8) == 256, "Test 7 failed"
    print("All tests passed")


tests()
