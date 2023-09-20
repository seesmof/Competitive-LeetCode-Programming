#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#


# @lc code=start
class Solution:
    def quickSort(self, arr):
        if len(arr) < 2:
            return arr

        p = arr[len(arr) // 2]
        less = [x for x in arr if x < p]
        more = [x for x in arr if x >= p]

        return self.quickSort(less) + [p] + self.quickSort(more)

    def sortArray(self, nums: [int]) -> [int]:
        return self.quickSort(nums)


# @lc code=end
