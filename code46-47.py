from typing import List, Dict
import time

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given an array nums of distinct integers, return all the possible permutations. 
        
        You can return the answer in any order.
    """
        def _permute(nums: List[int], dp_dict: Dict = None) -> List[List[int]]:
            permute_key: str = "-".join([str(num) for num in nums])

            if not dp_dict:
                dp_dict = {}

            if len(nums) == 0:
                return []
            
            if len(nums) == 1:
                dp_dict[permute_key] = [nums] 
            else:
                combinations: List[List[int]] = []
                for idx in range(len(nums)):
                    num: int = nums[idx]
                    rest_nums: List[int] = nums[:idx] + nums[idx+1:]

                    temp_combinations: List[List[int]] = _permute(rest_nums, dp_dict)
                    combinations.extend([[num, *combination] for combination in temp_combinations])
                dp_dict[permute_key] = combinations
            return dp_dict.get(permute_key)
        return _permute(nums)

    def permute2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]

        combinations: List[List[int]] = [] 
        for idx in range(len(nums)):
            first_num, *rest_nums = nums
            for combination in self.permute(rest_nums):
                combinations.extend([[first_num, *combination]])
            nums = [*rest_nums, first_num]

        return combinations

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def _permuteUnique(nums: List[int], dp_dict: Dict = None) -> List[List[int]]:
            permute_key: str = "_".join([str(num) for num in nums])

            if not dp_dict:
                dp_dict = {}

            if len(nums) == 0:
                return []
            
            if len(nums) == 1:
                dp_dict[permute_key] = [nums] 
            else:
                combinations: List[List[int]] = []
                unique_combinitions: List[str] = []
                for idx in range(len(nums)):
                    num: int = nums[idx]
                    rest_nums: List[int] = nums[:idx] + nums[idx+1:]
                    
                    cur_key: str = "_".join([str(val) for val in [num, *rest_nums]])
                    if cur_key in unique_combinitions:
                        continue

                    unique_combinitions.append(cur_key)

                    temp_combinations: List[List[int]] = _permuteUnique(rest_nums, dp_dict)
                    combinations.extend([[num, *combination] for combination in temp_combinations])
                dp_dict[permute_key] = combinations
                print(unique_combinitions)
                print(dp_dict)
            return dp_dict.get(permute_key)
            
        nums.sort()
        return _permuteUnique(nums)

if __name__ == "__main__":
    s = Solution()

    # test_arr = [i for i in range(1, 5)]

    # start = time.perf_counter()
    # r1 = s.permute(test_arr)
    # print(f"permute completed in: {time.perf_counter() - start} ms")

    # start = time.perf_counter()
    # r2 = s.permute2(test_arr)
    # print(f"permute2 completed in: {time.perf_counter() - start} ms")

    r = s.permuteUnique([3,3,0,3])
    print(r)