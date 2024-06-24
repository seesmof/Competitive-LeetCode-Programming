#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#


# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        arr = []
        for row in matrix:
            for item in row:
                arr.append(item)

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            guess = arr[mid]

            if guess == target:
                return True
            if guess > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


# @lc code=end
