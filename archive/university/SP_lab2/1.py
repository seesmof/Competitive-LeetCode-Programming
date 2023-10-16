"""
Скласти програму обчислення точного значення n!, де n>12
"""

import math


def factorial(n):
    return 1 if n == 1 else n * factorial(n - 1)


def tests():
    assert factorial(13) == math.factorial(13), "Test 1 failed"
    assert factorial(26) == math.factorial(26), "Test 2 failed"
    assert factorial(61) == math.factorial(61), "Test 3 failed"
    assert factorial(256) == math.factorial(256), "Test 4 failed"
    assert factorial(128) == math.factorial(128), "Test 5 failed"
    assert factorial(912) == math.factorial(912), "Test 6 failed"
    print("All tests passed")


def main():
    print()
    while True:
        print("1. Run tests")
        print("2. Enter custom data")
        print("3. Exit")
        choice = input("Enter your choice: ")
        print("\n---\n")
        if choice == "1":
            tests()
        elif choice == "2":
            print(
                f"Enter the numbers, that you would like to calculate factorial for, below:"
            )
            num = int(input())
            res = factorial(num)
            print(f"\nResult: {res}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
