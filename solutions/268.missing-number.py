#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        arr = sorted(nums)
        n = len(arr) + 1
        for i in range(n):
            if i not in arr:
                return i
        return 0


# @lc code=end
