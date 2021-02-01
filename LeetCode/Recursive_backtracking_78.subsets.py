#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []  # include []
        self.recursive(nums, [], result)
        return result

    def recursive(self, nums: List[int], temp, result) -> List[List[int]]:
        result.append(temp[:])
        if len(nums) == 0:
            return

        for i in range(len(nums)):
            temp.append(nums[i])  # append whenever temp is not empty
            # result.append(temp[:])
            self.recursive(nums[i+1:], temp, result)
            temp.pop()

        # @lc code=end
