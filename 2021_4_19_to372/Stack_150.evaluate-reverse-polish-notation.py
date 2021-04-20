'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
'''


#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = None
        q = deque([])
        for i in range(len(tokens)):
            if tokens[i] == "+":
                first = int(q.pop())
                second = int(q.pop())
                result = first + second
                q.append(result)

            elif tokens[i] == "-":
                first = int(q.pop())
                second = int(q.pop())
                result = second - first
                q.append(result)

            elif tokens[i] == "*":
                first = int(q.pop())
                second = int(q.pop())
                result = first * second
                q.append(result)

            elif tokens[i] == "/":
                first = int(q.pop())
                second = int(q.pop())
                if first * second < 0 and second % first != 0:  # critical: differentiate when negative
                    result = second // first + 1  # truncted toward zero
                else:
                    result = second // first
                q.append(result)

            else:
                q.append(tokens[i])

        if result == None:  # corner case, no operator found
            return int(tokens[-1])
        return result

        # @lc code=end

        '''
        ["3","11","5","+","-"] expected: -13
        ["3","11","+","5","-"] expected: 9
        ["4","-2","/","2","-3","-","-"] expected: -7

        (1) result also to be appended
        (2) a / b when negative AND non-integer will be farther from zero; when positive closer to zero
        '''
