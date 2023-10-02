"""
Задані Q та Y – дві послідовності. Чи можна отримати послідовність Q шляхом викреслення елементів з Y?
"""


def solve(Q: [int], Y: [int]) -> bool:
    # sort two arrays
    takeFrom, lookIn = sorted(Q), sorted(Y)
    # for keeping track of the items in the original array
    count = 0
    # loop over each item in the array
    for item in takeFrom:
        # check if the item is in our target array
        if item in lookIn:
            # if so, increment the counter
            count += 1
        # if its not, it means that we cannot get an array Q from an array Y
        else:
            # so we immediately return false
            return False
    return True if count == len(takeFrom) else False


def tests():
    assert solve([1, 2, 3], [1, 2, 3, 4, 5]) == True, "Test 1 failed"
    assert solve([1, 2, 3], [1, 2]) == False, "Test 2 failed"
    assert solve([], [1, 2, 3]) == True, "Test 3 failed"
    assert solve([1, 2, 3], []) == False, "Test 4 failed"
    assert solve([1, 2, 3], [3, 2, 1]) == True, "Test 5 failed"
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
            print("Enter an array Q separated by a space below")
            takeFrom = list(map(int, input("Q: ").split()))
            print("Enter an array Y separated by a space below")
            lookIn = list(map(int, input("Y: ").split()))
            print(f"Result: {solve(takeFrom,lookIn)}")
        else:
            break
        print("\n---\n")


if __name__ == "__main__":
    main()
