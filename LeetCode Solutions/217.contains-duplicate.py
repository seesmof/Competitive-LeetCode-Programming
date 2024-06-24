#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        seen = {element for element in nums}
        return len(seen) != len(nums)


# @lc code=end
