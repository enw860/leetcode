from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        You are given an n x n 2D matrix representing an image, 
        rotate the image by 90 degrees (clockwise).

        You have to rotate the image in-place, which means 
        you have to modify the input 2D matrix directly. 
        
        DO NOT allocate another 2D matrix and do the rotation.
        """
        if len(matrix) < 2:
            return
        
        dimension: int = len(matrix)
        for row_idx in range(len(matrix)):
            inner_dimension: int = len(matrix[row_idx]) - 2 * row_idx

            if inner_dimension < 2:
                return

            for col_idx in range(row_idx, row_idx + inner_dimension - 1):
                temp: int = matrix[row_idx][col_idx]
                matrix[row_idx][col_idx] = matrix[dimension - col_idx - 1][row_idx]
                matrix[dimension - col_idx - 1][row_idx] = matrix[dimension - row_idx - 1][dimension - col_idx - 1]
                matrix[dimension - row_idx - 1][dimension - col_idx - 1] = matrix[col_idx][dimension - row_idx - 1]
                matrix[col_idx][dimension - row_idx - 1] = temp

    def rotate2(self, matrix: List[List[int]]) -> None:
        if len(matrix) < 2:
            return

        matrix.reverse()
        for row_idx in range(len(matrix)):
            for col_idx in range(row_idx, len(matrix)):
                matrix[row_idx][col_idx], matrix[col_idx][row_idx] = matrix[col_idx][row_idx], matrix[row_idx][col_idx]

if __name__ == "__main__":
    matrix = [[1,2],[3,4]]
    # matrix = [[1,2,3],[4, 5, 6], [7,8,9]]
    # matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # matrix = [
    #     [i for i in range(1, 6)], 
    #     [i for i in range(6, 11)], 
    #     [i for i in range(11, 16)], 
    #     [i for i in range(16, 21)], 
    #     [i for i in range(21, 26)], 
    # ]
    s = Solution()
    r = s.rotate2(matrix)
    print(matrix)