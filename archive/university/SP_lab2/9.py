"""
Обчислити точне значення суми 1**n + 2**n + 3**n + ... + n**n за умови, що n >= 10
"""


def solve(n: int) -> int:
    res = 0

    for i in range(1, n + 1):
        tmp = int(pow(i, n))
        res += tmp

    return res


def pow(base, exponent):
    return 1 if exponent == 0 else base * pow(base, exponent - 1)


def tests():
    assert solve(5) == 1**5 + 2**5 + 3**5 + 4**5 + 5**5
    assert solve(3) == 1**3 + 2**3 + 3**3
    assert (
        solve(15)
        == 1**15
        + 2**15
        + 3**15
        + 4**15
        + 5**15
        + 6**15
        + 7**15
        + 8**15
        + 9**15
        + 10**15
        + 11**15
        + 12**15
        + 13**15
        + 14**15
        + 15**15
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
            print("Enter your N number below:")
            n = int(input(": "))
            res = solve(n)
            print(f"\nResult: {res}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
