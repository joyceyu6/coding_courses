#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start

from collections import deque


class Solution:
    def calculate(self, s: str) -> int:
        operator_q = deque([])
        number_q = deque([])
        total = 0
        start = 0
        end = 0

        while end < len(s):
            if s[end] == "+" or s[end] == "-" or s[end] == "*" or s[end] == "/":
                number_q.append(int(s[start:end]))
                operator_q.append(s[end])
                start = end + 1
            end += 1
        number_q.append(int(s[-1]))  # don't miss last number

        l = len(operator_q)
        for i in range(l):
            current_operator = operator_q.popleft()
            if current_operator == "*":
                print(number_q)
                first = number_q.popleft()
                second = number_q.popleft()
                print(first, second)
                number_q.append(first * second)
            elif current_operator == '/':
                first = number_q.popleft()
                second = number_q.popleft
                number_q.append(first // second)
            # elif current_operator = '+' or current_operator = '-':
            else:
                operator_q.append(current_operator)
                first = number_q.popleft()
                number_q.append(first)

        l2 = len(operator_q)
        for i in range(l2):
            current_operator = operator_q.popleft()
            first = number_q.popleft()
            second = number_q.popleft
            if current_operator == "+":
                total += (first + second)
            else:
                total += (first - second)

        return total

        # @lc code=end

        solution = Solution()
        print(solution.calculate("3+2*2+5/2"))
