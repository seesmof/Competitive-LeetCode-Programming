#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
class Solution:
    def searchInsert(self, nums, target):
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

        nums.append(target)
        nums.sort()
        return nums.index(target)


# @lc code=end
