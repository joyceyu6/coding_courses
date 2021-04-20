#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # from right to left, if left < right, next permutation exist
        # stop when exist

        if len(nums) == 1:
            return nums

        find = False
        find_index = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i-1 >= 0 and nums[i-1] < nums[i]:
                find = True
                find_index = i - 1
                break

        # no next permutation return lowest possible order:
        if find == False:
            for i in range(len(nums)//2):  # critical: divide by 2
                last_index = len(nums) - 1
                right_to_exchange = last_index - i
                nums[i], nums[right_to_exchange] = nums[right_to_exchange], nums[i]

        # two pointer to find the index to whose right the number is smaller than the index number or when it's right end of the number
        nbr_to_exchange = self.findNextBiggerNbr(nums, find_index)

        # exchange the two numbers
        nums[find_index], nums[nbr_to_exchange] = nums[nbr_to_exchange], nums[find_index]

        # inverse the number to the right of the index
        count = len(nums) - (1 + find_index)
        for i in range(count // 2):
            left = find_index + 1 + i
            last_index = len(nums) - 1
            right_to_exchange = last_index - i
            nums[left], nums[right_to_exchange] = nums[right_to_exchange], nums[left]

    def findNextBiggerNbr(self, nums, find_index):

        left = find_index + 1  # start from the next one
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            print(left, right, middle)
            # '=" to find next bigger one than nums[find_index]
            if nums[middle] <= nums[find_index]:  # critical
                right = middle - 1
            else:
                left = middle + 1
        return right


# @lc code=end
