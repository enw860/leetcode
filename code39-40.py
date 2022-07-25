from typing import Dict, List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given an array of distinct integers candidates and a target integer target, 
        return a list of all unique combinations of candidates where the chosen 
        numbers sum to target. You may return the combinations in any order.

        The same number may be chosen from candidates an unlimited number of times. 
        Two combinations are unique if the frequency of at least one of 
        the chosen numbers is different.

        It is guaranteed that the number of unique combinations that sum up to target 
        is less than 150 combinations for the given input.
        """

        results: List[List[int]] = []

        valid_candidates: List[int] = list(filter(lambda x: x <= target, candidates))
        for candidate in valid_candidates:
            if candidate == target:
                results.append([candidate])
                continue
            
            sub_sum_list: List[List[int]] = self.combinationSum(
                list(filter(lambda x: x >= candidate, valid_candidates)), 
                target - candidate
            )

            if sub_sum_list and len(sub_sum_list) > 0:
                results.extend([[candidate, *l] for l in sub_sum_list])
        
        return results
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given a collection of candidate numbers (candidates) and a target number (target), 
        find all unique combinations in candidates where the candidate numbers sum to target.
        
        Each number in candidates may only be used once in the combination.
        
        Note: The solution set must not contain duplicate combinations.
        """
        if isinstance(candidates, List) and len(candidates) > 0:
                candidates.sort()

        def sort_and_minimize_candidates(candidates: List[int], target: int) -> List[int]:
            candidates_local: List[int] = list(candidates)

            candidates_capacities: Dict = {}
            for candidate in set(candidates_local):
                candidates_capacities[f"{candidate}"] = target // candidate

            final_list: List[int] = []
            for candidate in candidates_local:
                if candidates_capacities.get(f"{candidate}") > 0:
                    final_list.extend([candidate])
                    candidates_capacities[f"{candidate}"] -= 1

            return final_list

        def _combinationSum2(candidates: List[int], target: int) -> List[List[int]]:
            results: List[List[int]] = []

            if len(candidates) == 0 or target < candidates[0]:
                return []

            valid_candidates = sort_and_minimize_candidates(candidates, target)
            valid_candidates = list(filter(lambda x: x <= target, valid_candidates))
            for idx in range(len(valid_candidates)):
                candidate = valid_candidates[idx]

                if target - candidate == 0:
                    results.extend([[candidate]])
                    continue

                if idx > 0 and valid_candidates[idx-1] == candidate:
                    continue

                sub_sum_list: List[List[int]] = _combinationSum2(
                    valid_candidates[idx+1:], 
                    target - candidate
                )
                
                if sub_sum_list and len(sub_sum_list) > 0:
                    results.extend([[candidate, *l] for l in sub_sum_list])
                
            return results
    
        return  _combinationSum2(candidates, target)
