#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        result = []
        self.recursive(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, result)
        return result

    def recursive(self, matrix: List[List[int]], row_start, row_end, col_start, col_end, result: List[int]):
        if (row_start > row_end) or (col_start > col_end):  # stop/base condition
            return

        row = row_end - row_start + 1
        col = col_end - col_start + 1

        for i in range(col):
            result.append(matrix[row_start][col_start+i])

        if row_start == row_end:  # if one row
            return

        for i in range(row-2):
            result.append(matrix[row_start + 1 + i][col_end])

        for i in range(col):
            result.append(matrix[row_end][col_end - i])

        if col_start == col_end:  # if one column
            return

        for i in range(row - 2):
            result.append(matrix[row_end-1-i][col_start])

        self.recursive(matrix, row_start+1, row_end -
                       1, col_start + 1, col_end - 1, result)

        # @lc code=end
