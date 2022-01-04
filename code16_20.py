from typing import List

# Given an array nums of n integers and an integer target, 
# find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      result = []
      for firstIndex,firstControl in enumerate(nums[:len(nums)-2]):
        for secondIndex, secondControl in enumerate(nums[firstIndex+1:len(nums)-2]):
          for thirdControl in nums[secondIndex+1:]:
            temp = (firstControl + secondControl + thirdControl)
            if len(result) < 3 or temp <= sum(result): 
              result = [firstControl, secondControl, thirdControl]
      return sum(nums) if len(result) < 3 else sum(result)

nums = [1,1,1,0]
s = Solution()
print(s.threeSumClosest(nums, 100))