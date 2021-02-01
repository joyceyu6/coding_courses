'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        row = len(grid)
        col = len(grid[0])
        for c in range(col):
            for r in range(row):
                if grid[r][c] == "1":
                    self.recursive(grid, r, c)
                    result += 1

        return result

    def recursive(self, grid, r, c):

        if r < 0 or r > len(grid)-1 or c < 0 or c > len(grid[0])-1:
            return

        if grid[r][c] == "0":
            return

        if grid[r][c] == "X":  # need to add/return as well
            return

        if grid[r][c] == "1":
            grid[r][c] = "X"

            self.recursive(grid, r-1, c)
            self.recursive(grid, r+1, c)
            self.recursive(grid, r, c-1)
            self.recursive(grid, r, c+1)

        # @lc code=end
