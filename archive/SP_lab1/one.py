"""
Дано масив M, складається з натуральних чисел, упорядкований за зростанням. Знайти перше натуральне число, яке не представляється сумою жодних елементів цього масиву, при цьому сума може складатися і з одного доданка, але кожен елемент масиву може входити в неї тільки один раз.
"""


def solve(arr):
    sum = 1

    for item in arr:
        if item > sum:
            break
        else:
            sum += item

    return sum


def tests():
    data = [
        {"array": [1, 2, 4], "answer": 8},
        {"array": [1, 3, 6, 10], "answer": 2},
        {"array": [2, 5, 11], "answer": 1},
    ]
    for item in data:
        assert solve(item["array"]) == item["answer"]
    print(f"All test passed successfully")


tests()
