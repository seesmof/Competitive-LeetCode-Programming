def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    t, b = 0, rows - 1
