'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
'''
#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set()
        max_len = 0
        for word in wordDict:
            word_set.add(word)
            max_len = max(max_len, len(word))

        s_dic = {}
        return self.recursive(s, word_set, max_len, s_dic)  # max_len needed

    def recursive(self, s, word_set, max_len, s_dic):
        if len(s) == 0:
            return True

        if s in s_dic:  # use dic for DP
            return s_dic[s]

        for i in range(min(max_len, len(s))):  # optimize:min of max_len or s
            prefix_word = s[:i+1]
            if prefix_word in word_set:
                if self.recursive(s[i+1:], word_set, max_len, s_dic):
                    s_dic[s[i+1:]] = True  # use dic for DP
                    return True

        s_dic[s] = False  # use dic for DP
        return False

        # @lc code=end


solution = Solution()
print(solution.wordBreak("cars", ["car", "ca", "rs"]))

'''
    Testcase
    "cars"
    ["car","ca","rs"]

    Expected Answer
    true

'''
