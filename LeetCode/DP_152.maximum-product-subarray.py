'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
'''
#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_max = [0 for _ in nums]
        dp_min = [0 for _ in nums]

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i-1] *
                            nums[i], dp_min[i-1]*nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1] *
                            nums[i], dp_min[i-1]*nums[i])

        return max(dp_max)

# @lc code=end
