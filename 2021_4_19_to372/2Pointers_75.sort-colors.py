#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums) - 1
        one_start = -1

        while left <= right:  # don't miss "="

            if nums[left] == 0:
                if one_start != -1:  # 0 switch with first 1
                    nums[one_start], nums[left] = nums[left], nums[one_start]
                    one_start += 1  # move 1 to the next 1
                left += 1
                continue

            if nums[left] == 1:
                if one_start == -1:
                    one_start = left  # set first 1 position
                left += 1
                continue

            if nums[right] == 2:
                right -= 1
                continue

            # if right = 0 or 1 exchange w left
            nums[left], nums[right] = nums[right], nums[left]


# @lc code=end
