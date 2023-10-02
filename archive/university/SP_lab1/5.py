"""
Дано бінарну матриця A(M, N). Знайти квадратну підматрицю одиниць максимального розміру.
"""


def solve(m):
    rows, cols = len(m), len(m[0])
    count = 0

    printMatrix([m[: len(m) - 1] for m in m[: len(m) - 1]])
    printMatrix([m[1 : len(m)] for m in m[: len(m) - 1]])
    printMatrix([m[: len(m) - 1] for m in m[1 : len(m)]])
    printMatrix([m[1 : len(m)] for m in m[1 : len(m)]])


def printMatrix(m):
    for row in m:
        for num in row:
            print(num, end=" ")
        print()
    print()


def tests():
    data = [
        {"matrix": [[1, 1, 1], [1, 1, 1], [1, 1, 1]], "answer": 3},
        {"matrix": [[0, 0, 0], [0, 0, 0], [0, 0, 0]], "answer": 0},
        {"matrix": [[1, 1, 0], [1, 1, 0], [0, 0, 0]], "answer": 2},
        {"matrix": [[1]], "answer": 1},
        {"matrix": [[0]], "answer": 0},
        {
            "matrix": [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 0]],
            "answer": 3,
        },
        {
            "matrix": [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
            "answer": 1,
        },
    ]
    matrix = data[5]["matrix"]
    printMatrix(matrix)
    solve(matrix)
    """
    for item in data:
        assert solve(item["matrix"]) == item["answer"]
    print("All test passed successfully")
    """


tests()
