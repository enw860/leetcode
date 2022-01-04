# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need 
# to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List

class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    return self.validateRows(board) and self.validateCols(board) and self.validateSquares(board)

  def validateRows(self, board: List[List[str]]) -> bool:
    for subboard in board:
      if not self.validateSubboard(subboard):
        return False
    return True

  def validateCols(self, board: List[List[str]]) -> bool:
    for i in range(0, len(board)):
      subboard = [row[i] for row in board]
      if not self.validateSubboard(subboard):
        return False
    return True

  def validateSquares(self, board: List[List[str]]) -> bool:
    for i in range(0, 3):
      for j in range(0, 3):
        subboard = []
        subboard += board[j * 3 + 0][i * 3:(i + 1) * 3]
        subboard += board[j * 3 + 1][i * 3:(i + 1) * 3]
        subboard += board[j * 3 + 2][i * 3:(i + 1) * 3]
        print(subboard)
        if not self.validateSubboard(subboard):
          return False
    return True

  def validateSubboard(self, subboard: List[str]) -> bool:
    hashTable = {}
    for item in subboard:
      item_key = f"key_{item}"
      if item_key not in hashTable:
        hashTable[item_key] = 1
      else:
        hashTable[item_key] += 1
        if item_key != "key_.":
          return False
    return True

if __name__ == "__main__":
  board = "board"
  expectedResult = "expectedResult"

  def temp(*args, **kargs):
    pass

  tests = [
    {board: [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ], expectedResult: True},
    {board:[
      ["8","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ], expectedResult: False},
    {board: [
      [".",".",".",".","5",".",".","1","."],
      [".","4",".","3",".",".",".",".","."],
      [".",".",".",".",".","3",".",".","1"],
      ["8",".",".",".",".",".",".","2","."],
      [".",".","2",".","7",".",".",".","."],
      [".","1","5",".",".",".",".",".","."],
      [".",".",".",".",".","2",".",".","."],
      [".","2",".","9",".",".",".",".","."],
      [".",".","4",".",".",".",".",".","."]
    ], expectedResult: False}
  ]

  s = Solution()
  for test in tests:
    result = s.isValidSudoku(test[board])
    print(f"{test[board]} => {result} => {result == test[expectedResult]}")  