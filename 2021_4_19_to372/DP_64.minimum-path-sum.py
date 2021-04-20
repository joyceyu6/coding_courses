#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # note which is column and which is row
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for c in range(n):
            for r in range(m):
                if r == 0 and c == 0:
                    matrix[r][c] = grid[r][c]
                    continue
                if r == 0:
                    # note where to use grid and where matrix
                    matrix[r][c] = matrix[r][c-1] + grid[r][c]
                elif c == 0:
                    matrix[r][c] = matrix[r-1][c] + grid[r][c]
                else:
                    matrix[r][c] = min(
                        matrix[r][c-1], matrix[r-1][c]) + grid[r][c]

        return matrix[m-1][n-1]

# @lc code=end
