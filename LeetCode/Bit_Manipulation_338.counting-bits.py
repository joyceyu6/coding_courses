'''
Given an integer num, return an array of the number of 1's in the binary
representation of every number in the range [0, num].



Example 1:

Input: num = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: num = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


Constraints:

0 <= num <= 105

'''

'''
Follow up:

It is very easy to come up with a solution with run time O(32n). Can you do it in linear time O(n) and possibly in a single pass?
Could you solve it in O(n) space complexity?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''

#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start


class Solution:
    def countBits(self, num: int) -> List[int]:
        # option 1:
        # result = []
        # for n in range(0, num+1):
        #     count = 0
        #     current = n
        #     while current != 0:
        #         if current & 1 == 1:
        #             count += 1
        #         current = current >> 1
        #     result.append(count)
        # return result

        # option 2: Kernighan's Algorithm: takes O(log N) to count set bits (1s) in an integer
        #  because An integer n has log(n) bits,
        setBits = [0] * (num+1)
        # (i & (i -1)) is actually Brian Kernighan’s Algorithm, so always keep it handy for counting ones
        for i in range(1, num+1):
            setBits[i] = setBits[i & (i-1)] + 1
        return setBits

        '''
        why Kernighan's Algorithm works. 

        What is the meaning of (i & (i-1))? We are doing a bit-wise-and 
        (masking) of i versus the previous number i-1. Since these two numbers
        are exactly off by 1, they will always have different 1-bits. 1 & 0 
        or 0 & 1 is always 0. So the masking will throw out the one-bit, which
        means we will always calculate an even number for our lookup.

        Why does Kernighan's Algorithm work?

        For the purpose of this discussion, let's define stable bits as the
         upper bits that don't change and unstable bits as the lower bits that
          do change as we go from i-1 to i. By definition, we will see all 1's in the stable bits. By observation, we see all 0's in the unstable bits, except one 1 (this is why we add one to the stable bits lookup to find our answer). This is the nature of addition. It's a consequence of the carry bit as you add one to any number. You will end up with zero or more upper bits that don't change (stable bits) and at least one unstable lower bit.

        For example, let's observe what happens when we go from i - 1 = 13 to i = 14. 
        13 is 0b1101. When we add 1 to it to get 14 or 0b1110. There are two upper 
        stable bits 0b11. In the unstable lower bits, we go from 01 to 10 due to one carry. We can observe that there is always exactly one 1 in the unstable lower bits.

        This is why we use the upper stable bits for our lookup and then add one to 
        get our answer. This is true for all numbers - you can try with other examples
        in the table to convince yourself.
        '''

# @lc code=end
