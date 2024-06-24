#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#


# @lc code=start
class Solution:
    def isMonotonic(self, nums: [int]) -> bool:
        return (
            True
            if nums == sorted(nums) or nums == sorted(nums, reverse=True)
            else False
        )


# @lc code=end
