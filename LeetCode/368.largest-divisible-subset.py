'''
Given a set of distinct positive integers nums, return the largest subset
 answer such that every pair (answer[i], answer[j]) of elements in this 
 subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.

'''
#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        S = {-1: set()}

        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
            # '|'(set union) to add the current element in the given set as when
            # we start the iterations, our set is initially empty
            print(S)
        return list(max(S.values(), key=len))  # key = len: sorts by len
        # max(iterable, *iterables, key, default)
        # max() Parameters
        # iterable - an iterable such as list, tuple, set, dictionary, etc.
        # *iterables (optional) - any number of iterables; can be more than one
        # key (optional) - key function where the iterables are passed and
        # comparison is performed based on its return value
        # default (optional) - default value if the given iterable is empty


# @lc code=end

'''
S[x] is the largest subset with x as the largest element, i.e., the subset
 of all divisors of x in the input. With S[-1] = emptyset as useful base case.
  Since divisibility is transitive, a multiple x of some divisor d is also a 
  multiple of all elements in S[d], so it's not necessary to explicitly test 
  divisibility of x by all elements in S[d]. Testing x % d suffices.

While storing entire subsets isn't super efficient, it's also not that bad. 
To extend a subset, the new element must be divisible by all elements in it, 
meaning it must be at least twice as large as the largest element in it. 
So with the 31-bit integers we have here, the largest possible set has 
size 31 (containing all powers of 2).
'''
