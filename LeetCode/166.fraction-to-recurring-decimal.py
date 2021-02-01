'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
'''

#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # (1) dic to store {remaining: index} so () knows where to start
        # (2) negative result to be treated as abs first

        if numerator % denominator == 0:
            return str(numerator // denominator)  # if result is integer

        # if negavie - critical
        negative = False
        if numerator * denominator < 0:
            negative = True

        numerator, denominator = abs(numerator), abs(denominator)

        brace_index = -1  # brace starts before this index
        result_list = []
        dic = {}

        while True:
            divide_result = numerator // denominator
            remainer = numerator % denominator

            if remainer == 0:
                result_list.append(str(divide_result))
                break

            if numerator//10 in dic:
                brace_index = dic[numerator//10]  # brace before brace_index
                break

            if len(result_list) > 1:
                dic[numerator//10] = len(result_list)

            result_list.append(str(divide_result))

            numerator = remainer * 10

        if brace_index == -1:  # no repeating fractional part
            # join - content and joiner must be string
            result = result_list[0]+"." + ''.join(result_list[1:])

        # with repeating fractional part
        elif brace_index == 1:  # repeating right after decimal
            result = result_list[0] + '.'+'('+result_list[1:] + ')'

        else:  # repeating not right after decimal
            result = result_list[0] + '.' + ''.join(
                result_list[1:brace_index]) + '('+''.join(result_list[brace_index:])+')'

        if negative:
            return '-'+result
        return result

        # @lc code=end
