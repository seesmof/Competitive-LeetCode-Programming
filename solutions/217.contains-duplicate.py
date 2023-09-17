#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums):
        st = set(nums)
        return len(st) != len(nums)


# @lc code=end
