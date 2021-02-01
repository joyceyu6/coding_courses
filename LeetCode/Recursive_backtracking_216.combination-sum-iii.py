'''
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
'''
#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n < (1+k) * k / 2:
            return []

        if n > 45:
            return []

        if k == 1:
            return [[k]]

        nums = [x for x in range(1, 10)]
        result = []
        self.recursive(nums, k, n, [], result)
        return result

    def recursive(self, nums, k, n, temp, result):
        # print("nums", nums, "temp", temp, "result",
        #       result, "k", k, "n", n)

        if len(temp) == k:
            if n == 0:
                result.append(temp[:])  # must be first condition

        if len(nums) == 0:
            return

        if len(temp) > k:
            return

        for i in range(len(nums)):
            temp.append(nums[i])
            self.recursive(nums[i+1:], k, n-nums[i], temp, result)
            temp.pop()

        # @lc code=end
