"""
Обчислити точне значення суми 1**n + 2**n + 3**n + ... + n**n за умови, що n >= 10
"""


def solve(nums: [int]) -> int:
    res = 0

    for num in nums:
        calculatedSquare = num * num
        res += calculatedSquare

    return res


def tests():
    assert solve([1, 2, 3, 4]) == 1**2 + 2**2 + 3**2 + 4**2
    assert solve([13, 5, 9, 11]) == 13**2 + 5**2 + 9**2 + 11**2
    assert (
        solve([52, 61, 94, 33, 333]) == 52**2 + 61**2 + 94**2 + 33**2 + 333**2
    )
    print("All tests passed!")


def main():
    print()
    while True:
        print("1. Run tests")
        print("2. Use custom data")
        print("3. Exit")
        choice = int(input(": "))
        print("\n---\n")
        if choice == 1:
            tests()
        elif choice == 2:
            print(
                "Enter the numbers, for each of which to calculate the sum of their squares, or a number, up to which to calculate a sum of squares, below:"
            )
            nums = list(map(int, input().split()))
            res = solve(nums) if len(nums) != 1 else solve(range(1, nums[0] + 1))
            print(f"\nResult: {res}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
