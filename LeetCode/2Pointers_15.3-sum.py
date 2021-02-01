#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        result = []  # no duplicate
        sorted_nums = sorted(nums)  # may have duplicate
        index = 0
        while index < len(sorted_nums):
            # skip if duplicate number
            current = sorted_nums[index]
            if index > 0 and current == sorted_nums[index - 1]:
                index += 1
                continue
            twoSumResult = self.twoSum(sorted_nums, index+1, -current)
            # print(sorted_nums[index+1:], -current)
            if twoSumResult:
                for item in twoSumResult:
                    result.append([current]+item)
            index += 1

        return result
        # helper to find two numbers that add up to target - current

    # pass original nums and index instead of sub_list, otherwise time limit exceeded
    def twoSum(self, nums: List[int], left: int, target: int) -> List[List[int]]:
        result_list = []
        original_left = left  # store orignal left
        right = len(nums) - 1
        while left < right:
            # >original left not 0
            if left - 1 > original_left and nums[left] == nums[left - 1]:
                left += 1
                continue
            if right + 1 < len(nums) and nums[right] == nums[right + 1]:
                right -= 1
                continue

            if nums[left] + nums[right] == target:
                result_list.append([nums[left], nums[right]])
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return result_list

        # @lc code=end


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
