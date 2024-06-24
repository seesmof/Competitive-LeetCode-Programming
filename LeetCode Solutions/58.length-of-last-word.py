#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[-1]) if arr else 0


# @lc code=end
