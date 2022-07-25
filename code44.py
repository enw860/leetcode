from typing import List

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

        '?' Matches any single character.
        '*' Matches any sequence of characters (including the empty sequence).
        The matching should cover the entire input string (not partial).
        """
        if s == p or p == "*":
            return True

        if len(p) - p.count("*") > len(s):
            return False

        if "*" not in p and "?" not in p:
            return s == p

        # initialize dp matrix
        dp_matrix: List[List[bool]] = []
        for p_idx in range(len(p) + 1):
            dp_matrix.append([False] * (len(s) + 1))
        dp_matrix[0][0] = True
        
        for p_idx in range(len(p) + 1):
            if p_idx > 0:
                p_char = p[p_idx - 1]
                for s_idx in range(len(s) + 1):
                    if s_idx == 0:
                        dp_matrix[p_idx][s_idx] = dp_matrix[p_idx-1][s_idx] and p_char == "*"
                    else:
                        s_char = s[s_idx - 1]
                        if p_char == "*":
                            # either extra parttern char or extra str char
                            dp_matrix[p_idx][s_idx] = dp_matrix[p_idx-1][s_idx] or dp_matrix[p_idx][s_idx-1]
                        else:
                            # diagonal means if previous segment matches, latter part means if the current match good or not
                            dp_matrix[p_idx][s_idx] = dp_matrix[p_idx-1][s_idx-1] and (p_char == s_char or p_char == "?")

        return dp_matrix[-1][-1]


if __name__ == "__main__":
    s = Solution()
    r = s.isMatch("sdmasd", "*a*?d*")
    print(r)