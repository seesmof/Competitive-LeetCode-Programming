#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)


# @lc code=end
