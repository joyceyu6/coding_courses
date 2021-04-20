
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''
#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        return self.recursive(preorder, inorder)

    def recursive(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        inorder_index = 0
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                inorder_index = i
                break

        root.left = self.recursive(
            preorder[1:inorder_index+1], inorder[:inorder_index])
        root.right = self.recursive(
            preorder[inorder_index+1:], inorder[inorder_index+1:])

        return root

        # @lc code=end
