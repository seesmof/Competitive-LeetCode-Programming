#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#


# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0].lower() in vowels:
                words[i] += "ma"
            elif words[i][0].lower() not in vowels:
                words[i] = words[i][1:] + words[i][0] + "ma"
            for _ in range(i + 1):
                words[i] += "a"

        return " ".join(words)


# @lc code=end
