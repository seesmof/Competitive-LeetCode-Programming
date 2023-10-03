"""
Скласти програму для обчислення точного значення n**k, де n>10
"""


def pow(n, power):
    res = 1
    for _ in range(power):
        res *= n
    return res


def tests():
    assert pow(13, 13) == 13**13, "Test 1 failed"
    assert pow(51, 51) == 51**51, "Test 2 failed"
    assert pow(318, 318) == 318**318, "Test 3 failed"
    assert pow(916, 916) == 916**916, "Test 4 failed"
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
                f"Enter two numbers, a base for the power and an exponent, separated by a space, below:"
            )
            num, power = list(map(int, input().split()))
            res = pow(num, power)
            print(f"\nResult: {res}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
