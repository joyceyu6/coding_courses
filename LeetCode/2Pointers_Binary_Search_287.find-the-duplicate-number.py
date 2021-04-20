'''
Given an array of integers nums containing n + 1 integers 
where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.
'''

'''
Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
'''


#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # left, right = 1, len(nums) - 1
        # while left < right:
        #     mid = left + (right - left) // 2
        #     count = 0
        #     for k in nums:
        #         if mid < k <= right:
        #             count += 1
        #     if count > right - mid:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return right

        low = 1
        high = len(nums)-1

        while low < high:
            mid = low+(high-low)//2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid+1
            else:
                high = mid
        return low

        # @lc code=end
