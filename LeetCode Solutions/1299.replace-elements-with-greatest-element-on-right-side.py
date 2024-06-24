#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#


# @lc code=start
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for index, num in enumerate(arr[:-1]):
            arr[index] = max(arr[index + 1 :])
        arr[-1] = -1
        return arr


# @lc code=end
