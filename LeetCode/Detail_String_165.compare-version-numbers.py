'''
Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
'''

#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split(".")
        version2_list = version2.split(".")

        length = max(len(version1_list), len(version2_list))
        index = 0

        while index < length:
            if index > len(version1_list) - 1:
                v1_current = 0
                v2_current = int(version2_list[index])
            elif index > len(version2_list) - 1:
                v2_current = 0
                v1_current = int(version1_list[index])
            else:
                v1_current = int(version1_list[index])
                v2_current = int(version2_list[index])

            if v1_current < v2_current:
                return -1

            if v2_current < v1_current:
                return 1

            index += 1

        return 0
        # @lc code=end
