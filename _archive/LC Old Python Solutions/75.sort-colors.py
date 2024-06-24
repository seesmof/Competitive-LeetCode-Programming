#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#


# @lc code=start
class Solution:
    def quickSort(self, arr):
        n = len(arr)
        if n < 2:
            return arr

        p = arr[n // 2]
        less = [x for x in arr if x < p]
        equal = [x for x in arr if x == p]
        more = [x for x in arr if x > p]

        return self.quickSort(less) + equal + self.quickSort(more)

    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = self.quickSort(nums)


# @lc code=end
