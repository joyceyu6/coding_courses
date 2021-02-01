'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums, return the minimum element of this array.
'''
#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # no duplicates, if duplicates, remove one number out of two duplicates
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:  # cirtical corner case: otherwise max recursion depth exceeded
            return min(nums)

        left = 0
        right = len(nums) - 1
        middle = left + (right - left)//2

        # L < R sorted -->P = L
        if nums[left] < nums[right]:
            return nums[left]

        # L > R and M > R: L M/P R --> L = M + 1 [4,5,6,7,0,1,2]
        if nums[middle] > nums[right]:

            # critical: don't skip middle as P may = M
            return self.findMin(nums[middle:])

        # L > R and M < R: L P/M R--> R = M -1 [6,7,0,1,2,4,5]
        if nums[middle] < nums[right]:
            # critical: dont skip middle as P may = M
            return self.findMin(nums[:middle+1])

        # @lc code=end
