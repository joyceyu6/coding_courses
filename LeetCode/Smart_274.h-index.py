'''
Given an array of citations (each citation is a non-negative integer) 
of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist 
has index h if h of his/her N papers have at least h citations each, 
and the other N − h papers have no more than h citations each."
'''
#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            if citations[0] > 0:  # [2]
                return 1
            return 0  # [0]
        citations.sort(reverse=True)
        h = 0
        for i in range(len(citations)):
            if citations[i] < i:  # [15,11]-->2
                return min(citations[i-1], i)  # [0,0]--> 0, [3,0,6,1,5]-->3
            h = min(citations[i], i + 1)  # [1,1]-->1

        return h

        # @lc code=end
