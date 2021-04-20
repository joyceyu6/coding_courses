'''
ll DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
'''


#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic = {}
        for i in range(len(s)):
            if i+9 < len(s):
                current = s[i:i+10]
                if current in dic:
                    dic[current] += 1
                else:
                    dic[current] = 1
        result = []

        for key in dic:
            if dic[key] > 1:
                result.append(key)

        return result

        # @lc code=end
