#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
'''


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()  # cannot use nums = nums.sort() otherwise return none
        result = []
        self.recursive(nums, [], result)
        return result

    def recursive(self, nums: List[int], temp: List[int], result: List[List[int]]):
        if len(nums) == 0:
            result.append(temp[:])
            return

        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.recursive(nums[:i]+nums[i+1:], temp, result)
            temp.pop()

            # @lc code=end
