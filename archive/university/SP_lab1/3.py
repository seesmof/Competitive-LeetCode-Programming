"""
Задано масив M[1: N] натуральних чисел, упорядкований за зростанням. Написати алгоритм виплати заданої суми S мінімальною кількістю купюр гідністю M(1), … , M(N).
"""


def solve(M: [int], S: int) -> int:
    # checking if either our cash register is empty, or we need no change to give
    if len(M) == 0 or S == 0:
        # in either case, just return 0
        return 0

    # sort the array in ascending order and make sure all element are less than or equal to the given amount
    existingBills = sorted([item for item in M if item <= S])
    # for keeping track of how much more do we need to give in change
    leftToPay = S
    # for keeping track of the number of bills we've used
    requiredNumberOfBills = 0

    # while we still have some change to give
    while leftToPay >= 0:
        # for chosing an optimal bill
        chosenBill = 0

        # check if the amount that is left to pay is in the array
        if leftToPay in existingBills:
            # in such case, choose this bill and remove it from the cash register
            chosenBill = leftToPay
            existingBills.remove(chosenBill)
        # if its not
        else:
            # then just remove the largest one
            chosenBill = existingBills.pop()

        # decrease the amount we have left to pay and increase the amount of bills we have payed so far
        leftToPay -= chosenBill
        requiredNumberOfBills += 1

        # check if we need no more to pay
        if leftToPay == 0:
            # if so, break out
            break

    return requiredNumberOfBills


def tests():
    assert solve([1, 2, 5, 10, 20, 50], 71) == 3, "Test 1 failed"
    assert solve([1, 2, 5, 10, 20, 50], 3) == 2, "Test 2 failed"
    assert solve([1, 2, 5, 10, 20, 50], 0) == 0, "Test 3 failed"
    assert solve([1, 2, 5, 10, 20, 50], 50) == 1, "Test 4 failed"
    assert solve([1, 3, 4], 4) == 1, "Test 5 failed"
    print(f"All tests passed")


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
            givenSum = int(input("S: "))
            print("Enter a list of bills separated by a space below")
            data = list(map(int, input("M: ").split()))
            print(f"Result: {solve(data,givenSum)}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
