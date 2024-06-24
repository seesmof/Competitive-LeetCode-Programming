#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        mergedList = sorted(nums1 + nums2)
        length = len(mergedList)
        if length % 2 == 1:
            return mergedList[length // 2]
        else:
            median = length // 2
            return (mergedList[median] + mergedList[median - 1]) / 2.0


# @lc code=end
