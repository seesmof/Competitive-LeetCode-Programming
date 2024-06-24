#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#


# @lc code=start
class Solution:
    def quickSort(self, array: [int]) -> [int]:
        numberOfItems = len(array)
        if numberOfItems < 2:
            return array

        pivot = array[numberOfItems // 2]
        lesserItems = [item for item in array if item < pivot]
        equalItems = [item for item in array if item == pivot]
        morerItems = [item for item in array if item > pivot]

        return self.quickSort(lesserItems) + equalItems + self.quickSort(morerItems)

    def sortArray(self, nums: [int]) -> [int]:
        return self.quickSort(nums)


# @lc code=end
