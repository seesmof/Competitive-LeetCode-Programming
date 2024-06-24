#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            guess = nums[mid]

            if guess == target:
                return mid
            elif guess > target:
                r = mid - 1
            else:
                l = mid + 1

        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)


# @lc code=end
