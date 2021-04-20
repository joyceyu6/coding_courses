#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
'''
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
 

Example 1:

Input: str = "42"
Output: 42
Example 2:

Input: str = "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign. Then take as many numerical digits as possible, which gets 42.
Example 3:

Input: str = "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
Example 4:

Input: str = "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:

Input: str = "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer. Thefore INT_MIN (−231) is returned.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits, ' ', '+', '-' and '.'.
'''


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        # find first non white space

        string_to_convert = ""
        isnegative = False

        for i in range(len(s)):
            if s[i] != " ":  # space, i.e., " " not ""
                string_to_convert = s[i:]
                break

        if len(string_to_convert) == 0:
            return 0

        # if first c is + or -
        if string_to_convert[0] == "-":
            isnegative = True
            string_to_convert = string_to_convert[1:]

        elif string_to_convert[0] == "+":  # cannot use if, rule out +-xx
            string_to_convert = string_to_convert[1:]

        if len(string_to_convert) == 0:  # if +/- and no other char
            return 0

        # if first non +/- char is not number
        if not string_to_convert[0].isnumeric():
            return 0

        # stop at first non-numeric
        for i in range(len(string_to_convert)):
            if not string_to_convert[i].isnumeric():
                string_to_convert = string_to_convert[0:i]
                break

        result = self.string2nbr(string_to_convert)

        # negative and exceed limit
        if isnegative:
            if result > 2**31:
                return -2**31
            return - result
        # positive and exceed limit
        if result > 2**31-1:
            return 2**31-1

        return result

    # help function to convert string to number

    def string2nbr(self, s: str) -> int:
        dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
               "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        convertednbr = 0
        for c in s:
            convertednbr = convertednbr * 10 + dic[c]  # trick
        return convertednbr


# solution = Solution()
# print(solution.myAtoi("4193 with words"))

# @lc code=end
