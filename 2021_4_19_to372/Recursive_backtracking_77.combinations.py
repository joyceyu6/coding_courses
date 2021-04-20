#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.
'''


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # # lambda without (x) will be a function instead of a list
        # nums = [(lambda x: x+1)(x) for x in range(n)]
        nums = [x+1 for x in range(n)]
        result = []
        self.recursive(nums, k, [], result)
        return result

    def recursive(self, nums: List[int], k: int, temp: List[int], result: List[int]) -> List[List[int]]:
        if len(temp) == k:
            result.append(temp[:])
            return
        if len(nums) == 0:
            return

        for i in range(len(nums)):
            temp.append(nums[i])
            self.recursive(nums[i+1:], k, temp, result)
            temp.pop()

        # @lc code=end
