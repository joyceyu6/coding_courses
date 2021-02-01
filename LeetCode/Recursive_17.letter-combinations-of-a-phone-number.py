#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        dic = {"2": "abc", "3": "def",
               "4": "ghi", "5": "jkl", "6": "mno",
               "7": "pqrs", "8": "tuv", "9": "wxyz"}

        list_to_interpret = []
        for digit in digits:
            list_to_interpret.append(dic[digit])

        result = []
        self.recursive(list_to_interpret, "", result)  # direct recursive
        return result

    def recursive(self, input, temp, result):
        # print(result)
        if len(input) == 0:  # stop/base condition
            if len(temp) != 0:
                result.append(temp)
            return

        for c in input[0]:   # resive within recursive
            temp += c
            self.recursive(input[1:], temp, result)
            temp = temp[:-1]  # pop last

        # @lc code=end


solution = Solution()
print(solution.letterCombinations("234"))
