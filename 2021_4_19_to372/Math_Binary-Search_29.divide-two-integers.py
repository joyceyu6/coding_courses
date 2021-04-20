#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        # very special case, with sign, negative number is one more than positive numbers
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        negativeFlag = False

        if dividend < 0 and divisor > 0:
            negativeFlag = True
            dividend = - dividend

        if dividend > 0 and divisor < 0:
            negativeFlag = True
            divisor = - divisor

        if dividend < 0 and divisor < 0:
            dividend = - dividend
            divisor = - divisor

        divisor_list = []
        count_list = []

        count = 1
        currentDivisor = divisor

        while currentDivisor <= dividend:
            divisor_list.append(currentDivisor)
            count_list.append(count)

            count = count + count
            currentDivisor = currentDivisor + currentDivisor

        result = 0
        for i in range(len(divisor_list)-1, -1, -1):
            currentDivisor = divisor_list[i]
            count = count_list[i]
            if dividend - currentDivisor < 0:
                continue
            result += count
            dividend -= currentDivisor

        return result if negativeFlag == False else - result


# @lc code=end
