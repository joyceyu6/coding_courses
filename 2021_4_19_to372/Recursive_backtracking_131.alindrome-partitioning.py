'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
'''

#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        self.recursive(s, result, [])
        return result

    def recursive(self, s, result, temp):
        if len(s) == 0:

            result.append(temp[:])
            return

        for i in range(len(s)):

            if self.isPalindrome(s[:i+1]) == False:
                continue
            temp.append(s[:i+1])
            self.recursive(s[i+1:], result, temp)
            temp.pop()

    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False


# @lc code=end
