#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correspondings = {"{": "}", "(": ")", "[": "]"}

        for letter in s:
            if letter in correspondings:
                stack.append(letter)
            elif len(stack) == 0 or letter != correspondings[stack.pop()]:
                return False

        return len(stack) == 0


# @lc code=end

# AC
