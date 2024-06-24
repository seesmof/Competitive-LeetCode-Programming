#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        low, high = 1, x
        while low <= high:
            guess = (low + high) // 2
            if guess * guess == x:
                return guess
            elif guess * guess < x:
                low = guess + 1
            else:
                high = guess - 1
        return high


# @lc code=end
