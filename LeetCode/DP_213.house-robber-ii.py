#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # excl. first
        has_number = [0, 0]
        no_number = [0, 0]
        index = 0
        self.dp(nums[1:], index, has_number, no_number)
        max_nofirst = max(has_number[-1], no_number[-1])
        # incl. first/excl. last
        has_number = [0, 0]
        no_number = [0, 0]
        index = 0
        self.dp(nums[:-1], index, has_number, no_number)
        max_nolast = max(has_number[-1], no_number[-1])
        return(max(max_nofirst, max_nolast))

    def dp(self, nums, index, has_number, no_number):
        if index > len(nums) - 1:
            return

        if index == 0:
            has_number[0] = nums[index]
            no_number[0] = 0

        has_number[0] = has_number[1]
        has_number[1] = no_number[1] + nums[index]
        no_number[0] = no_number[1]
        no_number[1] = max(no_number[0], has_number[0])

        self.dp(nums, index+1, has_number, no_number)


# @lc code=end
