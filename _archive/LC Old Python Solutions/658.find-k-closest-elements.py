#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#


# @lc code=start
class Solution:
    def findClosestElements(self, arr: [int], k: int, x: int) -> [int]:
        if len(arr) == 1:
            return arr
        res = []
        for _ in range(k):
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    if abs(arr[i] - x) < abs(arr[j] - x) or (
                        abs(arr[i] - x) == abs(arr[j] - x) and arr[i] < arr[j]
                    ):
                        res.append(arr[i])
        return sorted(set(res))


# @lc code=end
