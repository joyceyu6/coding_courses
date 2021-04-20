'''
Your task is to calculate a**b mod 1337 where a is a positive integer and b
 is an extremely large positive integer given in the form of an array.

 

Example 1:

Input: a = 2, b = [3]
Output: 8
Example 2:

Input: a = 2, b = [1,0]
Output: 1024
Example 3:

Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
Example 4:

Input: a = 2147483647, b = [2,0,0]
Output: 1198
 

Constraints:

1 <= a <= 231 - 1
1 <= b.length <= 2000
0 <= b[i] <= 9
b doesn't contain leading zeros.
''''
#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
#

# @lc code=start


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # option 1 Euler's Totient Theorem
        # return 0 if a % 1337 == 0 else pow(a, reduce(lambda x, y: (x * 10 + y) % 1140, b) + 1140, 1337)

        # The reduce(fun,seq) function
        '''
        import functools
        The reduce(fun,seq) function is used to apply a particular function passed in its argument
         to all of the list elements mentioned in the sequence passed along.This function is defined
         in “functools” module.

        Working :

        At first step, first two elements of sequence are picked and the result is obtained.
        Next step is to apply the same function to the previously attained result and the number just
        succeeding the second element and the result is again stored.
        This process continues till no more elements are left in the container.
        The final returned result is returned and printed on console.
        '''

        # python code to demonstrate working of reduce()
        '''
        # importing functools for reduce()
        import functools
        
        # initializing list
        lis = [ 1 , 3, 5, 6, 2, ]
        
        # using reduce to compute sum of list
        print ("The sum of the list elements is : ",end="")
        print (functools.reduce(lambda a,b : a+b,lis))
        
        # using reduce to compute maximum element from list
        print ("The maximum element of the list is : ",end="")
        print (functools.reduce(lambda a,b : a if a > b else b,lis))
        '''

        # option 2: recursion
        '''
        Here we use the following two properties:
        '''

        # n1*n2 % 1337 == (n1 % 1337)*(n2 % 1337) % 1337
        # If b = m*10 + d, we have a**b == (a**d)*(a**10)**m

        if not b:
            return 1
        return pow(a, b.pop(), 1337)*self.superPow(pow(a, 10, 1337), b) % 1337
        # pow(x, y, z) is equal to xy % z
        # @lc code=end


'''
Fermat's little theorem
https://en.wikipedia.org/wiki/Fermat%27s_little_theorem:
Fermat's little theorem states that if p is a prime number, 
then for any integer a, the number a**p − a is an integer multiple 
of p. In the notation of modular arithmetic, this is expressed as

a**p = a(mod p)
For example, if a = 2 and p = 7, then 27 = 128, and 128 − 2 = 126 = 7 × 18
 is an integer multiple of 7.

If a is not divisible by p, Fermat's little theorem is equivalent to the 
statement that ap − 1 − 1 is an integer multiple of p, or in symbols:[1][2]

a**(p-1) = 1(mod p)
For example, if a = 2 and p = 7, then 26 = 64, and 64 − 1 = 63 = 7 × 9 is
thus a multiple of 7.
'''

'''
Euler's Theorem
https://en.wikipedia.org/wiki/Euler%27s_theorem

In number theory, Euler's theorem (also known as the Fermat–Euler theorem or 
Euler's totient theorem) states that if n and a are coprime positive integers,
then a raised to the power of the totient of n is congruent to one, modulo n


The converse of Euler's theorem is also true: if the above congruence is true, then a and n must be coprime.

The theorem is a generalization of Fermat's little theorem, and is further generalized by Carmichael's theorem.

The theorem may be used to easily reduce large powers modulo n. For example, consider finding the ones place
decimal digit of 7**222(mod 10), i.e.  The integers 7 and 10 are coprime, and phi(10) = 4, So Euler's theorem
yields 7**4 = 1(mod 10). and we get 7**222=7**(4*55+2)==(7**4)**55*7**2=1**55*7**2=1**55*7**2=49=9(mod 10)

In general, when reducing a power of a modulo n(where a and n are coprime), one needs to work modulo
phi (n) in the exponent of a:
if x=y (mod phi(n)), then a**x = a ** y(mod n)
Euler's theorem underlies RSA cryptosystem, which is widely used in Internet communications. 
In this cryptosystem, Euler's theorem is used with n being a product of two large prime numbers, 
and the security of the system is based on the difficulty of factoring such an integer.

'''
'''
https://leetcode.com/problems/super-pow/discuss/84466/Math-solusion-based-on-Euler's-theorem-power-called-only-ONCE-C%2B%2BJava1-line-Python

1337 only has two divisors 7 and 191 exclusive 1 and itself, so judge if a has a divisor of 7 or 191, 
and note that 7 and 191 are prime numbers, phi of them is itself - 1, then we can use the Euler's theorem, 
see it on wiki https://en.wikipedia.org/wiki/Euler's_theorem, it's just Fermat's little theorem if the mod n
is prime.

see how 1140 is calculated out:
phi(1337) = phi(7) * phi(191) = 6 * 190 = 1140

optimized solution update at 2016-7-12
Today, seeing @myanonymos 's comments, and I find several days ago I AC it just by fortunate coincidence, 
it's not the best solution. now I get a better idea.

(1) Firstly, if a has both divisor 7 and 191, that's a % 1337 == 0, answer is 0.
(2) Then if a has neither divisor 7 nor 191, that's a and 1337 are coprime, so 
a**b % 1337 = a**b % phi(1337) % 1337 = a**b % 1140 % 1337.

(3) Finally, a could has either divisor 7 or 191, that's similar.
Let it be 7 for example.
Let a = 7**n*x
and let b = 1140p + q, where 0 < q <= 1140
then:

ab % 1337
= ((7nx)b) % 1337
= (7nbxb) % 1337
= ( (7nb % 1337) * (xb % 1337) ) % 1337
= ( (71140np + nq % 1337) * (x1140p + q % 1337) ) % 1337

now note x and 1337 are coprime, so

= ( (71140np + nq % 1337) * (xq % 1337) ) % 1337
= ( 7 * (71140np + nq - 1 % 191) * (xq % 1337) ) % 1337

note 7 and 191 are coprime too, and 1140 is a multiple of 190, where 190 = phi(191). 
What's more we should assure that q != 0, if b % 1140== 0, then let b = 1140. so

= ( 7 * (7nq - 1 % 191) * (xq % 1337) ) % 1337
= ( (7nq % 1337) * (xq % 1337) ) % 1337
= (7nqxq) % 1337
= ((7nx)q) % 1337
= (a**q) % 1337

now you see condition (2) and (3) can be merged as one solution, 
if you take care of when b % 1440 == 0, and let b += 1140. Actually (1) can be merged too, but not efficient.
'''
