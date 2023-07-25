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

/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function (nums) {
  const obj = {};

  for (let i = 0; i < nums.length; i++) {
    obj[num[i]] = obj[nums[i]] + 1 || 1;
    if (obj[num[i]] > nums.length / 2) {
      return num[i];
    }
  }
};
