#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]

        dic = {}
        for c in strs:
            # critical - list is unhashable
            sorted_current = ''.join(sorted(c))
            if sorted_current not in dic:
                dic[sorted_current] = []
            dic[sorted_current].append(c)

        result = []

        for key in dic:

            result.append(dic[key])

        return result

# @lc code=end
