'''
Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal to the product of all 
the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
'''
#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time + constant space
        p = 1
        n = len(nums)
        result = []
        for i in range(n):
            result.append(p)
            p = p * nums[i]  # product of prior numbers

        p = 1
        for i in range(n-1, -1, -1):
            # product of result[i] and reverse order of prior numbers
            result[i] = result[i] * p
            p = p*nums[i]

        return result


# @lc code=end
