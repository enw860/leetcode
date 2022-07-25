from typing import List
from functools import reduce

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where the width of each bar is 1, 
        compute how much water it can trap after raining.
        """

        def getTrapSegements(height: List[int]) -> List[List[int]]:
            start_idx = 0
            segements: List[List[int]] = []

            # find segements that contain at least one gap
            for idx in range(len(height)):
                if start_idx == idx:
                    continue

                h = height[idx]
                if height[start_idx] <= h:
                    segements.append(height[start_idx:idx + 1])
                    start_idx = idx

            remaining_segement = height[start_idx:]
            if remaining_segement[0] > remaining_segement[-1]:
                remaining_segement.reverse()
                segements.extend(getTrapSegements(remaining_segement))
            else:
                segements.append(remaining_segement)

            segements_true: List[int] = []
            for segement in segements:
                # flatten a segement
                max_height = min(segement[0], segement[-1])
                segement[0] = max_height
                segement[-1] = max_height

                # if segement is not turely fattened
                if len(segement) < 3:
                    continue
                
                if max_height != max(*segement):
                    segements_true.extend(getTrapSegements(segement))
                else:    
                    segements_true.append(segement)

            return segements_true

        return reduce(
            lambda gap_sum, segement: gap_sum + max(*segement) * len(segement) - sum(segement),
            getTrapSegements(height),
            0
        )
