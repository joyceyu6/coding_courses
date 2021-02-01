'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
'''
#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:  # corner case
            return 0

        if len(nums) == 2:  # must do corner case
            if nums[0] > nums[1]:
                return 0
            return 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            # print(left, right, mid, nums[mid])
            # will always exist or at 0 or len(nums) -1 because:
            # (1)nums[i] != nums[i + 1] for all valid i.
            # (2) nums[-1] = nums[n] = -∞.

            if mid - 1 < 0:
                if nums[mid] > nums[mid+1]:
                    return mid

            if mid + 1 > len(nums) - 1:
                if nums[mid] > nums[mid-1]:
                    return mid

            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid - 1] <= nums[mid] and nums[mid] < nums[mid+1]:  # increasing trend
                left = mid + 1
                continue

            if nums[mid - 1] > nums[mid] and nums[mid] >= nums[mid+1]:  # decreasing trend
                right = mid - 1
                continue

            right = mid - 1  # when it's trough

        # @lc code=end
