from collections import defaultdict

#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start


class Solution:
    def topKFrequent(self, nums, k):
        ocs = defaultdict(list)
        ans = []
        ori = list()

        for n in nums:
            ocs[n].append(n)

            if n not in ori:
                ori.append(n)

        count = 0
        while k > 0:
            ans.append(ori[count])
            k -= 1
            if count < len(ori):
                count += 1
            else:
                count = 0

        return ans
# @lc code=end
