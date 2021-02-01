#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        end_of_clean_array = 0
        count = 0
        prior = nums[0]

        for i in range(len(nums)):
            nums[end_of_clean_array] = nums[i]
            if nums[end_of_clean_array] != prior:
                count = 1

                prior = nums[i]
            else:
                count += 1

            if count <= 2:
                end_of_clean_array += 1

        return end_of_clean_array

        # @lc code=end
