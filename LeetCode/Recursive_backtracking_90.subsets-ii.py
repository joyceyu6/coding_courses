#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        nums.sort()
        result = []
        self.recursive(nums, result, [])
        return result

    def recursive(self, nums: List[int], result, temp) -> List[List[int]]:
        result.append(temp[:])  # append any temp

        if len(nums) == 0:
            return

        for i in range(len(nums)):
            if i-1 >= 0 and nums[i-1] == nums[i]:
                continue
            temp.append(nums[i])  # append nums[i] here
            self.recursive(nums[i+1:], result, temp)
            temp.pop()

            # @lc code=end
