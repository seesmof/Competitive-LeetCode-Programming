#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def isAnargam(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declaring anagrams array
        anagrams = []
        for i in strs:
            anagrams.append([i])
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                # so this works, but we have some duplicates, since we declare each anagram as its own list. we need to somehow prevent that, but other than that it works as intended
                if self.isAnargam(strs[i], strs[j]):
                    anagrams[i].append(strs[j])
        print(anagrams)
        # and im not even sure how to fix that honestly. what would we have to do? we would have to work through each internal list and see if items from it are already in some other list? but what about the list that is intended to stay? if we do that to the intended list, we will eliminate that as well, which we dont want. any other ideas?
        # i guess id just have to look into the solution, im not sure how to solve this. plus, its time complexity is like what, O(n^3) now? or something, maybe quadratic, not sure. but we run through everything trice, so extremely bad. there must be some algorithm here, which i dont know yet.
        return anagrams
# @lc code=end
