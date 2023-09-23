#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: [int]) -> int:
        arr = sorted(nums)
        if len(arr) == 1:
            return arr[0] + 1
        for i in range(len(arr) - 1):
            if arr[i + 1] != arr[i] + 1:
                return arr[i] + 1
        return arr[-1] + 1


# @lc code=end
