'''
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
'''
#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if len(board) == 0:  # corner case
            return board

        row = len(board)
        col = len(board[0])

        for r in range(row):
            for c in range(col):
                if r == 0 or r == row - 1 or c == 0 or c == col - 1:
                    if board[r][c] == "O":
                        self.recursive(board, r, c)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    continue
                if board[r][c] == "S":
                    board[r][c] = "O"
                    continue

    def recursive(self, board, r, c):

        row = len(board)
        col = len(board[0])
        if r < 0 or r > row - 1 or c < 0 or c > col - 1:
            return

        if board[r][c] != "O":  # not only "X" but "S" as well
            return

        board[r][c] = "S"

        self.recursive(board, r-1, c)
        self.recursive(board, r+1, c)
        self.recursive(board, r, c-1)
        self.recursive(board, r, c+1)

        # @lc code=end
