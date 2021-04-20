#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for number in nums:
            result ^= number
        return result


# @lc code=end
