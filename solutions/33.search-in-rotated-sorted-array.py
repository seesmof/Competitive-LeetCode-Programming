#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def search(self, nums: [int], target: int) -> int:
        min, max = 0, len(nums) - 1

        while min <= max:
            mid = (min + max) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            if guess > target:
                max = mid - 1
            else:
                min = mid + 1
        return -1


# @lc code=end
