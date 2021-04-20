'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
'''

#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#

# @lc code=start


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for w in words:
            mask = 0
            for c in set(w):  # return (x,y,z)
                mask |= (1 << (ord(c) - 97))  # unicode: a: 97; A: 65
            # return value: dictionary.get(key,optional what to return if not found)
            d[mask] = max(d.get(mask, 0), len(w))
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])


# @lc code=end
