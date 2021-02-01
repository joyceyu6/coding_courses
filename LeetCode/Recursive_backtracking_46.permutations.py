#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
'''
Given a collection of distinct integers, return all possible permutations.
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        result = []
        temp = []
        self.recursive(nums, temp, result)
        return result

    def recursive(self, nums: List[int], temp: List[int], result: List[List[int]]):
        if len(nums) == 0:
            result.append(temp[:])
            return

        for i in range(len(nums)):
            temp.append(nums[i])
            self.recursive(nums[:i]+nums[i+1:], temp, result)  # critical
            temp.pop()

        # @lc code=end
