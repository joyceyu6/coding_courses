'''
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
'''

#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        m = {}
        return self.dfs(input, m)

    def dfs(self, input, m):
        if input in m:
            return m[input]
        if input.isdigit():  # isdigit() method returns True if all the characters are digits
            m[input] = int(input)
            return [int(input)]
        result = []
        for i, c in enumerate(input):
            if c in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                result.extend(eval(str(x)+c+str(y))
                              for x in left for y in right)

        m[input] = result
        return result


# @lc code=end
