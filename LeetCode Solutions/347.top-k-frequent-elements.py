#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#


import heapq


# @lc code=start
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        frequencies = {num: 0 for num in nums}
        for num in nums:
            frequencies[num] += 1

        heap = []
        for key, value in frequencies.items():
            pair = (-value, key)
            heapq.heappush(heap, pair)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans


# @lc code=end

# [4,1,-1,2,-1,2,3]\n2
# [5,3,1,1,1,3,73,1]\n2
