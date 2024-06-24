/*
 * @lc app=leetcode id=4 lang=javascript
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function (nums1, nums2) {
  arr = nums1.concat(nums2).sort((a, b) => a - b);

  if (arr.length % 2 === 0) {
    return (
      (arr[Math.floor(arr.length / 2 - 1)] + arr[Math.floor(arr.length / 2)]) /
      2
    );
  }
  return arr[Math.floor(arr.length / 2)];
};
// @lc code=end
