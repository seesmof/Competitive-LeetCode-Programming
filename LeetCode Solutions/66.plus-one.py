#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#


# @lc code=start
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        num = int("".join([str(i) for i in digits]))
        num += 1
        return [int(i) for i in str(num)]


# @lc code=end
