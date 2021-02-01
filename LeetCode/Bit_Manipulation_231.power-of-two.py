'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
'''
#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False  # corner case

        if n & (n-1) == 0:  # bit manipulation
            return True

        return False


# @lc code=end
