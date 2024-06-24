#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#


# @lc code=start
class Solution:
    def isValidSudoku(self, board: [[str]]) -> bool:
        def validateLine(line: [str]):
            line = [el for el in line if el != "."]
            return True if len(line) == len(set(line)) else False

        for row in board:
            if not validateLine(row):
                return False

        columns = []
        for currentIndex in range(len(board)):
            columnHolder = []
            for row in board:
                for index, element in enumerate(row):
                    if index == currentIndex:
                        columnHolder.append(element)
            columns.append(columnHolder)
        for col in columns:
            if not validateLine(col):
                return False

        squares = {}
        for i in range(3):
            for j in range(3):
                squares[(i, j)] = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                identifier = (i // 3, j // 3)
                squares[identifier].append(board[i][j])
        for _, value in squares.items():
            if not validateLine(value):
                return False

        return True


# @lc code=end
