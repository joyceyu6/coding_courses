'''
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.
'''
#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start


def compare(num1, num2):
    new_num = int(str(num1) + str(num2))
    reverse_num = int(str(num2)+str(num1))
    if new_num > reverse_num:
        return 1
    elif new_num < reverse_num:
        return -1
    else:
        return 0


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = sorted(nums, key=cmp_to_key(
            compare), reverse=True)  # key = cmp_to_key()

        result = ''.join([str(x) for x in sorted_nums])
        if int(result) == 0:
            return "0"  # "00"-->"0" #corner case
        return result

        # @lc code=end
        '''
        [74,21,33,51,77,51,90,60,5,56]
        expected:"9077746056 5 51 51 3321"
        '''
