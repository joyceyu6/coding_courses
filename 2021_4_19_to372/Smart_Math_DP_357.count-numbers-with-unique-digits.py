'''
Given a non-negative integer n, count all numbers with unique digits
, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in
 the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
 

Constraints:

0 <= n <= 8
'''
#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#

# @lc code=start


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # # option 1 - time limit exceeded
        #     count = 0
        #     for number in range(10**n):
        #         s = str(number)
        #         if self.isDuplicate(s):
        #             continue
        #         count += 1
        #     return count

        # def isDuplicate(self, s):
        #     store = set()
        #     for c in s:
        #         if c in store:
        #             return True
        #         store.add(c)
        #     return False

        choices = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        ans, product = 1, 1

        for i in range(n):
            product *= choices[i]
            ans += product

        return ans

        '''
        For the first (most left) digit, we have 9 options (no zero); 
        for the second digit we used one but we can use 0 now, so 9 options; 
        and we have 1 less option for each following digits. Number can not be longer than 10 digits.
        '''


# @lc code=end
