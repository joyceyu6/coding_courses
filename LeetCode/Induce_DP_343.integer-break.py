#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        # option 1: DP
        case = [0, 0, 1, 2, 4, 6, 9]
        if n < 7:
            return case[n]
        dp = case + [0] * (n-6)
        for i in range(7, n+1):
            dp[i] = 3*dp[i-3]
        return dp[-1]

        # #option 2: DP + math
        # return int(math.pow(2, (-n)%3) * math.pow(3, (n-1)%3 + (n-4)//3)) if n > 3 else n-1


# @lc code=end

'''
Let's first consider the limiting behaviour of the solution.

For large n, our "integer break" will consist of splitting up n into b 
groups of x. So n = bx, where rearranging yields b = n⁄x.

Our goal is to maximize the product of these fragments, so we want to maximize
 f(x) = xn⁄x.

Using implicit differentiation, we find f'(x) = nxn⁄x - 2 (1 - logx). Setting
 f'(x) = 0 gives x = e, so our objective function f(x) is maximized at x = e.

Obviously, e is not an integer, so we cannot split n into groups of e for the
 purposes of this question. However, this result gives us the intuition that n
  should be split into 2's and 3's, wherever possible, since 2 < e < 3.

We begin by working through the first several cases of n and try to identify a
 pattern:

n	Maximum Product	# of 2's	# of 3's
2	1 x 1 = 1	0	0
3	1 x 2 = 2	1	0
4	2 x 2 = 4	2	0
5	2 x 3 = 6	1	1
6	3 x 3 = 9	0	2
7	2 x 2 x 3 = 12	2	1
8	2 x 3 x 3 = 18	1	2
9	3 x 3 x 3 = 27	0	3
10	2 x 2 x 3 x 3 = 36	2	2
11	2 x 3 x 3 x 3 = 54	1	3
12	3 x 3 x 3 x 3 = 81	0	4
13	2 x 2 x 3 x 3 x 3 = 108	2	3
14	2 x 3 x 3 x 3 x 3 = 162	1	4
15	3 x 3 x 3 x 3 x 3 = 243	0	5
We can deduce a number of things from this table. First, a DP solution jumps
 out at us. Let dp[n] be the maximum possible product for integer n. Starting
  at n=7, we notice that dp[n] = 3*dp[n-3]. We obtain the following O(n) 
  solution:

DP Implementation:

class Solution:
    def integerBreak(self, n: int) -> int:
        case = [0,0,1,2,4,6,9]
        if n < 7:
            return case[n]
        dp = case + [0] * (n-6)
        for i in range(7, n+1):
            dp[i] = 3*dp[i-3]
        return dp[-1]
(Note: we include the base cases for the invalid inputs of n=0 and n=1 to 
maintain alignment of the indexes of dp, avoiding the need for an offset.)



However, we aren't done yet. If we look a little more carefully at the above 
table, we see that the powers of 2 and 3 follow a pattern.

The "power of 2" pattern is fairly easy to spot. Starting at n=4, the number 
of 2's repeats the cycle of 2,1,0. So the "2 exponent" in the maximum product 
can be expressed as (-n)%3.

The "power of 3" pattern is similar, but slightly harder to express. Again, 
the pattern starts at n=4 and has a period of length 3. This time, the numbers
 in each cycle are all one more than the numbers in the previous cycle. 
 0,1,2 , 1,2,3 , 2,3,4 , ... . We figure out that we can express this 
 "3 exponent" as ((n-1)%3) + (n-4)//3. The first term handles the periodic 
 behavior and the second term captures the perpetual increases between cycles.

We now have an explicit formula to solve the problem, solving in O(1) time. 
Since the only special cases of n=2 and n=3 have maximum products of 1 and 2 
respectively, we can handle everything in one line:

Explicit Formula Implementation:

def integerBreak(self, n: int) -> int:
    return int(math.pow(2, (-n)%3) * math.pow(3, (n-1)%3 + (n-4)//3)) 
    if n > 3 else n-1

'''

'''
In Python, modulo is calculated according to two rules:

(a // b) * b + (a % b) == a, and
a % b has the same sign as b.
Combine this with the fact that integer division rounds down (towards −∞), 
and the resulting behavior is explained.

If you do -8 // 5, you get -1.6 rounded down, which is -2. Multiply that by 5 
and you get -10; 2 is the number that you'd have to add to that to get -8. Therefore, -8 % 5 is 2.
'''
