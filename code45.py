from typing import List

from numpy import inner

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

        Each element in the array represents your maximum jump length at that position.

        Your goal is to reach the last index in the minimum number of jumps.

        You can assume that you can always reach the last index.
        """
        if len(nums) <= 1:
            return 0

        idx: int = 0
        jump: int = 1

        while True:
            num: int = nums[idx]
            
            if idx + num >= len(nums) - 1:
                return jump

            opt_idx = 0
            pool: List[int] = nums[idx + 1 : idx + num + 1]
            for inner_idx in range(len(pool)):
                if inner_idx + pool[inner_idx] >= opt_idx + pool[opt_idx]:
                    opt_idx = inner_idx
            
            idx = idx + opt_idx + 1
            jump += 1

if __name__ == "__main__":
    s = Solution()
    r = s.jump([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5])
    print(r)