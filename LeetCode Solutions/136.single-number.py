#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        print(f"Set Values: {set(nums)}")
        print(f"Sum of Set: {sum(set(nums))}")
        print(f"Sum of Set times 2: {sum(set(nums)) * 2}")
        print(f"Sum of List: {sum(nums)}")
        # This is really smart
        return sum(set(nums)) * 2 - sum(nums)


# @lc code=end
