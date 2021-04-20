'''
You are given two jugs with capacities x and y litres. There is an infinite amount
 of water supply available. You need to determine whether it is possible to measure
  exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within
 one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the
 first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
 

Constraints:

0 <= x <= 10^6
0 <= y <= 10^6
0 <= z <= 10^6

'''
#
# @lc app=leetcode id=365 lang=python3
#
# [365] Water and Jug Problem
#

# @lc code=start

# from fractions import gcd
import math


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        # option 1: implement greatest common divisor(GCD)
        a, b = x, y
        while y:
            r = x % y
            x = y
            y = r
            print(r, x, y)
        return bool(not z or (x and z <= a+b and not z % x))

        # # option 2: use math.gcd
        # return z == 0 or x + y >= z and z % math.gcd(x, y) == 0


# @lc code=end

'''
greatest common divisor(GCD)
'''

'''
if x and y are coprime,  then we can and only can 
reach every integer z in [0, x + y]
'''