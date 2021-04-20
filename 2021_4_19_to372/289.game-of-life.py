#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#

# @lc code=start
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = len(board)
        c = len(board[0])
        matrix = [[0 for i in range(c)] for j in range(r)]

        for i in range(r):
            for j in range(c):
                count = 0
                matrix[i][j] = board[i][j]

                if i > 0 and board[i-1][j] == 1:
                    count += 1
                if i > 0 and j > 0 and board[i-1][j-1] == 1:
                    count += 1
                if i > 0 and j < c - 1 and board[i-1][j+1] == 1:
                    count += 1
                if i < r - 1 and board[i+1][j] == 1:
                    count += 1
                if i < r - 1 and j > 0 and board[i+1][j-1] == 1:
                    count += 1
                if i < r - 1 and j < c - 1 and board[i+1][j+1] == 1:
                    count += 1
                if j < c - 1 and board[i][j+1] == 1:
                    count += 1
                if j > 0 and board[i][j-1] == 1:
                    count += 1
                # print(i, j, count)
                if count < 2:
                    matrix[i][j] = 0
                if count > 3:
                    matrix[i][j] = 0
                if count == 3:
                    matrix[i][j] = 1
                print("count", count, i, j, matrix[i][j], matrix)

        print(matrix)
        return matrix

# @lc code=end
