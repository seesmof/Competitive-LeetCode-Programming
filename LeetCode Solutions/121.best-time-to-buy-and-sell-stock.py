#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0

        for sell in prices:
            if sell < buy:
                buy = sell
            else:
                res = max(res, sell - buy)
        return res


# @lc code=end
