'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
             
'''
#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#

# @lc code=start


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        size = len(primes)
        ugly, dp, index, ugly_nums = 1, [1], [0] * size, [1] * size
        for i in range(1, n):
            # compute possibly ugly numbers and update index
            for j in range(0, size):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            # get the minimum
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]


# @lc code=end

'''
As you can see, we need to keep:

The ugly number we found last time
All the ugly numbers we have found
The indexes in dp to multiply the prime number.

n = 1, of course, we return 1
n = 2, we already have [1], so, we do the calculation: 2 x 1, 7 x 1, 13 x 1, 19 x 1,
we got [2, 7, 13, 19], the smallest number is 2, so, we return 2.
n = 3, we already have [1, 2]. Last time, we chose 2 from [2, 7, 13, 19], so, we do the calculation: 2 x 2 to replace the 2. So, we got [4, 7, 13, 19, the smallest number is 4, so, we return 4.
n = 4
dp = [1, 2, 4] # the numbers we have found

# the index of the factors we choose from dp to multiply primes
# e.g if we choose nth number as ugly number, then, index[n-1] += 1
# so index will move to the right, which means we will replace the number
index = [2, 0, 0, 0]

# ** number ** means we will choose this number
ugly_nums = [ 2 x dp[index[0]], **7 x dp[index[1]]**, 13 x dp[index[2]], 19 x dp[index[3]] ]
n = 5
dp = [1, 2, 4, 7]
index  = [2, 1, 0, 0]
ugly_nums = [ **2 x 4**, 7 x 2, 13 x 1, 19 x 1 ]
n = 6
dp = [1, 2, 4, 7, 8]
index  = [3, 1, 0, 0]
ugly_nums = [ 2 x 7, 7 x 2, **13 x 1**, 19 x 1 ]
n = 7
dp = [1, 2, 4, 7, 8]
index  = [3, 1, 1, 0]
ugly_nums = [ **2 x 7**, **7 x 2**, 13 x 2, 19 x 1 ]
If we have some same numbers, we choose only one value, but we will replace all of them at next step.
8. n = 8

dp = [1, 2, 4, 7, 8]
index  = [4, 2, 1, 0]
ugly_nums = [ **2 x 8**, 7 x 4, 13 x 2, 19 x 1 ]
......
Finally, we will got the answers.
'''
