def searchInsert(nums: [int], target):
    min, max = 0, len(nums) - 1

    while min <= max:
        mid = (min + max) // 2
        guess = nums[mid]

        if guess == target:
            return mid
        if guess > target:
            max = mid - 1
        else:
            min = mid + 1

    nums.append(target)
    nums.sort()
    nums.index(target)
    print(nums, nums.index(target))
    return nums.index(target)


nums = [1, 3, 5, 6]
target = 2
print(searchInsert(nums, target))
