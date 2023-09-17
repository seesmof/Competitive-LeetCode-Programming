#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)
        mid = (0+(len(arr)-1))//2

        if len(arr) % 2 != 0:
            return arr[mid]
        return (arr[mid]+arr[mid+1])/2

# @lc code=end
