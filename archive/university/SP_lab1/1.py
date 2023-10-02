"""
Задано масив M[1: N] натуральних чисел, упорядкований за зростанням. Знайти перше натуральне число, яке не можна представити сумою жодних елементів масиву, при цьому сума може складатися і з одного доданка, але кожен елемент масиву може входити в неї лише один раз.
"""


def solve(M: [int]) -> int:
    # for keeping track of current sum
    sum = 1

    # loop over each item in the given array
    for item in M:
        # check if a current item is bigger than the sum
        # this would mean that either the sum can't be created by any elements in the array, so its too small, or that the sum we have is larger than the sum of all the elements in the array. in any case, we have the number we're looking for
        if item > sum:
            # so we just break out of the loop
            break
        # in any other case
        else:
            # just add the current element to our sum holder
            sum += item

    # and return the number we got
    return sum


def tests():
    assert solve([1, 2, 4]) == 8, "Test 1 failed"
    assert solve([1, 3, 6, 10]) == 2, "Test 2 failed"
    assert solve([2, 5, 11]) == 1, "Test 3 failed"
    print("All test passed")


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
            print("Enter an array of integers separated by a space below")
            data = list(map(int, input("M: ").split()))
            print(f"Result: {solve(data)}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
