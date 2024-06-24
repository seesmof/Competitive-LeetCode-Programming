#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        curr = nums[0]
        for num in nums:
            curr *= num
            prefix.append(curr)


# @lc code=end
