#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lc code=start
class Solution:
    def mergeAlternately(self, one: str, two: str) -> str:
        res = ""
        while one or two:
            if one:
                res += one[0]
                one = one[1:]
            if two:
                res += two[0]
                two = two[1:]
        return res


# @lc code=end
