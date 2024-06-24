#
# @lc app=leetcode id=2656 lang=python3
#
# [2656] Maximum Sum With Exactly K Elements
#

# @lc code=start
from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        score = 0

        for _ in range(k):
            score += nums[-1]
            nums[-1] += 1
        return score


# @lc code=end
