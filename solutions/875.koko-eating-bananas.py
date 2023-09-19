#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#
# [3,6,7,11]


# @lc code=start
class Solution:
    def minEatingSpeed(self, piles, h):
        minAllowed, maxAllowed = min(piles), max(piles)

        for i in range(minAllowed, maxAllowed + 1):
            currentIndex = 0
            allowedHours = h
            currentPiles = piles[:]
            while allowedHours > 0:
                if currentPiles[currentIndex] >= 0:
                    currentPiles[currentIndex] -= i
                    allowedHours -= 1
                currentIndex = (
                    0 if currentIndex == len(currentPiles) - 1 else currentIndex + 1
                )
            if allowedHours == 0 and currentPiles == [
                x for x in currentPiles if x <= 0
            ]:
                return i
        return -1


# @lc code=end

# 3,6,7,11
# 0,2,3,7
# 0,0,0,3
# 0,0,0,0

# so number of steps must be strictly less then the allowed number of hours. thats something, but not much
# i really dont wanna do the brute force of just choosing some random number and seeing how many steps it would take to reach h-1, cause this wont be efficient in any way. in problem tags it says "two-pointers", and thats something, but again, not much. and it is under a category of binary search on NeetCode, which is completely confusing me. i have no smallest idea how can we apply binary search here. im guessing that im not understanding it quite enough
