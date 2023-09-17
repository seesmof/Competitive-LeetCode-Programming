#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles, h):
        # can we assume that h wont be less then a piles len?
        if h == len(piles):
            return max(piles)
        else:
            return max(piles) - 1


# @lc code=end

# 3,6,7,11
# 0,2,3,7
# 0,0,0,3
# 0,0,0,0

# so number of steps must be strictly less then the allowed number of hours. thats something, but not much
# i really dont wanna do the brute force of just choosing some random number and seeing how many steps it would take to reach h-1, cause this wont be efficient in any way. in problem tags it says "two-pointers", and thats something, but again, not much. and it is under a category of binary search on NeetCode, which is completely confusing me. i have no smallest idea how can we apply binary search here. im guessing that im not understanding it quite enough
