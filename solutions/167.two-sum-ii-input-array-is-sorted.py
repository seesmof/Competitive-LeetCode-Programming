#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


# @lc code=start
class Solution:
    def twoSum(self, numbers, target):
        min, max = 0, len(numbers) - 1

        while min <= max:
            sum = numbers[min] + numbers[max]
            if sum == target:
                return [min + 1, max + 1]
            if sum > target:
                max -= 1
            else:
                min += 1
        return None


# @lc code=end
