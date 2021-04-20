#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
               "XL": 40, "L": 50, "XC": 90, "C": 100,
               "CD": 400, "D": 500, "CM": 900, "M": 1000}

        index = 0
        result = 0

        while index < len(s):
            # look current and next numbers together to rule out 4,9,etc.
            if index < len(s) - 1 and s[index:index+2] in dic:
                result += dic[s[index:index+2]]
                index += 2
            else:
                result += dic[s[index]]
                index += 1

        return result

        # @lc code=end
