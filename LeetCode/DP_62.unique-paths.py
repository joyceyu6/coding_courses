#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    matrix[r][c] = 1
                    continue
                matrix[r][c] = matrix[r][c-1] + matrix[r-1][c]

        return matrix[m-1][n-1]


# @lc code=end
