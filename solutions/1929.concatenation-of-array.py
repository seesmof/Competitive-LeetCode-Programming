#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#


# @lc code=start
class Solution:
    def getConcatenation(self, nums):
        # okay so here what can we do is pretty much just do two for loops where we take the current number and add it to the end of the list, this would work, but will result in a time complexity of O(n^2), which is bad. we can do better, but let's try this first and then see how we can improve. just to test the bruteforce.
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums

        # yeah this does work, lets even submit it and see how we can do better.
        # okay, so there's also this extend method, which we can use just like nums.extend(nums) and that would be it, then we just return it.
        # oh an by the way we ended up using only one for loop, so the time complexity is linear, which is good.
        # we apparently can also just do a nums*2 which should achieve the same. but lets not concentrate over such an easy problem. well watch neetcode solution and move on.

        # so neetcode proposed pretty much the same solution as i came up with, but wrapping it in another for loop that will just run a certain amount of times, in our case 2, just to make it ever more scalable.
        # here is how it would look
        # ans = []
        # for i in range(2):
        #     for n in nums:
        #         ans.append(n)
        # return ans


# @lc code=end
