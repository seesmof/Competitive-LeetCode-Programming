class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = nums[0]
        for i in range(1, len(nums)):
            if sum + nums[i] == target:
                return [0, i]
        if sum != target:
            for i in range(1, len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i, j]