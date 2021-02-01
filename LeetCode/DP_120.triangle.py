'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[0][0]]  # cannot use 0

        for level in range(1, len(triangle)):  # start w 1
            current_dp = [0 for _ in range(len(dp)+1)]  # one more list needed

            for i in range(len(triangle[level])):
                if i == 0:
                    current_dp[i] = dp[i] + triangle[level][i]
                    continue
                if i == len(triangle[level]) - 1:
                    current_dp[i] = dp[i-1] + triangle[level][i]
                    continue
                current_dp[i] = min(dp[i-1], dp[i])+triangle[level][i]

            dp = current_dp
        return min(dp)

        # @lc code=end
