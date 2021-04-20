'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
'''
#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0

        ugly_list = [1]
        current = 1
        while len(ugly_list) < n:
            current = min(ugly_list[i2]*2, ugly_list[i3]*3, ugly_list[i5]*5)
            ugly_list.append(current)
            if current == ugly_list[i2]*2:
                i2 += 1
            # prevent duplicate - use parallel 'if'
            if current == ugly_list[i3]*3:
                i3 += 1
            # prevent duplicate - use parallel 'if'
            if current == ugly_list[i5]*5:
                i5 += 1

        return current


# @lc code=end
