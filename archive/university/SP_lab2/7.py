"""
Скласти програму обчислення точного значення суми 1! + 2! + 3! + ⋯ + 𝑛! за умовою, що 𝑛 > 10
"""

import math


def solve(nums: [int]) -> int:
    res = 0

    for num in nums:
        calculatedFactorial = factorial(num)
        res += calculatedFactorial

    return res


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


def tests():
    assert solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == math.factorial(
        1
    ) + math.factorial(2) + math.factorial(3) + math.factorial(4) + math.factorial(
        5
    ) + math.factorial(
        6
    ) + math.factorial(
        7
    ) + math.factorial(
        8
    ) + math.factorial(
        9
    ) + math.factorial(
        10
    ) + math.factorial(
        11
    ), "Test 1 failed"
    assert solve([12, 13, 14, 15]) == math.factorial(12) + math.factorial(
        13
    ) + math.factorial(14) + math.factorial(15), "Test 2 failed"
    assert solve([16, 17, 18, 19, 20]) == math.factorial(16) + math.factorial(
        17
    ) + math.factorial(18) + math.factorial(19) + math.factorial(20), "Test 3 failed"
    assert solve([2, 3, 9, 5]) == math.factorial(2) + math.factorial(
        3
    ) + math.factorial(9) + math.factorial(5)
    print("All tests passed")


def main():
    print()
    while True:
        print("1. Run tests")
        print("2. Enter custom data")
        print("3. Exit")
        choice = input(": ")
        print("\n---\n")
        if choice == "1":
            tests()
        elif choice == "2":
            print(
                f"Enter the numbers, for which you'd like to calculate the sum of their factorials, or a number, up to which calculate the sum, below:"
            )
            nums = list(map(int, input().split()))
            res = solve(nums) if len(nums) != 1 else solve(range(1, nums[0] + 1))
            print(f"\nResult: {res}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
