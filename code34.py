# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

import math
from typing import List

class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    lowerIndex = upperIndex = index = Solution.binarySearch(nums, target)

    if lowerIndex == -1:
      return [lowerIndex, upperIndex]

    while lowerIndex - 1 >= 0:
      if nums[lowerIndex - 1] == target:
        lowerIndex -= 1
      else:
        break

    while upperIndex + 1 < len(nums):
      if nums[upperIndex + 1] == target:
        upperIndex += 1
      else:
        break
    
    return [lowerIndex, upperIndex]

  @staticmethod
  def binarySearch(nums: List[int], target: int) -> int:
    start = 0
    end = max(len(nums) - 1, 0)
    mid = math.floor(len(nums) / 2)

    if len(nums) == 0:
      return -1
    elif len(nums) == 1:
      return 0 if nums[0] == target else -1
    elif target > nums[end] or target < nums[start]:
      return -1
    elif target == nums[mid]:
      return mid
    elif target < nums[mid]:
      return Solution.binarySearch(nums[start:mid], target)
    else:
      result = Solution.binarySearch(nums[mid + 1:len(nums)], target)
      return -1 if result < 0 else (mid + 1 + result)

if __name__ == "__main__":
  nums = "nums"
  target = "target"
  expectedResult = "expectedResult"

  def temp(*args, **kargs):
    pass

  tests = [
    {nums: [5,7,7,8,8,10], target: 8, expectedResult: [3, 4]},
    {nums: [5,7,7,8,8,10], target: 6, expectedResult: [-1, -1]},
    {nums: [], target: 0, expectedResult: [-1, -1]},
    {nums: [0], target: 0, expectedResult: [0, 0]},
  ]

  s = Solution()
  for test in tests:
    result = s.searchRange(test[nums], test[target])
    print(f"{test[nums]} => {result} => {result == test[expectedResult]}")