#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#


# @lc code=start
class Solution:
    def search(self, nums, target) -> int:
        min, max = 0, len(nums) - 1

        while min <= max:
            mid = min + ((max - min) // 2)
            guess = nums[mid]

            if guess == target:
                return mid
            if guess > target:
                max = mid - 1
            else:
                min = mid + 1
        return -1


# @lc code=end
