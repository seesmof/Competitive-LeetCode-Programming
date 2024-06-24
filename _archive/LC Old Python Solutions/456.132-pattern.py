#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#


# @lc code=start
class Solution:
    def find132pattern(self, nums: [int]) -> bool:
        res = False
        for i in range(len(nums) - 2):
            j = i + 1
            k = i + 2
            if i < j < k and nums[i] < nums[k] < nums[j]:
                res = True
        return res


# @lc code=end
