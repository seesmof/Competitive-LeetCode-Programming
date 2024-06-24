#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#


# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: [int]) -> [int]:
        return [num for num in nums if num % 2 == 0] + [
            num for num in nums if num % 2 != 0
        ]


# @lc code=end
