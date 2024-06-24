#
# @lc app=leetcode id=629 lang=python3
#
# [629] K Inverse Pairs Array
#

# @lc code=start
from functools import cache


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def dp(n: int, k: int):
            if k == 0:
                return 1
            if n == 1 or k < 0:
                return 0
            return dp(n, k - 1) + dp(n - 1, k) - dp(n - 1, k - n)

        return dp(n=n, k=k) % (10**9 + 7)


# @lc code=end
