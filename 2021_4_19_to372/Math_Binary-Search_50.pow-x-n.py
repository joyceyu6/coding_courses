#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        isNegative = False
        if n < 0:
            isNegative = True
            n = - n

        powerResults = []
        powerList = []

        currentPower = 1
        powerResult = x
        while currentPower <= n:
            powerResults.append(powerResult)
            powerList.append(currentPower)
            currentPower *= 2
            powerResult *= powerResult

        result = 1

        for i in range(len(powerList)-1, -1, -1):
            currentPower = powerList[i]
            if n - currentPower >= 0:
                result *= powerResults[i]
                n -= currentPower

        return result if isNegative == False else 1/result

        # @lc code=end
