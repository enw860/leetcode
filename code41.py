from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Given an unsorted integer array nums, return the smallest missing positive integer.

        You must implement an algorithm that runs in O(n) time and uses constant extra space.
        """
        bit_str: List[str] = list("0" * len(nums))
        for num in filter(lambda x: 0 < x <= len(nums), nums):
            bit_str[num-1] = "1"
        return bit_str.index("0") + 1 if "0" in bit_str else len(nums) + 1
