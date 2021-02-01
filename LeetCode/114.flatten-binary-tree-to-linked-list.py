'''
Given a binary tree, flatten it to a linked list in-place.
'''
#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root

        self.recursive(root)

    def recursive(self, root):
        if root.left == None and root.right == None:
            return root

        left_tail = None
        right_tail = None

        if root.left:
            left_tail = self.recursive(root.left)

        if root.right:
            right_tail = self.recursive(root.right)

        if left_tail:
            left_tail.right = root.right
            root.right = root.left
            root.left = None

        return right_tail if right_tail != None else left_tail


# @lc code=end
