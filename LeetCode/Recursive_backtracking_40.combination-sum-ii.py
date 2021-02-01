#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        candidates.sort()  # sort to facilitate skipping

        self.recursive(candidates, target, [], result)

        return result

    def recursive(self, candidates: List[int], target: int, temp: List, result: List[List[int]]):
        if target == 0:
            result.append(temp[:])
            return

        if target < 0:
            return

        if len(candidates) == 0:
            return

        for i in range(len(candidates)):

            # skip when duplicates
            if i-1 >= 0 and candidates[i-1] == candidates[i]:
                continue

            temp.append(candidates[i])
            self.recursive(candidates[i+1:], target -
                           candidates[i], temp, result)
            temp.pop()


# @lc code=end
