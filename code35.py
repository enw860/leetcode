# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the 
# index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

import math
from typing import List

class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    mid = math.floor(len(nums) / 2)

    if len(nums) == 0:
      return 0
    elif len(nums) == 1:
      return 0 if target <= nums[0] else 1

    if target == nums[mid]:
      return mid
    elif target > nums[mid]:
      return mid + 1 + self.searchInsert(nums[mid+1:len(nums)], target)
    else:
      return self.searchInsert(nums[0:mid], target)

if __name__ == "__main__":
  nums = "nums"
  target = "target"
  expectedResult = "expectedResult"

  def temp(*args, **kargs):
    pass

  tests = [
    {nums: [1,3,5,6], target: 5, expectedResult: 2},
    {nums: [1,3,5,6], target: 2, expectedResult: 1},
    {nums: [1,3,5,6], target: 7, expectedResult: 4},
    {nums: [1], target: 0, expectedResult: 0},
    {nums: [1], target: 2, expectedResult: 1}
  ]

  s = Solution()
  for test in tests:
    result = s.searchInsert(test[nums], test[target])
    print(f"{test[nums]} => {result} => {result == test[expectedResult]}")