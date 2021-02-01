#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        # simplified: lambdar with one search function to find first/last position:
        # a = nums[middle]; b = target
        first = self.search(nums, target, lambda a, b: a >= b)
        last = self.search(nums, target, lambda a, b: a > b)
        if last >= 1:  # return left when right is needed, hence minus one
            last = last - 1

        # consideration 1: out of range:
        if first < 0 or first > len(nums) - 1 or last < 0 or last > len(nums) - 1:
            return [-1, -1]

        if nums[first] != target and nums[last] != target:  # consideration 2: not found
            return [-1, -1]

        # consideration 3: if only one such number exist, return that number
        if first == -1 and nums[last] == target:
            return[last, last]

        if last == -1 and nums[first] == target:
            return[first, first]

        return [first, last]

    def search(self, nums: List[int], target: int, compare):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2

            if compare(nums[middle], target):
                right = middle - 1

            else:
                left = middle + 1

        # left out of range such as [-1], 0
        # if left > len(nums) - 1 or left < 0:  # or nums[left] != target:
        #     return -1

        return left


# @lc code=end
