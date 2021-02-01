#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # left > right vs. left < right
        # left > target vs. left < target

        left = 0
        right = len(nums) - 1

        # no rotation: if nums[left] < nums[right]....guaranteed to be rotated

        while left <= right:
            middle = left + (right - left)//2
            if nums[middle] == target:
                return middle

            # if nums[left] == target:
            #     return left

            # if nums[right] == target:
            #     return right

            if nums[left] < nums[right]:  # target in ordered list
                if nums[middle] > target:
                    right = middle - 1

                else:
                    left = middle + 1

            else:
                if nums[left] <= target:  # target in first ordered part
                    if nums[middle] < nums[right]:  # middle is in second part
                        right = middle - 1
                    else:  # middle in first part together with target - normal two pointer:
                        if nums[middle] >= target:
                            right = middle - 1
                        else:
                            left = middle + 1

                else:  # target in second ordered part
                    if nums[middle] > nums[right]:  # middle in second ordered part
                        left = middle + 1
                    else:  # middle in second part together with target - normal two pointer:
                        if nums[middle] >= target:
                            right = middle - 1
                        else:
                            left = middle + 1

        return -1


# @lc code=end
