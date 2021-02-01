'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.
Follow up:

Recursive solution is trivial, could you do it iteratively?
'''
#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.recursive(root, result)
        return result

    def recursive(self, root, result):
        if root == None:

            return

        result.append(root.val)
        self.recursive(root.left, result)
        self.recursive(root.right, result)

        # @lc code=end
