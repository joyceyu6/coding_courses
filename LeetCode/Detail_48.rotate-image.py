#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for r in range(n):
            for c in range(n//2):
                matrix[r][c], matrix[r][n - 1 -
                                        c] = matrix[r][n - 1 - c], matrix[r][c]
        for r in range(n):
            for c in range(n):
                if r + c >= n - 1:  # critical, only half needed
                    continue
                matrix[r][c], matrix[n - 1 - c][n - 1 -
                                                r] = matrix[n - 1 - c][n - 1 - r], matrix[r][c]

                # @lc code=end
