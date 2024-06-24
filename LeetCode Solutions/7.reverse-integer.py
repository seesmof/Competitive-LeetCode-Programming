#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#


# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        neg = False
        if "-" in string:
            string = string[1:]
            neg = True
        reverse = string[::-1]
        res = int(reverse)
        if res > 2**31 - 1 or res < -(2**31):
            return 0
        return res if not neg else -res


# @lc code=end
