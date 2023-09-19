#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start


class Solution:
    def topKFrequent(self, nums: [int], k: int):
        print(sorted(nums))
        arr = list(set(nums))
        res = []
        print(arr)

        for i in range(k):
            res.append(arr[i % len(arr)])
        res = sorted(res)
        return res


# @lc code=end
