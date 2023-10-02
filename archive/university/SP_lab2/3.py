"""
Обчислити 100! + 2^100
"""

import math


def solve(factorialNumber=100, powerBase=2, powerExponent=100):
    return factorial(factorialNumber) + pow(powerBase, powerExponent)


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


def pow(n, power):
    return 1 if power == 0 else n * pow(n, power - 1)


def tests():
    assert solve() == math.factorial(100) + 2**100
    print("All tests passed")


def main():
    print()
    while True:
        print("1. Run tests")
        print("2. Use custom data")
        print("3. Exit")
        choice = int(input(": "))
        print(f"\n---\n")
        if choice == 1:
            tests()
        elif choice == 2:
            factorialNumber = int(input(f"Enter a number for factorial: "))
            print(f"Enter two numbers, a base and an exponent, for the power below:")
            powerBase, powerExponent = list(map(int, input().split()))
            res = solve(factorialNumber, powerBase, powerExponent)
            print(f"\nResult: {res}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
