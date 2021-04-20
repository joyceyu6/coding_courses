'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are 
not.
'''
#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from collections import deque
import math


class Solution:
    def numSquares(self, n: int) -> int:
        level = 1
        q = deque([n])

        while len(q) > 0:
            l = len(q)
            for i in range(l):
                current = q.popleft()
                # m = math.floor(math.sqrt(current))
                j = 1
                while j*j <= current:
                    temp = current - j*j
                    if temp == 0:
                        return level
                    q.append(temp)
                    j += 1
            level += 1

# @lc code=end
