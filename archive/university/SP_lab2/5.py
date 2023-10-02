"""
Обчислити 7^123
"""


def solve(powerBase=7, powerExponent=123):
    return pow(powerBase, powerExponent)


def pow(base, exponent):
    return 1 if exponent == 0 else base * pow(base, exponent - 1)


def tests():
    assert solve() == 7**123
    print("All tests passed")


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
            print(f"Enter power base and power exponent below: ")
            powerBase, powerExponent = list(map(int, input().split()))
            res = solve(powerBase, powerExponent)
            print(f"\nResult: {res}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
