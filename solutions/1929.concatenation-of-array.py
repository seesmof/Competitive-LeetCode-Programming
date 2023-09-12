#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # okay so here what can we do is pretty much just do two for loops where we take the current number and add it to the end of the list, this would work, but will result in a time complexity of O(n^2), which is bad. we can do better, but let's try this first and then see how we can improve. just to test the bruteforce.
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums

        # yeah this does work, lets even submit it and see how we can do better.
        # okay, so there's also this extend method, which we can use just like nums.extend(nums) and that would be it, then we just return it.
# @lc code=end
