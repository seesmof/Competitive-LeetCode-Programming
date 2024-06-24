#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        elements = {}
        for i, el in enumerate(nums):
            diff = target - el
            if diff in elements:
                return [elements[diff], i]
            elements[el] = i


# @lc code=end
