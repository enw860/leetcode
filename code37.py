# 37. Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/

# Write a program to solve a Sudoku puzzle by filling the empty cells.

# to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from typing import List

class Solution:
  def solveSudoku(self, board: List[List[str]]) -> None:
    dirty = False
    missingGrids = []

    for i in range(0, 9):
      for j in range(0, 9):
        if board[j][i] == ".":
          options = self.getOptionsForGrid(board, i, j)
          if len(options) == 1:
            dirty = True
            board[j][i] = options[0]
          else:
            missingGrids.append({
              "position": (j, i),
              "options": options
            })

    missingGrids.sort(key=lambda x: len(x["options"]))
    
    while dirty:
      dirty = False
      completedItems = []

      for index in range(0, len(missingGrids)):
        grid = missingGrids[index]
        j, i = grid["position"]
        options = self.getOptionsForGrid(board, i, j)
        if len(options) == 1:
          dirty = True
          board[j][i] = options[0]
          completedItems.append(index)
        else:
          grid["options"] = options

      completedItems.reverse()
      for item in completedItems:
        missingGrids.pop(item)

      missingGrids.sort(key=lambda x: len(x["options"]))
    
    if len(missingGrids) > 0:
      uncertainItem = missingGrids.pop(0)
      for option in uncertainItem["options"]:
        j, i = uncertainItem["position"]

        # make a proposal
        board[j][i] = option

        # clear dirty board
        for grid in missingGrids:
          grid_j, grid_i = grid["position"]
          board[grid_j][grid_i] = "."
        
        # try new board
        self.solveSudoku(board)

        # determine if the board is completed
        if True not in ["." in row for row in board]:
          return

  def getOptionsForGrid(seld, board: List[List[str]], i: int, j: int) -> List[str]:
    if board[j][i] != ".":
      return []

    constrains = set("")
    options = set([str(x) for x in range(1, 10)])
    
    # col 
    constrains.update([board[x][i] for x in range(0, len(board))])
    
    # row
    constrains.update(board[j])
    
    # square
    for x in range(0, 3):
      constrains.update(board[j // 3 * 3 + x][(i // 3 * 3): (i // 3 * 3 + 3)])

    return list(options - constrains)


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
    ]},
    {board: [
      [".",".","9","7","4","8",".",".","."],
      ["7",".",".",".",".",".",".",".","."],
      [".","2",".","1",".","9",".",".","."],
      [".",".","7",".",".",".","2","4","."],
      [".","6","4",".","1",".","5","9","."],
      [".","9","8",".",".",".","3",".","."],
      [".",".",".","8",".","3",".","2","."],
      [".",".",".",".",".",".",".",".","6"],
      [".",".",".","2","7","5","9",".","."]
    
    ]},
    {board: [
      [".",".",".","2",".",".",".","6","3"],
      ["3",".",".",".",".","5","4",".","1"],
      [".",".","1",".",".","3","9","8","."],
      [".",".",".",".",".",".",".","9","."],
      [".",".",".","5","3","8",".",".","."],
      [".","3",".",".",".",".",".",".","."],
      [".","2","6","3",".",".","5",".","."],
      ["5",".","3","7",".",".",".",".","8"],
      ["4","7",".",".",".","1",".",".","."]
    ]}
  ]

  s = Solution()
  for test in tests:
    print("-"*20)
    result = s.solveSudoku(test[board])
    [print(row) for row in test[board]]