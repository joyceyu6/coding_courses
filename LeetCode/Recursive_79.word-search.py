#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])

        for c in range(col):
            for r in range(row):
                if self.recursive(board, word, r, c):
                    return True

        return False

    def recursive(self, board: List[List[str]], word: str, r: int, c: int) -> bool:
        # must be 1st condition to avoid [["a"]] "a" --> false
        if len(word) == 0:
            return True

        if c < 0 or r < 0 or c > len(board[0]) - 1 or r > len(board) - 1:
            return False  # must return a boolean

        if board[r][c] != word[0]:
            return False

        original = board[r][c]
        board[r][c] = "."  # replace w ". " to avoid duplicate routing

        if self.recursive(board, word[1:], r-1, c):
            return True

        if self.recursive(board, word[1:], r+1, c):
            return True

        if self.recursive(board, word[1:], r, c-1):
            return True

        if self.recursive(board, word[1:], r, c+1):
            return True

        board[r][c] = original  # change back
        return False

        # @lc code=end
