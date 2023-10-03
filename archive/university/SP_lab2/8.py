"""
Обчислити точне значення суми 1**2 + 2**2 + 3**2 + ... + n**2 при умові, що n >= 400
"""


def solve(nums: [int]) -> int:
    res = 0

    for num in nums:
        calculatedSquare = num * num
        res += calculatedSquare

    return res


def tests():
    assert solve([1, 2, 3, 4, 5]) == 1**2 + 2**2 + 3**2 + 4**2 + 5**2
    assert solve([3, 9, 5, 4, 6]) == 3**2 + 9**2 + 5**2 + 4**2 + 6**2
    assert solve([11, 64, 32, 16]) == 11**2 + 64**2 + 32**2 + 16**2
    print("All tests solved!")


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
                "Enter a list of numbers, that you want to calculate the sum of their squares, or just a number, up to which to calculate the sum, below:"
            )
            nums = list(map(int, input().split()))
            res = solve(nums) if len(nums) != 1 else solve(range(1, nums[0] + 1))
            print(f"\nResult: {res}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
