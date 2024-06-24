#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# [1,1,1,2,2,3]
# @lc code=start


class Solution:
    def topKFrequent(self, nums: [int], k: int):
        arr = [{"count": 0, "num": x} for x in nums]
        arr = []
        res = []
        print(arr)


# @lc code=end
