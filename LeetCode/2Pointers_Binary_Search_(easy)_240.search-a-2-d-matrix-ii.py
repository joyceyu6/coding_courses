'''
Write an efficient algorithm that searches for a target value in an 
m x n integer matrix. The matrix has the following properties:
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
(1) Integers in each row are sorted in ascending from left to right.
(2) Integers in each column are sorted in ascending from top to bottom.

'''
#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            if matrix[r][-1] >= target:
                if self.binarySearch(matrix[r], target):
                    return True
        return False

    def binarySearch(self, sub_array, target):

        if sub_array[0] > target:
            return False

        left = 0
        right = len(sub_array) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if sub_array[mid] == target:
                return True
            elif sub_array[mid] > target:
                right -= 1
            else:
                left += 1

        return False


# @lc code=end
