def findMedianSortedArrays(nums1, nums2) -> float:
    arr = list(sorted(nums1 + nums2))
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    print(arr, arr[mid], )
    if len(arr) % 2 != 0:
        return arr[mid]
    return arr[mid]+arr[mid+1]


arr1, arr2 = [1, 2], [3, 4]
print(findMedianSortedArrays(arr1, arr2))
