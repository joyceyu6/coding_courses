

#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

from typing import List
# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        # note n*2 for total parenthesis
        self.recursive(n, "", result, 0, 0)
        return result

    def recursive(self, n: int, temp: str, result: List[str], left_nbr: int, right_nbr: int):
        # print(temp)
        if left_nbr < right_nbr or left_nbr > n:  # critical: not more than n
            return

        if len(temp) == n*2:
            result.append(temp)  # string okay no need for temp[:]
            return

        self.recursive(n, temp +
                       "(", result, left_nbr + 1, right_nbr)  # temp is not changed, generate new string hence no need to pop
        self.recursive(n, temp + ")",
                       result, left_nbr, right_nbr + 1)

        # below also works, but not needed for string:
        # temp += "("
        # self.recursive(n, temp, result, left_nbr+1, right_nbr)
        # temp = temp[:-1]

        # temp += ")"
        # self.recursive(n, temp, result, left_nbr, right_nbr+1)
        # temp = temp[:-1]

        # @lc code=end


solution = Solution()
print(solution.generateParenthesis(3))
