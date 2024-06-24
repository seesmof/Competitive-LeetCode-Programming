#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given an array of integers and a target number, return the indices of the two numbers
        that add up to the target.
        """

        # Sort the array first to make it easier to find the two numbers that add up to the target
        numbers.sort()

        # Use two pointers to find the two numbers that add up to the target
        # Move the pointers towards each other until they meet or cross each other
        left, right = 0, len(numbers) - 1
        while left < right:
            # Add the numbers at the current pointers and check if they equal the target
            # If they do, return the indices of the numbers
            # If they don't, move the pointers towards each other to find the two numbers that add up to the target
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1
        # If no two numbers add up to the target, return an empty list
        return []


# @lc code=end
