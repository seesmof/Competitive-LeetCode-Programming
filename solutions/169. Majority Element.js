// Given an array nums of size n, return the majority element.
// The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  const size = nums.length;
  const object = {};
  for (let i = 0; i < size; i++) {
    if (object[nums[i]]) {
      object[nums[i]]++;
    } else {
      object[nums[i]] = 1;
    }
  }
  for (let key in object) {
    if (object[key] > size / 2) {
      return key;
    }
  }
};
