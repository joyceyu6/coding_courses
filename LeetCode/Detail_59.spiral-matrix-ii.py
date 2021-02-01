#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        self.recursive(0, n-1, 1, matrix)
        return matrix

    def recursive(self, row_start: int, row_end: int, current_n: int, matrix: List[List[int]]):

        if row_start > row_end:
            return

        for c in range(row_start, row_end+1):  # column index = row index
            matrix[row_start][c] = current_n
            current_n += 1

        if row_start == row_end:
            return

        for r in range(row_start+1, row_end):
            matrix[r][row_end] = current_n
            current_n += 1

        for c in range(row_end, row_start-1, -1):
            matrix[row_end][c] = current_n
            current_n += 1

        for r in range(row_end - 1, row_start, -1):
            matrix[r][row_start] = current_n
            current_n += 1

        self.recursive(row_start+1, row_end-1, current_n, matrix)

        # @lc code=end
