# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at 
# an unknown pivot index k (1 <= k < nums.length) such that the resulting array 
# is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

import math
from typing import List

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    pivot = Solution.findRotationPivot(nums)

    lowerHalfResult = Solution.binarySearch(nums[pivot:len(nums)], target)
    upperHalfResult = Solution.binarySearch(nums[0:pivot], target)
    
    return max(
      lowerHalfResult + pivot if lowerHalfResult >= 0 else lowerHalfResult, 
      upperHalfResult
    )
  
  @staticmethod
  def findRotationPivot(nums: List[int]) -> int:
    start = 0
    end = max(len(nums) - 1, 0)
    mid = math.floor(len(nums) / 2)

    if len(nums) < 2 or nums[start] < nums[end]:
      return 0
    
    if len(nums) == 2: 
      return 0 if nums[start] < nums[end] else 1
    elif nums[start] > nums[mid]:
      return Solution.findRotationPivot(nums[start:mid+1])
    else:
      return mid + 1 + Solution.findRotationPivot(nums[mid + 1:len(nums)])

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

target = 3
testArr = [
  [4,5,6,7,0,1,2],
  [6,7,0,1,2,4,5],
  [2,0,1],
  [target],
  [3,1]
]

s = Solution()
[print(arr, s.search(arr, target)) for arr in testArr]