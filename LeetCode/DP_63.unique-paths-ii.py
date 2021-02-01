#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        matrix[0][0] = 0 if obstacleGrid[0][0] == 1 else 1

        for c in range(n):
            for r in range(m):
                if obstacleGrid[r][c] == 1:
                    matrix[r][c] = 0
                    continue
                if r == 0 and c == 0:
                    continue
                if r == 0:
                    matrix[r][c] = matrix[r][c-1]
                    continue
                if c == 0:
                    matrix[r][c] = matrix[r-1][c]
                    continue

                matrix[r][c] = matrix[r-1][c] + matrix[r][c-1]

        return matrix[m-1][n-1]

        # @lc code=end
