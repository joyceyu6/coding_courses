'''
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.
'''

#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # option 1 O(N)
        left = 0
        right = 0
        current_len = 0
        min_len = 0
        sum_subarray = 0

        # find first contiguous subarray whose sum >= s
        while right < len(nums):
            sum_subarray += nums[right]
            if sum_subarray < s:
                right += 1
                continue
            current_len = right + 1
            break

        min_len = current_len
        if current_len == 0:
            return 0  # if there isn't one
       # move left if still >= s, move right if < s:

        while True:

            while left < right:
                current_len -= 1
                sum_subarray -= nums[left]
                left += 1  # note left+1 after sum_subarray
                if sum_subarray < s:
                    break
                min_len = min(min_len, current_len)

            while right < len(nums) - 1:
                current_len += 1
                right += 1  # note right+1 before sum_subarray
                sum_subarray += nums[right]
                if sum_subarray >= s:
                    min_len = min(min_len, current_len)
                    break

            if right == len(nums) - 1 and left == right:  # both - break condition
                break

        return min_len
    # option 2 O(n log n) complexity

# @lc code=end
