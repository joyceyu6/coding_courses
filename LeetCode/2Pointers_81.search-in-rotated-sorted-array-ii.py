#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True  # exit

            if nums[left] == nums[mid]:  # no judgement of mid at this scenario
                left = left + 1
                continue
            if nums[right] == nums[mid]:  # no judgement of mid at this scenario
                right = right - 1
                continue

            if nums[right] > nums[left]:  # L M R
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[mid] < nums[right]:  # L P M  R
                if nums[mid] > target:  # L P (T) M R
                    right = mid - 1
                else:
                    if target > nums[left]:  # L (T) P M R
                        right = mid - 1
                    else:
                        left = mid + 1  # L P M (T) R

            else:  # L M P R
                if nums[mid] < target:  # L M (T) P R
                    left = mid + 1

                else:
                    if target < nums[right]:  # L M P (T) R
                        left = mid + 1
                    else:  # L (T) M P R
                        right = mid - 1

        return False

        # @lc code=end
