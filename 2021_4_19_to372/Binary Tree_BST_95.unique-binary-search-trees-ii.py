'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
0 <= n <= 8
'''
#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []

        nums = [i+1 for i in range(n)]
        return self.recursive(nums)

    def recursive(self, nums):  # return list of TreeNode
        if len(nums) == 0:
            return [None]  # tricky, Null node == None

        candidates = []  # return list of tree nodes
        for i in range(len(nums)):

            left_trees = self.recursive(nums[:i])

            right_trees = self.recursive(nums[i+1:])

            for l_node in left_trees:  # critical
                for r_node in right_trees:
                    current = TreeNode(nums[i])
                    current.left = l_node
                    current.right = r_node
                    candidates.append(current)

        return candidates

        # @lc code=end
