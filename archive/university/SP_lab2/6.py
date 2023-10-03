"""
З'ясувати яке з чисел a**m чи b**n більше і на скільки. За умови, що a,b <= 40000, а m,n <= 10
"""


def solve(a, b):
    biggerOne = a if a > b else b
    difference = b - a if b > a else a - b
    return biggerOne, difference


def pow(base, exponent):
    return 1 if exponent == 0 else base * pow(base, exponent - 1)


def tests():
    assert solve(pow(3, 2), pow(5, 3)) == (125, 116)
    assert solve(pow(7, 9), pow(9, 8)) == (43046721, 2693114)
    assert solve(pow(12, 3), pow(9, 16)) == (1853020188851841, 1853020188850113)
    assert solve(pow(24, 15), pow(17, 59)) == (
        3948992976476546055807962117305548095339102740462421587418915544041816753,
        3948992976476546055807962117305548095339102740462421082561632587995710129,
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
                "Enter two numbers for the first element, one for the base and one for the exponent of the power, separated by a space below: "
            )
            oneBase, oneExponent = list(map(int, input().split()))
            one = pow(oneBase, oneExponent)

            print(
                "Enter two numbers for the second element, one for the base of the power, another for the exponent of the power, separated by a space below:"
            )
            twoBase, twoExponent = list(map(int, input().split()))
            two = pow(twoBase, twoExponent)

            bigger, difference = solve(one, two)
            print(f"\nResult: Larger one - {bigger}, difference - {difference}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
