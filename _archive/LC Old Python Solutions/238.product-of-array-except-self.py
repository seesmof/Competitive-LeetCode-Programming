#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: [int]) -> [int]:
        ans = []
        for i in range(len(nums)):
            print(nums[i])
            res = 1
            for j in range(i + 1, len(nums)):
                res *= nums[j]
            ans.append(res)
        return ans


# @lc code=end
