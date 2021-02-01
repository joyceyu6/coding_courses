#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1  # minus 1
        max_area = 0
        current_area = 0

        while left < right:
            if height[left] <= height[right]:  # height[x] not left/right directly
                current_area = (right - left) * height[left]
                left += 1
            else:
                current_area = (right - left) * height[right]
                right -= 1

            max_area = max(max_area, current_area)

        return max_area

# @lc code=end
