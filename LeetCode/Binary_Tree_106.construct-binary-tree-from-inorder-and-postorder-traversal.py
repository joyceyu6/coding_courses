'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''
#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.recursive(inorder, postorder)

    def recursive(self, inorder, postorder):
        if len(postorder) == 0:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)

        inorder_index = 0
        for i in range(len(inorder)):
            if inorder[i] == postorder[-1]:
                inorder_index = i
                break

        root.left = self.recursive(
            inorder[:inorder_index], postorder[:inorder_index])
        root.right = self.recursive(
            inorder[inorder_index+1:], postorder[inorder_index:-1])
        return root
# @lc code=end
