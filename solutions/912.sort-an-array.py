#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#


# @lc code=start
class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        n = len(nums)
        if n < 2:
            return nums

        pivot = nums[n // 2]
        less = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        more = [x for x in nums if x > pivot]

        return self.sortArray(less) + equal + self.sortArray(more)


# @lc code=end
