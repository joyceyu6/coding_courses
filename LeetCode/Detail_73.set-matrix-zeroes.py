#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row_iszero = False
        first_col_iszero = False
        row = len(matrix)
        col = len(matrix[0])

        # step 1: use first row and first column to mark out 0s
        for c in range(col):
            for r in range(row):
                if matrix[r][c] == 0:
                    if r == 0:
                        first_row_iszero = True
                    if c == 0:
                        first_col_iszero = True

                    matrix[0][c] = 0
                    matrix[r][0] = 0

        # step 2: change rows and columns to 0s

        for c in range(col):
            for r in range(row):
                if r == 0 or c == 0:  # critical: exclude first row/colum:
                    continue
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # step 3: first row and first column itself
        if first_col_iszero == True:
            for r in range(row):
                matrix[r][0] = 0

        if first_row_iszero == True:
            for c in range(col):
                matrix[0][c] = 0

                # @lc code=end
