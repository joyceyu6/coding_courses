'''
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
'''
#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        count_list = [0] * 32  # store in reverse order of digits
        for number in nums:

            for i in range(32):
                if number & 1 << i != 0:
                    count_list[i] += 1  # get the last one

        result_list = [0]*32
        for i in range(len(count_list)):
            result_list[i] = count_list[i] % 3

        result = 0
        is_negative = True if result_list[31] == 1 else False

        for i in range(30, -1, -1):  # exclude sign bit
            if is_negative:
                if result_list[i] == 0:  # simulate 2 complement, ignore sign bit
                    result += 1 << i
            else:
                result += result_list[i] << i

        if is_negative:
            # 2 complement/negative, in Python no real sign bit
            result = -(result + 1)  # python specific
            # in computer: - 4 + 4 = 2*33 since we only have 32 digits, it adds up to 0
            # in 2 complement: positive = negative reverse every bit + 1,and vice versa, which causes overflow
            # in Python, no real sign bit/32 digit is not sign,

        return result

        # @lc code=end
