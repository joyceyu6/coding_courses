#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        temp = []
        self.recursive(candidates, target, temp, result)
        return result

    def recursive(self, substring: List[int], target: int, temp: List[int], result: List[List[int]]):

        if target == 0:
            result.append(temp[:])
            return

        if target < 0:
            return

        if len(substring) == 0:
            return

        firstNumber = substring[0]
        count = target // firstNumber
        for i in range(count + 1):  # without the firstNumber also should be counted
            if i != 0:
                temp.append(firstNumber)
            # for _ in range(i):
            #     temp.append(firstNumber)
            self.recursive(substring[1:], target-firstNumber*i, temp, result)
        for _ in range(count):  # pop all appended
            temp.pop()

        # @lc code=end
