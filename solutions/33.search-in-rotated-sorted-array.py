#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def search(self, nums: [int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


# @lc code=end
