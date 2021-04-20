#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dpList = [False for _ in range(len(nums))]
        # dpList[0] = True

        # for i in range(len(nums)):
        #     step = nums[i]
        #     if dpList[i] == False:
        #         return False
        #     if dpList[i]:
        #         for j in range(step+1):
        #             if i + j > len(nums) - 1:
        #                 break
        #             dpList[i+j] = True

        # return dpList[-1]

        max_index = 0
        for i in range(len(nums)):
            if i > max_index:
                return False

            current_max_index = i + nums[i]
            max_index = max(max_index, current_max_index)

            # if max_index >= len(nums) - 1:
            #     return True
        return True
        # @lc code=end
