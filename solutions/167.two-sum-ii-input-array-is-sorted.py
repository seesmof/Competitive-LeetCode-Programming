#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1

        while left <= right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum > target:
                right -= 1
            else:
                left += 1
        return None


# @lc code=end
