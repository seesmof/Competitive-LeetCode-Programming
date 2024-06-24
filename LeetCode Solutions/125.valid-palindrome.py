#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strippedString = ""
        for character in s:
            if character.isalnum():
                strippedString += character
        strippedString = strippedString.lower()
        return strippedString == strippedString[::-1]


# @lc code=end
