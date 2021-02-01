'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
1 <= n <= 19
'''
#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start


class Solution:
    def numTrees(self, n: int) -> int:
        nums = [x + 1 for x in range(n)]
        dic = {}  # memorization

        for i in range(len(nums)+1):
            dic[i] = 0

        dic[0] = 1

        self.recursive(nums, dic)
        return dic[len(nums)]

    def recursive(self, nums, dic):
        '''solution 2 - no count'''
        if len(nums) == 0:
            return

        if dic[len(nums)] != 0:
            return

        for i in range(len(nums)):
            self.recursive(nums[:i], dic)
            self.recursive(nums[i+1:], dic)
            dic[len(nums)] += dic[len(nums[:i])]*dic[len(nums[i+1:])]

        '''solution 1 - count'''

        # if len(nums) == 0:
        #     return 1  # remember to return 1 not 0

        # if len(nums) in dic:
        #     return dic[len(nums)]

        # count = 0
        # for i in range(len(nums)):
        #     count += self.recursive(nums[:i], dic) * \
        #         self.recursive(nums[i+1:], dic)

        # dic[len(nums)] = count
        # return count

        # @lc code=end
