#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        # okay what do we have in here? a list of numbers, and we need to run through them all to see the differences between each and if one is distinct then it deserves a buff in the amount of candies. lets try brute forcing
        c = {}
        for i in range(len(ratings)):
            if i == 0:
                if ratings[i] > ratings[i+1]:
                    c[ratings[i]] = 1
            elif i == len(ratings)-1:
                if ratings[i] > ratings[i-1]:
                    c[ratings[i]] = c[ratings[i-1]] + 1
            else:
                if ratings[i] > ratings[i+1]:
                    c[ratings[i]] = c[ratings[i+1]] + 1
        return sum(c.values())
        # okay our brute force doesnt work so we need to come up with something else. so right now we're just checking if the next element is more than the current one, if it is then we add one to the candies.
        # tweaked it up a bit, accounted for the edge cases like the first and last elements, but still no luck when submitting
        # yeah i dont really know, my mental abilities end there, lets watch the solution and learn about greedy algorithms.
        # although lets first learn about greedy algorithms and then watch the solution? maybe we could figure more stuff out like that.
# @lc code=end
