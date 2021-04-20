#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # if len(matrix) == "0":
        #     return 0

        # if len(matrix) == 1:
        #     if matrix[0][0] == "1":
        #         return 1
        # return 0

        row = len(matrix)
        col = len(matrix[0])
        dp = [[0 for c in range(col)] for r in range(row)]
        max_s = 0

        for r in range(row):
            for c in range(col):
                if r == 0 or c == 0:
                    dp[r][c] = int(matrix[r][c])

                elif matrix[r][c] == "1" and matrix[r-1][c] == "1" and matrix[r][c-1] == "1" and matrix[r-1][c-1] == "1":
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + 1

                elif matrix[r][c] == "1":
                    dp[r][c] = max(1, min(dp[r-1][c], dp[r][c-1]))

                else:
                    dp[r][c] = 0
                max_s = max(max_s, dp[r][c])
        print(dp, max_s)

        return max_s * max_s


# @lc code=end

'''
[["1","0","1","0","0","1","1","1","0"],["1","1","1","0","0","0","0","0","1"],["0","0","1","1","0","0","0","1","1"],["0","1","1","0","0","1","0","0","1"],["1","1","0","1","1","0","0","1","0"],["0","1","1","1","1","1","1","0","1"],["1","0","1","1","1","0","0","1","0"],["1","1","1","0","1","0","0","0","1"],["0","1","1","1","1","0","0","1","0"],["1","0","0","1","1","1","0","0","0"]]
'''
