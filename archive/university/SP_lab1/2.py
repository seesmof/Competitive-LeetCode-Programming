"""
У покупця є N монет гідністю H(1), … , H(n). У продавця є M монет номіналом B(1), … , B(n). Чи може покупець купити річ вартості S так, щоб у продавця знайшлася точна решта (якщо вона необхідна)
"""


def solve(N: [int], M: [int], S) -> bool:
    pass


def tests():
    assert solve([1, 2, 3], [1, 2, 3], 4) == True, "Test 1 failed"
    assert solve([1, 2, 3], [1, 2, 3], 10) == False, "Test 2 failed"
    assert solve([5, 10, 20], [1, 2, 5], 15) == True, "Test 3 failed"
    assert solve([5, 10, 20], [1, 2, 5], 30) == False, "Test 4 failed"
    print("All test cases passed")


tests()
