#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#


# @lc code=start
class Solution:
    def replaceElements(self, arr):
        # so in this one we have to replace each given element with the greatest element to its right side and replace the last element with -1. well we can replace the last one right away
        # in python we can very easily do that by setting an index to -1, real nice. now, we have to go through each element and for it, run a loop which will check for the greatest element to its right. doesn't seem to complicated, lets try it.
        for i in range(len(arr) - 1):
            arr[i] = max(arr[i + 1 : len(arr)])
        arr[-1] = -1
        return arr
        # okay so right now it all works fine, but the pre-last element is set to -1, which is not what we want, so lets fix that. we can fix by just leaving the arr[-2] element as it is, im pretty sure, which is just not touching it at all, lets try.
        # okay, i understood the problem. we dont need to set the last element to -1, because it ruins our comparisons. lets just try to move the line where we set it to after the algortihm.
        # okay, perfect, it works as expected now. lets try to submit and see the solution.
        # just submitted and it passed 85/90 cases :| one of which is some insanely long and i cannot even see what went wrong there. well thats unfortunate, but lets try to fix it somehow.
        # well yeah i dont know honestly, lets just watch the neetcode now.


# @lc code=end
