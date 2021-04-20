'''
Given an integer array nums, in which exactly two elements appear only once 
and all the other elements appear exactly twice. Find the two elements that 
appear only once. You can return the answer in any order.

Follow up: Your algorithm should run in linear runtime complexity. 
Could you implement it using only constant space complexity?
'''
#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        # bit manipulation
        # find XOR of all nums
        # s&(s^(s-1)) to find the first differred digit to the right
        # n & [s^(s-1)] to partition nums to two groups: 1 and 0
        # XOR within each group to find the numbers

        s = nums[0]
        for i in range(1, len(nums)):
            s ^= nums[i]

        # critical: leave only the first differed digit to the right
        p = s & (s ^ (s-1))
        sum1 = None
        sum0 = None
        print(p)
        for c in nums:
            if p & c == 0:
                if sum0 == None:
                    sum0 = c
                else:
                    sum0 ^= c
            else:
                if sum1 == None:
                    sum1 = c
                else:
                    sum1 ^= c

        return [sum1, sum0]

        # @lc code=end
