#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # step 1: first binary search to know which row is it
        row = len(matrix)
        if row == 0:  # corner case []
            return False

        col = len(matrix[0])  # corner case [[]]
        if col == 0:
            return False

        left = 0
        right = row - 1  # note row - 1 not row
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        # after above loop, right is the row to do step #2

        # step 2: second binary search to know if it exist in that row

        r = right
        left = 0
        right = col - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[r][mid] == target:
                return True
            if matrix[r][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


# @lc code=end
