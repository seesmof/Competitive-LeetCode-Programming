#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in paranthesis.values():
                stack.append(char)
            elif char in paranthesis.keys():
                if stack and stack[-1] == paranthesis[char]:
                    stack.pop()
                else:
                    return False

        return not stack


# @lc code=end
