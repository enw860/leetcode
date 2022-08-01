from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together. 
        You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters 
        of a different word or phrase, typically using all the original 
        letters exactly once.
        """
        if len(strs) < 2:
            return [strs]

        anagrams_dict: Dict = {}
        for s in strs:
            s_key: str = self._formatStrKey(s)
            if s_key in anagrams_dict:
                anagrams_dict.get(s_key).append(s)
            else:
                anagrams_dict[s_key] = [s]

        return [val for val in anagrams_dict.values()]
    
    def _formatStrKey(self, s: str) -> str:
        s_dict: Dict = {}
        for char in list(s):
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        s_counts: List[str] = []
        for key, val in s_dict.items():
            s_counts.append(f"{key}{val}")

        s_counts.sort()
        return "_".join(s_counts)


        
        
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    s = Solution()
    r = s.groupAnagrams(strs)
    print(r)