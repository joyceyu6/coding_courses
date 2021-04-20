#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        dic = {"[": "]", "(": ")", "{": "}"}

        for c in s:
            if c in dic:
                stack.append(c)  # critical: only take care of left parentheses
                continue

            if len(stack) == 0:  # judge if stack[-1] exist before operation
                return False

            poped_left = stack[-1]  # may not exist
            if c != dic[poped_left]:
                return False

            stack.pop()  # cover all branches, i.e., what if not exist

        if len(stack) != 0:
            return False

        return True

# @lc code=end
