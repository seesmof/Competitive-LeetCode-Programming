#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        table = {"".join(sorted(el)): [] for el in strs}
        for el in strs:
            table["".join(sorted(el))].append(el)
        return list(table.values())


# @lc code=end
